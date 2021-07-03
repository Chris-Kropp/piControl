from tkinter import *
from PIL import ImageTk, Image
from phue import Bridge
import webbrowser
import os

class Main:
    def __init__(self):
        self.b = Bridge("192.168.0.20")
        self.chair_on = self.b.get_light(1, "on")
        self.chair_bri = self.b.get_light(1, "bri")
        self.desk_on = self.b.get_light(2, "on")
        self.desk_bri = self.b.get_light(2, "bri")
        self.screen_bri = int(open("/sys/class/backlight/rpi_backlight/brightness").read())
        self.fullscreen = True
        self.window = Tk()
        # self.window.attributes('-type', 'dock')
        self.window.attributes('-fullscreen', True)
        self.window.focus_force()
        self.window.title("piControl")
        self.window.resizable(True, True)
        self.window.geometry("800x480")

        self.mainFrame = Frame(self.window)
        self.light_img = PhotoImage(file="lights.png")
        self.settings_img = PhotoImage(file="settings.png")
        self.alarm_img = PhotoImage(file="alarm.png")
        self.stock_img = PhotoImage(file="stocks.png")
        self.power_img = PhotoImage(file="power.png")
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
        Button(lightFrame, text="Lights", image=self.light_img, compound=TOP, command=self.load_lights).grid(sticky="wens")
        lightFrame.columnconfigure(0, weight=1)
        lightFrame.rowconfigure(0, weight=1)
        lightFrame.pack(fill="both", expand=True)

        settingsFrame = Frame(frame_one, width=100, height=100)
        settingsFrame.grid_propagate(False)
        Button(settingsFrame, text="Settings", image=self.settings_img, compound=TOP, command=self.load_settings).grid(sticky="wens")
        settingsFrame.columnconfigure(0, weight=1)
        settingsFrame.rowconfigure(0, weight=1)
        settingsFrame.pack(fill="both", expand=True)

        frame_two = Frame(self.mainFrame)
        frame_two.pack(side="left", fill="both", expand=True)

        stockFrame = Frame(frame_two, width=100, height=100)
        stockFrame.grid_propagate(False)
        Button(stockFrame, text="Alarm", image=self.alarm_img, compound=TOP, command=self.open_alarm).grid(sticky="wens")
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

    def load_lights(self):
        for item in self.mainFrame.winfo_children():
            item.pack_forget()

        frame_back = Frame(self.mainFrame, height=10, background="")
        Button(frame_back, text="<", compound=TOP, command=self.loadMain).grid(sticky="wens")

        frame_back.pack(side="top", fill="both", expand=False)

        frame_one = Frame(self.mainFrame)
        frame_one.pack(side="left", fill="both", expand=True)

        lightFrame = Frame(frame_one, width=100, height=100)
        lightFrame.grid_propagate(False)
        self.chair_scale = Scale(lightFrame, from_=254, to=30, length=400, showvalue=0, resolution=10, command=self.chair_light_brightness)
        self.chair_scale.pack(side=LEFT)
        self.chair_scale.set(self.chair_bri)
        Button(lightFrame, text="Chair", image=self.power_img, compound=TOP, command=self.toggle_chair).grid(padx=(25, 0), sticky="WENS")
        lightFrame.columnconfigure(0, weight=1)
        lightFrame.rowconfigure(0, weight=1)
        lightFrame.pack(side=LEFT, fill="both", expand=True)

        lightFrameTwo = Frame(frame_one, width=100, height=100)
        lightFrameTwo.grid_propagate(False)
        self.desk_scale = Scale(lightFrameTwo, from_=254, to=30, length=400, showvalue=0, resolution=10, command=self.desk_light_brightness)
        self.desk_scale.pack(side=RIGHT)
        self.desk_scale.set(self.desk_bri)
        Button(lightFrameTwo, text="Desk", image=self.power_img, compound=TOP, command=self.toggle_desk).grid(padx=(0, 25), sticky="WENS")
        lightFrameTwo.columnconfigure(0, weight=1)
        lightFrameTwo.rowconfigure(0, weight=1)
        lightFrameTwo.pack(expand=True, fill="both", side=RIGHT)

    def load_settings(self):
        for item in self.mainFrame.winfo_children():
            item.pack_forget()

        frame_back = Frame(self.mainFrame, height=10, background="")
        Button(frame_back, text="<", compound=TOP, command=self.loadMain).grid(sticky="wens")

        frame_back.pack(side="top", fill="both", expand=False)

        frame_one = Frame(self.mainFrame)
        frame_one.pack(side="left", fill="both", expand=True)

        briFrame = Frame(frame_one, width=100, height=100)
        briFrame.grid_propagate(False)
        self.bri_scale = Scale(briFrame, from_=255, to=25, length=400, showvalue=0, resolution=10, command=self.screen_brightness)
        self.bri_scale.pack(side=LEFT)
        self.bri_scale.set(self.screen_bri)
        Button(briFrame, text="Exit", image=self.power_img, compound=TOP, command=self.toggle_fullscreen).grid(padx=(25, 0), sticky="WENS")
        briFrame.columnconfigure(0, weight=1)
        briFrame.rowconfigure(0, weight=1)
        briFrame.pack(side=LEFT, fill="both", expand=True)

        exitFrame = Frame(frame_one, width=100, height=100)
        exitFrame.grid_propagate(False)
        Button(exitFrame, text="Desk", image=self.power_img, compound=TOP, command=self.exit).grid(padx=(0, 25), sticky="WENS")
        exitFrame.columnconfigure(0, weight=1)
        exitFrame.rowconfigure(0, weight=1)
        exitFrame.pack(expand=True, fill="both", side=RIGHT)

    def toggle_chair(self):
        self.chair_on = not self.chair_on
        self.b.set_light(1, 'on', self.chair_on)

    def toggle_desk(self):
        self.desk_on = not self.desk_on
        self.b.set_light(2, 'on', self.desk_on)

    def chair_light_brightness(self, brightness):
        if(self.chair_on):
            self.b.set_light(1, 'bri', int(brightness))
            self.chair_bri = int(brightness)
        else:
            self.chair_scale.set(self.chair_bri)

    def desk_light_brightness(self, brightness):
        if(self.desk_on):
            self.b.set_light(2, 'bri', int(brightness))
            self.desk_bri = int(brightness)
        else:
            self.desk_scale.set(self.desk_bri)

    def screen_brightness(self, brightness):
        self.screen_bri = brightness
        os.system("echo {} > /sys/class/backlight/rpi_backlight/brightness".format(brightness))

    def toggle_fullscreen(self, brightness):
        self.fullscreen = not self.fullscreen
        self.window.attributes('-fullscreen', self.fullscreen)

    def exit(self):
        self.window.destroy()

    def open_alarm(self):   #TODO: replace with function that gets and sends data to api instead of opening web interface
        webbrowser.open("192.168.0.45:8080")

Main()
