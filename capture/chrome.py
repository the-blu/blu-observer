import os
from multiprocessing import Process, Value

class Chrome(object):
  def __init__(self):
    super(Chrome,self).__init__()
    self.process = None

  def run(self):
    self.process = Process(target=self.run_headless, args=('is_run',))
    self.process.start()

  def kill_headless(self):
    os.kill(self.process.pid)

  def run_headless(self, is_run):
    # cmd = 'google-chrome --headless --disable-gpu --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 --no-sandbox'
    cmd = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --headless'
    while True:
      os.system(cmd)
    print('Chrome Headless hab been closed')

  def stop_headless(self):
    self.run = False

