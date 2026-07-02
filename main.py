
from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        name = name_entry.get()
        electricity = float(electricity_entry.get())
        car = float(car_entry.get())
        public = float(public_entry.get())
        meat = float(meat_entry.get())
        plastic = int(plastic_entry.get())

        recycle = recycle_var.get()

        electricity_emission = electricity * 0.85
        car_emission = car * 0.12
        public_emission = public * 0.05
        meat_emission = meat * 1.5
        plastic_emission = (plastic * 0.1) / 7

        total = (electricity_emission + car_emission + public_emission +
                 meat_emission + plastic_emission)

        if recycle == "Yes":
            total *= 0.9

        if total < 5:
            advice = "Excellent 🌱"
        elif total < 10:
            advice = "Good 🙂"
        elif total < 20:
            advice = "Average ⚠️"
        else:
            advice = "High 🚨"

        result.config(text=f"{name}\n{total:.2f} kg CO2/day\n{advice}")

    except:
        messagebox.showerror("Error", "Invalid input")

window = Tk()
window.title("Carbon Footprint Tracker")
window.geometry("520x650")
window.configure(bg="black")

Label(window, text="🌍 Carbon Footprint Tracker 🌱",
      bg="black", fg="#00FF7F",
      font=("Arial", 16, "bold")).pack()

def make_entry(text):
    Label(window, text=text, bg="black", fg="white").pack()
    e = Entry(window, bg="#2C2C2C", fg="white", insertbackground="white")
    e.pack()
    return e

name_entry = make_entry("Name")
electricity_entry = make_entry("Electricity (kWh)")
car_entry = make_entry("Car km")
public_entry = make_entry("Public Transport km")
meat_entry = make_entry("Meat meals")
plastic_entry = make_entry("Plastic/week")

recycle_var = StringVar(value="No")
Label(window, text="Recycle?", bg="black", fg="white").pack()
Radiobutton(window, text="Yes", variable=recycle_var, value="Yes",
            bg="black", fg="white", selectcolor="#2C2C2C").pack()
Radiobutton(window, text="No", variable=recycle_var, value="No",
            bg="black", fg="white", selectcolor="#2C2C2C").pack()

Button(window, text="Calculate", bg="#00C853",
       command=calculate).pack(pady=10)

result = Label(window, text="", bg="black", fg="#00FF7F")
result.pack()

window.mainloop()
