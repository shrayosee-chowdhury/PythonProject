import customtkinter
from tkinter import *


root = customtkinter.CTk()
root.title("Unit Converter")
root.geometry("600x500")
root.configure(bg_color="DarkBlue")


unit_options = {
    'Length': ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile'],
    'Mass': ['milligram', 'gram', 'kilogram', 'ounce', 'pound'],
    'Temperature': ['Celsius', 'Fahrenheit', 'Kelvin']
}
length_factors = {
    'millimeter': 0.001, 'centimeter': 0.01, 'meter': 1, 'kilometer': 1000,
    'inch': 0.0254, 'foot': 0.3048, 'yard': 0.9144, 'mile': 1609.34
}
mass_factors = {
    'milligram': 0.001, 'gram': 1, 'kilogram': 1000,
    'ounce': 28.3495, 'pound': 453.592
}


variable1 = StringVar(value=list(unit_options.keys())[0])
variable2 = StringVar()
variable3 = StringVar()
input_value = DoubleVar()
output_value = StringVar()


def update_options(*args):
    selected_category = variable1.get()
    new_options = unit_options[selected_category]
    
    from_option.configure(values=new_options)
    to_option.configure(values=new_options)

    variable2.set(new_options[0])
    variable3.set(new_options[1])

# Function 
def convert_units():
    category = variable1.get()
    from_unit = variable2.get()
    to_unit = variable3.get()
    value = input_value.get()

    try:
        if category == "Length":
            result = value * (length_factors[to_unit] / length_factors[from_unit])
        elif category == "Mass":
            result = value * (mass_factors[to_unit] / mass_factors[from_unit])
        elif category == "Temperature":
            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
        else:
            result = "Invalid Conversion"
        
        output_value.set(f"Result: {round(result, 4)} {to_unit}")

    except Exception as e:
        output_value.set("Error!")

variable1.trace_add("write", update_options)




title_label = customtkinter.CTkLabel(root, text="UNIT CONVERTER", text_color="black",
                                     font=("calibri", 30, "bold"), bg_color="white")
title_label.place(x=150, y=20)

unit_label = customtkinter.CTkLabel(root, text="UNIT", text_color="black",
                                    font=("calibri", 20, "bold"), bg_color="white")
unit_label.place(x=180, y=80)

unit_option = customtkinter.CTkComboBox(root, font=("calibri", 15), text_color="black",
                                        fg_color="pink", bg_color="mintcream",
                                        values=list(unit_options.keys()), variable=variable1, width=150)
unit_option.place(x=180, y=110)

from_label = customtkinter.CTkLabel(root, text="From", text_color="black",
                                    font=("calibri", 20, "bold"), bg_color="white")
from_label.place(x=20, y=160)

from_option = customtkinter.CTkComboBox(root, font=("calibri", 15), text_color="black",
                                        fg_color="pink", bg_color="mintcream",
                                        values=unit_options['Length'], variable=variable2, width=150)
from_option.place(x=20, y=190)

to_label = customtkinter.CTkLabel(root, text="To", text_color="black",
                                  font=("calibri", 20, "bold"), bg_color="white")
to_label.place(x=200, y=160)

to_option = customtkinter.CTkComboBox(root, font=("calibri", 15), text_color="black",
                                      fg_color="pink", bg_color="mintcream",
                                      values=unit_options['Length'], variable=variable3, width=150)
to_option.place(x=200, y=190)

value_label = customtkinter.CTkLabel(root, text="Value", text_color="black",
                                     font=("calibri", 20, "bold"), bg_color="white")
value_label.place(x=400, y=160)

value_entry = customtkinter.CTkEntry(root, textvariable=input_value, font=("calibri", 15),
                                     fg_color="white", text_color="black", width=100)
value_entry.place(x=400, y=190)

convert_button = customtkinter.CTkButton(root, text="CONVERT", font=("calibri", 20, "bold"),
                                         text_color="black", fg_color="lightcyan",
                                         hover_color="lightskyblue", corner_radius=10, width=150,
                                         command=convert_units)
convert_button.place(x=220, y=250)

result_label = customtkinter.CTkLabel(root, textvariable=output_value, font=("calibri", 20, "bold"),
                                      text_color="black", bg_color="lightpink")
result_label.place(x=220, y=300)

update_options()  

root.mainloop()
