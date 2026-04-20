# LLM Basics - Simple AI Chat Example

# This is a very simple simulation of how an AI model responds

def simple_ai_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "name" in user_input:
        return "I am a simple AI agent."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "I am still learning. Ask me something simple."

# Run the chatbot
if __name__ == "__main__":
    print("AI Agent Started (type 'bye' to exit)\n")

    while True:
        user = input("You: ")
        response = simple_ai_response(user)
        print("AI:", response)

        if "bye" in user.lower():
            break
