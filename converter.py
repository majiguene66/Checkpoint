import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the temperature from Fahrenheit to Celsius and display the result."""
    try:
        # Get the value from the entry widget and convert it to a float
        fahrenheit = float(ent_temperature.get())
        
        # Calculate Celsius formula: (F - 32) * 5/9
        celsius = (fahrenheit - 32) * 5 / 9
        
        # Round the result to 2 decimal places and update the result label
        lbl_result["text"] = f"{round(celsius, 2)}\N{DEGREE CELSIUS}"
    except ValueError:
        # Handle the error if the input is not a valid number
        lbl_result["text"] = "Invalid Input"

# Create the main Tkinter window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=True, height=True)

# Create a frame to hold the Fahrenheit entry and its unit label
frm_entry = tk.Frame(master=window)

# Create the entry widget for the input temperature
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Create the label widget to display the Fahrenheit symbol ℉
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Arrange the entry and label widgets inside the frame using grid
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion button widget linking to the function
btn_convert = tk.Button(
    master=window, 
    text="\N{RIGHTWARDS BLACK ARROW}", 
    command=fahrenheit_to_celsius
)

# Create the label widget to display the result in Celsius ℃
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Arrange the frame, button, and result label layout in the main window
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Start the application loop
window.mainloop()
