import openai
import json
from flask import Flask, request, jsonify

# Set up OpenAI API key
openai.api_key = 'your-openai-api-key'

# Initialize Flask app
app = Flask(__name__)

# Dictionary to store business details
business_details = {}

# Endpoint to upload business details
@app.route('/upload_details', methods=['POST'])
def upload_details():
    global business_details
    details = request.json
    business_details.update(details)
    return jsonify({"message": "Business details uploaded successfully."})

# Function to handle dynamic queries using OpenAI
def handle_query(query):
    prompt = f"""
    Here are the business details:
    {json.dumps(business_details, indent=4)}

    Respond to the following query based on the above details:
    {query}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Endpoint to handle queries
@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data['query']
    response = handle_query(query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
