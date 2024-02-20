defmodule DataStore do
  use Agent
  @file_path "data.json"

  def start_link() do
    Agent.start_link(fn -> load_data() end, name: __MODULE__)
  end

  def get(:grid, key) do
    Agent.get(__MODULE__, fn data -> data |> Map.get("grid", %{}) |> Map.get(key, []) end)
  end

  def get(:log, key) do
    Agent.get(__MODULE__, fn data -> data |> Map.get("log", %{}) |> Map.get(key, []) end)
  end

  def put(:grid, key, value) do
    Agent.update(__MODULE__, fn data ->
      grid_data = data |> Map.get("grid", %{})
      replace_at_key = grid_data |> Map.put(key, value)
      data |> Map.put("grid", replace_at_key)
    end)

    persist_data()
  end

  def put(:log, key, value) do
    Agent.update(__MODULE__, fn data ->
      log_data = data |> Map.get("log", %{})
      replace_at_key = log_data |> Map.put(key, value)
      data |> Map.put("log", replace_at_key)
    end)

    persist_data()
  end

  def init_grid(id, height, width) do
    grid = for _ <- 1..height, do: for(_ <- 1..width, do: "")
    put(:grid, id, grid)
  end

  def init_log(id) do
    put(:log, id, [
      [Helpers.get_time(), "Logging initialized on id #{id}"]
    ])
  end

  def set_grid(id, x, y, to) do
    data = get(:grid, id)
    data_y = data |> Enum.at(y)
    data_y_new = data_y |> List.replace_at(x, to)
    data_new = data |> List.replace_at(y, data_y_new)
    put(:grid, id, data_new)
  end

  def add_log(id, msg) do
    new = get(:log, id) ++ [[Helpers.get_time(), msg]]
    put(:log, id, new)
  end

  defp load_data() do
    case File.read(@file_path) do
      {:ok, contents} ->
        Jason.decode!(contents)

      {:error, reason} ->
        IO.puts("Starting with a blank DataStore (#{reason})")
        %{}
    end
  end

  defp persist_data() do
    Agent.get(__MODULE__, fn data ->
      File.write!(@file_path, Jason.encode!(data))
    end)
  end
end
