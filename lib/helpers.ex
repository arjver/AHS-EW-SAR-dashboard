defmodule Helpers do
  @tz_offset -7 # -8 for PST, -7 for PST with daylight saving

  def get_time do
    DateTime.utc_now() |> DateTime.add(@tz_offset, :hour) |> DateTime.to_string()
  end
end
