import pytest

from src.vacancy_worker import VacancyWorker


def test_vacancy_is_str():
    with pytest.raises(ValueError):
        test_entity = VacancyWorker(123, "url", 100000, "employer")


def test_salary_is_positive_number():
    test_entity = VacancyWorker(
        "Developer", "https://example.com/job123", "salary", "employer"
    )
    assert test_entity.salary == 0


def test_url_is_str():
    with pytest.raises(ValueError):
        test_entity = VacancyWorker("EnergoTech", "url", 100000, "employer")


def test_employer_is_str():
    with pytest.raises(ValueError):
        test_entity = VacancyWorker(
            "EnergoTech", "https://example.com/job123", 100000, 123
        )
