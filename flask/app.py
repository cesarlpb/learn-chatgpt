from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from openai import OpenAI
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación

# Obtener la API key de OpenAI desde las variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configure OpenAI API key
client = OpenAI(
    api_key=openai_api_key,
)

@app.route('/api/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    try:
        # Hacer solicitud a OpenAI completions API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente que ayuda a quien pregunta. Responde al prompt."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extraer el texto de la respuesta
        response_text = completion.choices[0].message.content

        return jsonify({'response': response_text}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
