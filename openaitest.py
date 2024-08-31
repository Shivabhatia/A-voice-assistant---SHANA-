# """
# At the command line, only need to run once to install the package via pip:

# $ pip install google-generativeai
# """

# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCFo9WmPMCNK0AP_Cjg0D3OvDFG3qqbzQA")

# # Set up the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 0,
#   "max_output_tokens": 192,
# }

# safety_settings = [
#   {
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
#   {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#   },
# ]

# model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
#                               generation_config=generation_config,
#                               safety_settings=safety_settings)

# convo = model.start_chat(history=[
#   {
#     "role": "user",
#     "parts": ["write an email to boss for resignation"]
#   },
#   {
#     "role": "model",
#     "parts": ["## Resignation Email Templates:\n\n**Template 1: Simple & Direct**\n\nSubject: Resignation - [Your Name]\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your Job Title] at [Company Name]. My last day of employment will be [Your last day - usually 2 weeks from the date of the email]. \n\nThank you for the opportunity to work at [Company Name] for the past [Number] years. I've enjoyed my time here and appreciate the opportunities I've been given. \n\nPlease let me know how I can help to ensure a smooth transition during this time.\n\nSincerely,\n\n[Your Name]\n\n\n**Template 2:  Adding a reason for leaving**\n\nSubject: Resignation - [Your Name]\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your Job Title] at [Company Name]. My last day of employment will be [Your last day - usually 2 weeks from the date of the email]. \n\nI have accepted a position at another company that will allow me to [Reason - e.g., further develop my skills in a specific area, pursue a different career path, etc.].\n\nThank you for the opportunity to work at [Company Name] for the past [Number] years. I've enjoyed my time here and appreciate the opportunities I've been given. \n\nPlease let me know how I can help to ensure a smooth transition during this time.\n\nSincerely,\n\n[Your Name]\n\n\n**Template 3: Expressing gratitude & offering more assistance**\n\nSubject: Resignation - [Your Name]\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your Job Title] at [Company Name]. My last day of employment will be [Your last day - usually 2 weeks from the date of the email]. \n\nI am incredibly grateful for the opportunities I've been given during my time at [Company Name]. I've learned a great deal and value the experience I've gained here. \n\nI am happy to assist in any way to ensure a smooth transition during this time, including helping to train my replacement and documenting my current projects. Please let me know how I can be of service.\n\nSincerely,\n\n[Your Name]\n\n\n**Additional Tips:**\n\n* **Customize the template:**  Add personal touches to make the email more meaningful.\n* **Keep it professional:** Even if you are unhappy with the company or your boss, maintain a professional tone throughout the email. \n* **Proofread carefully:** Ensure there are no typos or grammatical errors. \n* **Be prepared to discuss your departure:** Your boss may want to schedule a meeting to discuss your resignation and next steps.\n\n\n**Please note that these are just templates, and you may need to modify them based on your specific situation.**"]
#   },
# ])

# convo.send_message("write an essay on tiger")
# print(convo.last.text)

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyCFo9WmPMCNK0AP_Cjg0D3OvDFG3qqbzQA")

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
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["write an email to boss for resignation"]
  },
  {
    "role": "model",
    "parts": ["[\n {\n  \"subject\": \"Resignation - Your Name\",\n  \"body\": \"Dear [Boss's name],\\n\\nPlease accept this email as formal notification that I am resigning from my position as [Your position] at [Company name]. My last day of employment will be [Your last day].\\n\\nThank you for the opportunity to work at [Company name] for the past [Number] years. I have enjoyed my time here and appreciate the opportunities I have been given to [List of things you've learned or experiences you've had]. I have learned a lot and grown both professionally and personally.\\n\\nI wish you and the company all the best in the future. Please let me know if there is anything I can do to help during this transition.\\n\\nSincerely,\\n[Your name]\"\n }\n]"]
  },
])

convo.send_message("write an essay on electricity")
print(convo.last.text)