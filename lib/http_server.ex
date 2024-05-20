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

  get "/plot/:id" do
    id = conn.params["id"]
    data = DataStore.get(:plot, id)

    if data == %{} do
      conn |> send_resp(404, "Unknown ID")
    else
      xvals = data |> Map.get("x", [])
      yvals = data |> Map.get("y", [])
      colors = data |> Map.get("color", [])

      conn
      |> put_resp_content_type("text/html")
      |> send_resp(
        200,
        WebUtils.make_plot(id, xvals, yvals, colors)
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
