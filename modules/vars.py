import os

API_ID    = os.environ.get("API_ID", "25403301")
API_HASH  = os.environ.get("API_HASH", "d700b4abe3d023165894291b6fcbd3a0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7585830486:AAEIfqrVUoX9sSVGXaO0ICVhbQVh7EuOsyw") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
