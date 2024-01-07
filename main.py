from fastapi import FastAPI
from chunks import Chunk
import openai
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Глобальная переменная для подсчета общего количества запросов
requests_per_hour = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# инициализация индексной базы
chunk = Chunk(path_to_base="Simble.txt")

# класс с типами данных параметров
class Item(BaseModel):
    text: str

# создаем объект приложения
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

@app.get("/api/get_number_requests")
def get_number_requests():
    global requests_per_hour
    return requests_per_hour

# функция обработки post запроса + декоратор
@app.post("/api/get_answer")
def get_answer(question: Item):
    global requests_per_hour
    current_hour = datetime.now().hour
    requests_per_hour[current_hour] += 1
    answer = chunk.get_answer(query=question.text)
    return {"message": answer}
