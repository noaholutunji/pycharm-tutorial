import Flask as Flask

app = Flask(__name__)

def highest_random(limit):
    highest = 0
    for i in range(6):
        r = randint(0, limit)
        if r > highest:
            highest = r
    msg = "Hello {num:d}".format(num=highest)
    return msg

