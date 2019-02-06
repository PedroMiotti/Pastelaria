import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executables("Loginform.py", base = base)]

cx_Freeze.setup(
    name = "SeaofBTC-Client",
    options = {"build_exe": {"packages":["tkinter" , "sqlite3"], "include_files":["logotipo-Tio-Di.gif", "plussign.gif"]}},
    version = "0.01",
    description = "Di Pastel",
    executables = executables
    )
