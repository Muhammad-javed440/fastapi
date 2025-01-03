# 1- pip install fastapi in terminal
# 2- pip install uvicorn in terminal
# 3- play the python file
# 4- uvicorn fast:app --reload in terminal
# 5- Uvicorn running on http://127.0.0.1:8000/api

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return {"message": "Hello, javed store"}
