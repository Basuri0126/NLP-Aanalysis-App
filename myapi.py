import paralleldots as pd


class API:
    def __init__(self):
        pd.set_api_key("uKuaBuP2NGjyvS2zX6GmeATQK9RTRcLOWEX08RbOj54");

    def sentiment_analysis(self, text):
        response = pd.sentiment(text)
        return response

    def ner_analysis(self, text):
        response = pd.ner(text)
        return response

    def emotion_analysis(self, text):
        response = pd.emotion(text)
        return response

