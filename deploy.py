import cx_Freeze
import sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]

cx_Freeze.setup(
    name = "Timer App",
    options = {"build_exe": {"packages":["tkinter"]}},
    version = "0.01",
    description = "Quick python timer application",
    executables = executables
)