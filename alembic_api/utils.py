import os


def get_current_path() -> str:
    return os.path.join(os.path.dirname(__file__))
