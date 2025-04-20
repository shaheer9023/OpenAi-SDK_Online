# Code Explanation :

### Code:

```python
@cl.on_chat_start
async def start():
    cl.user_session.set("history",[])
    await cl.Message(content="I am Urdu Chatbot").send()

# UI of Chatbot
@cl.on_message
async def UI(message:cl.Message):
    history=cl.user_session.get("history")
    msg=cl.Message(content=f"Assistant Response 👇 \n")
    await msg.send()

    prompt=message.content
    history.append({"role":"user","content":prompt})

    # Streaming

    response=Runner.run_streamed(
        starting_agent=await (UrduBot()),
        input=history,
    )
    async for event in response.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
            token = event.data.delta
            await msg.stream_token(token)
    history.append({"role": "assistant", "content": msg.content})
```

### **Step-by-Step Explanation:**

#### **1. `@cl.on_chat_start`**

* **Explanation:** Ye decorator hai, jo chat start hone par trigger hota hai. Iska matlab hai jab chatbot ka interaction start hota hai, ye function execute hota hai.
* **Real-life Example:** Maan lo aap kisi customer service chatbot ko start karte ho. Jab aap chatbot ko open karte ho, to chatbot aapko greet karta hai. Ye function wahi kaam karta hai, jab chat session start hota hai.

#### **2. `async def start():`**

* **Explanation:** Ye ek asynchronous function hai jo chatbot ke start hone par execute hota hai. Iska matlab hai ki ye function koi time-consuming task perform karega (jaise database ya network se data laana), aur jab tak wo task complete nahi hota, wo system ko block nahi karega.
* **Real-life Example:** Jaise jab aap ek app open karte ho, to wo background mein data load karta hai (jaise news ya notifications), lekin app ko aap use kar paate ho bina rukawat ke. Ye function bhi waise hi kaam karta hai.

#### **3. `cl.user_session.set("history",[])`**

* **Explanation:** Ye line user session mein ek empty list `history` set karti hai. `history` mein chat ka pura record store hota hai, jaise user ka input aur assistant ke responses.
* **Real-life Example:** Socho aap ek diary likh rahe ho. Jab aap kuch likhte ho, wo diary mein save hota hai. Yahan `history` waise hi kaam kar raha hai, jo har message aur response ko store karta hai.

#### **4. `await cl.Message(content="I am Urdu Chatbot").send()`**

* **Explanation:** Ye line asynchronous hai, jo ek message send karti hai jo content "I am Urdu Chatbot" hota hai. Matlab chatbot apne start hone par user ko greet karta hai.
* **Real-life Example:** Jaise jab aap ek customer service chat open karte ho, chatbot aapko welcome message bhejta hai. Ye waise hi hota hai.

#### **5. `@cl.on_message`**

* **Explanation:** Ye decorator hai jo message receive hone par trigger hota hai. Matlab jab user koi message bhejta hai, toh ye function execute hota hai.
* **Real-life Example:** Jab aap chat mein koi message type karte ho, wo message chatbot ko milta hai aur chatbot uske response mein jawab deta hai. Ye function usi tarah kaam karta hai.

#### **6. `async def UI(message: cl.Message):`**

* **Explanation:** Ye ek asynchronous function hai jo `message` object ko handle karta hai. Jab user koi message bhejta hai, ye function us message ko process karta hai.
* **Real-life Example:** Jaise aap ek chat box mein koi message type karte ho, uske baad chatbot us message ko process karta hai aur response bhejta hai. Ye function waise hi kaam karta hai.

#### **7. `history = cl.user_session.get("history")`**

* **Explanation:** Ye line user session se `history` ko get karti hai. Yani jitna bhi chat history hai, wo fetch kar liya jaata hai.
* **Real-life Example:** Jaise aap ek chat app mein purani baatein dekhte ho, waise hi ye line history ko retrieve karti hai.

#### **8. `msg = cl.Message(content=f"Assistant Response 👇 \n")`**

