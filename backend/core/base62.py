import random
import string

# Base62字符集 0-9 a-z A-Z
BASE62_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase

def generate_short_code(length: int = 6) -> str:
    """随机生成指定长度Base62短码"""
    return ''.join(random.choice(BASE62_CHARS) for _ in range(length))