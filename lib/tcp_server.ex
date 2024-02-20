defmodule TCPServer do
  @port 3101

  def start_link do
    {:ok, listener} =
      :gen_tcp.listen(@port, [
        :binary,
        packet: 0,
        active: false,
        reuseaddr: true,
        ip: {0, 0, 0, 0}
      ])

    accept_loop(listener)
  end

  defp accept_loop(listener) do
    {:ok, client} = :gen_tcp.accept(listener)
    spawn(fn -> handle_connection(client) end)
    accept_loop(listener)
  end

  defp handle_connection(client) do
    IO.puts("Connection accepted")

    case :gen_tcp.recv(client, 0) do
      {:ok, data} ->
        IO.puts("Received: #{inspect(data)}")
        do_action(data)
        handle_connection(client)

      {:error, reason} ->
        :gen_tcp.close(client)
        IO.puts("Connection closed: #{reason}")
    end
  end

  defp int!(int_str) do
    case(Integer.parse(int_str)) do
      {int, _} -> int
    end
  end

  defp do_action(data) do
    case(data |> String.split("/")) do
      ["set", id, x, y, to] ->
        DataStore.set_grid(id, int!(x), int!(y), to)

      ["init", "grid", id, height, width] ->
        DataStore.init_grid(id, int!(height), int!(width))

      ["init", "logs", id] ->
        DataStore.init_log(id)

      ["log", id, msg] ->
        DataStore.add_log(id, msg)

      _ ->
        IO.puts("Unmatched: #{data}")
    end
  end
end