* **Explanation:** Ye line ek new message object create karti hai jisme assistant ka response hoga. Content mein "Assistant Response 👇" likha gaya hai, jo message ke shuru mein dikhega.
* **Real-life Example:** Jab aap kisi message ka response dekhte ho, toh usme "Assistant Response 👇" jaise message dikhayi deta hai jo assistant ka response start karta hai.

#### **9. `await msg.send()`**

* **Explanation:** Ye line asynchronous hai, jo `msg` ko send karti hai.
* **Real-life Example:** Jaise jab aap chat mein koi message bhejte ho, wo message chat window mein appear hota hai. Ye waise hi hota hai.

#### **10. `prompt = message.content`**

* **Explanation:** Ye line user ke message ka content (`message.content`) fetch kar ke `prompt` variable mein store karti hai.
* **Real-life Example:** Jab aap koi query ya message bhejte ho, wo message `prompt` ke roop mein store ho jata hai, jise assistant process karega.

#### **11. `history.append({"role": "user", "content": prompt})`**

* **Explanation:** Ye line user ka message history mein append kar deti hai. `role` "user" hota hai aur `content` mein user ka message hota hai.
* **Real-life Example:** Jaise jab aap ek diary mein apna kuch likhte ho, waise hi user ka message history mein save ho jata hai, jise baad mein assistant process karega.

#### **12. `response = Runner.run_streamed(...)`**

* **Explanation:** Ye line `Runner.run_streamed` ko call karti hai, jo streaming mode mein response generate karta hai. `starting_agent=await (UrduBot())` ka matlab hai ke hum `UrduBot` ko start kar rahe hain, aur `input=history` ka matlab hai ke hum previous history ko input ke roop mein use kar rahe hain.
* **Real-life Example:** Jaise aap ek live news feed dekh rahe ho, aur aapko continuously new updates mil rahi hain. Yahan `run_streamed` aise hi kaam karta hai, jo continuous stream of data ko handle karta hai.

---

### Code:

```python
async for event in response.stream_events():
    if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
        token = event.data.delta
        await msg.stream_token(token)
history.append({"role": "assistant", "content": msg.content})
```

### Explanation:

#### **1. `async for event in response.stream_events():`**

* **Explanation:** Ye ek `asynchronous for loop` hai, jo events ko continuously stream karta hai. Matlab jab bhi koi new event aata hai, wo immediately process hota hai bina kisi block ke.
* **Real-life Example:** Socho aap ek live cricket match dekh rahe hain, jahan har ball ke baad score update hota hai. Aapko har update ek ek karke milti rehti hai, bina match ko pause kiye. Jaise live match update ho raha hai, waise hi `async for` har event ko stream karta hai.

#### **2. `if event.type == "raw_response_event" and hasattr(event.data, 'delta'):`**

* **Explanation:** Is line mein, hum check karte hain ke kya event ka type "raw_response_event" hai (matlab ek direct response hai jo system ne bheja), aur kya event mein `delta` attribute (jo nayi update ya token hai) maujood hai.
* **Real-life Example:** Maan lo aap ek customer service chatbot use kar rahe hain. Jab chatbot ka response directly aapko milta hai, wo ek "raw response" hota hai, jo seedha aapke screen pe aata hai bina kisi formatting ya processing ke. Agar response mein koi naya update (jaise ek token) ho, toh wo `delta` ke roop mein store hota hai.

#### **3. `token = event.data.delta`**

* **Explanation:** Agar condition satisfy hoti hai, toh `delta` ko `token` variable mein store kiya jaata hai. `delta` basically wo nayi information hai jo stream ke through aayi hoti hai.
* **Real-life Example:** Socho aap ek live chat mein ho aur koi person typing kar raha hai, toh har new character ko token ke roop mein capture kiya jaata hai. Har new update jo aapke screen pe dikhayi jaati hai, wo ek naya `token` hota hai.

#### **4. `await msg.stream_token(token)`**

