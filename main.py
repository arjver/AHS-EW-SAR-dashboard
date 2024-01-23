from sanic import Sanic
from sanic.response import html



def make_grid(arr: list[list[str]]):
    height = len(arr)
    width = len(arr[0])

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
            
        </style>
    </head>
    <body>
        <table>
            __table__
        </table>
    </body>
    </html>
    """

    page = page.replace("__height__", str(height)).replace("__width__", str(width))

    table = ""
    for row in arr:
        table += "<tr>"
        for cell in row:
            table += f"<td {cell}></td>"
        table += "</tr>"
    page = page.replace("__table__", table)

    return page



# app = Sanic("MyHelloWorldApp")

# @app.get("/")
# async def hello_world(request):
#     return html(make_grid([
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"],
#         ["red", "red", "red", "red", "red", "red", "red", "red", "red", "red"]
#     ]))
    
# app.run()

print(
    make_grid(
        [
            ["red", "red", "red", "green"],
            ["magnet", "green", "green", "magnet"]
            ]
    )
)