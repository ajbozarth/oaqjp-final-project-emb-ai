import json
import requests

def emotion_detector(text_to_analyse):
    url = ('https://sn-watson-emotion.labs.skills.network'
        '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    input_json = {'raw_document': {'text': text_to_analyse}}

    response = requests.post(url, json=input_json, headers=headers)

    formatted_response = json.loads(response.text)

    output = formatted_response['emotionPredictions'][0]['emotion']
    output['dominant_emotion'] = max(output, key=output.get)

    return output