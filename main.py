from fastapi import FastAPI
from chunks import Chunk
import openai
from pydantic import BaseModel
from dotenv import load_dotenv

# Глобальная переменная для подсчета общего количества запросов
total_requests = 0

# инициализация индексной базы
chunk = Chunk(path_to_base="Simble.txt")

# класс с типами данных параметров
class Item(BaseModel):
    text: str

# создаем объект приложения
app = FastAPI()

@app.get("/api/get_number_requests")
def get_number_requests():
    global total_requests
    return {"number_requests": total_requests}

# функция обработки post запроса + декоратор
@app.post("/api/get_answer")
def get_answer(question: Item):
    global total_requests
    total_requests += 1
    answer = chunk.get_answer(query=question.text)
    return {"message": answer}
