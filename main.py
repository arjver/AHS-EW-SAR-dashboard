from sanic import Sanic
from sanic.response import html, json, text


page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pico Car Grid</title>
    <style>
        table {
            border-collapse: collapse;
            border-spacing: 0;
            padding: 0;
            width: 80vmin;
            height: 80vmin;
            margin: auto;
        }
        td {
            width: calc(100% / __height__);
            height: calc(100% / __width__);
            background-color: #eee;
            border: 1px solid #000;
        }
        td[red] {
            background-color: #f00;
        }
        td[green] {
            background-color: #0f0;
        }
        td[blue] {
            background-color: #00f;
        }
        td[yellow] {
            background-color: #ff0;
        }
        td[cyan] {
            background-color: #0ff;
        }
        td[magenta] {
            background-color: #f0f;
        }
        td[magnet] {
            box-shadow: inset 0 0 0 25px #eee;    
            background-color: #555;
        }
        div {
            text-align: center;
            margin-top: 1em;
            font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif
        }
    </style>
</head>
<body>
    <table>
        __table__
    </table>
    <div>
        Your group ID is: <b>__id__</b>
        <br>
    </div>
</body>
</html>
"""



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