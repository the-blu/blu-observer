import os

class Chrome(object):
  def __init__(self):
    super(Chrome,self).__init__()

  def run_headless(self):
    cmd = 'google-chrome --headless --disable-gpu --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 --no-sandbox'
    # cmd = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --headless'
    os.system(cmd)
    print('Chrome Headless hab been closed')

