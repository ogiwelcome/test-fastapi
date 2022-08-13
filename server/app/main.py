from typing import Union
import os
import logging

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.DEBUG)
    logger.info("start application......")
    uvicorn.run("main:app", port=os.getenv("PORT"))
