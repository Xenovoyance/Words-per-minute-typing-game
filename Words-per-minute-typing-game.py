import curses
from curses import wrapper

### This is my take on a great pyhton tutorial made by Tech with Tim,
### check out his YT channel at https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
### Thanks!

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM game!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "Hello world this is some text!"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)

    while True:
        key = stdscr.getkey()
        current_text.append(key)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

    stdscr.refresh()

# Set at screen over the standardoutput screen. Also to be able to restore it afterwards
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
