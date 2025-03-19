class VacancyWorker:
    """Создаем класс для работы с вакансиями. В этом классе нужно
    определить атрибуты, такие как название вакансии, ссылка на вакансию,
    зарплата, краткое описание или требования и т. п. (всего не менее
    четырех атрибутов). Класс должен поддерживать методы сравнения
    вакансий между собой по зарплате и валидировать данные, которыми
    инициализируются его атрибуты."""

    __slots__ = ["name", "url", "salary", "employer"]

    name: str
    url: str
    salary: int
    employer: str

    def __init__(self, name, url, salary, employer):
        self.name = self._validate_name(name)
        self.url = self._validate_url(url)
        self.salary = self._validate_salary(salary)
        self.employer = self._validate_employer(employer)

    def _validate_name(self, name):
        """Метод для проверки того, что в name передана строка"""
        if not isinstance(name, str):
            raise ValueError("Название вакансии должно быть строкой.")
        return name

    def _validate_url(self, url):
        """Метод для проверки корректности формата url"""
        if not isinstance(url, str) or not url.startswith("http"):
            raise ValueError(
                "Ссылка на вакансию должна быть " 'строкой и начинаться с "http".'
            )
        return url

    def _validate_salary(self, salary):
        """Метод для проверки корректности значения, переданного в salary"""
        if not isinstance(salary, (int, float)) or salary < 0:
            return 0
        return salary

    def _validate_employer(self, employer):
        """Метод для проверки корректности значения, переданного в employer"""
        if not isinstance(employer, str) or not employer.strip():
            raise ValueError("Имя работодателя должно быть строкой.")
        return employer

    def __lt__(self, other):
        """Магический метод, возвращающий True, если
        зарплата текущей вакансии меньше зарплаты другой вакансии."""
        return self.salary < other.salary

    def __gt__(self, other):
        """Магический метод, возвращающий True, если
        зарплата текущей вакансии больше зарплаты другой вакансии."""
        return self.salary > other.salary

    def __eq__(self, other):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии равна зарплате другой вакансии."""
        return self.salary == other.salary

    def __le__(self, other):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии меньше или равна зарплате другой вакансии."""
        return self.salary <= other.salary

    def __ge__(self, other):
        """Магический метод, возвращающий True, если зарплата
        текущей вакансии больше или равна зарплате другой вакансии."""
        return self.salary >= other.salary

    def __str__(self):
        """Метод, возвращающий строковое представление объекта."""
        return (
            f"VacancyWorker(name={self.name}, url={self.url}, "
            f"salary={self.salary}, employer={self.employer})"
        )
