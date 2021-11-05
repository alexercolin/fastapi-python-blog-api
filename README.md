API built with FastAPI + SQLalch

<h1 align="center">
    API built with FastAPI + SQLAlchemy
</h1>
## 🔖&nbsp; About

This project was built with python using the framework FastAPI, you can create, read, update and delete blogs and users from the database SQLAlchemy. The password from the user will bem saved hashed by the bcrypt tool and to some requests you need the JWT authentication.

Folders Structure created by me =D
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   └── routers
│   │   ├── __init__.py
│   │   ├── blog.py
│   │   ├── authentication.py
│   │   └── users.py
│   └── repository
│   │   ├── blog.py
│   │   └── users.py
│   └── db
│   │    ├── database.py
│   └── core
│   │   ├── models
│   │   └── schemas
│   └── auth
│   │   ├── hashing.py
│   │   └── oauth2.py
│   │   └── token.py



```bash

    # Clone the repository
    $ git clone https://github.com/alexercolin/fastapi-python-blog-api

    # Go to the directory
    $ cd fastapi-python-blog-api

    # install dependencies
    $ pip install -r requirements.txt

    # run the server
    $ uvicorn blog.main:app --reload

    # access 
    $ localhost:8000/docs to use Swagger UI
```

