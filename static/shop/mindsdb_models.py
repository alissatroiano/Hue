import json
from django.shortcuts import render

import requests

# server = mindsdb_sdk.connect('https://cloud.mindsdb.com', settings.MINDSDB_EMAIL, settings.MINDSDB_PASSWORD)

# def predict_artwork_titles(description):
#     """
#     A method to send outputted artwork titles to MindsDB Cloud, passing the description as the parameter
#     """

#     url = 'https://cloud.mindsdb.com'
#     payload = {'description': description}
#     response = requests.post(url, json=payload)
#     if response.ok:
#         return response.json()['predictions']
#     else:
        raise Exception('Prediction failed')

    # store the artwork description in the database
    # artwork = Product(description=description, predicted_titles=predicted_titles)
    # artwork.save()
