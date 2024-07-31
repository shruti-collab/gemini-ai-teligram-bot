"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyC4jlHF3Ie4pVdsot-ZqbYphn4YRB7oCdU")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

system_instruction = "hii\n\n"

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hii"]
  },
  {
    "role": "model",
    "parts": ["Hello! 👋 How can I help you today? 😊"]
  },
  {
    "role": "user",
    "parts": ["hello"]
  },
  {
    "role": "model",
    "parts": ["Hello! 👋  It's nice to hear from you again. 😊\n\nWhat would you like to talk about today?"]
  },
  {
    "role": "user",
    "parts": ["who are you"]
  },
  {
    "role": "model",
    "parts": ["My name is shruti, and I'm a large language model created by Google AI and being managed by shruti (project member) . I'm here to assist you with various tasks, answer your questions, and engage in conversations.  \n\nIs there anything specific you'd like to know about me or how I can help you?"]
  },
])

convo.send_message("hello! how are you doing")
print(convo.last.text)