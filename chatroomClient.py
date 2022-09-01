import network, Tkinter
global root

serverIp = "localhost"
serverPort = 1234
username = ""
def init(username):
    client = network.makeClient(serverIp, serverPort)
    client.send(username)
    
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

username = raw_input("Enter a username:")
init(username)
windowInit()
