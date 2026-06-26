from django.apps import AppConfig
import pickle
import os
import joblib

class HandwrRecognizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handwr_recognizer'
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'digits.pkl')

    def ready(self):
        # joblib.load can take a filename directly – no need for open()
        self.classifier, self.scaler = joblib.load(self.MODEL_PATH)