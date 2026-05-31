"""Python 101 mini-challenges.

Each function/class below corresponds to a required problem. Students should
replace the `raise NotImplementedError` statements with working code that meets
the specification in the docstrings.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Sequence, Tuple


# Problem 1 ------------------------------------------------------------------
def temperature_logger(inputs: Iterable[str]):# -> List[Tuple[int, float]]:
    """Convert Fahrenheit readings to Celsius until 'done' is encountered.

    Args:
        inputs: Strings representing user input (e.g., values read from input()).
                Processing should stop once "done" (case-insensitive) is seen.
                Every prior entry must convert to an integer.
    
    Returns:
        A list of tuples ``[(fahrenheit, celsius_float), ...]`` preserving order.

    Raises:
        ValueError: If a non-integer entry (other than 'done') is encountered.
    """
    values=[]
    for i in inputs:
        if i.lower == 'done':
            return values
        else:
            try:
                i=int(i)
                values.append([(i,(i - 32) / 1.8)])
            except:
                raise ValueError



# Problem 2 ------------------------------------------------------------------
def top_words_from_file(path: Path, limit: int = 5) -> List[Tuple[str, int]]:
    """Return the most common words from ``path`` (case-insensitive).

    Steps students must implement:
      1. Load the file contents (UTF-8) and normalize to lowercase.
      2. Keep only alphabetic characters (treat others as separators).
      3. Count word frequency and return the ``limit`` most common entries,
         sorted by frequency desc, word asc.
    """

    raise NotImplementedError


# Problem 3 ------------------------------------------------------------------
class Inventory:
    """Track inventory counts for named items.

    Requirements:
      * Store items as ``{name: quantity}`` with integer quantities.
      * ``add_item(name, qty)`` increases quantity (qty must be positive).
      * ``remove_item(name, qty)`` decreases quantity, not below zero; raise
        ``ValueError`` if removing more than available or item missing.
      * ``total_items()`` returns the sum of all quantities.
      * ``__str__`` returns entries sorted alphabetically formatted as
        ``"item:qty"`` separated by commas.
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def add_item(self, name: str, quantity: int) -> None:
        raise NotImplementedError

    def remove_item(self, name: str, quantity: int) -> None:
        raise NotImplementedError

    def total_items(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# Problem 4 ------------------------------------------------------------------
def is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime number, False otherwise."""

    raise NotImplementedError


def next_prime(n: int) -> int:
    """Return the smallest prime strictly greater than ``n`` using is_prime."""

    raise NotImplementedError


# Problem 5 ------------------------------------------------------------------
def csv_to_json(src: Path, dest: Path) -> List[dict]:
    """Convert ``students.csv`` style data into JSON with pass/fail status.

    Requirements:
      * CSV columns: ``name,grade,major`` (grade is numeric).
      * Output JSON is a list of dicts saved to ``dest`` with an added field
        ``status`` = "pass" if grade >= 70 else "fail".
      * Return the list so tests can inspect it.
      * Handle missing files by raising ``FileNotFoundError``.
      * A sample file ``sample_students.csv`` is included in this folder and
        may be used while developing locally.
    """

    raise NotImplementedError


# Problem 6 ------------------------------------------------------------------
def password_strength(password: str) -> Tuple[int, str]:
    """Calculate a password strength score (0-5) and label.

    Scoring guidelines:
      * +1 length >= 8
      * +1 contains uppercase letter
      * +1 contains lowercase letter
      * +1 contains digit
      * +1 contains symbol (punctuation or whitespace not counting)

    Return (score, label) where label is "Weak" (0-2), "Moderate" (3-4),
    or "Strong" (5).
    """

    raise NotImplementedError


# Problem 7 ------------------------------------------------------------------
def play_hangman(secret_word: str, guesses: Sequence[str], max_attempts: int = 6) -> Tuple[bool, List[str]]:
    """Simulate a mini hangman session using predetermined guesses.

    Args:
        secret_word: Word to guess (lowercase letters).
        guesses: Ordered sequence of single-character guesses.
        max_attempts: Maximum wrong guesses allowed.

    Returns:
        Tuple ``(won, states)`` where ``won`` indicates whether the word was
        guessed and ``states`` is the progressive display ("a_p__", etc.).
    """

    raise NotImplementedError
