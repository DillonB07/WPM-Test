import curses
import time
import random

def replit_warning(stdscr):
    stdscr.clear()
    stdscr.addstr('WARNING: You are using this project on Replit which is known to have issues with how the text is displayed. For the best experience download this project from GitHub.\nTo exit press Escape\nIf you still want to procede, press any other key.', curses.color_pair(4))
    stdscr.refresh()
    key = stdscr.getkey()
    if ord(key) == 27:
        exit('Goodbye! The GitHub repository for this project is at https://github.com/DillonB07/WPM-Test')

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome to the Speed Typing Test!')
    stdscr.addstr('\nPress any key to start the test.')
    stdscr.refresh()
    stdscr.getkey()


def load_text():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f'WPM: {wpm}')

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.perf_counter()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.perf_counter() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if ''.join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except curses.error:
            continue

        if ord(key) == 27:
            break

        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_WHITE)

    # replit_warning(stdscr)
    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(
            2, 0, 'You completed the text!\nPress Escape to exit.\nPress any other key to continue')
        key = stdscr.getkey()

        if ord(key) == 27:
            break

curses.wrapper(main)