import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI()

DEVICE = torch.device("cpu")
# Загружаем токенизатор и модель из локальной папки
tokenizer = GPT2Tokenizer.from_pretrained("./models")
model = GPT2LMHeadModel.from_pretrained("./models").to(DEVICE)

# Pydantic модель для запроса
class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, description="Текст для генерации")

@app.get("/health")
def health():
    logger.info("request: /health")
    return {"status": "OK"}

@app.post("/predict")
def predict(request: PredictRequest):
    logger.info("request: /predict")
    logger.info(f"user's text: {request}")
    input_ids = tokenizer.encode(request.text, return_tensors="pt").to(DEVICE)
    model.eval()
    with torch.no_grad():
        out = model.generate(
            input_ids,
            do_sample=True,
            num_beams=2,
            temperature=0.7,
            top_p=0.9,
            max_length=100,
        )

    generated_text = tokenizer.decode(out[0], skip_special_tokens=True)
    logger.info(f"model's response: {generated_text}")
    return {"generated_text": generated_text}
