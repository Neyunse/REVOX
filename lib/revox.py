import pandas as pd
import os
from urllib.request import urlopen
from urllib.parse import urlencode
import requests
import threading
import googletrans
import json
import config
class GenVoices(threading.Thread):
  def __init__(self, text, id):
     super(GenVoices, self).__init__()
     self.text = text
     self.id = id
  def genVoices(self):
      voicevox_url = 'http://127.0.0.1:50021'
       
      tts = translate_google(self.text, config.def_lang, "JA")

      if tts:
        params_encoded = urlencode({'text': tts, 'speaker': config.speaker})
        request = requests.post(f'{voicevox_url}/audio_query?{params_encoded}')
        params_encoded = urlencode({'speaker': config.speaker, 'enable_interrogative_upspeak': True})
        request = requests.post(f'{voicevox_url}/synthesis?{params_encoded}', json=request.json())

        with open(os.path.join(os.getcwd(), "audio" ,f"{self.id}.wav"), "wb") as outfile:
            outfile.write(request.content)

  def run(self):
    self.genVoices()
  
def translate_google(text, source, target):
    try:
        translator = googletrans.Translator()
        result = translator.translate(text, src=source, dest=target)
        return result.text
    except:
        print("Error translate")
        
def detect_google(text):
    try:
        translator = googletrans.Translator(raise_exception=True)
        result = translator.detect(text)
        return result.lang.upper()
    except:
        print("Error detect")
        return
    
def LoadData(character):
  in_file = os.path.join(os.getcwd(), "dialogue.tab")
  out_file = os.path.join(os.getcwd(), "dialogue.json")
 
  if os.path.exists(in_file) and not os.path.exists(out_file):
    with open(in_file, encoding='utf-8-sig', errors='replace') as file:
      df = pd.read_table(file, 
        encoding='utf-8-sig',
      )
     
      json_data = df[['Character', "Identifier", "Dialogue"]].to_json(
        os.path.join(os.getcwd(), "dialogue.json"),
        orient="records",
        force_ascii=False
      )

      with open(os.getcwd()+"/dialogue.json", encoding="utf8") as j:
        json_data = json.load(j)

        for rp in json_data:
          if character == rp["Character"]:
            GenVoices(rp["Dialogue"], rp["Identifier"]).start()
  else:
     with open(os.getcwd()+"/dialogue.json", encoding="utf8") as j:
        json_data = json.load(j)

        for rp in json_data:
          if character == rp["Character"]:
            GenVoices(rp["Dialogue"], rp["Identifier"]).start()



      
  
 
    
  