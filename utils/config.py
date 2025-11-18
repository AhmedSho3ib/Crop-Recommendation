from dotenv import load_dotenv
import os
import joblib


load_dotenv(override=True)

# .env variables
APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_FOLDER_PATH = os.path.join(BASE_DIR, 'models')

# Models
encoder_preprocessor = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'encoder_preprocessor.pkl'))
scaler_preprocessor = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'scaler_preprocessor.pkl'))
logistic_regression_model = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'logistic_regression_model.pkl'))
random_forest_model = joblib.load(os.path.join(MODELS_FOLDER_PATH, 'random_forest_model.pkl'))