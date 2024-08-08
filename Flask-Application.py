import openai
import json
import logging
from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError, Field

# Set up OpenAI API key
openai.api_key = 'your-openai-api-key'

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Dictionary to store business details
business_details = {}

# Pydantic models for validation
class ClassDetails(BaseModel):
    availability: str
    price: str
    syllabus: str

class TeacherDetails(BaseModel):
    availability: str
    subjects: str

class BusinessDetails(BaseModel):
    classrooms: dict[str, ClassDetails]
    teachers: dict[str, TeacherDetails]

# Endpoint to upload business details
@app.route('/upload_details', methods=['POST'])
def upload_details():
    global business_details
    try:
        details = request.json
        validated_details = BusinessDetails(**details)
        business_details.update(validated_details.dict())
        return jsonify({"message": "Business details uploaded successfully."})
    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        return jsonify({"error": "Invalid business details"}), 400

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
    try:
        data = request.json
        query = data['query']
        response = handle_query(query)
        return jsonify({"response": response})
    except Exception as e:
        logging.error(f"Error handling query: {e}")
        return jsonify({"error": "Error processing query"}), 500

if __name__ == '__main__':
    app.run(debug=True)
