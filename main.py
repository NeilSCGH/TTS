import sys
from lib.utils import *
import requests, json, base64

utils.checkRequirements(["shadow_useragent"])
import shadow_useragent

class tts():
  def __init__(self,args):
    self.utils = utils(args)
    self.setup(args)

  def setup(self,args):
    if self.utils.argExist("-h"):
      self.help()
      exit(0)

    if self.utils.argHasValue("-txt"):
      self.text=self.utils.argValue("-txt")
    else:
      print("-txt text is missing !")
      self.help()
      exit(1)

    self.voice = "fr-FR-Wavenet-C"
    self.languageCode = "fr-FR"
    self.rate = 1 #between 0 and 2
    self.pitch = 0 #between -20 and 20

    self.fileName = "output.wav"

  def help(self):
  	print("")
  	print("Usage: python main.py -txt text [-h]")
  	print("")
  	print("Options:")
  	print("   -txt text  Text to convert to speech.")
  	print("   -h         (Optional) Print this help.")
  	print("")

  def run(self):
    print("Generating... ", end="")

    ua = shadow_useragent.ShadowUserAgent()
    userAgent = ua.percent(0.05)

    url = 'https://texttospeech.googleapis.com/v1beta1/text:synthesize?key=AIzaSyCpE0t4v_h4NTJbTSEIaAuLuV0FmzahJD0'
    headers = {'Host': 'texttospeech.googleapis.com',
               'User-Agent': userAgent,
               'Referer': 'https://www.voicebooking.com/ttsfr-v5/'}


    data = '{\"input\":{\"text\":\"' + self.text + '\"},\"voice\":{\"name\":\"' + self.voice + '\",\"languageCode\":\"' + self.languageCode + '\"},\"audioConfig\":{\"audioEncoding\":\"LINEAR16\",\"speakingRate\":' + str(self.rate) + ',\"pitch\":' + str(self.pitch) + '}}'
    data=data.encode('utf-8') 
    res = requests.post(url=url, data=data, headers=headers)
    
    if res.status_code == 200: #ok
      content = res.content
      content = json.loads(content.decode('utf-8'))
      binaryAudio=content["audioContent"]

      decode_string = base64.b64decode(binaryAudio)
      wav_file = open(self.fileName, "wb")
      wav_file.write(decode_string)
      print("Done!")
    else:
      print("Failed!")

if __name__ == '__main__':
	prog = tts(sys.argv)
	prog.run()
"""
  curl -i -s -k -X $'POST' \
    --data-binary $'{\"input\":{\"text\":\"coucou\"},\"voice\":{\"name\":\"fr-FR-Wavenet-C\",\"languageCode\":\"fr-FR\"},\"audioConfig\":{\"audioEncoding\":\"LINEAR16\",\"speakingRate\":1,\"pitch\":0}}' \
    $'https://texttospeech.googleapis.com/v1beta1/text:synthesize?key=AIzaSyCpE0t4v_h4NTJbTSEIaAuLuV0FmzahJD0'
"""