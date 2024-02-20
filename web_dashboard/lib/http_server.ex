# from urllib.parse import unquote

# @app.route("/set/<id>/<x>/<y>/<to>")
# async def set_one(req, id: str, x: int, y: int, to: str):
#     if to not in [
#         "red",
#         "green",
#         "blue",
#         "yellow",
#         "cyan",
#         "magenta",
#         "none",
#         "magnet",
#         "grey",
#     ]:
#         return json({"status": "error", "message": "Invalid color"}, status=400)

#     to = to if to != "none" else ""

#     try:
#         data[id][y][x] = to
#         return json({"status": "ok"})
#     except KeyError:
#         return json(
#             {"status": "error", "message": "Invalid ID '" + id + "'"}, status=400
#         )
#     except IndexError:
#         return json({"status": "error", "message": "Invalid X or Y"}, status=400)

# @app.route("/init/<id>/<height>/<width>")
# async def init(req, id: str, height: int, width: int):
#     global data
#     data[id] = [["" for _ in range(width)] for _ in range(height)]
#     save_data()
#     return json({"status": "ok"})

# @app.route("/initlog/<id>")
# async def initlog(req, id: str):
#     global data
#     data[id] = [
#         [
#             f"{datetime.now()}",
#             f"Logging initialized on id {id.replace('_log', '')}",  # Note: this text decides if it's a log or not
#         ]
#     ]
#     save_data()
#     return json({"status": "ok"})

# @app.route("/log/<id>/<msg>")
# async def log(req, id: str, msg: str):
#     global data

#     decoded_msg = unquote(msg)
#     data[id].append([f"{datetime.now()}", decoded_msg])
#     save_data()
#     return json({"status": "ok"})
defmodule HTTPServer.Router do
  use Plug.Router

  @enterid_page File.read!("enterid.html")

  plug(:match)
  plug(:dispatch)

  get "/" do
    conn
    |> put_resp_content_type("text/html")
    |> send_resp(200, @enterid_page)
  end

  get "/view/:id" do
    id = conn.params["id"]
    data = DataStore.get(:grid, id)

    if data == [] do
      conn |> send_resp(404, "Unknown ID")
    else
      conn
      |> put_resp_content_type("text/html")
      |> send_resp(
        200,
        WebUtils.make_grid(id, data)
      )
    end
  end

  get "/logs/:id" do
    id = conn.params["id"]
    data = DataStore.get(:log, id)

    if data == [] do
      conn |> send_resp(404, "Unknown ID")
    else
      conn
      |> put_resp_content_type("text/html")
      |> send_resp(
        200,
        WebUtils.make_log(id, data)
      )
    end
  end

  match _ do
    send_resp(conn, 404, "404 Not Found")
  end
end

defmodule HTTPServer do
  @port 3102

  def start() do
    IO.puts("Starting HTTP server on port #{@port}")
    Plug.Cowboy.http(HTTPServer.Router, [], port: @port)
  end
end
