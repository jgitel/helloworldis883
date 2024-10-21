import streamlit as st
from openai import OpenAI
import os
import transformers
from transformers import pipeline

st.title("My Super Awesome OpenAI API Deployment!")

prompt = st.text_input("What is your prompt today?", "Damascus is")
tokens = st.text_input("How many tokens do you want your response to be today?", "50")

### Load your API Key
os.environ["OPENAI_API_KEY"] = st.secrets["MyOpenAIKey"]

### OpenAI stuff
client = OpenAI()
response = client.chat.completions.create(
  model="gpt2",
  messages=[
    {"role": "system", "content": "Complete the following prefix", max_tokens=tokens},
    {"role": "user", "content": prompt}
  ],
)

### Display
st.write(
    response.choices[0].message.content
)


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')


### Generate the answer to the question the prompt and Display result
st.write(generator(prompt, max_length=tokens, num_return_sequences=2, truncation=True)
        )
