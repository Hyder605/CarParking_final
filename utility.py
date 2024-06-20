import json
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"p1":[[None, None, None,None], [None, None, None,None],[None, None, None,None],[None, None, None,None]],
                 "p2":[[None, None, None,None], [None, None, None,None],[None, None, None,None],[None, None, None,None]]}

# Function to save data to file
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)



def parking_table(filename):
    data = load_data(filename)
    l1 = data['p1']
    l2 = data['p2']

    print("Parking1".ljust(25), "Parking2".ljust(25))  # Print headings for l1 and l2

    for sublist1, sublist2 in zip(l1, l2):
        # Print elements from l1
        for elem1 in sublist1:
            if elem1 is not None:
                print(f"{elem1:<6}", end=" ")
            else:
                print("None".ljust(6), end=" ")  # Print 'None' with proper spacing
        # Add spacing between l1 and l2
        print(" " * 5, end="")
        # Print elements from l2
        for elem2 in sublist2:
            if elem2 is not None:
                print(f"{elem2:<6}", end=" ")
            else:
                print("None".ljust(6), end=" ")  # Print 'None' with proper spacing
        print()



# Function to find the coordinates of a specific car in the data structure
def find_car_position(data, car):
    for parking_lot in data:
        for i, row in enumerate(data[parking_lot]):
            for j, val in enumerate(row):
                if val == car:
                    print(parking_lot,i,j)
                    return parking_lot, i, j
    return None, None, None  # Car not found

# Function to find the nearest null value to a given position
# def find_nearest_null(data, start_p, start_i, start_j):
#     nearest_distance = float('inf')
#     nearest_position = None
    
#     for p in data:
#         for i, row in enumerate(data[p]):
#             for j, val in enumerate(row):
#                 if val is None:
#                     distance = abs(start_i - i) + abs(start_j - j)
#                     if distance < nearest_distance:
#                         nearest_distance = distance
#                         nearest_position = (p, i, j)
    
#     return nearest_position

def find_nearest_null(data, start_p, start_i, start_j):
    nearest_distance = float('inf')
    nearest_position = None

    for p in data:
        for i, row in enumerate(data[p]):
            if i == start_i and p == start_p:  # Skip the same row
                continue
            for j, val in enumerate(row):
                if val is None:
                    distance = abs(start_i - i) + abs(start_j - j)
                    if distance < nearest_distance:
                        nearest_distance = distance
                        nearest_position = (p, i, j)

    return nearest_position