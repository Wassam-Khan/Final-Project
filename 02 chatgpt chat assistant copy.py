import openai

# Set your API key and directly assign the API key here
openai.api_key = "sk-proj-apn7BSWTfOqzwGyOOYqvT3BlbkFJDG8b8WM4VKFVwijqPsYU"

# Initialize an empty list to store messages
messages = []

# Get the system message to initialize the chatbot
system_msg = input("What type of chatbot would you like to create?\n")
# Append the system message to the messages list
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")

try:
    # Start the conversation loop
    while True:
        # Get user input
        message = input()

        # Check if the user wants to quit
        if message.lower() == "quit()":
            break

        # Append the user message to the messages list
        messages.append({"role": "user", "content": message})

        # Create a completion using the OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use, here we use "gpt-3.5-turbo"
            messages=messages  # The list of messages to be sent to the model
        )

        # Extract the assistant's reply from the response
        reply = response["choices"][0]["message"]["content"]

        # Append the assistant's reply to the messages list
        messages.append({"role": "assistant", "content": reply})

        # Print the assistant's reply
        print("\n" + reply + "\n")

except Exception as e:
    # If an error occurs during the API call, it will be caught here
    print(f"An error occurred: {e}")
