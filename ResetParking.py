from utility import load_data, save_data
filename = "parking_data.json"

# Load data from file
parking_data = load_data(filename)
p1=parking_data["p1"]

p2=parking_data["p2"]


# # Reset the Car Parking Slots
parking_data = {"p1": [[None,None,None, None],[None,None,None, None], [None,None,None, None], [None,None,None, None]], 
      "p2": [[None,None,None, None],[None,None,None, None], [None,None,None, None], [None,None,None, None]]}
save_data(parking_data, filename)
