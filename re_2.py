import re
# import pyperclip


def IsAdvPw(text):
    # text = str(pyperclip.paste())
    PwRegex = re.compile(r'^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$')
    matches = PwRegex.search(text)
    if not matches:
        return False
    else:
        return True
