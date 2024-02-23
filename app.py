from flask import Flask, render_template, jsonify, request
from openai import OpenAI
import env

app = Flask(__name__, static_url_path='/')
client = OpenAI(api_key=env.API_KEY)

def text_generation(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/another')
def another():
    
    return render_template('another.html')

@app.route('/getinfo',methods=['POST'])
def getinfo():
    value = request.json.get("input")
    gen = text_generation(value)
    data = {"text": gen}
    return jsonify(data)

if __name__ == '__main__':
    app.run('0.0.0.0', port=env.PORT, debug=env.DEBUG_MODE)