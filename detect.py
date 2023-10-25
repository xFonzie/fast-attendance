"""
Detection functions.
To start working with it, you have to import "get_photo" and "detect_faces" functions.
For more info, see docs of these functions.
"""
import numpy as np
import cv2
import io
from typing import Union

__author__ = "Zener085"
__version__ = "1.1"

TRAINED_MODEL_PATH = "data/trained"
TRAINED_MODEL_NAME = "frontalface_alt2.xml"
SCALE_FACTOR = 1.3
MIN_NEIGHBORS = 4

face_detector = cv2.CascadeClassifier(TRAINED_MODEL_PATH + "/" + TRAINED_MODEL_NAME)


def get_photo(__photo_lib: str, __filename: str) -> np.ndarray:
    """
    Reads a photo from the folder.

    Parameters:
        __photo_lib: Path to photo.
        __filename: Name of the file that must be loaded.

    Returns:
        Array of values representing the pixels of photo.
    """
    return cv2.cvtColor(cv2.imread(__photo_lib + "/" + __filename), cv2.COLOR_BGR2RGB)


def detect_faces(__image: Union[np.ndarray, io.BytesIO]) -> list[np.ndarray]:
    """
    Detects faces in an image.

    Parameters:
        __image: An image where the faces will be detected.

    Returns:
        A list of images within faces.
    """
    global face_detector, MIN_NEIGHBORS, SCALE_FACTOR

    if isinstance(__image, io.BytesIO):
        bytes_data = __image.getvalue()
        __image = cv2.cvtColor(cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)

    _gray = cv2.cvtColor(__image, cv2.COLOR_BGR2GRAY)
    _faces = face_detector.detectMultiScale(_gray, SCALE_FACTOR, MIN_NEIGHBORS)
    _images = []

    for (x, y, w, h) in _faces:
        face = __image[x:x + w, y:y + h]
        if 0 not in face.shape:
            _images.append(face)

    return _images
