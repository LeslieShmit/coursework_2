import json

from src.file_worker import JSONFileWorker


def test_add_vacancy(sample_vacancy, tmp_path):
    """Тест добавления вакансии в JSON"""
    test_file = tmp_path / "vacancies.json"  # Временный JSON-файл
    processor = JSONFileWorker(str(test_file))

    processor.add_vacancy(sample_vacancy)

    with open(test_file, encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"
    assert data[0]["url"] == sample_vacancy["url"]
