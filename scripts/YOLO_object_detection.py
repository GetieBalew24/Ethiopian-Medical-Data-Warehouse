import torch
import os
import cv2
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def load_yolo_model(model_name='yolov5s'):
    """
    Load the YOLOv5 model.

    Parameters:
    model_name (str): The version of YOLOv5 to load (e.g., 'yolov5s').

    Returns:
    model: The loaded YOLOv5 model.
    """
    return torch.hub.load('ultralytics/yolov5', model_name)