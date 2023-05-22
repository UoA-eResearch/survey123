#!/usr/bin/env python3

import requests
import json
import pandas as pd
import os

TOKEN = os.getenv("TOKEN")
ORGANISATION_ID = os.getenv("ORGANISATION_ID", "OKRmMRUG6dRnfUBh")
SERVICE = os.getenv("SERVICE", "survey123_76e72b6460df4d599440dcb56a67b763_form")

response = requests.post(f"https://services2.arcgis.com/{ORGANISATION_ID}/arcgis/rest/services/{SERVICE}/FeatureServer/0/deleteFeatures", params = {
    "where": "1=1",
    "f": "json",
    "token": TOKEN
})
print(response)
print(response.json())
