import tkinter as tk
import customtkinter

class colors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x240")
        self.window.resizable(0, 0)
        self.window.title("Empty Recycle Bin")
        self.window.configure(bg='#222831')
        self.entry = customtkinter.CTkEntry(master=self.window, justify=tk.CENTER, width=120, height=30, corner_radius=10)
        self.entry.insert(0, "Enter color here")
        self.entry.place(x=140, y=30)
        self.entry.bind('<FocusIn>', self.temp_text)
        self.button()

    def button(self):
        button_to_rgb = customtkinter.CTkButton(master=self.window, corner_radius=10, text="Hex to RGB", width = 120, command=self.hex_to_rgb)
        button_to_rgb.place(x=40, y=120)
        button_to_hex = customtkinter.CTkButton(master=self.window, corner_radius=10, text="RGB to Hex", width = 120, command=self.rgb_to_hex)
        button_to_hex.place(x=240, y=120)
        button_close = customtkinter.CTkButton(master=self.window, corner_radius=10, text="close", width = 120, command=self.close)
        button_close.place(x=140, y=170)
    
    def temp_text(self,e):
        e = e
        self.entry.delete(0, "end")
    
    def close (self):
        self.window.destroy()
        
    def hex_to_rgb(self):
        try:
            h = self.entry.get()
            g = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
            f = "RGB value for [" + str(h) + "] is " + str(g)
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text=f, width = 300)
            label.place(x=50, y=75)
        except:
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text="please enter a proper Hex color", width = 300)
            label.place(x=50, y=75)
    def rgb_to_hex(self):
        try:
            h = self.entry.get()
            rgb_values = h.split(',')
            r = int(rgb_values[0])
            g = int(rgb_values[1])
            b = int(rgb_values[2])
            g = '#{:02x}{:02x}{:02x}'.format(r, g, b)
            f = "Hex value for [" + str(h) + "] is " + str(g)
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text=f, width = 300)
            label.place(x=50, y=75)
        except:
            label = customtkinter.CTkLabel(master=self.window, text_color="white", text="please enter a proper RGB color", width = 300)
            label.place(x=50, y=75)
    def run(self):
        self.window.mainloop()
    
C = colors()
C.run()