defmodule Helpers do
  @tz_offset -8

  def get_time do
    DateTime.utc_now() |> DateTime.add(@tz_offset, :hour) |> DateTime.to_string()
  end
end
