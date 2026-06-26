from django.apps import AppConfig
import pickle
import os
import joblib

class HandwrRecognizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handwr_recognizer'
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'digits.pkl')

    def ready(self):
        
        self.classifier, self.scaler = joblib.load(self.MODEL_PATH)