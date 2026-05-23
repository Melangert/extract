Reset = "\033[0m"
Green = "\033[32m"
Yellow = "\033[33m"
Red = "\033[31m"


def success(msg: str) -> str:
    return f"{Green}✓ {msg}{Reset}"


def error(msg: str) -> str:
    return f"{Red}✗ {msg}{Reset}"


def warning(msg: str) -> str:
    return f"{Yellow}! {msg}{Reset}"