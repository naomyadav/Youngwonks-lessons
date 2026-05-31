import json
from pathlib import Path

import pytest

import python_mini_challenge as pmc


# --------------------------- Problem 1 tests -------------------------------
def test_temperature_logger_basic():
    data = ["32", "212", "done"]
    result = pmc.temperature_logger(data)
    assert result[0][0] == 32
    assert pytest.approx(result[0][1], rel=1e-3) == 0
    assert pytest.approx(result[1][1], rel=1e-3) == 100


def test_temperature_logger_invalid():
    with pytest.raises(ValueError):
        pmc.temperature_logger(["90", "oops", "done"])


# --------------------------- Problem 2 tests -------------------------------
def my_test_top_words_from_file(tmp_path: Path):
    content = "Hello, hello! Python world. python code; world?"
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content)
    top_words = pmc.top_words_from_file(file_path, limit=3)
    assert top_words == [("hello", 2), ("python", 2), ("world", 2)]


# --------------------------- Problem 3 tests -------------------------------
def my_test_inventory_flow():
    inv = pmc.Inventory()
    inv.add_item("Apples", 5)
    inv.add_item("Bananas", 3)
    inv.add_item("Apples", 2)
    assert inv.total_items() == 10
    inv.remove_item("Bananas", 1)
    assert str(inv) == "Apples:7, Bananas:2"
    with pytest.raises(ValueError):
        inv.remove_item("Bananas", 5)


# --------------------------- Problem 4 tests -------------------------------
def my_test_prime_utils():
    assert pmc.is_prime(2)
    assert not pmc.is_prime(1)
    assert pmc.next_prime(10) == 11
    assert pmc.next_prime(11) == 13


# --------------------------- Problem 5 tests -------------------------------
def my_test_csv_to_json(tmp_path: Path):
    src = tmp_path / "students.csv"
    dest = tmp_path / "students.json"
    src.write_text("name,grade,major\nAlice,85,CS\nBob,60,Math\n")
    data = pmc.csv_to_json(src, dest)
    assert dest.exists()
    saved = json.loads(dest.read_text())
    assert saved == data
    assert data[0]["status"] == "pass"
    assert data[1]["status"] == "fail"


# --------------------------- Problem 6 tests -------------------------------
def my_test_password_strength():
    score, label = pmc.password_strength("Aa1!test")
    assert score >= 4
    assert label in {"Moderate", "Strong"}
    score2, label2 = pmc.password_strength("abc")
    assert score2 == 1
    assert label2 == "Weak"


# --------------------------- Problem 7 tests -------------------------------
def my_test_play_hangman():
    won, states = pmc.play_hangman("apple", list("aplxyz"), max_attempts=6)
    assert won is True
    assert states[-1] == "apple"

    won2, _ = pmc.play_hangman("banana", list("xyz"), max_attempts=3)
    assert won2 is False


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
