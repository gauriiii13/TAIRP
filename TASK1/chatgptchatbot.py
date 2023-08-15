import openai
import streamlit as st
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a psychologist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

def main():
    st.title("Your Personal Psychologist")
    
    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        response = CustomChatGPT(user_input)
        st.text_area("Psychologist:", response, height=200)
    
if __name__ == "__main__":
    main()
