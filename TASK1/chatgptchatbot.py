import openai
import streamlit as st

openai.api_key = "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"

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
        st.text_area("Psychologist:", response)
    
if __name__ == "__main__":
    main()