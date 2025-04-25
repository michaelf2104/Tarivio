from fastapi import FastAPI

app = FastAPI(title="Tarivio")

@app.get("/")
def read_root():
    return {"message": "Welcome to Tarivio"}