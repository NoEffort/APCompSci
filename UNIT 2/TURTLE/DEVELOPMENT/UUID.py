import random
import string


def gennum(x, y, iterations):
    NUM = random.sample(range(x, y), iterations)
    return "".join(str(e) for e in NUM)


def genstr(x):
    return "".join(random.choice(string.ascii_letters) for i in range(x))


def genid():
    PREFIX = "PY."
    SUFFIX = "_2017"

    print(PREFIX + gennum(0, 9, 1) + genstr(1) + gennum(0, 9, 1) + genstr(2) +
          gennum(0, 9, 1) + genstr(3) + "-" + genstr(1) + gennum(0, 9, 3) + "-" +
          gennum(0, 9, 2) + genstr(1) + gennum(0, 9, 1) + "-" + genstr(1) + gennum(0, 9, 2) +
          genstr(1) + "-" + gennum(0, 9, 7) + genstr(1) + gennum(0, 9, 4) + SUFFIX)


genid()