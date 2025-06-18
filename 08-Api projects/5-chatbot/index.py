def get_reply(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bunch of Python code, but I'm doing great!",
        "what is your name": "I'm PyBot, your offline assistant!",
        "bye": "Goodbye! Have a great day.",
        "help": "You can ask things like 'hello', 'how are you', or say 'bye' to exit."
    }

    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I didn't understand that.")


def main():
    print("Welcome to PyBot! Type 'help' to see commands.")
    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply)
        if user_input.lower() == "bye":
            break


if __name__ == "__main__":
    main()
