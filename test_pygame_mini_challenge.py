"""Pytest suite for pygame_mini_challenge."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

pygame = pytest.importorskip("pygame")
import pygame_mini_challenge as pmc_pg


@pytest.fixture(autouse=True)
def pygame_init_teardown():
    pygame.quit()
    pygame.init()
    pygame.display.init()
    yield
    pygame.quit()


def test_init_window():
    screen = pmc_pg.init_window((320, 240), caption="Test Window")
    assert isinstance(screen, pygame.Surface)
    current = pygame.display.get_surface()
    assert current is screen
    caption, _ = pygame.display.get_caption()
    assert caption == "Test Window"


def test_compute_next_position_bounce():
    pos = (310.0, 100.0)
    vel = (15.0, 0.0)
    bounds = (320, 200)
    (new_pos, new_vel) = pmc_pg.compute_next_position(pos, vel, bounds, radius=5)
    assert new_vel[0] == pytest.approx(-15.0)
    assert new_pos[0] <= bounds[0] - 5


def test_draw_scene_writes_pixels():
    screen = pygame.display.set_mode((200, 200))
    pmc_pg.draw_scene(screen, (100, 120), radius=15, background=(0, 0, 0), ball_color=(255, 0, 0))
    assert screen.get_at((100, 120))[:3] == (255, 0, 0)


def test_handle_events():
    events = [pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE})]
    assert pmc_pg.handle_events(events) is True
    events = [pygame.event.Event(pygame.USEREVENT, {})]
    assert pmc_pg.handle_events(events) is False


if __name__ == "__main__":
    raise SystemExit(pytest.main([Path(__file__).name]))
