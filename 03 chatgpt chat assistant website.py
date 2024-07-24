import openai
import gradio

# Set your API key and directly assign the API key here
openai.api_key = "sk-proj-apn7BSWTfOqzwGyOOYqvT3BlbkFJDG8b8WM4VKFVwijqPsYU"

# Initialize the messages list with a system message to set the context
messages = [{"role": "system",
             "content": "You are a financial expert that specializes in real estate investment and negotiation"}]


# This function takes user input, sends it to the OpenAI API, and returns the assistant's reply.
def CustomChatGPT(user_input):
    try:
        # Append the user's message to the messages list
        messages.append({"role": "user", "content": user_input})

        # Create a completion using the OpenAI ChatCompletion API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Specify the model to use, here we use "gpt-3.5-turbo"
            messages=messages  # The list of messages to be sent to the model
        )

        # Extract the assistant's reply from the response
        ChatGPT_reply = response["choices"][0]["message"]["content"]

        # Append the assistant's reply to the messages list
        messages.append({"role": "assistant", "content": ChatGPT_reply})

        # Return the assistant's reply
        return ChatGPT_reply

    except Exception as e:
        # If an error occurs during the API call, it will be caught here
        return f"An error occurred: {e}"


# Create a Gradio interface for the chatbot
# fn: The function to be called for each input
# inputs: The type of input, here we use "text"
# outputs: The type of output, here we use "text"
# title: The title of the Gradio interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

# Launch the Gradio interface
# share=True allows the interface to be shared publicly
demo.launch(share=True)
