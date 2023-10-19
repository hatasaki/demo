import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# openaiのエンドポイントとバージョンを環境変数から取得
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
# openaiのapiタイプをAzureに設定
openai.api_type = "azure"

# Define function to query API
def ask_openai(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {question}\nA:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return answer

# Create Streamlit app
st.title("Ask OpenAI")
question = st.text_input("Ask a question:")
if st.button("Submit"):
    answer = ask_openai(question)
    st.write(answer)