from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "NestNudge API is live 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

# 👇 THIS is the key
handler = Mangum(app)
