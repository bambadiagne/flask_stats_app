
import random
import string

def gen_secret_key(length:int=48):
    print("".join(random.choice(string.printable) for i in range(length)))

if(__name__=='__main__'):
    gen_secret_key()