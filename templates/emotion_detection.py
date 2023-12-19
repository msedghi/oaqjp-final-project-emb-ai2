import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    return response.text

def emotion_predictor(text_to_analyze):
    response_text = emotion_detector(text_to_analyze)
    formatted_response = json.loads(response_text)

    labels = {'anger', 'disgust', 'fear', 'joy', 'sadness'}
    result = {}
    max_score = float('-inf')
    dominant_emotion = ""

    for label in labels:
        score = formatted_response['emotionPredictions'][0]['emotion'][label]
        result[label] = score
        if score > max_score:
            max_score = score
            dominant_emotion = label

    result['dominant_emotion'] = dominant_emotion

    return result
    
