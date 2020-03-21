#! python3
# mapIt.py launches a map in the browser using an address from the
# community line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # sys.argv 为当前运行的文件名([0]) + 命令行输入的语句([1:])
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

print("Done.")

webbrowser.open("https://www.google.com/maps/place/" + address)
