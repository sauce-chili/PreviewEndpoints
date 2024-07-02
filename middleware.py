import logging

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from domain.exeptions import CameraNotAvailableException, ScalesUnavailable, WeightDecodingException

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except CameraNotAvailableException as e:
            logger.error(f"Camera error occurred: {str(e)}", exc_info=True)
            return JSONResponse(
                status_code=503,
                content={"detail": f"Failed to connect to {e.cam_name} camera"},
            )
        except ScalesUnavailable as e:
            logger.error(f"Scales error occurred: {str(e)}", exc_info=True)
            return JSONResponse(
                status_code=503,
                content={"detail": f"Failed to connect to {e.scale_name} scales"},
            )
        except WeightDecodingException as e:
            logger.error(f"Weight decoding error occurred: {str(e)}", exc_info=True)
            return JSONResponse(
                status_code=400,
                content={"detail": "Failed to decode weight."},
            )
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}", exc_info=True)
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal Server Error"},
            )
