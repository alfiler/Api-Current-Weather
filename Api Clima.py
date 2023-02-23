# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:30:32 2023

@author: aleja
"""

import pandas as pd
import numpy as np
import matplotlib as mtl
import requests

url_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=de4c1acbd67d09969a914a4bca2586fd')

print(url_weather.json())


