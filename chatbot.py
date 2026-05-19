print("Simple Chatbot Started!")

while True:
    user = input("You: ")

    if user.lower() == "hello":
        print("Hi!")

    elif user.lower() == "how are you":
        print("I am fine")

    elif user.lower() == "bye":
        break

    else:
        print("I don't understand")
