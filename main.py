from tkinter import *
from PIL import ImageTk, Image

class Main:
    def __init__(self):
        self.window = Tk()
        # self.window.attributes('-type', 'dock')
        # self.window.attributes('-fullscreen', True)
        self.window.focus_force()
        self.window.title("piControl")
        self.window.resizable(True, True)
        self.window.geometry("720x480")

        self.mainFrame = Frame(self.window)
        self.light_img = PhotoImage(file="lights.png")
        self.settings_img = PhotoImage(file="settings.png")
        self.alarm_img = PhotoImage(file="alarm.png")
        self.stock_img = PhotoImage(file="stocks.png")
        self.loadMain()

        mainloop()

    def loadMain(self):
        for item in self.mainFrame.winfo_children():
            item.pack_forget()
        self.mainFrame.pack(side="left", fill="both", expand=True)

        frame_one = Frame(self.mainFrame)
        frame_one.pack(side="left", fill="both", expand=True)

        lightFrame = Frame(frame_one, width=100, height=100)
        lightFrame.grid_propagate(False)
        Button(lightFrame, text="Lights", image=self.light_img, compound=TOP, command=self.loadLights).grid(sticky="wens")
        lightFrame.columnconfigure(0, weight=1)
        lightFrame.rowconfigure(0, weight=1)
        lightFrame.pack(fill="both", expand=True)

        settingsFrame = Frame(frame_one, width=100, height=100)
        settingsFrame.grid_propagate(False)
        Button(settingsFrame, text="Settings", image=self.settings_img, compound=TOP).grid(sticky="wens")
        settingsFrame.columnconfigure(0, weight=1)
        settingsFrame.rowconfigure(0, weight=1)
        settingsFrame.pack(fill="both", expand=True)

        frame_two = Frame(self.mainFrame)
        frame_two.pack(side="left", fill="both", expand=True)

        stockFrame = Frame(frame_two, width=100, height=100)
        stockFrame.grid_propagate(False)
        Button(stockFrame, text="Alarm", image=self.alarm_img, compound=TOP).grid(sticky="wens")
        stockFrame.columnconfigure(0, weight=1)
        stockFrame.rowconfigure(0, weight=1)
        stockFrame.pack(fill="both", expand=True)

        alarmFrame = Frame(frame_two, width=100, height=100)
        alarmFrame.grid_propagate(False)
        Button(alarmFrame, text="Test").grid(sticky="wens")
        alarmFrame.columnconfigure(0, weight=1)
        alarmFrame.rowconfigure(0, weight=1)
        alarmFrame.pack(fill="both", expand=True)

        frame_three = Frame(self.mainFrame)
        frame_three.pack(side="left", fill="both", expand=True)

        fifthFrame = Frame(frame_three, width=100, height=100)
        fifthFrame.grid_propagate(False)
        Button(fifthFrame, text="Stocks", image=self.stock_img, compound=TOP).grid(sticky="wens")
        fifthFrame.columnconfigure(0, weight=1)
        fifthFrame.rowconfigure(0, weight=1)
        fifthFrame.pack(fill="both", expand=True)

        sixthFrame = Frame(frame_three, width=100, height=100)
        sixthFrame.grid_propagate(False)
        Button(sixthFrame, text="Test").grid(sticky="wens")
        sixthFrame.columnconfigure(0, weight=1)
        sixthFrame.rowconfigure(0, weight=1)
        sixthFrame.pack(fill="both", expand=True)

    def loadLights(self):
        for item in self.mainFrame.winfo_children():
            item.pack_forget()

        frame_back = Frame(self.mainFrame, height=10, background="")
        Button(frame_back, compound=TOP, command=self.loadMain).grid(sticky="wens")

        frame_back.pack(side="top", fill="x", expand=False)

        # frame_back = Frame(self.mainFrame)
        # frame_back.pack(side="top", fill="both", expand=True)

        frame_one = Frame(self.mainFrame)
        frame_one.pack(side="left", fill="both", expand=True)

        lightFrame = Frame(frame_one, width=100, height=100)
        lightFrame.grid_propagate(False)
        Button(lightFrame, text="Lights", image=self.light_img, compound=TOP, command=self.loadLights).grid(sticky="wens")
        lightFrame.columnconfigure(0, weight=1)
        lightFrame.rowconfigure(0, weight=1)
        lightFrame.pack(fill="both", expand=True)

        settingsFrame = Frame(frame_one, width=100, height=100)
        settingsFrame.grid_propagate(False)
        Button(settingsFrame, text="Settings", image=self.settings_img, compound=TOP).grid(sticky="wens")
        settingsFrame.columnconfigure(0, weight=1)
        settingsFrame.rowconfigure(0, weight=1)
        settingsFrame.pack(fill="both", expand=True)

        frame_two = Frame(self.mainFrame)
        frame_two.pack(side="left", fill="both", expand=True)

Main()
