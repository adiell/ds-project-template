import pwd
from pathlib import Path
import os

def get_project_root_dir():
    return Path(__file__).parent.parent

def get_source_root_dir():
    return Path(__file__).parent

def get_running_user():
    try:
        return pwd.getpwuid(os.getuid())[0]
    except:
        return "Unknown"


def copy_source_dir(source_dir, destination, entry_point, requirements_file=None):
    from subprocess import call
    call(["cp", source_dir, destination, "-r"])
    call(["cp", os.path.join(source_dir, entry_point), destination])
    if requirements_file:
        call(["cp", os.path.join(source_dir, requirements_file), os.path.join(destination, 'requirements.txt')])



