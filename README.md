
<h1 align="center">
    API built with FastAPI + SQLAlchemy
</h1>
## 🔖&nbsp; About

This project was built with python using the framework FastAPI, you can create, read, update and delete blogs and users from the database SQLAlchemy. The password from the user will bem saved hashed by the bcrypt tool and to some requests you need the JWT authentication.

Folders Structure created by me =D

├── app<br>
│   ├── __init__.py<br>
│   ├── main.py<br>
│   ├── requirements.txt<br>
│   └── routers<br>
│   │   ├── __init__.py<br>
│   │   ├── blog.py<br>
│   │   ├── authentication.py<br>
│   │   └── users.py<br>
│   └── repository<br>
│   │   ├── blog.py<br>
│   │   └── users.py<br>
│   └── db<br>
│   │    ├── database.py<br>
│   └── core<br>
│   │   ├── models<br>
│   │   └── schemas<br>
│   └── auth<br>
│   │   ├── hashing.py<br>
│   │   └── oauth2.py<br>
│   │   └── token.py<br>



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

