import sys
import requests
import os
import subprocess
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import threading
def CheckModule(module):
  """
  The function `CheckModule` checks if a module exists in the current working directory.
  
  :param module: The parameter "module" is a string that represents the name of a module
  :return: a boolean value indicating whether the specified module exists in the current working
  directory.
  """
  
  md = os.path.exists(os.path.join(os.getcwd(),"module", module))

  return md

def DownLoadModule(url):
  with urlopen(url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall(os.path.join(os.getcwd(),"module"))


class voicevox(threading.Thread):
  def run(self):
    subprocess.Popen(os.path.join(os.getcwd(),"module", "VOICEVOX", "run.exe"))