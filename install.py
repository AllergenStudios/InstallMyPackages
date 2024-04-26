from os.path import expanduser
import os


def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
prGreen("Installing IMP!")
os.system("python.exe -m pip install --upgrade pip --quiet")
os.system("pip install -r requirements.txt --quiet")
try:
    os.mkdir(expanduser("~") + "/imp")
except FileExistsError:
    pass

imp_main = expanduser("~") + "\\imp\\main.py"

try:
    os.replace("main.py", imp_main)
except FileNotFoundError:
    pass

prGreen("IMP is almost installed! Refer to the rest of the install process to get it set up!")
