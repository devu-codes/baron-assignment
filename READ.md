#### Setup project

1. Create Virtual Environment (Optional) -

   1. `python -m venv venv`
   2. `source venv/bin/activate` # Windows: venv\Scripts\activate

2. install dependencies - `pip install -r requirements.txt`
3. Run the app `uvicorn main:app --reload`

Endpoints -

1. `POST /signup` - Register User
   1. payload = {
      "username": "string",
      "password": "string"
      }
2. `POST /login` - Login with existing credentials
   1. payload = {
      "username": "string",
      "password": "string"
      }

Use Swagger UI or Postman to test these endpoints.

- Swagger UI path - `http://127.0.0.1:8000/docs`
