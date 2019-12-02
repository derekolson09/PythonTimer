from timeit import default_timer as timer
import tkinter.simpledialog
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, title, width, height, start=0.0, end=0.0, master=None):
        super().__init__(master)
        self.pack(fill='both', expand=1)
        self.title = title
        self.width = width
        self.height = height
        self.start = start
        self.end = end
    
    def initializeWidgets(self):
        self.master.title(self.title)
        self.master.minsize(self.width, self.height)
        
        tk.Label(self, text="Timer in Python").pack(side="top")
        StartBtn = tk.Button(self)
        StartBtn["text"] = "Start"
        StartBtn["relief"] = "groove"
        StartBtn["fg"] = "white"
        StartBtn["bg"] = "#32a852"
        StartBtn["command"] = self.startTimer
        StartBtn.pack(side="left", expand=1, padx=(5,5), pady=(5,5))
        
        StopBtn = tk.Button(self)
        StopBtn["text"] = "Stop"
        StopBtn["relief"] = "groove"
        StopBtn["fg"] = "white"
        StopBtn["bg"] = "#a83232"
        StopBtn["command"] = self.stopTimer
        StopBtn.pack(side="right", expand=1, padx=(5,5), pady=(5,5))

    def startTimer(self):
        self.start = timer()

    def stopTimer(self):
        self.end = timer()
        timeElapsed = self.end-self.start
        CustomDialog(self, title="Output Time Elapsed", text="{}".format(timeElapsed))

class CustomDialog(tkinter.simpledialog.Dialog):
    def __init__(self, parent, title=None, text=None):
        self.data = text
        tkinter.simpledialog.Dialog.__init__(self, parent, title=title)
    
    def body(self, parent):
        self.text= tk.Text(self, width=40, height=4)
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", self.data)
        return self.text

def main():
    root = tk.Tk()
    timer = Application("Timer Application", 200, 200, 0.0, 0.0, root)
    timer.initializeWidgets()
    timer.mainloop()

if __name__ == "__main__":
    main()