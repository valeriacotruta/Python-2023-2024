def is_empty(value):
    return value.strip() != ''


def is_integer(value):
    try:
        if isinstance(value, int):
            return True
    except ValueError:
        return False
