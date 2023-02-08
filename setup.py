import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["datetime", "time"],
    "includes": ["pywhatkit", "pyautogui"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win64GUI" if sys.platform == "win64" else None

setup(
    name="WhatsappBot",
    version="0.1",
    description="My Whatsapp Bot!",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base)],
)