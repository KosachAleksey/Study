import asyncio
from dataclasses import dataclass

@dataclass
class FakeAPI:
    base_url: str  # объявляем поле класса как переменную экземпляра

    async def get_data(self, endpoint):
        print(f" API get {self.base_url}/{endpoint}")
        await asyncio.sleep(2)
        print(f"Answer from API {self.base_url}/{endpoint} got!")
        return f"Data with {endpoint}"  # возвращаем осмысленное значение

async def main():
    api = FakeAPI("https://example.com/api/v1")  # задаём базовый URL

    data1 = await api.get_data("users/1")  # меняем "user" на "users" для единообразия
    data2 = await api.get_data("posts/1")  # аналогично для "post"

    print(data1)
    print(data2)

asyncio.run(main())  # исправляем метод запуска корутины (run вместо rin)