import tkinter as tk
from metro_network import MetroNetwork
from metro_gui import MetroGUI

def main():
    metro_network = MetroNetwork()
    
    stations = [
        "Jhil Mil", "DLF Phase 3", "Okhla NSIC", "Dwarka Mor", "Dilli Haat INA [Conn: Yellow]", 
        "Noida Sector 143", "Moolchand", "Chawri Bazar", "Maya Puri", 
        "Central Secretariat [Conn: Violet]", "Noida Sector 146", "Tikri Border", 
        "Jangpura", "Major Mohit Sharma", "Majlis Park", "Bhikaji Cama Place", 
        "Mundka Industrial Area (MIA)", "Belvedere Towers", "Adarsh Nagar", 
        "Noida City Center", "Arjan Garh", "Dwarka Sector 9", "Azadpur [Conn: Yellow]", 
        "Qutab Minar", "R K Ashram Marg", "Uttam Nagar West", "Dwarka [Conn: Blue]", 
        "Delta 1 Greater Noida", "Golf Course", "Shiv Vihar", "Kashmere Gate [Conn: Yellow]", 
        "Jawaharlal Nehru Stadium", "Patel Chowk", "Janak Puri West [Conn: Magenta]", 
        "Kalkaji Mandir [Conn: Violet]", "Dwarka Sector 21(First station) [Conn: Orange]", 
        "Subhash Nagar", "Tughlakabad", "Old Faridabad", "Rohini Sector 18-19", 
        "Keshav Puram", "Kohat Enclave", "Paschim Vihar (West)", "Dwarka Sector 14", 
        "IIT Delhi", "Rajouri Garden [Conn: Blue]", "Karkarduma Court", 
        "Rajendra Place", "Hauz Khas [Conn: Yellow]", "Noida Sector 137", 
        "Okhla", "Jhandewalan", "Raj Bagh", "Inderlok Conn:Red", "Noida Sector 51 [Conn: Blue]", 
        "Pari Chowk Greater Noida", "Noida Sector 148", "Pitam Pura", "Moti Nagar"
    ]
    
   
    for station in stations:
        metro_network.add_station(station)

    
    connections = [
        ("Jhil Mil", "Welcome [Conn: Red]", 5.0),
        ("Welcome [Conn: Red]", "DLF Phase 3", 6.0),
        ("DLF Phase 3", "Okhla NSIC", 8.0),
        ("Okhla NSIC", "Dwarka Mor", 10.0),
        ("Dwarka Mor", "Dilli Haat INA [Conn: Yellow]", 12.0),
        ("Dilli Haat INA [Conn: Yellow]", "Noida Sector 143", 15.0),
        ("Noida Sector 143", "Moolchand", 7.0),
        ("Moolchand", "Chawri Bazar", 9.0),
        ("Chawri Bazar", "Maya Puri", 13.0),
        ("Maya Puri", "Central Secretariat [Conn: Violet]", 11.0),
        ("Central Secretariat [Conn: Violet]", "Noida Sector 146", 16.0),
        ("Noida Sector 146", "Tikri Border", 14.0),
        ("Tikri Border", "Jangpura", 12.0),
        ("Jangpura", "Major Mohit Sharma", 18.0),
        ("Major Mohit Sharma", "Majlis Park", 20.0),
        ("Majlis Park", "Bhikaji Cama Place", 14.0),
        ("Bhikaji Cama Place", "Mundka Industrial Area (MIA)", 22.0),
        ("Mundka Industrial Area (MIA)", "Belvedere Towers", 19.0),
        ("Belvedere Towers", "Adarsh Nagar", 23.0),
        ("Adarsh Nagar", "Noida City Center", 17.0),
        ("Noida City Center", "Arjan Garh", 16.0),
        ("Arjan Garh", "Dwarka Sector 9", 13.0),
        ("Dwarka Sector 9", "Azadpur [Conn: Yellow]", 11.0),
        ("Azadpur [Conn: Yellow]", "Qutab Minar", 12.0),
        ("Qutab Minar", "R K Ashram Marg", 15.0),
        ("R K Ashram Marg", "Uttam Nagar West", 10.0),
        ("Uttam Nagar West", "Dwarka [Conn: Blue]", 7.0),
        ("Dwarka [Conn: Blue]", "Delta 1 Greater Noida", 21.0),
        ("Delta 1 Greater Noida", "Golf Course", 19.0),
        ("Golf Course", "Shiv Vihar", 17.0),
        ("Shiv Vihar", "Kashmere Gate [Conn: Yellow]", 12.0),
        ("Kashmere Gate [Conn: Yellow]", "Jawaharlal Nehru Stadium", 9.0),
        ("Jawaharlal Nehru Stadium", "Patel Chowk", 8.0),
        ("Patel Chowk", "Janak Puri West [Conn: Magenta]", 13.0),
        ("Janak Puri West [Conn: Magenta]", "Kalkaji Mandir [Conn: Violet]", 11.0),
        ("Kalkaji Mandir [Conn: Violet]", "Dwarka Sector 21(First station) [Conn: Orange]", 20.0),
        ("Dwarka Sector 21(First station) [Conn: Orange]", "Subhash Nagar", 18.0),
        ("Subhash Nagar", "Tughlakabad", 15.0),
        ("Tughlakabad", "Old Faridabad", 14.0),
        ("Old Faridabad", "Rohini Sector 18-19", 22.0),
        ("Rohini Sector 18-19", "Keshav Puram", 13.0),
        ("Keshav Puram", "Kohat Enclave", 12.0),
        ("Kohat Enclave", "Paschim Vihar (West)", 16.0),
        ("Paschim Vihar (West)", "Dwarka Sector 14", 11.0),
        ("Dwarka Sector 14", "IIT Delhi", 15.0),
        ("IIT Delhi", "Rajouri Garden [Conn: Blue]", 10.0),
        ("Rajouri Garden [Conn: Blue]", "Karkarduma Court", 14.0),
        ("Karkarduma Court", "Rajendra Place", 12.0),
        ("Rajendra Place", "Hauz Khas [Conn: Yellow]", 9.0),
        ("Hauz Khas [Conn: Yellow]", "Noida Sector 137", 8.0),
        ("Noida Sector 137", "Okhla", 13.0),
        ("Okhla", "Jhandewalan", 17.0),
        ("Jhandewalan", "Raj Bagh", 12.0),
        ("Raj Bagh", "Inderlok Conn:Red", 10.0),
        ("Inderlok Conn:Red", "Noida Sector 51 [Conn: Blue]", 18.0),
        ("Noida Sector 51 [Conn: Blue]", "Pari Chowk Greater Noida", 21.0),
        ("Pari Chowk Greater Noida", "Noida Sector 148", 19.0),
        ("Noida Sector 148", "Pitam Pura", 17.0),
        ("Pitam Pura", "Moti Nagar", 12.0),

        
        ("Moti Nagar", "Paschim Vihar (West)", 7.0),
        ("Paschim Vihar (West)", "Welcome [Conn: Red]", 10.0),
        ("Welcome [Conn: Red]", "Majlis Park", 12.0)
    ]

    for conn in connections:
        metro_network.add_connection(*conn)

    root = tk.Tk()
    app = MetroGUI(root, metro_network)
    root.mainloop()

if __name__ == "__main__":
    main()
