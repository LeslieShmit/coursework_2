import json
from typing import Any, Dict, List


def print_search_query(vacancies: List[Dict[str, Any]], keyword: str) -> None:
    """Функция фильтрует вакансии по ключевому слову в названии и выводит их в формате JSON"""
    filtered_vacancies = [
        vacancy for vacancy in vacancies if keyword.lower() in vacancy["name"].lower()
    ]
    print(json.dumps(filtered_vacancies, indent=4, ensure_ascii=False))


def sort_vacancies_by_top_salary(vacancies: List[Dict[str, Any]], n: int) -> None:
    """Функция сортирует вакансии по убыванию верхней границы зарплаты и выводит топ-N вакансий"""
    sorted_vacancies = sorted(
        vacancies,
        key=lambda v: (
            (v.get("salary", {}).get("to") or v.get("salary", {}).get("from") or 0)
            if isinstance(v.get("salary"), dict)
            else 0
        ),
        reverse=True,
    )
    top_vacancies = sorted_vacancies[:n]
    print(f"Топ {n} вакансий по зарплате:")
    for vacancy in top_vacancies:
        print(f"Вакансия: {vacancy['name']}")
        print(f"Зарплата: {vacancy.get('salary', 'Не указана')}")
        print()


def search_by_query_desc(desc_keyword: str, vacancies: List[Dict[str, Any]]) -> None:
    """Функция ищет вакансии по ключевому слову в описании и выводит их"""
    filtered_desc_list = [
        vacancy
        for vacancy in vacancies
        if desc_keyword.lower() in vacancy.get("description", "").lower()
    ]

    if filtered_desc_list:
        for vacancy in filtered_desc_list:
            print(f"Вакансия: {vacancy['name']}")
            print(f"Описание: {vacancy['description']}")
            print()
    else:
        print("Вакансии не найдены.")
