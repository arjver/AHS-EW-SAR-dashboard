from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)

@app.route("/hi")
async def hello(request):
    return json({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
