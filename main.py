import logging

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

from middleware import ExceptionHandlingMiddleware
from routes.v1.endpoints import router as router_v1

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("launch_app.log"),
        logging.StreamHandler()
    ]
)

app = FastAPI()
app.add_middleware(ExceptionHandlingMiddleware)


@app.get("/")
def root():
    return {"msg": "running"}


app.include_router(router_v1, prefix="/api/v1")

if __name__ == "__main__":
    try:
        logging.info("Starting the application")
        app.add_middleware(HTTPSRedirectMiddleware)
        uvicorn.run("main:app", host="0.0.0.0", port=8000)
    except Exception as e:
        logging.error(f"Error during application start: {str(e)}")
