import datetime


def up(text):
    return text.upper()


if __name__ == '__main__':
    result = 121583568563862032089
    pi = 3.141592
    s = f"{result:,.2f}"
    today = datetime.datetime.now()
    s1 = f"Today: {today:%d-%m-%Y  %H:%M}"
    print(s)
    print(s1)
