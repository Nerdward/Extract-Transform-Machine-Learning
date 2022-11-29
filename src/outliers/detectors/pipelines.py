from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

class OutlierDetector():
    def __init__(self, model=None) -> None:
        if model is not None:
            self.model = model

        self.pipeline = make_pipeline(StandardScaler(), self.model)
    def detect(self, data):
        return self.pipeline.fit(data).predict(data)
