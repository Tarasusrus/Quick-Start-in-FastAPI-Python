# Импортируем необходимый класс для определения модели данных
from pydantic import BaseModel


# Создаём модель данных, которая будет представлять пользователя
class User(BaseModel):
    id: int  # Поле для хранения идентификатора пользователя (целочисленное значение)
    name: str  # Поле для хранения имени пользователя (строковое значение)
    age: int  # Поле для хранения возраста пользователя (целочисленное значение)


# Фейковые данные о пользователе
external_data = {
    "id": "1",  # Внимание: "id" указано в кавычках, это строковое значение, а не целое число
    "name": "John Doe",  # Имя пользователя "John Doe"
}

"""Расширьте существующее приложение FastAPI, создав конечную точку POST, которая позволяет пользователям отправлять 
отзывы. Конечная точка должна принимать данные JSON, содержащие имя пользователя и сообщение обратной связи.
Определите Pydantic модель с именем "Feedback" (обратная связь) со следующими полями:
   - `name` (str)
   - `message` (str)
"""


class Feedback(BaseModel):
    name: str
    message: str
