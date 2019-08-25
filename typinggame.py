import random
import time


def get_words():
    return [word[1].strip("\r\n ") for word in enumerate(open("words_alpha.txt"))]

def main():
    numCorrect = 0
    words = get_words()

    finish = time.time() + 180
    start = time.time()

    while finish - time.time() > 0:
        word = random.choice(words)
        if input(f"{word}:\t").strip("\r\n ") == word:
            numCorrect += 1

    end = time.time()

    print(f"You type at {numCorrect / 3} words per minute!")
    print(f"You completed {numCorrect} words correctly.")


if __name__ == '__main__':
    main()
