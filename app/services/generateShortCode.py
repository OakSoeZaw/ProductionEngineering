import random
import string

from app.models.url import Url

def generate_short_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits   # a‑z, A‑Z, 0‑9
    while True:
        code = "".join(random.choices(chars, k=length))
        # Check no Url already has this short_code
        if not Url.select().where(Url.short_code == code).exists():
            return code