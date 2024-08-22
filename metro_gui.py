import tkinter as tk
from tkinter import ttk

class MetroGUI:
    def __init__(self, root, metro_network):
        self.root = root
        self.root.title("Metro Network Simulation")
          
        self.metro_network = metro_network  
        self.setup_gui()

    def setup_gui(self):
        
        self.station_var = tk.StringVar()
        self.station_var.set("Select Station")
        self.station_select = ttk.Combobox(self.root, textvariable=self.station_var)
        self.station_select.grid(row=2, column=2, padx=10, pady=10)

        
        self.destination_var = tk.StringVar()
        self.destination_var.set("Select Destination")
        self.destination_select = ttk.Combobox(self.root, textvariable=self.destination_var)
        self.destination_select.grid(row=2, column=3, padx=10, pady=10)

       
        self.show_path_button = tk.Button(self.root, text="Show Shortest Path", command=self.show_shortest_path)
        self.show_path_button.grid(row=2, column=4, padx=10, pady=10)

        
        self.path_text = tk.Text(self.root, height=10, width=100)
        self.path_text.grid(row=3, column=0, columnspan=5, padx=20, pady=20)

        
        self.set_metro_network(self.metro_network)

    def set_metro_network(self, metro_network):
        self.metro_network = metro_network
        if self.metro_network:
            stations = self.metro_network.get_stations()
            self.station_select['values'] = stations
            self.destination_select['values'] = stations

    def show_shortest_path(self):
        if self.metro_network:
            source = self.station_var.get()
            destination = self.destination_var.get()
            if source and destination:
                shortest_path = self.metro_network.shortest_path(source, destination)
                self.path_text.delete(1.0, tk.END)  # Clear previous text
                self.path_text.insert(tk.END, f"Shortest path from {source} to {destination}: {shortest_path}")

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    metro_network = None  # Replace with your metro network object
    app = MetroGUI(root, metro_network)
    root.mainloop()
