# AI-Driven Chatbot 

This project is a Flask-based AI-driven chatbot designed for an education company. The chatbot can handle various customer queries regarding class availability, prices, syllabus details, and more, using the OpenAI API.

## Features

- Upload business details such as classroom availability, teacher availability, and prices.
- Handle dynamic queries from parents and students.
- Validate and sanitize input data.
- Comprehensive error handling and logging.
- Easily extensible for additional functionalities.

## Prerequisites

- Python 3.8+
- OpenAI API Key

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-driven-chatbot.git
    cd ai-driven-chatbot
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key:**
    Replace `your-openai-api-key` in the `app.py` file with your actual OpenAI API key:
    ```python
    openai.api_key = 'your-openai-api-key'
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    flask run
    ```
    The application will start on `http://127.0.0.1:5000/`.

2. **Upload Business Details:**

    Send a `POST` request to `/upload_details` with JSON data containing classroom and teacher details:
    ```json
    {
        "classrooms": {
            "Math101": {
                "availability": "Mon-Fri 10am-12pm",
                "price": "100",
                "syllabus": "Basic Algebra, Geometry"
            }
        },
        "teachers": {
            "Mr. Smith": {
                "availability": "Mon-Wed 1pm-3pm",
                "subjects": "Math, Physics"
            }
        }
    }
    ```

3. **Query the Chatbot:**

    Send a `POST` request to `/query` with a JSON payload containing the query:
    ```json
    {
        "query": "What is the availability of Math101 class?"
    }
    ```
    The chatbot will respond based on the uploaded business details.

## Endpoints

### `/upload_details` [POST]
Uploads business details such as classroom availability, teacher availability, and prices.

**Request Body:**
```json
{
    "classrooms": {
        "ClassroomName": {
            "availability": "AvailabilityDetails",
            "price": "PriceDetails",
            "syllabus": "SyllabusDetails"
        }
    },
    "teachers": {
        "TeacherName": {
            "availability": "AvailabilityDetails",
            "subjects": "SubjectsDetails"
        }
    }
}
