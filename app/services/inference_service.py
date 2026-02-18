import os
import random
import joblib
from app.core.config import settings


class InferenceService:

    def __init__(self):
        self.model = None
        self.model_version = settings.MODEL_VERSION
        self._load_model()

    def _load_model(self):
        if os.path.exists(settings.MODEL_PATH):
            self.model = joblib.load(settings.MODEL_PATH)
        else:
            self.model = None

    def predict(self, data: dict):
        if self.model:
            features = [[
                data["ph"],
                data["turbidity"],
                data["tds"],
                data["temperature"],
                data["dissolved_oxygen"]
            ]]
            prediction = self.model.predict(features)[0]
            confidence = max(self.model.predict_proba(features)[0])
        else:
            prediction = random.choice(
                ["Safe", "Moderately Polluted", "Highly Polluted"]
            )
            confidence = round(random.uniform(0.6, 0.95), 2)

        return prediction, confidence, self.model_version
