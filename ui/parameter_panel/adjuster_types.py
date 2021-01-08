from .parameter_adjuster_base import ParameterAdjusterBase
import tkinter as tk


class CheckboxAdjusterType(ParameterAdjusterBase):
    def __init__(self, parameter_panel, name, default, **kwargs):
        super().__init__(parameter_panel, name, tk.BooleanVar(value=default), pad_y=3, **kwargs)

        self.widget = tk.Checkbutton(self.frame, variable=self.var)
        self.widget.pack(side='left')


class EntryAdjusterType(ParameterAdjusterBase):
    def __init__(self, parameter_panel, name, default, **kwargs):
        super().__init__(parameter_panel, name, tk.StringVar(value=default), pad_y=3, **kwargs)

        self.widget = tk.Entry(self.frame, textvariable=self.var, width=5, relief='solid')
        self.widget.config(font=self.normal_font)
        self.widget.pack(side='left')


class PickerAdjusterType(ParameterAdjusterBase):
    """An adjuster type that can be used to choose an item from a list of (or function that returns) choices, shown as a
    dropdown list"""

    def __init__(self, parameter_panel, name, default, **kwargs):
        super().__init__(parameter_panel, name, tk.StringVar(value=default), **kwargs)

        self.widget = tk.OptionMenu(self.frame, self.var, [])
        self.widget.config(font=self.normal_font)
        self.widget.bind('<Button-1>', self.on_dropdown)
        self.widget.pack(side='left')

    def on_dropdown(self, _):
        """Refresh the choices in the list using the get_choices function"""
        self.widget['menu'].delete(0, 'end')
        for choice in self.get_choices():
            self.widget['menu'].add_command(label=choice, font=self.normal_font,
                                            command=lambda c=choice: self.choose(c))

    def choose(self, choice):
        self.var.set(choice)

    def get_choices(self):
        """Overridden by subclasses, returns all choices valid"""
        return []
