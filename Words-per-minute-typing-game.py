import curses
from curses import wrapper

### This is my take on a great pyhton tutorial made by Tech with Tim,
### check out his YT channel at https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
### Thanks!

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to WPM game!")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.refresh()
    stdscr.getkey()

    #key = stdscr.getkey()

# Set at screen over the standardoutput screen. Also to be able to restore it afterwards
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

wrapper(main)