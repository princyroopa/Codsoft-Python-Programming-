def chatbot():
    print("Hello! I'm Chatty the chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == 'bye':
            print("Chatty: Goodbye! Have a great day!")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatty: Hi there! How can I help you?")
        elif 'how are you' in user_input:
            print("Chatty: I'm just a program, but I'm doing fine. Thanks for asking!")
        elif 'your name' in user_input:
            print("Chatty: I'm Chatty, your friendly chatbot!")
        elif 'help' in user_input:
            print("Chatty: I'm here to chat and answer simple questions. Try asking about my name or say hello.")
        elif 'weather' in user_input:
            print("Chatty: I can't check real-time weather yet, but it’s always a good day to chat!")
        else:
            print("Chatty: I'm not sure how to respond to that. Can you ask something else?")
chatbot()
