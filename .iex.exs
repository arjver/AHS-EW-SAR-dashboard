spawn(&DataStore.start_link/0)
spawn(&HTTPServer.start/0)
spawn(&TCPServer.start_link/0)
