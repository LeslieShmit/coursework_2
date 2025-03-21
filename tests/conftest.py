import pytest

from src.vacancy_worker import VacancyWorker


@pytest.fixture
def sample_vacancy():
    return {
        "name": "Python Developer",
        "company": "Google",
        "url": "https://example.com/job123",
        "salary": 100000,
    }


@pytest.fixture
def sample_vacancies():
    return [
        {
            "name": "Бухгалтер",
            "company": "Google",
            "url": "https://example.com/job1234",
            "salary": 50000,
        },
        {
            "name": "Юрист",
            "company": "Google",
            "url": "https://example.com/job1214",
            "salary": 70000,
        },
        {
            "name": "бухгалтер",
            "company": "Google",
            "url": "https://example.com/job214",
            "salary": 60000,
        },
    ]


@pytest.fixture
def list_of_objects():
    obj_1 = VacancyWorker("Бухгалтер", "https://example.com/job1234", 50000, "Google")
    obj_2 = VacancyWorker("Юрист", "https://example.com/job1214", 70000, "Google")
    obj_3 = VacancyWorker("бухгалтер", "https://example.com/job214", 60000, "Google")
    return [obj_1, obj_2, obj_3]
