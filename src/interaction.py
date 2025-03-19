from src.parser import HH
from src.utils import (print_search_query, search_by_query_desc,
                       sort_vacancies_by_top_salary)


def interact():
    print("Выберете одну из предложенных опций и введите его номер без точки:")
    print("1. Поиск вакансий на сайте hh.ru по ключевому слову")
    print("2. Топ самых высокооплачиваемых вакансий")
    print("3. Поиск вакансий по ключевому слову в описании")
    choice = input()
    if choice not in ("1", "2", "3"):
        print("Введенные вами данные некорректны. Завершение работы программы.")
        return
    if choice == "1":
        print("Введите ключевое слово")
        keyword = input()
        vacancies = HH().load_vacancies(keyword)
        print_search_query(vacancies, keyword)
    elif choice == "2":
        print("Введите желаемое количество вакансий в топе")
        number_of_vacancies = int(
            input()
        )
        vacancies = HH().load_vacancies()
        sort_vacancies_by_top_salary(vacancies, number_of_vacancies)
    elif choice == "3":
        print("Введите ключевое слово")
        desc_keyword = input()
        vacancies = HH().load_vacancies()
        search_by_query_desc(desc_keyword, vacancies)
