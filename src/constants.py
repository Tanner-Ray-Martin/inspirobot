import os

INSPIROBOT_BASE_URL = "https://inspirobot.me/"
INSPIROBOT_GENERATE_URL = INSPIROBOT_BASE_URL + "api?generate=true"
INSPIROBOT_GENERATED_IMAGE_BASE_URL = "https://generated.inspirobot.me/"
INSPIROBOT_CAPTION = "Inspirobot Display"
INSPIROBOT_GENERATE_HEADERS = {
    "Host": "inspirobot.me",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://inspirobot.me/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "Priority": "u=0",
}
INSPIROBOT_IMAGE_HEADERS = {
    "Host": "generated.inspirobot.me",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
    "Referer": "https://inspirobot.me/",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "Sec-GPC": "1",
    "Priority": "u=5, i",
}
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAX_IMAGE_LENGTH = min(WINDOW_WIDTH, WINDOW_HEIGHT)
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "downloads")
