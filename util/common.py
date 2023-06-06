import hashlib
import json
import os
import random
import re
import zipfile


def get_random_string(length=24, allowed_chars='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'):
    code = ''
    for _ in range(length):
        code += allowed_chars[random.randint(0, len(allowed_chars) - 1)]
    return code


def natural_sort_key(s, _nsre=re.compile(r"(\d+)")):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


def rand_str(length=32, type="lower_hex"):
    if type == "str":
        return get_random_string(length, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    elif type == "lower_str":
        return get_random_string(length, allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789")
    elif type == "lower_hex":
        return random.choice("123456789abcdef") + get_random_string(length - 1, allowed_chars="0123456789abcdef")
    else:
        return random.choice("123456789") + get_random_string(length - 1, allowed_chars="0123456789")
