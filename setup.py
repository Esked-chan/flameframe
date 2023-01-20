import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
	"packages": ["os", "pygame", "sys", "mixer", "moviepy", "enum", "refactored_very_epic_code_less_go", "video_preview"], 
	"excludes": [""],
	"include_files": ["herculanum.ttf", "images/", "sounds/", "preview.mp4"],
	"zip_exclude_packages": ["os", "pygame", "sys", "mixer", "moviepy", "enum", "refactored_very_epic_code_less_go", "video_preview"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="gamejam",
    version="1.0",
    description="MLDE2022",
    options={"build_exe": build_exe_options},
    executables=[Executable("menu_test.py", base=base)],
)