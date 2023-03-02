import threading
import time

from datetime import datetime

from api.decorators import TOKEN_CACHE


def _garbage_cleaner():
    while True:
        now = int(datetime.now().timestamp())

        expired_tokens = [
            token for token, data in TOKEN_CACHE.items()
            if data['exp'] <= now
        ]

        for token in expired_tokens:
            del TOKEN_CACHE[token]

        time.sleep(60)


def start_garbage_cleaner():
    t = threading.Thread(target=_garbage_cleaner, daemon=True)
    t.start()
