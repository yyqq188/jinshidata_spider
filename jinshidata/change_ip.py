from stem import Signal
from stem.control import Controller
def change_ip():
  with Controller.from_port(port=9051) as controller:
      controller.authenticate(password='juhuhu')
      controller.signal(Signal.NEWNYM)