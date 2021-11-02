import cv2
from detector import Detector

detector = Detector("Eigen")

detector.train_model()
detector.save_model()

