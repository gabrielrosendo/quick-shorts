import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
import os
from IPython.display import Markdown
# Used to securely store your API key

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

def summarize_function(text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(f"Split the following texts by context and give me a summary of each block, include the time frames that the blocks happen: {text}.")
        return response
    except Exception as e:
        return str(e)
def find_best(text):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(f"I will provide a transcript for a video with the timestamps for it, give me the most interesting intervals of the video and that have the most potential to go viral by themselves(They should be 40-80 second long intervals): {text}")
        return response
    except Exception as e:
        return str(e)

# call the function to test
sample = "Test"
print(find_best(sample).text)