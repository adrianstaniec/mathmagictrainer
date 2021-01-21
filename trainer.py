#!/usr/bin/env python
import sys

import cursor
import getch
import simpleaudio as sa

from levels import levels

cursor.hide()
width = 7
good_sound = sa.WaveObject.from_wave_file("blaster.wav")


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def format_question(a, b, op):
    question = f"{a}".rjust(width)
    question += f"\n{op}" + f"{b}".rjust(width - 1) + "\n"
    question += "-" * width
    return question


def choose_level_generator(levels):
    n_levels = len(levels)
    level = 0
    print(f"Available levels: ")
    for i, level in enumerate(levels):
        level_name = level.__name__.replace('_',' ').ljust(36)
        print(f"  {i+1}: {level_name}  {level.__doc__}")
    while True:
        print(f"Choose level: ", end="")
        sys.stdout.flush()
        level = getch.getch()
        if level.isnumeric():
            level = int(level)
            if level >= 1 and level <= n_levels:
                break
    print(level)
    return levels[level - 1]


def wait_for_correct_answer(correct_answer):
    correct_answer = str(correct_answer)
    user_answer = []
    while "".join(user_answer) != correct_answer:
        char = getch.getch()
        if char == "q":
            print("quitter :P")
            exit()
        if char == "\x7f":
            if len(user_answer) > 0:
                user_answer.pop()
        if char in "1234567890":
            user_answer.append(char)
        print(bcolors.FAIL + "".join(user_answer).rjust(width) + "  ", end="\r")
    print(bcolors.OKGREEN + "".join(user_answer).rjust(width) + " ✔ \n" + bcolors.ENDC)
    good_sound.play()


def main():
    generate_question = choose_level_generator(levels)
    while True:
        a, b, op, correct_answer = generate_question()
        print(format_question(a, b, op))
        wait_for_correct_answer(correct_answer)


if __name__ == "__main__":
    main()
