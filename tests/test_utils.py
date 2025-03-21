
from src.utils import print_search_query, sort_vacancies_by_top_salary


def test_print_search_query(list_of_objects, capsys):

    # Вызываем функцию
    print_search_query(list_of_objects)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод содержит ожидаемые данные
    expected_output = (
        "Название вакансии: Бухгалтер\n"
        "Работодатель: Google\n"
        "Зарплата: от 50000\n"
        "Ссылка на вакансию: https://example.com/job1234\n\n"
        "Название вакансии: Юрист\n"
        "Работодатель: Google\n"
        "Зарплата: от 70000\n"
        "Ссылка на вакансию: https://example.com/job1214\n\n"
        "Название вакансии: бухгалтер\n"
        "Работодатель: Google\n"
        "Зарплата: от 60000\n"
        "Ссылка на вакансию: https://example.com/job214\n\n"
    ).strip()
    assert captured.out.strip() == expected_output


def test_sort_vacancies_by_top_salary(list_of_objects, capsys):
    sort_vacancies_by_top_salary(list_of_objects, 2)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем, что вывод содержит ожидаемые данные
    expected_output = (
        "Топ 2 вакансий по зарплате:\n"
        "Вакансия: Юрист\n"
        "Зарплата: 70000\n"
        "Ссылка на вакансию: https://example.com/job1214\n\n"
        "Вакансия: бухгалтер\n"
        "Зарплата: 60000\n"
        "Ссылка на вакансию: https://example.com/job214"
    ).strip()
    assert captured.out.strip() == expected_output
