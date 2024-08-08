from flask import Flask, request, jsonify
from openai import OpenAI
import pandas as pd

app = Flask(__name__)

# OpenAI client initialization
client = OpenAI(api_key='YOUR_API_KEY')

# Load business data
classroom_availability = pd.read_csv('classroom_availability.csv')
teacher_availability = pd.read_csv('teacher_availability.csv')
pricing_info = pd.read_csv('pricing_info.csv')

# Utility function to handle unexpected questions
def handle_unexpected_questions(question):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    response = completion.choices[0].message.content.strip()
    return response

# Endpoint for the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['input']
    
    # Check for classroom availability
    if 'classroom availability' in user_input.lower():
        response = classroom_availability.to_dict(orient='records')
    # Check for teacher availability
    elif 'teacher availability' in user_input.lower():
        response = teacher_availability.to_dict(orient='records')
    # Check for pricing information
    elif 'pricing' in user_input.lower():
        response = pricing_info.to_dict(orient='records')
    # Handle unexpected questions
    else:
        response = handle_unexpected_questions(user_input)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
