from typing import Union
import os
import logging

import uvicorn
from fastapi import FastAPI

from logger import setup_logger
from routers.routers import register_routers

app = FastAPI()
logger = setup_logger()

register_routers(app, logger)
