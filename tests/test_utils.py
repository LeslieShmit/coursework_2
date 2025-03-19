import json

from src.utils import print_search_query, sort_vacancies_by_top_salary


def test_print_search_query(sample_vacancies, capsys):
    keyword = "Бухгалтер"

    # Вызываем функцию
    print_search_query(sample_vacancies, keyword)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод содержит ожидаемые данные
    expected_output = json.dumps(
        [
            {
                "name": "Бухгалтер",
                "company": "Google",
                "url": "https://example.com/job1234",
                "salary": {"from": 50000, "to": 60000},
            },
            {
                "name": "бухгалтер",
                "company": "Google",
                "url": "https://example.com/job214",
                "salary": {"from": 60000, "to": 70000},
            },
        ],
        indent=4,
        ensure_ascii=False,
    )
    assert captured.out.strip() == expected_output


def test_sort_vacancies_by_top_salary(sample_vacancies, capsys):
    sort_vacancies_by_top_salary(sample_vacancies, 2)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод содержит ожидаемые данные
    expected_output = (
        "Топ 2 вакансий по зарплате:\n"
        "Вакансия: Юрист\n"
        "Зарплата: {'from': 70000, 'to': 80000}\n\n"
        "Вакансия: бухгалтер\n"
        "Зарплата: {'from': 60000, 'to': 70000}"
    ).strip()
    assert captured.out.strip() == expected_output
