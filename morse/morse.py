import time


def dit():
    print("X", end="", flush=True)
    time.sleep(.1)
    print("\b", end="", flush=True)
    print(" ", end="", flush=True)
    time.sleep(.2)
    print("\b", end="", flush=True)

def dah():
    print("X", end="", flush=True)
    time.sleep(.3)
    print("\b", end="", flush=True)
    print(" ", end="", flush=True)
    time.sleep(.2)
    print("\b", end="", flush=True)

def a():
    dit()
    dah()
    time.sleep(.3)

def bb():
    dah()
    dit()
    dit()
    dit()
    time.sleep(.3)

def c():
    dah()
    dit()
    dah()
    dit()
    time.sleep(.3)

def d():
    dah()
    dit()
    dit()
    time.sleep(.3)

def e():
    dit()
    time.sleep(.3)

def ff():
    dit()
    dit()
    dah()
    dit()
    time.sleep(.3)

def g():
    dah()
    dah()
    dit()
    time.sleep(.3)

def h():
    dit()
    dit()
    dit()
    dit()
    time.sleep(.3)

def i():
    dit()
    dit()
    time.sleep(.3)

def j():
    dit()
    dah()
    dah()
    dah()
    time.sleep(.3)

def k():
    dah()
    dit()
    dah()
    time.sleep(.3)

def l():
    dit()
    dah()
    dit()
    dit()
    time.sleep(.3)

def m():
    dah()
    dah()
    time.sleep(.3)

def n():
    dah()
    dit()
    time.sleep(.3)

def o():
    dah()
    dah()
    dah()
    time.sleep(.3)

def p():
    dit()
    dah()
    dah()
    dit()
    time.sleep(.3)

def q():
    dah()
    dah()
    dit()
    dah()
    time.sleep(.3)

def rr():
    dit()
    dah()
    dit()
    time.sleep(.3)

def s():
    dit()
    dit()
    dit()
    time.sleep(.3)

def t():
    dah()
    time.sleep(.3)

def uu():
    dit()
    dit()
    dah()
    time.sleep(.3)

def v():
    dit()
    dit()
    dit()
    dah()
    time.sleep(.3)

def w():
    dit()
    dah()
    dah()
    time.sleep(.3)

def x():
    dah()
    dit()
    dit()
    dah()
    time.sleep(.3)

def y():
    dah()
    dit()
    dah()
    dah()
    time.sleep(.3)

def z():
    dah()
    dah()
    dit()
    dit()
    time.sleep(.3)

def space():
    time.sleep(.7)

letters = {"a": a, "b": bb, "c": c, "d": d, "e": e, "f": ff, "g": g, "h": h, "i": i, "j": j, "k": k, "l": l, "m": m, "n": n, "o": o, "p": p, "q": q, "r": rr, "s": s, "t": t, "u": uu, "v": v, "w": w, "x": x, "y": y, "z": z, " ": space}

if __name__ == '__main__':

    msg = input("Message: ")
    for letter in msg.lower():
        letters[letter]()

    