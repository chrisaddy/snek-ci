def echo(msg: str) -> str:
    return msg


if __name__ == "__main__":
    import sys
    msg = sys.argv[1]

    print(echo(msg))
