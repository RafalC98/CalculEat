from tkinter import *
from tkinter import ttk

from ScrolledFrame import ScrolledWindow
from NewMeal import NewMeal


class CalculEat(Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title("CalculEat")
        self.geometry('400x700')
        self.minsize(400, 400)

        # Variables
        self.breakfast_labels = {}
        self.breakfast_buttons = {}
        self.snack_labels = {}
        self.snack_buttons = {}
        self.lunch_labels = {}
        self.lunch_buttons = {}
        self.dinner_labels = {}
        self.dinner_buttons = {}

        self.breakfast_macros = {}
        self.lunch_macros = {}
        self.snack_macros = {}
        self.dinner_macros = {}

        self.global_calories = StringVar()
        self.global_calories_value = 0
        self.global_calories.set(f'Calories:{self.global_calories_value}')

        self.breakfast_calories = StringVar()
        self.breakfast_calories.set('Calories:0')

        self.lunch_calories = StringVar()
        self.lunch_calories.set('Calories:0')

        self.snack_calories = StringVar()
        self.snack_calories.set('Calories:0')

        self.dinner_calories = StringVar()
        self.dinner_calories.set('Calories:0')

        self.global_proteins = StringVar()
        self.global_proteins_value = 0
        self.global_proteins.set(f'Proteins:{self.global_proteins_value}')

        self.breakfast_proteins = StringVar()
        self.breakfast_proteins.set('Proteins:0')

        self.lunch_proteins = StringVar()
        self.lunch_proteins.set('Proteins:0')

        self.snack_proteins = StringVar()
        self.snack_proteins.set('Proteins:0')

        self.dinner_proteins = StringVar()
        self.dinner_proteins.set('Proteins:0')

        self.global_cabrohydrates = StringVar()
        self.global_cabrohydrates_value = 0
        self.global_cabrohydrates.set(
            f'Cabrohydrates:{self.global_cabrohydrates_value}')

        self.breakfast_cabrohydrates = StringVar()
        self.breakfast_cabrohydrates.set('Cabrohydrates:0')

        self.lunch_cabrohydrates = StringVar()
        self.lunch_cabrohydrates.set('Cabrohydrates:0')

        self.snack_cabrohydrates = StringVar()
        self.snack_cabrohydrates.set('Cabrohydrates:0')

        self.dinner_cabrohydrates = StringVar()
        self.dinner_cabrohydrates.set('Cabrohydrates:0')

        self.global_fats = StringVar()
        self.global_fats_value = 0
        self.global_fats.set(f'Fats:{self.global_fats_value}')

        self.breakfast_fats = StringVar()
        self.breakfast_fats.set('Fats:0')

        self.lunch_fats = StringVar()
        self.lunch_fats.set('Fats:0')

        self.snack_fats = StringVar()
        self.snack_fats.set('Fats:0')

        self.dinner_fats = StringVar()
        self.dinner_fats.set('Fats:0')

        # Styles
        self.s = ttk.Style()
        self.s.configure('dark.TFrame', background='#64CCC5')
        self.s.configure('bright.TFrame', background='#DAFFFB')
        self.s.configure('white.TLabel', background='#64CCC5',
                         foreground='#DAFFFB')
        self.s.configure('name.TLabel', background='#64CCC5',
                         foreground='#DAFFFB')
        self.s.configure('basic.TButton', relief="raised",
                         background='#64CCC5', foreground='#04364A',
                         highlightbackground='red', borderwidth=2,
                         focuscolor='white')

        # create a frame concerning breakfast

        self.breakfast_frame = ttk.Frame(self, padding="8 5 8 5",
                                         style='dark.TFrame')
        self.breakfast_frame.grid(column=0, row=0, sticky='NWES')

        # Widgets in breakfastframe

        ttk.Label(self.breakfast_frame, text='CalculEat ',
                  style='name.TLabel').grid(column=0, row=0, sticky='NW',
                                            padx=5,
                                            pady=5)
        ttk.Label(self.breakfast_frame, text='Breakfast: ',
                  style='name.TLabel').grid(column=0, row=1, sticky='NW',
                                            padx=5,
                                            pady=5)
        ttk.Button(self.breakfast_frame, text='New Product / Meal',
                   command=self.add_breakfast_product,
                   style='basic.TButton').grid(column=3, row=1, sticky='NE')

        self.breakfast_inner_frame = ScrolledWindow(self.breakfast_frame)
        self.breakfast_inner_frame.scrollwindow.configure(
            style='bright.TFrame')
        self.breakfast_inner_frame.grid(column=0, row=2, sticky='NWES',
                                        columnspan=4)

        ttk.Label(self.breakfast_frame, textvariable=self.breakfast_calories,
                  style='white.TLabel').grid(column=0, row=3, padx=5,
                                             sticky='SW')
        ttk.Label(self.breakfast_frame, textvariable=self.breakfast_proteins,
                  style='white.TLabel').grid(column=1, row=3, padx=5,
                                             sticky='SW')
        ttk.Label(self.breakfast_frame,
                  textvariable=self.breakfast_cabrohydrates,
                  style='white.TLabel').grid(column=2, row=3, padx=5,
                                             sticky='SW')
        ttk.Label(self.breakfast_frame, textvariable=self.breakfast_fats,
                  style='white.TLabel').grid(column=3, row=3, padx=5,
                                             sticky='SW')

        # create a frame concerning snack
        self.snack_frame = ttk.Frame(self, padding="8 5 8 5",
                                     style='dark.TFrame')
        self.snack_frame.grid(column=0, row=1, sticky='NWES')

        # Widgets in snackframe

        ttk.Label(self.snack_frame, text='Snack: ', style='white.TLabel').grid(
            column=0, row=0, sticky='NW', padx=5, pady=5)
        ttk.Button(self.snack_frame, text='New Product / Meal',
                   command=self.add_snack_product, style='basic.TButton').grid(
            column=3, row=0, sticky='NE')

        self.snack_inner_frame = ScrolledWindow(self.snack_frame)
        self.snack_inner_frame.scrollwindow.configure(style='bright.TFrame')
        self.snack_inner_frame.grid(column=0, row=1, sticky='NWES',
                                    columnspan=4)

        ttk.Label(self.snack_frame, textvariable=self.snack_calories,
                  style='white.TLabel').grid(column=0, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.snack_frame, textvariable=self.snack_proteins,
                  style='white.TLabel').grid(column=1, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.snack_frame, textvariable=self.snack_cabrohydrates,
                  style='white.TLabel').grid(column=2, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.snack_frame, textvariable=self.snack_fats,
                  style='white.TLabel').grid(column=3, row=2, padx=5,
                                             sticky='W')

        # create a frame concerning lunch
        self.lunch_frame = ttk.Frame(self, padding="8 5 8 5",
                                     style='dark.TFrame')
        self.lunch_frame.grid(column=0, row=2, sticky='NWES')

        # Widgets in lunchframe
        ttk.Label(self.lunch_frame, text='Lunch: ', style='white.TLabel').grid(
            column=0, row=0, sticky='NW', padx=5, pady=5)
        ttk.Button(self.lunch_frame, text='New Product / Meal',
                   command=self.add_lunch_product, style='basic.TButton').grid(
            column=3, row=0, sticky='NE')

        self.lunch_inner_frame = ScrolledWindow(self.lunch_frame)
        self.lunch_inner_frame.scrollwindow.configure(style='bright.TFrame')
        self.lunch_inner_frame.grid(column=0, row=1, sticky='NWES',
                                    columnspan=4)

        ttk.Label(self.lunch_frame, textvariable=self.lunch_calories,
                  style='white.TLabel').grid(column=0, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.lunch_frame, textvariable=self.lunch_proteins,
                  style='white.TLabel').grid(column=1, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.lunch_frame, textvariable=self.lunch_cabrohydrates,
                  style='white.TLabel').grid(column=2, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.lunch_frame, textvariable=self.lunch_fats,
                  style='white.TLabel').grid(column=3, row=2, padx=5,
                                             sticky='W')

        # create a frame concerning dinner
        self.dinner_frame = ttk.Frame(self, padding="8 5 8 5",
                                      style='dark.TFrame')
        self.dinner_frame.grid(column=0, row=3, sticky='NWES')

        # Widgets in dinnerframe

        ttk.Label(self.dinner_frame, text='Dinner: ',
                  style='white.TLabel').grid(column=0, row=0, sticky='NW',
                                             padx=5, pady=5)
        ttk.Button(self.dinner_frame, text='New Product / Meal',
                   command=self.add_dinner_product,
                   style='basic.TButton').grid(
            column=3, row=0, sticky='NE')

        self.dinner_inner_frame = ScrolledWindow(self.dinner_frame)
        self.dinner_inner_frame.scrollwindow.configure(style='bright.TFrame')
        self.dinner_inner_frame.grid(column=0, row=1, sticky='NWES',
                                     columnspan=4)

        ttk.Label(self.dinner_frame, textvariable=self.dinner_calories,
                  style='white.TLabel').grid(column=0, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.dinner_frame, textvariable=self.dinner_proteins,
                  style='white.TLabel').grid(column=1, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.dinner_frame, textvariable=self.dinner_cabrohydrates,
                  style='white.TLabel').grid(column=2, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.dinner_frame, textvariable=self.dinner_fats,
                  style='white.TLabel').grid(column=3, row=2, padx=5,
                                             sticky='W')

        # Labels with global calories and macros

        self.calories_frame = ttk.Frame(self, padding="8 5 8 5",
                                        style='dark.TFrame')
        self.calories_frame.grid(column=0, row=4, sticky='NWES')
        ttk.Label(self.calories_frame, textvariable=self.global_calories,
                  style='white.TLabel').grid(column=0, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.calories_frame, textvariable=self.global_proteins,
                  style='white.TLabel').grid(column=1, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.calories_frame, textvariable=self.global_cabrohydrates,
                  style='white.TLabel').grid(column=2, row=2, padx=5,
                                             sticky='W')
        ttk.Label(self.calories_frame, textvariable=self.global_fats,
                  style='white.TLabel').grid(column=3, row=2, padx=5,
                                             sticky='W')

        # Grid configurations

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=12)
        self.rowconfigure(1, weight=12)
        self.rowconfigure(2, weight=12)
        self.rowconfigure(3, weight=12)
        self.rowconfigure(4, weight=1)

        self.breakfast_frame.columnconfigure(0, weight=1)
        self.breakfast_frame.columnconfigure(1, weight=1)
        self.breakfast_frame.columnconfigure(2, weight=1)
        self.breakfast_frame.columnconfigure(3, weight=1)
        self.breakfast_frame.rowconfigure(0, weight=0)
        self.breakfast_frame.rowconfigure(1, weight=0)
        self.breakfast_frame.rowconfigure(2, weight=1)
        self.breakfast_frame.rowconfigure(3, weight=0)

        self.snack_frame.columnconfigure(0, weight=1)
        self.snack_frame.columnconfigure(1, weight=1)
        self.snack_frame.columnconfigure(2, weight=1)
        self.snack_frame.columnconfigure(3, weight=1)
        self.snack_frame.rowconfigure(0, weight=0)
        self.snack_frame.rowconfigure(1, weight=1)
        self.snack_frame.rowconfigure(2, weight=0)

        self.lunch_frame.columnconfigure(0, weight=1)
        self.lunch_frame.columnconfigure(1, weight=1)
        self.lunch_frame.columnconfigure(2, weight=1)
        self.lunch_frame.columnconfigure(3, weight=1)
        self.lunch_frame.rowconfigure(0, weight=0)
        self.lunch_frame.rowconfigure(1, weight=1)
        self.lunch_frame.rowconfigure(2, weight=0)

        self.dinner_frame.columnconfigure(0, weight=1)
        self.dinner_frame.columnconfigure(1, weight=1)
        self.dinner_frame.columnconfigure(2, weight=1)
        self.dinner_frame.columnconfigure(3, weight=1)
        self.dinner_frame.rowconfigure(0, weight=0)
        self.dinner_frame.rowconfigure(1, weight=1)
        self.dinner_frame.rowconfigure(2, weight=0)

        self.breakfast_inner_frame.columnconfigure(0, weight=1)
        self.breakfast_inner_frame.rowconfigure(0, weight=1)

        self.snack_inner_frame.columnconfigure(0, weight=1)
        self.snack_inner_frame.rowconfigure(0, weight=1)

        self.lunch_inner_frame.columnconfigure(0, weight=1)
        self.lunch_inner_frame.rowconfigure(0, weight=1)

        self.dinner_inner_frame.columnconfigure(0, weight=1)
        self.dinner_inner_frame.rowconfigure(0, weight=1)

        self.calories_frame.rowconfigure(0, weight=1)
        self.calories_frame.columnconfigure(0, weight=1)
        self.calories_frame.columnconfigure(1, weight=1)
        self.calories_frame.columnconfigure(2, weight=1)
        self.calories_frame.columnconfigure(3, weight=1)

        self.breakfast_inner_frame.bind('<Configure>', self.widnow_refresh)

    def add_breakfast_product(self):
        new_window = NewMeal(self, self.breakfast_inner_frame,
                             self.breakfast_macros, self.breakfast_calories,
                             self.breakfast_proteins,
                             self.breakfast_cabrohydrates, self.breakfast_fats,
                             self.breakfast_labels, self.breakfast_buttons)
        new_window.grab_set()

    def add_snack_product(self):
        new_window = NewMeal(self, self.snack_inner_frame, self.snack_macros,
                             self.snack_calories, self.snack_proteins,
                             self.snack_cabrohydrates, self.snack_fats,
                             self.snack_labels, self.snack_buttons)
        new_window.grab_set()

    def add_lunch_product(self):
        new_window = NewMeal(self, self.lunch_inner_frame, self.lunch_macros,
                             self.lunch_calories, self.lunch_proteins,
                             self.lunch_cabrohydrates, self.lunch_fats,
                             self.lunch_labels, self.lunch_buttons)
        new_window.grab_set()

    def add_dinner_product(self):
        new_window = NewMeal(self, self.dinner_inner_frame, self.dinner_macros,
                             self.dinner_calories, self.dinner_proteins,
                             self.dinner_cabrohydrates, self.dinner_fats,
                             self.dinner_labels, self.dinner_buttons)
        new_window.grab_set()

    def widnow_refresh(self, event):
        self.update_idletasks()


if __name__ == "__main__":
    app = CalculEat()
    app.mainloop()
