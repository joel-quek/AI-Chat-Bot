import openai
from flask import Flask, request, jsonify

# Set up OpenAI API key
openai.api_key = 'your-openai-api-key'

# Initialize Flask app
app = Flask(__name__)

# Define functions to handle different types of queries

def get_class_availability(class_name):
    prompt = f"What is the availability for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_prices(class_name):
    prompt = f"What are the prices for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_syllabus_details(class_name):
    prompt = f"Can you provide the syllabus details for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_schedule(class_name):
    prompt = f"What is the schedule for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_teacher_info(teacher_name):
    prompt = f"Can you provide information about the teacher {teacher_name}?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_enrollment_process():
    prompt = "What is the enrollment process for new students?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_refund_policy():
    prompt = "What is the refund policy for the classes?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_contact_information():
    prompt = "How can I contact the education company for further questions?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_duration(class_name):
    prompt = f"What is the duration of the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_format(class_name):
    prompt = f"Is the {class_name} class conducted online or in-person?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_prerequisites(class_name):
    prompt = f"What are the prerequisites for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_class_reviews(class_name):
    prompt = f"Can you provide reviews or testimonials for the {class_name} class?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_available_discounts():
    prompt = "Are there any available discounts for the classes?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Define the Flask route to handle queries

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_type = data['type']
    class_name = data.get('class_name', '')
    teacher_name = data.get('teacher_name', '')

    if query_type == 'availability':
        response = get_class_availability(class_name)
    elif query_type == 'prices':
        response = get_class_prices(class_name)
    elif query_type == 'syllabus':
        response = get_syllabus_details(class_name)
    elif query_type == 'schedule':
        response = get_class_schedule(class_name)
    elif query_type == 'teacher_info':
        response = get_teacher_info(teacher_name)
    elif query_type == 'enrollment_process':
        response = get_enrollment_process()
    elif query_type == 'refund_policy':
        response = get_refund_policy()
    elif query_type == 'contact_information':
        response = get_contact_information()
    elif query_type == 'class_duration':
        response = get_class_duration(class_name)
    elif query_type == 'class_format':
        response = get_class_format(class_name)
    elif query_type == 'prerequisites':
        response = get_class_prerequisites(class_name)
    elif query_type == 'class_reviews':
        response = get_class_reviews(class_name)
    elif query_type == 'available_discounts':
        response = get_available_discounts()
    else:
        response = "Sorry, I don't understand your question."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
