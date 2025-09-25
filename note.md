# On macOS and Linux:

source fastapi-env/bin/activate

# Install FastAPI and Uvicorn:

```

pip install fastapi uvicorn

```

# Running Your FastAPI Project: Now let’s start the server using Uvicorn.

```
uvicorn main:app --reload

```

#doc

```
We define an instance of FastAPI (app).
We then create a simple route (@app.get("/")) that listens for GET requests at the root URL (/). This returns a JSON response: {"message": "Hello, World!"}.

```

#Accessing Your API: Open your browser and go to:

```
http://127.0.0.1:8000
{"message": "Hello, World!"}
```

#when outsite the dir

use ->

```
    uvicorn my_fastapi_project.main:app --reload
```
