#!/data/data/com.termux/files/usr/bin/python3
import os
from shutil import which
from time import sleep
from subprocess import Popen
package = "MainServiceManager"
os.chdir(os.path.dirname(__file__))
for i in os.listdir("src"):
  if os.path.exists(f"src/{i}/__init__.py"):
    Popen(["nano", f"src/{i}/__init__.py"]).wait()
    if which("autopep8"):
      Popen(["autopep8", "-r", "--in-place", f"src/{i}"]).wait()
Popen(["nano", "pyproject.toml"]).wait()
Popen(["poetry", "publish", "--build"]).wait()
Popen(["pip", "install", "-U", package]).wait()
sleep(10)
Popen(["pip", "install", "-U", package]).wait()
