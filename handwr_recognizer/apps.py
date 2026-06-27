from django.apps import AppConfig
import joblib
import os
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

class HandwrRecognizerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'handwr_recognizer'
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_model', 'digits_svm.pkl')

    def ready(self):
        data = joblib.load(self.MODEL_PATH)          # dict
        self.model = data['model']                   # the Pipeline
        self.hog_params = data['hog_params']  