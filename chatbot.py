print("Simple AI Chatbot (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")
        
    elif user == "how are you":
        print("Bot: I am fine! How are you?")
        
    elif user == "your name":
        print("Bot: I am a simple AI chatbot.")
        
    elif user == "bye":
        print("Bot: Goodbye!")
        break
        
    else:
        print("Bot: Sorry, I don't understand.")