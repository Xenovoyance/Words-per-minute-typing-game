import curses
from curses import wrapper
import time
import random

###     This is my take on a great pyhton tutorial made by Tech with Tim, with some
###     additions not in the tuturial from start. Check out his YouTube channel at 
###     https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
###     Thanks!

# BUG: If I type multiple wrong letters and then backspace them all, 
###     the last backspace gives me a negative error count due to the fact the string at this 
###     point is correct.

# TODO: Refactor away global variables
error_count = 0
error_switch = False

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM game!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    global error_count
    global error_switch

    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
    stdscr.addstr(1, 10, f"Error counter: {error_count}")
    stdscr.addstr(3, 0, "Press ESC twice to exit game.")

    for i, char in enumerate(current):
        if target[i] == current[i]: 
            color_code = 1
        else:
            color_code = 2
            if error_switch:
                # If we get an invalid input, increase our error counter
                error_count_mgr(1)
                error_switch = False
        stdscr.addstr(0, i, char, curses.color_pair(color_code))

def error_count_mgr(number_of_errors=0):
    global error_count
    error_count = error_count + number_of_errors

def load_text():
    with open("wpm_game_text_strings.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    global error_switch
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()

    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # If we are done and all characters have been written -> stop
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
            error_switch = True
        except:
            continue

        # ord(key) 27 is the ESC key
        if ord(key) == 27:
            exit()

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
                error_count_mgr(-1)
        elif len(current_text) < len(target_text):
            current_text.append(key)

# Set at screen over the standardoutput screen. Also to be able to restore it afterwards
def main(stdscr):
    global error_count
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        error_count = 0
        wpm_test(stdscr)
        
        stdscr.addstr(3,0, "You completed the test! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            exit()

wrapper(main)
