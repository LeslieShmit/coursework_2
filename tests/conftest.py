import pytest


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
            "salary": {"from": 50000, "to": 60000},
        },
        {
            "name": "Юрист",
            "company": "Google",
            "url": "https://example.com/job1214",
            "salary": {"from": 70000, "to": 80000},
        },
        {
            "name": "бухгалтер",
            "company": "Google",
            "url": "https://example.com/job214",
            "salary": {"from": 60000, "to": 70000},
        },
    ]
