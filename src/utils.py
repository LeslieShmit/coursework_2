from typing import Any, Dict, List

from src.vacancy_worker import VacancyWorker


def print_search_query(vacancies: List) -> None:
    """Функция принимает вакансии в виде списка объектов класса VacancyWorker и выводит информацию о них в
    читабельном виде"""
    for vacancy in vacancies:
        print(f"Название вакансии: {vacancy.name}")
        print(f"Работодатель: {vacancy.employer}")
        if vacancy.salary == 0:
            print("Зарплата не указана")
        else:
            print(f"Зарплата: от {vacancy.salary}")
        print(f"Ссылка на вакансию: {vacancy.url}")
        print()


def sort_vacancies_by_top_salary(vacancies: List[VacancyWorker], n: int) -> None:
    """Функция сортирует вакансии по убыванию верхней границы зарплаты и выводит топ-N вакансий"""
    sorted_vacancies = sorted(vacancies, reverse=True)
    top_vacancies = sorted_vacancies[:n]
    print(f"Топ {n} вакансий по зарплате:")
    for vacancy in top_vacancies:
        print(f"Вакансия: {vacancy.name}")
        print(f"Зарплата: {vacancy.salary}")
        print(f"Ссылка на вакансию: {vacancy.url}")
        print()


def search_by_query_desc(desc_keyword: str, vacancies: List[Dict[str, Any]]) -> None:
    """Функция ищет вакансии по ключевому слову в описании и выводит их"""
    filtered_desc_list = []
    for vacancy in vacancies:
        if vacancy["snippet"]["requirement"]:
            if desc_keyword.lower() in vacancy["snippet"]["requirement"]:
                filtered_desc_list.append(vacancy)
        if vacancy["snippet"]["responsibility"]:
            if desc_keyword.lower() in vacancy["snippet"]["responsibility"]:
                filtered_desc_list.append(vacancy)
    if filtered_desc_list:
        for vacancy in filtered_desc_list:
            print(f"Вакансия: {vacancy['name']}")
            if vacancy["snippet"]["requirement"]:
                print(
                    f"Требования: {((vacancy["snippet"]["requirement"]).replace('<highlighttext>', '')).replace('</highlighttext>', '')}"  # noqa: E501
                )
            else:
                print("Требования: не указано")
            if vacancy["snippet"]["responsibility"]:
                print(
                    f"Обязанности: {(vacancy["snippet"]["responsibility"].replace('<highlighttext>', '')).replace('</highlighttext>', '')}"  # noqa: E501
                )
            else:
                print("Обязанности: не указано")
            print(vacancy["alternate_url"])
            print()
    else:
        print("Вакансии не найдены.")
