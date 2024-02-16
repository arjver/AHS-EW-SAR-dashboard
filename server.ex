defmodule TCPServer do
  def start_link do
    {:ok, listener} = :gen_tcp.listen(65432, [:binary, packet: 0, active: false, reuseaddr: true])
    spawn(fn -> accept_loop(listener) end)
  end

  defp accept_loop(listener) do
    {:ok, client} = :gen_tcp.accept(listener)
    spawn(fn -> handle_connection(client) end)
    accept_loop(listener)
  end

  defp handle_connection(client) do
    case :gen_tcp.recv(client, 0) do
      {:ok, data} -> 
        IO.puts("Received: #{inspect(data)}")
        handle_connection(client)
      {:error, _reason} ->
        :gen_tcp.close(client)
    end
  end 
end

# Start the server
TCPServer.start_link()
