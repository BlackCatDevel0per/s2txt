import subprocess
import sys
import os
# Script use only python, pip & pipwin!
# build-linux.sh - build by nuitka for linux
# This script for a while..
# For windows and linux normal build scripts/scripts coming soon
###
# Now you need to run this script in python and if you build on linux run ./build-linux.sh too


def pip(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def apt(package):
    subprocess.check_call(["sudo", "apt", "install", package])


def pipwin(package):
    subprocess.check_call([sys.executable, "-m", "pipwin", "install", package])


if os.name == "posix":  # For debian (tested on debian 10)
    subprocess.check_call(["sudo", "apt", "update"])
    pkgsl = ["portaudio19-dev", "libportaudiocpp0",
             "libportaudio2", "python3-pyqt5", "python3-pyaudio", "swig"]

elif os.name == "nt":
    pkgsl = ["pyaudio"]

else:
    print("Unknown os!")

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "--upgrade", "pip"])

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "--upgrade", "setuptools"])

subprocess.check_call([sys.executable, "-m", "pip",
                       "install", "-r", "requirements.txt"])
"""
if os.name == 'posix':
    subprocess.check_call(["sudo", sys.executable, "-m", "pip", "install", "pyaudio"])
    subprocess.check_call(["sudo", sys.executable, "-m", "pip", "install", "PyQt5"])
"""

for pkg in pkgsl:
    if os.name == 'nt':
        pipwin(pkg)
    elif os.name == 'posix':
        apt(pkg)
