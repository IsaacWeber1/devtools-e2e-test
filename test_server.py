"""Test ASGI server for E2E testing.

A minimal hypercorn-compatible ASGI app that serves a health endpoint.
"""

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def health(request):
    """Health check endpoint."""
    return JSONResponse({"status": "ok"})


async def hello(request):
    """Hello endpoint."""
    return JSONResponse({"message": "hello"})


app = Starlette(
    debug=True,
    routes=[
        Route("/api/health", health),
        Route("/api/hello", hello),
    ],
)
