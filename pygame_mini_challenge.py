"""Pygame-focused mini challenges for Python 101."""

from __future__ import annotations

from typing import Sequence, Tuple

try:  # pragma: no cover - import guard for environments without pygame
    import pygame
except Exception as exc:  # pragma: no cover
    raise RuntimeError(
        "pygame must be installed to work on pygame_mini_challenge.py"
    ) from exc


def init_window(size: Tuple[int, int] = (640, 480), caption: str = "Mini Challenge") -> "pygame.Surface":
    """Initialize pygame display and return the primary Surface.

    Students must:
      * Ensure pygame is initialized (``pygame.init()``).
      * Call ``pygame.display.set_mode(size)`` and set the caption.
      * Return the created Surface.
    """

    raise NotImplementedError


def compute_next_position(
    position: Tuple[float, float],
    velocity: Tuple[float, float],
    bounds: Tuple[int, int],
    radius: int = 10,
) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """Advance a bouncing ball one frame.

    The function should add ``velocity`` to ``position``. If the ball hits a
    horizontal or vertical boundary (respecting ``radius``), reverse the
    corresponding velocity component and clamp the position so the ball stays in
    bounds. Return ``(new_position, new_velocity)``.
    """

    raise NotImplementedError


def draw_scene(
    screen: "pygame.Surface",
    ball_position: Tuple[int, int],
    radius: int = 10,
    background: Tuple[int, int, int] = (30, 30, 30),
    ball_color: Tuple[int, int, int] = (200, 30, 30),
) -> None:
    """Fill the screen, draw the ball, and flip the display buffer."""

    raise NotImplementedError


def handle_events(events: Sequence["pygame.event.Event"]) -> bool:
    """Return True if the game should quit.

    Treat ``pygame.QUIT`` or ``KEYDOWN`` with ``K_ESCAPE`` as termination
    signals. All other events should leave the loop running.
    """

    raise NotImplementedError
