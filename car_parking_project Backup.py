
from utility import load_data, save_data,parking_table 
filename = "parking_data.json"

load_data(filename)
parking_table("parking_data.json")

def display_menu():
    print("Select an option:")
    print("1. Option 1- Want To Park the vehicle")
    print("2. Option 2-Want to Exit the vehicle ")

filename = "parking_data.json"
# Load data from file
parking_data = load_data(filename)
p1=parking_data["p1"]
p2=parking_data["p2"]

## Display Menu for Selecting Either You want to Enter Or Exit Your Vehicle
def display_menu():
    print("Select an option:")
    print("1. Option 1- Want To Park the vehicle")
    print("2. Option 2-Want to Exit the vehicle ")
last_row_key_p1 = len(p1)-1 # Get the key of the last row dynamically
last_row_key_p2 = len(p2)-1 # Get the key of the last row dynamically


# Main Function
def CarParking():

    filename = "parking_data.json"
    parking_data = load_data(filename)
    p1=parking_data["p1"]
    p2=parking_data["p2"]
    display_menu()
    choice = input("Enter your choice (1 or 2 )")

    Total_Empty_slots_p1 = sum(sublist.count(None) for sublist in p1)
    Total_Empty_slots_p2 = sum(sublist.count(None) for sublist in p2)
    # print("Total Empty slots in Parking 1 is ", Total_Empty_slots_p1)
    # print("Total Empty slots in Parking 2 is ", Total_Empty_slots_p2)

    ## If you want to Enter Your Car
    if choice == '1':
            print("You selected Option 1.")
            veh=input("enter veh: ")
            print("Your selected Vehicle No is ", veh)
            print("After Parking the Car in the Slot")
                
            for row_p1, row_p2 in zip(p1, p2):

                #counting Number of None values in each rows
                none_in_p1=row_p1.count(None)
                # print(row_p1)
                # print("none_in_p1",none_in_p1)
                none_in_p2=row_p2.count(None)
                # print(row_p2)
                # print("none_in_p2",none_in_p2)
                
                ## Checking either there is None/Empty slot in the iteration of the Row in either Parking1 or Parking2
                if none_in_p1!=0 or none_in_p2!=0:
                    
                    ## checking the length of None/Empty slots in Row of Parking1 is equal or greater than Row of Parking2
                    if none_in_p1>=none_in_p2 and Total_Empty_slots_p1>3:
                        for rows in range(len(p1)):  # Iterate over the keys of parking slots in "p1"
                            # print("Parking slot:", p1[rows])
                            if None in p1[rows]:
                                for items in reversed(range(len(p1[rows]))):
                                    print("items",items)
                                    if p1[rows][items] is None:
                                        # print("None value found at index", items, "in slot", rows)
                                        if rows != last_row_key_p1:  # Check if it's not the last row
                                            print(items,len(p1[rows]))
                                        # Move existing cars to one index lower
                                            for j in range(items, len(p1[rows]) - 1):
                                                print(j)
                                                p1[rows][j] = p1[rows][j + 1]
                                            # Insert the new car at the highest available index
                                            p1[rows][-1] = veh
                                            # Save data to file
                                            save_data(parking_data, filename)
                                            break
                                        else:
                                            print("Parking  is FUll, You can't Park your vehicle Here")
                                            break

                                break
                        break    
                    elif none_in_p2>none_in_p1 and Total_Empty_slots_p2>3:    
                        # print("Length of p2 row:", len(row_p2))

                        for rows in range(len(p2)):  # Iterate over the keys of parking slots in "p2"
                            # print("Parking slot:", p2[rows])
                            if None in p2[rows]:
                                for items in (range(len(p2[rows]))):
                                    # print("items",items)
                                    if p2[rows][items] is None:
                                        # print("None value found at index", items, "in slot", rows)

                                        if rows != last_row_key_p2:  # Check if it's not the last row
                                        #     # Move existing cars to one at Higher Index
                                            
                                            for j in reversed(range(items)):
                                                p2[rows][j+1] = p2[rows][j]
                                        #         # Insert the new car at the lowest available index
                                            p2[rows][0] = veh
                                            # Save data to file
                                            save_data(parking_data, filename)
                                            break
                                        else:
                                            print("Parking  is FUll, You can't Park your vehicle Here")
                                            break

                                break
                        break
                    else:
                        print("Parking  is FUll, You can't Park your vehicle Here")
                        break
                else:
                    pass
            save_data(parking_data, filename)
        #################################################################################################################################################################
        ## EXIT FOR PARKING 

    elif choice == '2':
            veh=input("enter Exit vehicle no : ")

            print("Your selected Vehicle No is ", veh)

         ###############################################################
                    ### Exit for Parking 1
            # move_vehicle_from_p1(veh)
            for slot_item_in_list in p1:
                # print(slot_item_in_list)
                if veh in slot_item_in_list:
                    # print(slot_item_in_list)
                    last_index = len(p1) - 1
                    veh_ahead_list=[]
                    veh_behind_list=[]
                    # print("veh111111111111", veh)
                   
                    for slot_rows in (range(len(p1))): 
                    
                        if veh in p1[slot_rows]:
                            print("veh is in p1")

                            veh_index = p1[slot_rows].index(veh)
                        
                            # print("vehicle is in the slot", slot_rows, "at index", veh_index)

                            # store value and index of vehicles greater than veh
                            for index_veh_ahead,value_veh_ahead in reversed(list(enumerate(p1[slot_rows]))):
                                # print(index_veh_ahead,value_veh_ahead)
                                if index_veh_ahead>veh_index and  value_veh_ahead is not None:
                                    veh_ahead_list.append((index_veh_ahead, value_veh_ahead))
                                    print("veh_ahead_list",veh_ahead_list)

                            # store value and index of vehicles less than veh
                            for index_veh_behind, value_veh_behind in enumerate(p1[slot_rows]):
                                if index_veh_behind<veh_index and value_veh_behind is not None:
                                    veh_behind_list.append((index_veh_behind, value_veh_behind))
                                    print("veh_behind_list",veh_behind_list)
  

                            if p1[slot_rows].index(veh)==last_index:
                                p1[slot_rows][last_index]=None
                                # print(p1[slot_rows])
                                for i in range(len(p1[slot_rows])-2, -1, -1): #or reversed(range(p1[slot_rows])-1) #index===>2,1,0
                                    print(i)
                                    # If the current item is not None
                                    if p1[slot_rows][i] is not None:
                                        # Move the item to the right until it finds a Not None value or reaches the end
                                        j = i + 1
                                        print(j)
                                        while j < len(p1[slot_rows]) and p1[slot_rows][j] is None:
                                            p1[slot_rows][j],p1[slot_rows][j-1] = p1[slot_rows][j-1], p1[slot_rows][j]
                                            j += 1
                                            save_data(parking_data, filename)
                            else:
                                for i in (range(len(veh_ahead_list))):
                                    # print("vehicle is in the First slot",i)
                                    for empty_iter in (range(len(p1))):
                                        if None in p1[empty_iter] and veh not in p1[empty_iter]:
                                            # print(p1[empty_iter])
                                            ## moving the vehices ahead of the required Veh to remove to other Empty slot , so that there should be vacant space
                                            p1[empty_iter].append(veh_ahead_list[i][1])
                                            p1[slot_rows].pop()
                                            p1[slot_rows].insert(0, None)
                                            # print(p1[slot_rows])
                                            # print(p1[empty_iter])
                                            p1[empty_iter].pop(0)
                                            # print(p1[empty_iter])
                                            break
                                        # print("empty_iter", empty_iter)
                                
                                p1[slot_rows].pop() ## Required veh is removed here
                                p1[slot_rows].insert(0, None)
                                
                                                
                            save_data(parking_data, filename)
                            break
            
                #################################################################################################################################################################
                ## EXIT FOR PARKING 2
            for slot_item_list_p2 in p2:
                            # print(slot_item_in_list)
                            if veh in slot_item_list_p2:
                                print("veh is in p2")
                                first_index = 0
                                veh_ahead_list=[]
                                veh_behind_list=[]
                                
                                for slot_rows in reversed(range(len(p2))):
                                    print(slot_rows)

                                    
                                    if veh in p2[slot_rows]:
                                        print(p2[slot_rows])
                                        veh_index = p2[slot_rows].index(veh)
                                    
                                        # print("vehicle is in the slot", slot_rows, "at index", veh_index)

                                        # store value and index of vehicles greater than veh
                                        for index_veh_ahead,value_veh_ahead in reversed(list(enumerate(p2[slot_rows]))):
                                            # print(index_veh_ahead,value_veh_ahead)
                                            if index_veh_ahead>veh_index and  value_veh_ahead is not None:
                                                veh_ahead_list.append((index_veh_ahead, value_veh_ahead))

                                        # store value and index of vehicles less than veh
                                        for index_veh_behind, value_veh_behind in enumerate(p2[slot_rows]):
                                            if index_veh_behind<veh_index and value_veh_behind is not None:
                                                veh_behind_list.append((index_veh_behind, value_veh_behind))  

                                        if p2[slot_rows].index(veh)==first_index:
                                            p2[slot_rows][first_index]=None
                                            for i in range(1,len(p2[slot_rows])):
                                                # If the current item is not None
                                                if p2[slot_rows][i] is not None:
                                                    # Move the item to the right until it finds a None or reaches the end
                                                    j = i - 1
                                                    while j < (len(p2[slot_rows])-1) and p2[slot_rows][j] is None:
                                                        p2[slot_rows][j],p2[slot_rows][j+1] = p2[slot_rows][j+1], p2[slot_rows][j]
                                                        j += 1
                                        else:
                                            for i in (range(len(veh_behind_list))):
                                                # print("vehicle is in the First slot",i)
                                                for empty_iter in (range(len(p2))):
                                                    if None in p2[empty_iter] and veh not in p2[empty_iter]:
                                                        # print(p2[empty_iter])
                                                        # print(p2[slot_rows])
                                                        p2[empty_iter].insert(0,veh_behind_list[i][1])
                                                        p2[slot_rows].pop(0)
                                                        p2[slot_rows].append(None)
                                                        # print(p2[slot_rows])
                                                        # print(p2[empty_iter])
                                                        p2[empty_iter].pop()
                                                        # print(p2[empty_iter])
                                                        break
                                                    # print("empty_iter", empty_iter)
                                            
                                            p2[slot_rows].pop(0)
                                            p2[slot_rows].append(None)
                                            
                                save_data(parking_data, filename)
                                break
                          
                    
                    
                
        # else:
        #     print("Invalid choice. Please try again.")

print("*****************************************************************************")
print("                     BEFORE                             ")
parking_table("parking_data.json")
print("========================================================")
CarParking()
print("========================================================")
print("                     AFTER                             ")
parking_table("parking_data.json")
