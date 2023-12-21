from dotenv import load_dotenv
load_dotenv()
import os


broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = os.getenv('CELERY_RESULT_BACKEND')
timezone = "Asia/Kolkata"
broker_connection_retry_on_startup=True
