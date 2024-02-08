from sanic import Sanic
from sanic.response import html, json, text

page = open("page.html").read()

data: dict[str, list[list[str]]] = {
    "test": [
            ["", "", "magnet", "yellow", "cyan"],
            ["", "red", "green", "blue", "yellow"],
            ["", "cyan", "red", "green", "blue"],
            ["blue", "yellow", "cyan", "red", "green"],
            ["green", "blue", "yellow", "cyan", "red"],
         ],
}




def make_grid(id: str):
    arr = data[id]

    height = len(arr)
    width = len(arr[0])

    table = ""
    for row in arr:
        table += "<tr>"
        for cell in row:
            table += f"<td {cell}></td>"
        table += "</tr>"

    return (page
            .replace("__height__", str(height))
            .replace("__width__", str(width))
            .replace("__table__", table)
            .replace("__id__", id)
            )

app = Sanic(__name__)

@app.get("/view/<id>")
async def main(req, id: str):
    try:
        return html(make_grid(id))
    except KeyError:
        return text("Invalid ID '" + id + "'", status=400)

@app.route("/set/<id>/<x>/<y>/<to>")
async def set_one(req, id: str, x: int, y: int, to: str):
    if to not in ["red", "green", "blue", "yellow", "cyan", "magenta", "none", "magnet"]:
        return json({"status": "error", "message": "Invalid color"}, status=400)

    to = to if to != "none" else ""

    try:
        data[id][y][x] = to
        return json({"status": "ok"})
    except KeyError:
        return json({"status": "error", "message": "Invalid ID '" + id + "'"}, status=400)
    except IndexError:
        return json({"status": "error", "message": "Invalid X or Y"}, status=400)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)