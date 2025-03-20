import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Weather App")  
root.geometry("300x200")

# Function to handle button click
def get_weather():
    city = city_entry.get()
    print("City entered:", city)  # For now, just print it

# Create a label
label = tk.Label(root, text="Enter City:", font=("Arial", 12))
label.pack(pady=5)

# Create an entry field
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

# Create a button and link it to get_weather()
get_weather_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_weather_btn.pack(pady=5)

# Run the application
root.mainloop()
