from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NestNudge API is live 🚀"}
