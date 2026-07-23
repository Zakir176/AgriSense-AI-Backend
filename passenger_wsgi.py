import sys
import os

# Ensure the current directory is in Python module search path
sys.path.insert(0, os.path.dirname(__file__))

from a2wsgi import ASGIMiddleware
from app.main import app

# Bridge FastAPI (ASGI) to Passenger / WSGI
application = ASGIMiddleware(app)
