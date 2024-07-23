import PIL.Image
import google.generativeai as genai

from key import key

genai.configure(api_key=key)

img = PIL.Image.open("lixo_plastico.jpg")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

response = model.generate_content(img)
descricao_imagem = response.text

chat_session = model.start_chat(
  history=[]
)

pergunta = "existe lixo nesta imagem? "

contexto_com_pergunta = f"Baseado na seguinte descrição de imagem: {descricao_imagem}. {pergunta}"

response = chat_session.send_message(contexto_com_pergunta)
print(response.text)