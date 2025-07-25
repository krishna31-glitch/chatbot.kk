# question:answer

import  time 
now = time.ctime()

qna  = {
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm just a program, but I'm here to help you!",
    "what is your name": " I am a simple Q&A bot simple created to assist you.",
    "what is the time now": now,
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])