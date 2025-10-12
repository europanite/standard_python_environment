import csv
import os

from app.main import run


def test_run(capfd):
    run()
    output, _ = capfd.readouterr()
    assert "Hello World!" in output


def test_sample_csv_content():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample.csv")
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == [{"a": "1", "b": "1", "c": "1"}]