* **Explanation:** Ye line asynchronous hoti hai, jo `token` ko stream karne ka kaam karti hai. Matlab, jo naya data (`token`) abhi aaya hai, wo kisi aur part of the system (jaise UI) tak pohchaya jaata hai.
* **Real-life Example:** Socho ke aap ek live chat mein ho, aur har time koi user typing kar raha ho, aapke screen par ek ek letter appear hota hai. Ye function har ek token (ya character) ko show karne ka kaam karta hai, jaise chat box mein har ek message dikhta hai.

#### **5. `history.append({"role": "assistant", "content": msg.content})`**

* **Explanation:** Is line mein `history` naam ki list ko update kiya ja raha hai, jisme `role` ke roop mein "assistant" aur `msg.content` ko add kiya ja raha hai. Ye record rakhta hai ke jo response assistant ne diya hai, wo kya tha.
* **Real-life Example:** Agar aap ek customer support chat mein ho, toh har reply jo assistant deta hai, wo ek history ke roop mein store hota hai. Har naya message history mein add hota rehta hai, jise aap baad mein dekh sakte ho.

---

### **Detailed Breakdown of Each Term:**

#### **1. `stream_events()`**

* **Explanation:** `stream_events()` ek method hai jo events ko asynchronously stream karta hai. Iska matlab hai ki events ek ek karke aapko bina rukawat ke milte hain, jaise real-time updates.
* **Real-life Example:** Maan lo aap ek live sports match dekh rahe ho. Har ball ke baad score update hoti hai. Aapko ye updates bina rukhe milte hain. Ye event stream waise hi kaam karta hai.

#### **2. `event.type`**

* **Explanation:** `event.type` ek property hai jo event ke type ko batata hai. Jaise kisi event ka type "raw_response_event" ho sakta hai.
* **Real-life Example:** Socho aap ek weather app use kar rahe ho. Jab koi weather update hoti hai, toh uska ek type ho sakta hai jaise "rain", "sunny", ya "cloudy". Aap us update ka type dekh ke samajhte ho ke kya ho raha hai.

#### **3. `raw_response_event`**

* **Explanation:** Ye ek specific type ka event hota hai, jo system se directly response ko represent karta hai. Matlab jab koi raw response (jaise ek simple message) milta hai.
* **Real-life Example:** Socho aap ek customer service chatbot use kar rahe ho. Jab chatbot ka response directly aapko milta hai, wo ek "raw response" hota hai, bina kisi formatting ke.

#### **4. `hasattr()`**

* **Explanation:** `hasattr()` ek function hai jo check karta hai ke kya kisi object mein ek specific attribute (property) hai ya nahi. Agar wo attribute exist karta hai, toh ye `True` return karta hai, otherwise `False`.
* **Real-life Example:** Socho ke aap ek toolbox mein koi tool dhoond rahe ho. Aap check karte ho ke kya toolbox mein screwdriver hai ya nahi. Agar screwdriver hai, toh aap usse use karenge. `hasattr()` waise hi check karta hai ke object mein `delta` naam ka attribute hai ya nahi.

#### **5. `event`**

* **Explanation:** `event` ek object hai jo ek event ko represent karta hai. Har event ka apna kuch data hota hai, jo event ke baare mein information deta hai.
* **Real-life Example:** Socho aap ek online order place karte ho. Jab order successfully place ho jaata hai, toh wo ek event trigger karta hai. Is event mein order ka number, date, aur status hoti hai.

#### **6. `data`**

* **Explanation:** `data` wo information hoti hai j event ke saath aati hai. Har event ka apna `data` hota hai jo uske context ko explain karta hai.
* **Real-life Example:** Socho ke aap ek online shopping website use kar rahe ho. Jab aap item add karte ho, toh wo ek `data` generate karta hai jisme item ka naam, price, aur quantity hoti hai.

#### **7. `delta`**

* **Explanation:** `delta` ek specific property hai jo kisi update mein jo badlaav ya naya data aa raha hai, usko represent karta hai.
* **Real-life Example:** Maan lo aap ek live news app use kar rahe ho. Jab koi breaking news hoti hai (jaise "Breaking News: XYZ"), toh `delta` wo nayi information hoti hai jo abhi update hui hai.

---
