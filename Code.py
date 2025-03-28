import google.generativeai as genai
import json
from create_image import create_term_image
genai.configure(api_key="AIzaSyBQaFrZpYYEpGRPTE67V5Hv90S-KbCqXqA")

pdf = genai.upload_file("/Users/_kodiko_/Downloads/Statistics.pdf")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

prompt = open("Prompt.txt").read()

response = model.generate_content([pdf, prompt], generation_config={"response_mime_type": "application/json"})
print(response.text)

terms = json.loads(response.text)

for term in terms:
    filename = term["term"].replace("/", " or ")
    create_term_image(term["term"], term["meaning"], f"output/{filename}.png")


