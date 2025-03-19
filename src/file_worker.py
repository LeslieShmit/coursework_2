import json
from abc import ABC, abstractmethod


class FileWorker(ABC):
    """Абстрактный класс для обработки файлов с вакансиями"""

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Абстрактный метод для добавления вакансии в файл"""
        pass

    @abstractmethod
    def get_vacancy(self):
        """Абстрактный метод для получения вакансии из файла"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Абстрактный метод для удаления вакансии из файла"""
        pass


class JSONFileWorker(FileWorker):
    """Класс для работы с JSON-файлами с вакансиями"""

    def __init__(self, path: str = "vacancies.json"):
        self._path = path

    def add_vacancy(self, vacancy: dict):
        """Добавляет вакансию в JSON-файл"""
        try:
            with open(self._path, mode="r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        if any(v["url"] == vacancy["url"] for v in vacancies):
            print(f"Вакансия с url {vacancy['url']} уже существует.")
            return
        vacancies.append(vacancy)

        with open(self._path, mode="w", encoding="utf-8") as file:
            json.dump(
                vacancies, file, indent=4, ensure_ascii=False
            )

    def get_vacancy(self):
        pass

    def delete_vacancy(self):
        pass
