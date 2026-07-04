import csv
from pathlib import Path

import pytest

from keyword_driven.keyword_engine import KeywordEngine

TESTCASE_DIR = Path(__file__).parent / "testcases"


def _load_steps(csv_path: Path):
    with csv_path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


@pytest.mark.parametrize(
    "csv_file",
    sorted(TESTCASE_DIR.glob("*.csv")),
    ids=lambda p: p.stem,
)
def test_keyword_driven(csv_file):
    engine = KeywordEngine()

    try:
        for step in _load_steps(csv_file):
            print(
                f"-> {step['keyword']} | "
                f"{step['locator_type']} | "
                f"{step['locator']} | "
                f"{step['value']}"
            )

            engine.execite(
                step["keyword"],
                step["locator_type"],
                step["locator"],
                step["value"],
            )

    finally:
        if engine.driver:
            engine.driver.quit()