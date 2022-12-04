from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/news')
def html():
    resposne = requests.request('GET','https://newsapi.org/v2/everything?q=education&from=2022-11-04&sortBy=publishedAt&apiKey=2549e51b02384fafa6675e6eea77ba4a')
    return resposne.json()

origins = ["*"]

app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)