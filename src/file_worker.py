import json
from abc import ABC, abstractmethod

from config import PATH_TO_DATA


class FileWorker(ABC):
    """Абстрактный класс для обработки файлов с вакансиями"""

    @abstractmethod
    def __init__(self, path):
        pass  # pragma: no cover

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Абстрактный метод для добавления вакансии в файл"""
        pass  # pragma: no cover

    @abstractmethod
    def get_vacancy(self, keyword):
        """Абстрактный метод для получения вакансии из файла"""
        pass  # pragma: no cover

    @abstractmethod
    def delete_vacancy(self):
        """Абстрактный метод для удаления вакансии из файла"""
        pass  # pragma: no cover


class JSONFileWorker(FileWorker):
    """Класс для работы с JSON-файлами с вакансиями"""

    def __init__(self, path):
        if path:
            self._path = PATH_TO_DATA / path
        else:
            self._path = PATH_TO_DATA / "vacancies.json"

    def add_vacancy(self, vacancy: dict):
        """Добавляет вакансию в JSON-файл"""
        try:
            with open(self._path, mode="r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        if any(v["url"] == vacancy["url"] for v in vacancies):
            return
        vacancies.append(vacancy)

        with open(self._path, mode="w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4, ensure_ascii=False)

    def get_vacancy(self, keyword: str):
        """Получение вакансий из файла по ключевому слову в описании, и их вывод в консоль в формате JSON"""
        filtered_vacancies_list = []
        try:
            with open(self._path, mode="r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Файл {self._path} не найден или содержит некорректные данные")
            return
        else:
            for v in vacancies:
                if v["snippet"]["requirement"]:
                    if keyword.lower() in v["snippet"]["requirement"]:
                        filtered_vacancies_list.append(v)
                if v["snippet"]["responsibility"]:
                    if keyword.lower() in v["snippet"]["responsibility"]:
                        filtered_vacancies_list.append(v)
            print(json.dumps(filtered_vacancies_list, indent=4, ensure_ascii=False))

    def delete_vacancy(self):
        """Удаление данных из файла"""
        with open(self._path, mode="w"):
            pass
