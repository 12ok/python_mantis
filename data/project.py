import random
import string
import re

from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    random_string = prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    return clear(random_string)


def clear(s):
    return re.sub(" +", " ", s)


testdata = [Project(name=random_string("name", 10), description=random_string("description", 20))]
