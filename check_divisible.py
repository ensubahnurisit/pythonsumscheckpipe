def is_divisible(a, b):
    """Return True if a is divisible by b, else False"""
    if b == 0:
        return False
    return a % b == 0
