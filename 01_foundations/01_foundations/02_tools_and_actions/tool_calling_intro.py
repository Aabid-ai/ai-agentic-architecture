# Tool Calling Intro - Simple AI Agent using Tools

# Tool 1: Calculator
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# Tool 2: Fake Web Search
def web_search(query):
    return f"Search result for '{query}': Example information found online."

# Agent Logic (decides which tool to use)
def agent(user_input):
    user_input = user_input.lower()

    if "calculate" in user_input:
        try:
            parts = user_input.split()
            a = int(parts[1])
            op = parts[2]
            b = int(parts[3])
            return calculator(a, b, op)
        except:
            return "Usage: calculate 5 add 3"
    
    elif "search" in user_input:
        query = user_input.replace("search", "").strip()
        return web_search(query)

    else:
        return "I can either calculate or search. Try: 'calculate 5 add 3' or 'search AI agents'"

# Run the agent
if __name__ == "__main__":
    print("AI Agent with Tools Started (type 'exit' to stop)\n")

    while True:
        user = input("You: ")
        if user.lower() == "exit":
            break

        result = agent(user)
        print("Agent:", result)
