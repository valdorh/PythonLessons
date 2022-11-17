import datetime
import typing
import string


def up(text: str) -> typing.Any:
    return text.upper()


if __name__ == '__main__':
    result = 121583568563862032089
    pi = 3.141592
    s = up("pi")
    print(s)
    s = f"{result:,.2f}"
    today = datetime.datetime.now()
    s1 = f"Today: {today:%d-%m-%Y  %H:%M}"
    print(s)
    print(s1)
