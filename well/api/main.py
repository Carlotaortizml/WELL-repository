from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from well.ml_logic.model import MLModel
from well.ml_logic.dialoGPT_model import DialoGPTModel

app = FastAPI()
bot = MLModel()
model = DialoGPTModel()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {"Server": "Running"}

@app.post("/send")
def get_response(input_text: str):
    input_text = str(input_text)
    response = bot.predict(input_text)
    #latest_reply = response[-1][1] if response else None
    reply = response[0] if response else None
    return {"response": reply}

@app.post("/chat")
def get_response(input_text: str):
    input_text = str(input_text)
    response = model.predict(input_text)
    #latest_reply = response[-1][1] if response else None
    reply = response if response else None
    return {"response": reply}
