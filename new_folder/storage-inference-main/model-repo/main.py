import logging
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting FastAPI application")

app = FastAPI()

logger.info("FastAPI application initialized")
