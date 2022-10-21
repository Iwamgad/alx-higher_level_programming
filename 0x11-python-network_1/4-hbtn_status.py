#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests

r = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:\n\t"
      "- type: {}\n\t"
      "- content: {}".format(type(r.text), r.text))
