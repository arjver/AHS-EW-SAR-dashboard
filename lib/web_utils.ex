defmodule WebUtils do
  @grid_page File.read!("viewgrid.html")
  @log_page File.read!("viewlog.html")

  def row_to_tr(row) do
    "<tr>" <> (row |> Enum.map(fn cell -> "<td #{cell}></td>" end) |> Enum.join()) <> "</tr>"
  end

  def make_grid(id, arr) do
    height = length(arr)
    width = length(arr |> Enum.at(0))

    table = arr |> Enum.map(&row_to_tr/1) |> Enum.join()

    @grid_page
    |> String.replace("__height__", Integer.to_string(height))
    |> String.replace("__width__", Integer.to_string(width))
    |> String.replace("__table__", table)
    |> String.replace("__id__", id)
  end

  def make_log(id, arr) do
    log =
      arr
      |> Enum.reverse()
      |> Enum.map(fn row ->
        "<p><span>#{String.slice(row |> Enum.at(0), 0..-5)}</span> #{row |> Enum.at(1)}</p>"
      end)
      |> Enum.join()

    @log_page
    |> String.replace("__log__", log)
    |> String.replace("__id__", id)
  end
end
