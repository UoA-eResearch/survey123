#!/usr/bin/env python3

import requests
import json
import pandas as pd
import os

ORGANISATION_ID = os.getenv("ORGANISATION_ID", "OKRmMRUG6dRnfUBh")
SERVICE = os.getenv("SERVICE", "survey123_76e72b6460df4d599440dcb56a67b763_form")

df = pd.read_csv("motuora_raw_data_SR.csv")
features = [{"attributes": a} for a in df.to_dict("records")]
print(len(features))

response = requests.post(f"https://services2.arcgis.com/{ORGANISATION_ID}/arcgis/rest/services/{SERVICE}/FeatureServer/0/addFeatures", data={
    "features": json.dumps(features),
    "rollbackOnFailure": True,
    "f": "json"
})
print(response)
print(response.json())
