import random
import time
import os


def low_reproducibility_random(a:int, b:int) -> int:
    # Introduce entropy using system time and OS randomness
    seed = time.time() + int.from_bytes(os.urandom(4), 'little')
    random.seed(seed)

    return random.randint(a, b)

def game():
    times = low_reproducibility_random(1,14)
    print("|" * times)
    print("Your turn!")


if __name__ == '__main__':
    game()