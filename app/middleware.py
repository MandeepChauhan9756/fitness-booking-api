import time
from fastapi import Request
from app.logger import logger

async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    process_time = round(time.time() - start_time, 4)
    
    logger.info(
        f"{request.method} {request.url.path} |"
        f"Status: {response.status_code} |"
        f"{process_time}s"
    )
    
    return response