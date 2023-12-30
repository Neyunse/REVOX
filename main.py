from lib.revox import LoadData
from server import *
import config
if __name__ == '__main__':
  voice = start_server()
 
  try:
      if voice:
          LoadData(config.character)
  except KeyboardInterrupt:
        print("Stopped")
