# Prompt-Engineering
Exploring different LLM models
## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-example.git
   ```
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended) depending on your python version:
   ```
   python3 -m venv venv
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
5. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
## Usage
1. Run the FastAPI application:
   for auto reload
   ```
   uvicorn main:app --reload
   ```
2. Open your web browser and go to http://localhost:8000/docs to access the interactive API documentation.
3. Test the endpoints using the provided Swagger UI or external tool like Postman
## Dependencies
FastAPI: FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

Uvicorn: Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Pydantic: Pydantic is a data validation and settings management using Python type annotations.
