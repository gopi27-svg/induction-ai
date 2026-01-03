from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Induction AI Server is running"}
