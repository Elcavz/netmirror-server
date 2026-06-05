from workers import WorkerEntrypoint
import asgi
from main import app   # Make sure 'app' is the name of your FastAPI() object

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request.js_object, self.env)