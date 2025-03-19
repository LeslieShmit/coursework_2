from abc import ABC, abstractmethod

import requests

class Parser(ABC):
    """Абстрактный класс для работы с API сервисом"""

    @abstractmethod
    def _connect_to_api(self, keyword):
        """Абстрактный метод для подключения к API"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        """Абстрактный метод для получения вакансий по ключевому слову"""
        pass

class HH(Parser):
    """Класс для работы с API hh.ru """

    def _connect_to_api(self, keyword):
        """Приватная функция подключения к API"""
        url = "https://api.hh.ru/vacancies"
        params = {"text": keyword, "per_page": 20}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Ошибка при обработке запроса: {response.status_code}")
            return None
        data = response.json()
        return data

    def load_vacancies(self, keyword=""):
        """Функция получает вакансии по ключевому слову"""
        data = self._connect_to_api(keyword)
        if data and "items" in data:
            return data["items"]
        else:
            return []
