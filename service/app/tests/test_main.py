import csv
import os
import subprocess
import sys


def test_main_script_output():
    result = subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(__file__), "..", "main.py")],
        capture_output=True,
        text=True,
        check=True
    )
    output = result.stdout
    assert "Hello World!" in output
    assert "abspath:" in output


def test_sample_csv_content():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "sample.csv")
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == [{"a": "1", "b": "1", "c": "1"}]
