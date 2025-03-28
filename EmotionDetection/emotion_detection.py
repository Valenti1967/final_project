import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    myobj = { "raw_document": { "text": text_to_analyse } }

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,
                'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    predicted_emotion_scores = {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score,
                                'joy': joy_score, 'sadness': sadness_score
    }

    dominant_emotion = max(predicted_emotion_scores, key=predicted_emotion_scores.get)

    predicted_emotion_scores['dominant_emotion'] = dominant_emotion

    return predicted_emotion_scores