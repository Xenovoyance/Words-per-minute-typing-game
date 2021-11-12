import curses
from curses import wrapper
import time

### This is my take on a great pyhton tutorial made by Tech with Tim,
### check out his YT channel at https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
### Thanks!

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM game!")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        if target[i] == current[i]: 
            color_code = 1
        else:
            color_code = 2
        stdscr.addstr(0, i, char, curses.color_pair(color_code))

def wpm_test(stdscr):
    target_text = "Hello world this is some example text to get a valid result on the words per minute counter!"
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

        try:
            key = stdscr.getkey()
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
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)

