from src.file_worker import JSONFileWorker
from src.parser import HH
from src.utils import (print_search_query, search_by_query_desc,
                       sort_vacancies_by_top_salary)
from src.vacancy_worker import VacancyWorker


def interact():
    print("Введите имя файла, в который будет записан результат работы программы")
    file_name = input()
    file_worker_obj = JSONFileWorker(file_name)
    print("Введите ключевое слово для поиска среди вакансий на сайте hh.ru")
    keyword = input()
    vacancies = HH().load_vacancies(keyword)
    vacancies_objects = []
    for vacancy in vacancies:
        file_worker_obj.add_vacancy(vacancy)
        name = vacancy["name"]
        url = vacancy["alternate_url"]
        employer = vacancy["employer"]["name"]
        try:
            salary = vacancy["salary"]["from"]
        except TypeError:
            salary = 0
        vacancy_obj = VacancyWorker(name, url, salary, employer)
        vacancies_objects.append(vacancy_obj)
    print("Выберете одну из предложенных опций и введите его номер без точки:")
    print("1. Вывести найденные вакансии")
    print("2. Топ самых высокооплачиваемых вакансий")
    print("3. Поиск вакансий по ключевому слову в описании")
    choice = input()
    if choice not in ("1", "2", "3"):
        print("Введенные вами данные некорректны. Завершение работы программы.")
        return
    if choice == "1":
        print_search_query(vacancies_objects)
    elif choice == "2":
        print("Введите желаемое количество вакансий в топе")
        number_of_vacancies = int(input())
        sort_vacancies_by_top_salary(vacancies_objects, number_of_vacancies)
    elif choice == "3":
        print("Введите ключевое слово")
        desc_keyword = input()
        search_by_query_desc(desc_keyword, vacancies)
