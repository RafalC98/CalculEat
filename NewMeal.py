from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class NewMeal(Toplevel):
    def __init__(self, parent, frame, macros, calories, proteins,
                 cabrohydrates, fats, labels, buttons):
        super().__init__(parent)
        self.parent = parent
        self.frame = frame
        self.macros = macros
        self.calories = calories
        self.proteins = proteins
        self.cabrohydrates = cabrohydrates
        self.fats = fats
        self.labels = labels
        self.buttons = buttons
        self.calories_value = 0
        self.proteins_value = 0
        self.cabrohydrates_value = 0
        self.fats_value = 0
        self.title("New Meal")
        self.geometry('400x400')
        self.minsize(400, 400)
        self.maxsize(800, 800)

        # Variables
        self.enter_name = StringVar()
        self.enter_calories = StringVar()
        self.enter_protein = StringVar()
        self.enter_carbohydrates = StringVar()
        self.enter_fats = StringVar()

        # Styles
        parent.s.configure('new_meal.TLabel', background='#DAFFFB',
                           foreground='#053B50')
        parent.s.configure('meal.TLabel', background='#DAFFFB',
                           foreground='#053B50', font=(None, 10))
        parent.s.configure('new_meal.TEntry', background='#black',
                           foreground='#053B50')
        parent.s.configure('newmeal.TButton', relief="raised",
                           background='#DAFFFB', foreground='#04364A',
                           highlightbackground='red', borderwidth=2,
                           focuscolor='white')
        parent.s.configure('close.TButton', relief="raised",
                           background='#DAFFFB', foreground='red',
                           highlightbackground='red', borderwidth=1,
                           focuscolor='white', font=(None, 7), height=7,
                           width=3)

        # Widgets
        self.outer_frame = ttk.Frame(self, padding="8 8 8 8",
                                     style='dark.TFrame')
        self.outer_frame.grid(column=0, row=0, sticky='NWES')
        self.inner_frame = ttk.Frame(self.outer_frame, padding="5 5 5 5",
                                     style='bright.TFrame', )
        self.inner_frame.grid(column=0, row=0, sticky='NWES')
        ttk.Label(self.inner_frame, text='Name: ',
                  style='new_meal.TLabel').grid(column=0, row=0, sticky='NW',
                                                padx=5,
                                                pady=5)
        ttk.Entry(self.inner_frame, style='new_meal.TEntry',
                  textvariable=self.enter_name).grid(column=1, row=0,
                                                     sticky='NWE', padx=5,
                                                     pady=5)

        ttk.Label(self.inner_frame, text='Calories: ',
                  style='new_meal.TLabel').grid(column=0, row=1, sticky='NW',
                                                padx=5,
                                                pady=5)
        ttk.Entry(self.inner_frame, style='new_meal.TEntry',
                  textvariable=self.enter_calories).grid(column=1, row=1,
                                                         sticky='NWE', padx=5,
                                                         pady=5)

        ttk.Label(self.inner_frame, text='Protein: ',
                  style='new_meal.TLabel').grid(column=0, row=2, sticky='NW',
                                                padx=5,
                                                pady=5)
        ttk.Entry(self.inner_frame, style='new_meal.TEntry',
                  textvariable=self.enter_protein).grid(column=1, row=2,
                                                        sticky='NWE', padx=5,
                                                        pady=5)

        ttk.Label(self.inner_frame, text='Carbohydrates: ',
                  style='new_meal.TLabel').grid(column=0, row=3, sticky='NW',
                                                padx=5,
                                                pady=5)
        ttk.Entry(self.inner_frame, style='new_meal.TEntry',
                  textvariable=self.enter_carbohydrates).grid(column=1, row=3,
                                                              sticky='NWE',
                                                              padx=5, pady=5)
        ttk.Label(self.inner_frame, text='Fats: ',
                  style='new_meal.TLabel').grid(column=0, row=4, sticky='NW',
                                                padx=5,
                                                pady=5)
        ttk.Entry(self.inner_frame, style='new_meal.TEntry',
                  textvariable=self.enter_fats).grid(column=1, row=4,
                                                     sticky='NWE', padx=5,
                                                     pady=5)

        ttk.Button(self.inner_frame, style='newmeal.TButton',
                   text='Add Product/Meal', command=self.add_meal).grid(
            column=1, row=5,
            sticky='SE', padx=5, pady=5)

        # Grid configurations
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.outer_frame.columnconfigure(0, weight=1)
        self.outer_frame.rowconfigure(0, weight=1)
        self.inner_frame.columnconfigure(0, weight=0)
        self.inner_frame.columnconfigure(1, weight=3)
        self.inner_frame.rowconfigure(0, weight=1)
        self.inner_frame.rowconfigure(1, weight=1)
        self.inner_frame.rowconfigure(2, weight=1)
        self.inner_frame.rowconfigure(3, weight=1)
        self.inner_frame.rowconfigure(4, weight=1)
        self.inner_frame.rowconfigure(5, weight=1)

    def check_scrollbar(self):
        if self.frame.scrollwindow.winfo_reqheight() <= self.frame.canv.winfo_height():
            self.frame.yscrlbr.grid_forget()
        else:
            self.frame.yscrlbr.grid(column=1, row=0, sticky='nes')

        if self.frame.scrollwindow.winfo_reqwidth() != self.frame.canv.winfo_width():
            self.frame.canv.itemconfigure(self.frame.scrollwindow_id,
                                          width=self.frame.canv.winfo_width())

        if self.frame.scrollwindow.winfo_reqheight() < self.frame.canv.winfo_height():
            self.frame.canv.itemconfigure(self.frame.scrollwindow_id,
                                          height=self.frame.canv.winfo_height())
        else:
            self.frame.canv.itemconfigure(self.frame.scrollwindow_id,
                                          height=self.frame.scrollwindow.winfo_reqheight())

    def delete_meal(self, label, button, key, meal):
        label.destroy()
        button.destroy()
        del self.macros[key]
        self.add_local_calories(self.macros)
        self.delete_global_calories(meal)
        self.check_scrollbar()
        self.parent.update_idletasks()

    def delete_global_calories(self, meal):
        self.parent.global_calories_value -= meal[0]
        self.parent.global_proteins_value -= meal[1]
        self.parent.global_cabrohydrates_value -= meal[2]
        self.parent.global_fats_value -= meal[3]

        self.parent.global_calories.set(
            f'Calories:{self.parent.global_calories_value}')
        self.parent.global_proteins.set(
            f'Proteins:{self.parent.global_proteins_value}')
        self.parent.global_cabrohydrates.set(
            f'Cabrohydrates:{self.parent.global_cabrohydrates_value}')
        self.parent.global_fats.set(f'Fats:{self.parent.global_fats_value}')
        self.parent.update_idletasks()

    def add_global_calories(self, meal):
        self.parent.global_calories_value += meal[0]
        self.parent.global_proteins_value += meal[1]
        self.parent.global_cabrohydrates_value += meal[2]
        self.parent.global_fats_value += meal[3]

        self.parent.global_calories.set(
            f'Calories:{self.parent.global_calories_value}')
        self.parent.global_proteins.set(
            f'Proteins:{self.parent.global_proteins_value}')
        self.parent.global_cabrohydrates.set(
            f'Cabrohydrates:{self.parent.global_cabrohydrates_value}')
        self.parent.global_fats.set(f'Fats:{self.parent.global_fats_value}')
        self.parent.update_idletasks()

    def add_local_calories(self, meal):

        self.calories_value = 0
        self.proteins_value = 0
        self.cabrohydrates_value = 0
        self.fats_value = 0

        if self.macros is not None:
            for key, value in meal.items():
                self.calories_value += value[0]
                self.proteins_value += value[1]
                self.cabrohydrates_value += value[2]
                self.fats_value += value[3]

        self.calories.set(f'Calories:{self.calories_value}')
        self.proteins.set(f'Proteins:{self.proteins_value}')
        self.cabrohydrates.set(f'Cabrohydrates:{self.cabrohydrates_value}')
        self.fats.set(f'Fats:{self.fats_value}')
        self.parent.update_idletasks()

    def add_meal(self):
        if not self.labels:
            i = 0
        else:
            keys = list(self.labels.keys())
            i = keys[-1] + 1

        # create list with macros of meal and add to dictionary
        try:
            self.meal = [int(self.enter_calories.get()),
                         int(self.enter_protein.get()),
                         int(self.enter_carbohydrates.get()),
                         int(self.enter_fats.get())]

        except ValueError:
            messagebox.showerror('Error',
                                 'Error: Entered values except name have to be integer')

        else:
            # create and add label to dictionary
            self.meal_label = ttk.Label(self.frame.scrollwindow,
                                        text=self.enter_name.get(),
                                        style='meal.TLabel')
            self.labels[i] = self.meal_label
            self.meal_label.grid(row=i, column=0, sticky='NW')

            # create and add button which delete meal to dictionary
            self.meal_button = ttk.Button(self.frame.scrollwindow,
                                          style='close.TButton', text='X')
            self.buttons[i] = self.meal_button
            self.meal_button.grid(row=i, column=1, sticky='NE')

            self.macros[i] = self.meal

            self.add_local_calories(self.macros)
            self.add_global_calories(self.meal)

            self.meal_button.configure(
                command=lambda: self.delete_meal(self.labels[i],
                                                 self.buttons[i], i,
                                                 self.macros[i]))
        self.check_scrollbar()
        self.parent.update_idletasks()
