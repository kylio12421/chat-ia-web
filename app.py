from flask import Flask, request, jsonify, render_template
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        print(f"Erreur: {str(e)}")  # Pour le débogage
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)