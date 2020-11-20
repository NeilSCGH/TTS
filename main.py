import sys
from lib.utils import *
#utils.checkRequirements(["numpy"])

class tts():
  def __init__(self,args):
    self.utils = utils(args)
    self.setup(args)

  def setup(self,args):
    if self.utils.argExist("-h"):
      self.help()
      exit(0)

    if self.utils.argHasValue("-txt"):
      self.firstName=self.utils.argValue("-txt")
    else:
      print("-txt text is missing !")
      self.help()
      exit(1)


  def help(self):
  	print("")
  	print("Usage: python main.py -txt text [-h]")
  	print("")
  	print("Options:")
  	print("   -txt text  Text to convert to speech.")
  	print("   -h         (Optional) Print this help.")
  	print("")

  def run(self):
    print("Running !")


if __name__ == '__main__':
	prog = tts(sys.argv)
	prog.run()