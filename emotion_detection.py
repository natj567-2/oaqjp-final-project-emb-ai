import requests

def emotion_detector(text_to_analyze):
    url = "YOUR_EMOTION_DETECTION_API_URL"

    response = requests.post(
        url,
        json={
            "raw_document": {
                "text": text_to_analyze
            }
        }
    )

    result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }

    # Blank input returns status code 400
    if response.status_code == 400:
        return result

    response_data = response.json()
    emotions = response_data["emotionPredictions"][0]["emotion"]

    result["anger"] = emotions["anger"]
    result["disgust"] = emotions["disgust"]
    result["fear"] = emotions["fear"]
    result["joy"] = emotions["joy"]
    result["sadness"] = emotions["sadness"]

    result["dominant_emotion"] = max(
        emotions,
        key=emotions.get
    )

    return result