import network, Tkinter, threading
global running, serverIp, serverPort, clientconns, clientaddrs, clientusernames, root
running = True
serverIp = "localhost"
serverPort = 1234
clientconns = []
clientaddrs = []
clientusernames = []

def callback():
    global e
    print e.get()

def windowInit():
        global root, e
        root = Tkinter.Tk()
        frame = Tkinter.Frame(root)
        frame.pack()
        e = Tkinter.Entry(root)
        e.pack()
        e.focus_set()
        b = Tkinter.Button(root, text="Enter", width=10, command=callback)
        b.pack()
        text = e.get()
        Tkinter.mainloop()
        

def init():
    server = network.makeMultiServer(serverIp, serverPort)
    while running == True:
        conn, addr = server.accept()
        username = server.recv(1024)
        server.send("1")
        clientconns.append(conn)
        clientaddrs.append(addrs)
        clientusernames.append(username)
        print(username)

init()
#windowInit()
