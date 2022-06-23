from tkinter import Button, Frame, Label, NSEW, W, E
# from os import popen
import os

from click import command

     
class Machine:
    def __init__(self, root, pc, ip, frame, row, column,interval=1):
        self.pc = pc
        self.ip = ip
        self.frame = frame
        self.row = row
        self.column = column
        self.root = root
        self.status = 0 # OFFLINE. 1==ONLINE
        self.__create_widgets()
        self.interval = interval
        self.ping()
        
    def ping(self):
        cmd = f"ping -c 1 { self.ip } > /dev/null 2>&1"
        print(f"Executando comando: '{cmd}' \t", end=" ==> ")
        ping = os.system(cmd)
        print(ping, end="\n")
        ## + " > /dev/null 2>&1" serve para não mandar para terminal a escrita do ping, só o resultado.
        if ping == 0:
            self.status = 1
            self.label_status["text"] = "ONLINE"
            self.label_status["fg"] = "green"
            self.frame_pc["highlightbackground"] = "green"
        else:
            self.status = 0
            self.label_status["text"] = "OFFLINE"
            self.label_status["fg"] = "red"
            self.frame_pc["highlightbackground"] = "red"
            
        self.frame.after(self.interval*60000, self.ping)    
        

    def shutdown(self):
        cmd = f"shutdown {self.ip} " # sei lá
        response = os.system(cmd)
        return response
        
    def __create_widgets(self):
        self.frame_pc = Frame(self.frame, highlightbackground="black", highlightthickness=2)
        self.frame_pc.grid(padx=3, pady=3, row=self.row, column=self.column, sticky=NSEW)
        self.frame_pc.columnconfigure(0, weight=1)

        self.frame_nome = Frame(self.frame_pc)
        self.frame_nome.grid(padx=3, pady=3, row=0, column=0, sticky=W)
        self.label_nome = Label(self.frame_nome, text=self.pc, font="Arial, 12")
        self.label_nome.grid()

        self.frame_status = Frame(self.frame_pc)
        self.frame_status.grid(padx=3, pady=3, row=0, column=1, sticky=E)
        self.label_status = Label(self.frame_status, text="", font="Arial, 12")
        self.label_status.grid()
        
        self.frame_button = Button(self.frame_pc, command=self.ping, text="PING")
        self.frame_button.grid(padx=3, pady=3, row=0, column=2, sticky=E)
        
        self.frame_button_shutdown = Button(self.frame_pc, command=self.shutdown, text="OFF")
        self.frame_button_shutdown.grid(padx=3, pady=3, row=0, column=3, sticky=E)
        

