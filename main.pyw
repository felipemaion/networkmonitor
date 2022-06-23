from tkinter import Frame, Tk, Label
from tkinter import ttk
from digitalclock import DigitalClock
from ping import Machine

    
class App():
    def __init__(self, root):
        self.root = root
        self.machines = []
    
    def load(self):
        frame_menu_inicial = Frame(self.root, highlightbackground="black", highlightthickness=2)
        frame_menu_inicial.grid()
        pc_nome = Label(frame_menu_inicial, text="", font="Arial, 9")
        pc_nome.grid(row=0, column=0, padx=3, pady=3)
        
        
        with open("pcs.txt", "r") as file:
            maquinas = file.readlines()
        file.close()
        pb = ttk.Progressbar(frame_menu_inicial, orient="horizontal", length=200, maximum=len(maquinas))
        pb.grid(row=1, column=0, padx=3, pady=3)

        row = 0
        column = 0
        frame_principal = Frame(self.root, highlightbackground="black", highlightthickness=2)
        DigitalClock(frame_principal)
        
        # clock.mainloop()
        for maquina in maquinas:
            pc_nome["text"] = maquina.split(",")[0]
            ip=maquina.split(",")[1].replace("\n","")
            self.machines.append(Machine(root=self.root, pc=maquina.split(",")[0], ip=ip, interval=1, frame=frame_principal, row=row, column=column))
            row += 1
            if row == 11:
                column +=1
                row = 0
            pb["value"] += 1
            self.root.update()
        frame_menu_inicial.grid_forget()
        frame_principal.grid(padx=3, pady=3)
root = Tk()
app = App(root)
app.load()
root.mainloop()