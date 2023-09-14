# Django Rest Framework Person API

The Django Rest Framework Person API is a web application that provides CRUD (Create, Read, Update, Delete) operations for managing information about people. It is built using Django Rest Framework and provides the following endpoints:

- `GET /api/`: Retrieve a list of all people in the database.
- `POST /api/`: Add a new person to the database.
- `GET /api/{id}/`: Retrieve a person's information based on their unique id.
- `PUT /api/{id}/`: Update a person's data by their id.
- `DELETE /api/{id}/`: Delete a person's data based on the entered id.

## Getting Started

To run the Django Rest Framework Person API on your local machine, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- svn
- git

### Installation

1. Clone this repository to your local machine(this command copies only the folder that the code is in to your local machine):

   ```
   svn export https://github.com/johnafariogun/HNGInternship/trunk/HngApi
   ```

2. Change to the project directory:

    ```
    cd your-repo
    ```

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

### Usage

1. Start the Django development server:

   ```
   python manage.py runserver
   ```

2. Access the API using the provided endpoints:

- To retrieve a list of all people: GET: http://localhost:8000/api/persons/
- To add a new person: POST: http://localhost:8000/api/persons/
- To get a person by id: GET: http://localhost:8000/api/persons/{id}/
- To update a person's data by id: PUT: http://localhost:8000/api/persons/{id}/
- To delete a person by id: DELETE: http://localhost:8000/api/persons/{id}/

## Example 1 (Adding a New Person)

**Request:**

POST: http://localhost:8000/api/persons/

```json
{
    "name": "John Doe",
    "track": "Backend",
    "slack_username": "johndoe",
    "email": "john@example.com"
}
```

**Response:**

```json
{
    "id": 3,
    "name": "Daniel",
    "track": "backend",
    "slack_username": "danilo",
    "created_at": "2023-09-14T22:13:21.670154Z",
    "email": "danio@gmail.com"
}
```

## API Endpoints

### GET /api/persons/

Use this endpoint to retrieve a list of all people in the database.

### POST /api/persons/

Use this endpoint to add a new person to the database. Send a POST request with JSON data containing the person's information, including fields like `name`, `track`, `slack_username`, and `email`.

### GET /api/persons/{id}/

Retrieve a person's information based on their unique id. Replace `{id}` in the URL with the person's actual id.

### PUT /api/persons/{id}/

Update a person's data by their id. Replace `{id}` in the URL with the person's actual id. Send a PUT request with JSON data containing the updated information.

### DELETE /api/persons/{id}/

Delete a person's data based on the entered id. Replace `{id}` in the URL with the person's actual id.

## Acknowledgments

- Django Rest Framework: https://www.django-rest-framework.org/
- Django: https://www.djangoproject.com/
- Feel free to customize this README to include your specific project details, such as repository links, installation instructions, and any additional information about your project's usage, contributors, or deployment instructions.
```
