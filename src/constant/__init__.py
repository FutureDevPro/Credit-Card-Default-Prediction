from datetime import datetime
import os

MONGO_DATABASE_NAME = "credit-card"
MONGO_COLLECTION_NAME = "card"
MONGO_DB_URL =  os.getenv("MONGO_DB_URL")

TARGET_COLUMN = "default payment next month"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"