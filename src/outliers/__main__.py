from .utils.data import create_data
from .detectors.detection_models import DetectionModels
from .detectors import pipelines
from .definitions import MODEL_CONFIG_PATH

if __name__ == "__main__":
    data = create_data()
    models = DetectionModels(MODEL_CONFIG_PATH).get_models()
    for model in models:
        detector = pipelines.OutlierDetector(model=model)
        result = detector.detect(data)
        print(result)