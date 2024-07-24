import openai

# Set your API key and directly assign the API key here.
openai.api_key = "sk-proj-apn7BSWTfOqzwGyOOYqvT3BlbkFJDG8b8WM4VKFVwijqPsYU"

try:
    # Create a completion using the OpenAI ChatCompletion API
    # This method sends a message to the specified model and gets a response
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use, here we use "gpt-3.5-turbo"
        messages=[{"role": "user", "content": "What do you know about moye moye?"}]
        # The message to be sent to the model
    )

    # Print the content of the response message from the model
    print(completion.choices[0].message["content"])

except Exception as e:
    # If an error occurs during the API call, it will be caught here
    print(f"An error occurred: {e}")
