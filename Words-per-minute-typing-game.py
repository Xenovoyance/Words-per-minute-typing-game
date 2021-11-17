import curses
from curses import wrapper
import time

### This is my take on a great pyhton tutorial made by Tech with Tim,
### check out his YT channel at https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
### Thanks!

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
    stdscr.addstr(3, 0, "Press ESC to quit")

    for i, char in enumerate(current):
        if target[i] == current[i]: 
            color_code = 1
        else:
            color_code = 2
            if error_switch:
                error_count_mgr(1)
                error_switch = False
        stdscr.addstr(0, i, char, curses.color_pair(color_code))

def error_count_mgr(number_of_errors=0):
    global error_count
    error_count = error_count + number_of_errors

def wpm_test(stdscr):
    global error_switch
    target_text = "Hello world"
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

        # If we are done and all characters have been written, we should stop
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
            break

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
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
            break

wrapper(main)

