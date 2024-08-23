from src.constants import (
    INSPIROBOT_CAPTION,
    INSPIROBOT_GENERATE_HEADERS,
    INSPIROBOT_GENERATE_URL,
    INSPIROBOT_IMAGE_HEADERS,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MAX_IMAGE_LENGTH,
    DOWNLOAD_FOLDER,
)

# Suppress the specific RuntimeWarning
import warnings
import requests  # type: ignore
import os
import time

warnings.filterwarnings("ignore", message=".*Your system is avx2 capable.*")

import pygame


def startup():
    pygame.init()


# Requests
def generate_image() -> str:
    response = requests.get(
        INSPIROBOT_GENERATE_URL, headers=INSPIROBOT_GENERATE_HEADERS
    )
    response.raise_for_status()
    return response.text


def download_image(image_url: str) -> bytes:
    response = requests.get(image_url, headers=INSPIROBOT_IMAGE_HEADERS)
    response.raise_for_status()
    return response.content


def save_image(image: bytes, filename: str):
    with open(filename, "wb") as file:
        file.write(image)


# Pygame
def create_window() -> pygame.Surface:
    return pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def create_clock() -> pygame.time.Clock:
    return pygame.time.Clock()


def get_new_image_scale(image: pygame.Surface) -> tuple[int, int]:
    image_width, image_height = image.get_size()
    new_image_height = MAX_IMAGE_LENGTH
    new_image_width = int(image_width * new_image_height / image_height)
    return new_image_width, new_image_height


def load_image(filename: str) -> pygame.Surface:
    return pygame.image.load(filename)


def scale_image(image: pygame.Surface) -> pygame.Surface:
    new_image_width, new_image_height = get_new_image_scale(image)
    return pygame.transform.scale(image, (new_image_width, new_image_height))


def load_and_scale_image(filename: str) -> pygame.Surface:
    image = pygame.image.load(filename)
    return scale_image(image)


def display_image(window: pygame.Surface, image: pygame.Surface, x: int, y: int):
    window.blit(image, (x, y))
    pygame.display.set_caption(INSPIROBOT_CAPTION)
    pygame.display.flip()


def handle_events(clock: pygame.time.Clock):
    start_time = time.time()
    while time.time() - start_time < 60:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        clock.tick(60)
    return True


def main():
    startup()
    window = create_window()
    clock = create_clock()
    running = True
    while running:
        image_url = generate_image()
        image_name = image_url.split("/")[-1]
        image = download_image(image_url)
        image_path = os.path.join(DOWNLOAD_FOLDER, image_name)
        save_image(image, image_path)
        image_surface = load_and_scale_image(image_path)
        image_width, image_height = image_surface.get_size()
        x = (WINDOW_WIDTH - image_width) // 2
        y = (WINDOW_HEIGHT - image_height) // 2
        display_image(window, image_surface, x, y)
        running = handle_events(clock)
    pygame.quit()


if __name__ == "__main__":
    main()
