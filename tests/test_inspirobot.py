from src.constants import (
    INSPIROBOT_GENERATED_IMAGE_BASE_URL,
    MAX_IMAGE_LENGTH,
    DOWNLOAD_FOLDER,
)
import os
from main import (
    generate_image,
    download_image,
    save_image,
    startup,
    load_image,
    get_new_image_scale,
    scale_image,
)
import pygame
import pytest


@pytest.fixture
def image_path() -> str:
    return os.path.join(DOWNLOAD_FOLDER, "test_image.jpg")


@pytest.fixture
def image_url() -> str:
    return "https://generated.inspirobot.me/a/wlPbX05zex.jpg"


@pytest.fixture
def image_bytes(image_path) -> bytes:
    with open(image_path, "rb") as file:
        return file.read()


def test_generate_image():
    assert generate_image().startswith(INSPIROBOT_GENERATED_IMAGE_BASE_URL)


def test_download_image(image_url):
    image = download_image(image_url)
    assert isinstance(image, bytes)


def test_save_image(image_bytes, image_path):
    save_image(image_bytes, image_path)
    assert os.path.exists(image_path)


def test_load_image(image_path):
    startup()
    image = load_image(image_path)
    assert isinstance(image, pygame.Surface)


def test_get_new_image_scale(image_path):
    startup()
    image = load_image(image_path)
    new_image_width, new_image_height = get_new_image_scale(image)
    assert new_image_width <= MAX_IMAGE_LENGTH
    assert new_image_height <= MAX_IMAGE_LENGTH


def test_scale_image(image_path):
    startup()
    image = load_image(image_path)
    scaled_image = scale_image(image)
    assert isinstance(scaled_image, pygame.Surface)
    assert scaled_image.get_size() == get_new_image_scale(image)
