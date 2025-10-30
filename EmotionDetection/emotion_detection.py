"""This module provides functionality for dectect emotion of text provided."""

import requests
import json


def emotion_detector(text_to_analyze=""):
    """
        This method is using to detect emotion in a text.
    """
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        emotions = formatted_response.get('emotionPredictions')[0].get('emotion')

        for i in emotions.keys():
            result[i] = emotions[i]

        dominant = sorted(emotions, key=emotions.get, reverse=True)[0]

        result['dominant_emotion'] = dominant

        return emotions
    
    return result
