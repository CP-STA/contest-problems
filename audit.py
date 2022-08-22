#!/usr/bin/env python

import os
import sys

# If this is python2, check if python3 is available and re-execute with that
# interpreter.
if sys.version_info.major < 3:
  try:
    # On Windows, `py -3` sometimes works.
    # Try this first, because 'python3' sometimes tries to launch the app
    # store on Windows
    os.execvp("py", ["py", "-3"] + sys.argv)
  except OSError:
    os.execvp("python3", ["python3"] + sys.argv)
        

import pytest
import argparse
import subprocess
import functools

dir_path = None
problem_path = None
parser = argparse.ArgumentParser("Audit the syntax of the problems written")
parser.add_argument("-a", "--all", action='store_true', default=False)
parser.add_argument("files", metavar='F', nargs="*")
args = parser.parse_args()

def check_dir():
  global dir_path, problem_path
  file_changed = args.files
  if not len(file_changed):
    raise ValueError("No file to test, check if you have passed in the directory or file into the command line")
  dir_path = os.path.commonpath(map(lambda x: os.path.dirname(os.path.abspath(x)) if not os.path.isdir(x) else os.path.abspath(x), file_changed))
  print("Auditing " + dir_path)
  problem_path, _ = os.path.split(dir_path)
  if not (os.path.isfile(os.path.join(problem_path, 'audit.py')) and os.path.samefile(os.path.join(problem_path, 'audit.py'), __file__)):
    raise ValueError("It appears that you are auditing multiple problem directories or changing multiple problems in one PR, please audit or PR one problem at a time.")
  return dir_path

def main():
  if args.all:
    list_of_files = subprocess.check_output(['git', 'ls-tree', '--name-only', 'master'], cwd=os.path.dirname(__file__)).splitlines()
    returncodes = []
    for path in list_of_files:
      path = path.decode('utf-8')
      abs_path = os.path.join(os.path.dirname(__file__), path)
      if os.path.isdir(abs_path) and not path.startswith('.'):
        print(['python', __file__, abs_path])
        p = subprocess.run(['python', __file__, abs_path])
        returncodes.append(p.returncode)
    return functools.reduce(lambda x, y: x | y, returncodes)
  else:
    global dir_path
    dir_path = check_dir()
    os.chdir(dir_path)
    return pytest.main(['-rs', '--dir', dir_path, os.path.join(problem_path, 'test_files.py')])

if __name__ == '__main__':
  exit(main())