import json
import requests

def emotion_detector(text_to_analyse):
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the emotion predict service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion predict API
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extract the scores from the JSON response
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    # Map the emotion scores to their respective emotions
    predicted_emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    # Find the emotion with the maximum score
    dominant_emotion = max(predicted_emotion_scores, key=predicted_emotion_scores.get)

    # Add the dominant emotion to the dictionary
    predicted_emotion_scores['dominant_emotion'] = dominant_emotion

    # Returning a response as text
    return predicted_emotion_scores