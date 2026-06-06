from mangum import Mangum
from main import app  # points to your existing main.py

handler = Mangum(app)