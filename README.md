# learn-chatgpt
Repositorio para jugar con ChatGPT y cosas de OpenAI

API key

Crea un api key en https://platform.openai.com/api-keys

Copia este api key en flask/.env:
```
OPENAI_API_KEY=sk-...
```

Abre una consola y ejecuta los siguientes comandos para instalar las dependencias de la API de ChatGPT:

Front-end con React:
```
cd react-gpt
npm install
npm run dev
```

Con React iniciado, abre otra consola para iniciar el backend:

```
cd flask
source venv/bin/activate # (Mac, Linux) o venv\Scripts\activate (Windows)
pip install -r requirements.txt
python app.py
```

Con ambos servidores corriendo, abre tu navegador en http://localhost:5173/ y comienza a jugar con ChatGPT.

🤠