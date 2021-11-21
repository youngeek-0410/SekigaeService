from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import Request, Response


class HttpRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response = await call_next(request)
            request.state.db_session.commit()
            return response

        finally:
            request.state.db_session.remove()
