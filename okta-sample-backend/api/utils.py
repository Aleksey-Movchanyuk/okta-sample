import threading
import time

from datetime import datetime

from api.decorators import TOKEN_CACHE


def _garbage_cleaner():
    while True:
        now = datetime.utcnow().timestamp()

        tokens_to_remove = [key for key, data in TOKEN_CACHE.items() if data.exp <= now]
        for token in tokens_to_remove:
            TOKEN_CACHE.pop(token, None)

        time.sleep(60)


def start_garbage_cleaner():
    t = threading.Thread(target=_garbage_cleaner, daemon=True)
    t.start()
  