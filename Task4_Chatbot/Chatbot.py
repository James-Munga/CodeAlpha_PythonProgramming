
# Basic Rule-Based Chatbot

# Function to handle chatbot responses
def chatbot():

    print("====================================")
    print("          PYTHON CHATBOT")
    print("====================================")

    print("Hello! I am your Python chatbot.")
    print("You can start chatting with me.")
    print("Type 'bye' to exit.\n")

    # Main chatbot loop
    while True:

        # Get user input
        user_input = input("You: ").lower().strip()

        # Check user messages and provide responses
        if user_input == "hello" or user_input == "hi":

            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":

            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":

            print("Bot: My name is Python Chatbot.")

        elif user_input == "what can you do":

            print("Bot: I can respond to simple messages.")

        elif user_input == "thank you" or user_input == "thanks":

            print("Bot: You're welcome!")

        elif user_input == "bye" or user_input == "goodbye":

            print("Bot: Goodbye! Have a great day!")
            break

        else:

            print("Bot: Sorry, I don't understand that message.")


# Run the chatbot
chatbot()
