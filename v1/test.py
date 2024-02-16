import random

# import network

# wifi = network.WLAN(network.STA_IF)
# wifi.active(True)
# wifi.connect("electronics-workshop", "elecwork123")

# while not wifi.isconnected():
#     print(wifi.status())

import web_dashboard as wd

wd.id = input("ID: ")
wd.init_grid(10)
wd.init_log()

i = 0
while ...:
    # wd.log(str(random.random())) # stress test
    i += 1
    wd.log(str(i))
    print(i)
    # wd.log(input("> "))  # send from REPL test
    ...
