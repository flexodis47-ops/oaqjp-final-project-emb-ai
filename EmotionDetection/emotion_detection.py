import requests  # Importa la librería request para manejar HTTP requests
import json
    # Define una función llamada emotion_detector que toma una entrada de texto (text_to_analyze)
def emotion_detector(text_to_analyze): 
    # URL del servicio EmotionPredict
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    # Crea un diccionario con el texto a analizar
    myobj = { "raw_document": { "text": text_to_analyze } } 
    # Ajusta las cabeceras requeridas para la API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    # Envia una solicitud POST request a la API con el texto y las cabeceras
    response = requests.post(url, json = myobj, headers=header)  
    # Devuelve el texto formateado como diccionario de la API
    formatted_response = json.loads(response.text)

    # Manejo de errores para entradas vacías o fallos de petición (Status 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Maneja el diccionario
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    # Lógica para encontrar la emoción dominante
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
