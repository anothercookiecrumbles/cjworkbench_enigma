import requests
from urllib.parse import urlencode

import pandas as pd

class EnigmaDataLoader:
  @staticmethod
  def __init__(self):
    pass

  @staticmethod
  def event():
    pass

  @staticmethod
  def render(wf_module, table):
    url = wf_module.get_param_string('enigma_url')
    response = requests.get(url)
    table = pd.read_json(json.dumps(xx['result']))
    return table
