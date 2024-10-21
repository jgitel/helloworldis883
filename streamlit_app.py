import streamlit as st
from openai import OpenAI
import os
import transformers
from transformers import pipeline

st.title("Justin's Spectacle of Artificial Intelligence's Peak Capabilities")

prompt = st.text_input("What is your prompt today?", "Damascus is")
prompt2 = st.text_input("How many tokens do you want your response to be today?", "50")
tokens = int(prompt2)

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["MyOpenAIKey"]


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')


### Generate the answer to the prompt with low temperature and Display result
st.write(generator(prompt, max_length=tokens, temperature=0.5, num_return_sequences=1, truncation=True)
        )

### Generate the answer to the prompt with high temperature and Display result
st.write(generator(prompt, max_length=tokens, temperature=2.0, num_return_sequences=1, truncation=True)
        )
