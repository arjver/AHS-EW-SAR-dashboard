# AHS Electronics Workshop Search and Report Project Web Dashboard

### The Project:
- Students make a car-thing
- It's placed on a flat square surface (OOM 1 meter-ish) with walls on all sides
- There are magnets hidden underneath the surface, and coloured squares on the surface
- Students use the RPi Pico W, time-of-flight sensors, RGB color sensors, hall effect sensors, etc. to find out where the squares/magnets are
- The libraries we have written for/ported to MicroPython to be used in this project at [AHS Programming Club's Github](https://github.com/AHSPC)

### This:
- Is a web interface that visualizes the data sent by the vehicle (positions of magnets and coloured squares on a grid)
- Also provides a simple log over wifi for debugging without being connected to serial
- Provides a helper library (`web_dashboard.py`) for sending data to the web interface

Made by [@blobbybilb](https://github.com/blobbybilb)

## Technical Stuff 
*mostly for whomever maintainership of this goes to after I graduate*
- The school blocks HTTP on basically every port
- The school blocks UDP on AFAIK every port (not that I want to implement retransmissions, etc. anyway)
- The school sometimes blocks inbound TCP packets (and not outbound)
- The school randomly blocks domains (via DNS (but it seems some IPs are blocked at a different level?))
- The school has several network, the rules are different for each (as I found out during 6th Period (AP CSA) 14.Feb.2024)
- All the above statements may or may not be accurate, so please don't modify the setup unless needed. It's okay. Rewriting it in Rust won't make the network any faster. Well don't say I didn't warn you.
- MicroPython doesn't support WPA2 Enterprise which is what the student wifi uses as of when I wrote this
### The Setup:
1. We have a wifi router connected to the modem connected to the port near the big TV in the computer lab side of the workshop. FYI, connecting it to ethernet upstairs in Room 310 doesn't work (stricter TCP blocking or something).
2. `pico-dashboard.deno.dev` proxies all HTTP requests to an HTTP server on a google cloud VM (I'll call this "HTTP server at port 3010" now)
3. The google cloud VM also runs a socket server on port 3020 (`socket_server.py`) that acts as a proxy from TCP sockets to the HTTP server at port 3010.
4. The HTTP server at port 3010 (`web_server.py`) does all the work.
### Justification
- Another wifi network because school wifi is bad for some reason inside the workshop (it works perfectly well right outside, and there is some kind of access point inside the workshop) (it might be a 2.3ghz/5ghz thing)
- The HTTP server does everything because I wrote that first, hoping that'd be all that was needed. It wasn't.
- TCP sockets are fast (and aren't blocked in specifically our current setup), so it wouldn't take too much time on the Pico.
- The Deno Deploy proxy is because port 80 was in use on the gcloud VM, and other ports are blocked for HTTP (except 443 but good luck trying to get 40 students to make sure chrome/safari don't auto redirect that to https)

**Note:** A setup too cursed to mention here might be available in some file on the super-heavy Dell Xeon laptop in Room 310 to get a development setup in Room 310 (Room 310 is the actual CS room right now (in case that changes in the future)). (if it doesn't boot then select the 5.7.X kernel at boot, the 6.2.X kernel is corrupted)

**Update:** The above setup wasn't reliable, apparently due to the school's network policies. We are running everything locally on an SBC connected to the wifi network above. I also rewrote it (in Elixir) and removed all the hacky stuff (for reliability and to be sure it could easily handle all the picos/computers concurrently without performance issues on the relatively low-power SBC).


## Usage
```sh
# To run the new version:
git clone https://github.com/blobbybilb/AHS-EW-SAR-dashboard
# Make sure elixir and mix are installed
mix deps.get
iex -S mix
# Now web_dashboard.py should be able to send stuff to the server (after you put in the correct server IP)
# It will also start an interactive Elixir session, where you can enter:
DataStore.persist_data()
# to save data to disk (this is done to avoid frequent writes to the Micro SD and avoid wearing it out)
```

## Screenshots

![image](https://github.com/blobbybilb/AHS_Electronics_pico_search_project_web_dashboard/assets/58201828/12c03934-407a-461c-b25b-2c1d57de6875)
<img width="648" alt="Screenshot 2024-02-14 at 9 30 37 PM" src="https://github.com/blobbybilb/AHS_Electronics_pico_search_project_web_dashboard/assets/58201828/0332f15e-98a4-465f-8359-c4d75afade2c">
