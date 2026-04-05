import random
import string

from app.models.url import Url

def generate_short_code(length: int = 6) -> str:
    while True:
        code = generate_random_code
        # Check no Url already has this short_code
        if not Url.select().where(Url.short_code == code).exists():
            return code

def generate_random_code(length: int = 6) -> str:
    if not isinstance(length, int):
        raise ValueError("length need to be an integer")
    if(length > 10 or length < 0 ):
        raise ValueError("length must be between 1 and 10")
    
    
    chars = string.ascii_letters + string.digits
    return "". join(random.choices(chars, k = length))