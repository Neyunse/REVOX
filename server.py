from lib.voicebox import CheckModule, DownLoadModule, voicevox
voicevox_server_started = False

def start_server():
  global voicevox_server_started
  if CheckModule("VOICEVOX"):
    if (voicevox_server_started):
        return voicevox_server_started
    voicevox().start()
    voicevox_server_started = True

    return voicevox_server_started

  else:
    print("The VOICEVOX module is downloading, please wait a few moments.")
    DownLoadModule("https://github.com/VOICEVOX/voicevox/releases/download/0.14.10/voicevox-windows-cpu-0.14.10.zip")
    print("The download is complete, re-run the script.")
    voicevox_server_started = False
    return voicevox_server_started