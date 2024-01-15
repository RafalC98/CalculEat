import tkinter as tk
from tkinter import ttk

class ScrolledWindow(ttk.Frame):


    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # creating a scrollbars
        self.yscrlbr = ttk.Scrollbar(self)
        self.yscrlbr.grid(column = 1, row = 0, sticky = 'nes')
        # creating a canvas
        self.canv = tk.Canvas(self,bd=0,highlightthickness=0,yscrollcommand=self.yscrlbr.set,height=150)
        # placing a canvas into frame
        self.canv.grid(column = 0, row = 0, sticky = 'nsew')


        # accociating scrollbar comands to canvas scroling
        self.yscrlbr.config(command = self.canv.yview)

        # Reset the view
        self.canv.xview_moveto(0)
        self.canv.yview_moveto(0)

        # creating a frame to insert to canvas
        self.scrollwindow = ttk.Frame(self.canv)

        self.scrollwindow_id = self.canv.create_window(0, 0, window = self.scrollwindow, anchor = 'nw')

        self.scrollwindow.bind('<Configure>', self.configure_window)
        self.canv.bind('<Configure>', self. configure_canvas)


        self.scrollwindow.bind('<Enter>', self.bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self.unbound_to_mousewheel)




    def bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self.on_mousewheel)

    def unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1*(event.delta/120)), "units")

    def configure_window(self, event):
        self.update_idletasks()
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight())
        self.canv.config(scrollregion='0 0 %s %s' % size)
        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canv.config(width = self.scrollwindow.winfo_reqwidth())


    def configure_canvas(self,event):
        self.update_idletasks()
        if self.scrollwindow.winfo_reqheight()<= self.canv.winfo_height():
            self.yscrlbr.grid_forget()
        else:
            self.yscrlbr.grid(column=1, row=0, sticky='nes')


        if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
            self.canv.itemconfigure(self.scrollwindow_id, width=self.canv.winfo_width())

        if self.scrollwindow.winfo_reqheight() < self.canv.winfo_height():
            self.canv.itemconfigure(self.scrollwindow_id, height=self.canv.winfo_height())
        else:
            self.canv.itemconfigure(self.scrollwindow_id, height=self.scrollwindow.winfo_reqheight())



