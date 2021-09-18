# List of buildings accross the street. Each building has appartments and some
# extra facilities such as gyms, supermarkets, etc.
lis_buildings = [{'building_number' : 0, 'facilities' : {"gym" : True, "supermarket" : False, "office" : False, "pharmacy" : True}},
                 {'building_number' : 1, 'facilities' : {"gym" : False, "supermarket" : False, "office" : True, "pharmacy" : False}},
                 {'building_number' : 2, 'facilities' : {"gym" : False, "supermarket" : True, "office" : False, "pharmacy" : False}},
                 {'building_number' : 3, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 4, 'facilities' : {"gym" : True, "supermarket" : False, "office" : True, "pharmacy" : True}},
                 {'building_number' : 5, 'facilities' : {"gym" : False, "supermarket" : True, "office" : True, "pharmacy" : True}},
                 {'building_number' : 6, 'facilities' : {"gym" : False, "supermarket" : False, "office" : True, "pharmacy" : False}},
                 {'building_number' : 7, 'facilities' : {"gym" : True, "supermarket" : True, "office" : True, "pharmacy" : True}},
                 {'building_number' : 8, 'facilities' : {"gym" : True, "supermarket" : False, "office" : True, "pharmacy" : False}},
                 {'building_number' : 9, 'facilities' : {"gym" : False, "supermarket" : True, "office" : False, "pharmacy" : True}},
                 {'building_number' : 10, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 11, 'facilities' : {"gym" : False, "supermarket" : False, "office" : True, "pharmacy" : False}},
                 {'building_number' : 12, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : True}},
                 {'building_number' : 13, 'facilities' : {"gym" : True, "supermarket" : False, "office" : False, "pharmacy" : True}},
                 {'building_number' : 14, 'facilities' : {"gym" : True, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 15, 'facilities' : {"gym" : False, "supermarket" : True, "office" : False, "pharmacy" : False}},
                 {'building_number' : 16, 'facilities' : {"gym" : True, "supermarket" : True, "office" : True, "pharmacy" : True}},
                 {'building_number' : 17, 'facilities' : {"gym" : True, "supermarket" : False, "office" : False, "pharmacy" : True}},
                 {'building_number' : 18, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 19, 'facilities' : {"gym" : True, "supermarket" : False, "office" : True, "pharmacy" : False}},
                 {'building_number' : 20, 'facilities' : {"gym" : False, "supermarket" : True, "office" : False, "pharmacy" : True}},
                 {'building_number' : 21, 'facilities' : {"gym" : True, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 22, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : False}},
                 {'building_number' : 23, 'facilities' : {"gym" : True, "supermarket" : True, "office" : True, "pharmacy" : True}},
                 {'building_number' : 24, 'facilities' : {"gym" : False, "supermarket" : False, "office" : False, "pharmacy" : True}}]


# Getting user's input to know his preferences on facilities
usr_inp = input("Please enter your preferences(use commas) : ")
pref_lst = usr_inp.split(",")

# List of available facilities
lst_facilities = lis_buildings[0].get('facilities').keys()

print(lst_facilities)

# For loop for warning user if they put a facility which is unavailable!
for pref in pref_lst:
    if pref not in lst_facilities:
        print("Sorry you gave a facility which is not available!! please try again!!")
        exit()

# The purpose of this list is to store the data of the analization of each building for the required facilities and finding 
# the optimum building! It's a list of dicts and each dict will look like this : pref=gym,supermarket { "gym" : 2 , "supermarket" : 1}  
lst_building_analisys = []



len_lis_buildings = len(lis_buildings)

for z in range(len_lis_buildings):
    lst_building_analisys.append({})

print(lst_building_analisys)

# Running a forloop to enter values in the analisys list's dicts as -1
for dic in lst_building_analisys:
    for pref in pref_lst:
        dic[pref] = -1

print(lst_building_analisys)


# Function for checking if all preferences are available in one building itself!
def search_in_curr_building(building,building_no):
    # function will return true if all pref are found in building else it will return false
    # The flag helps the* function with that
    flag = True
    for preference in pref_lst:
        if building.get(preference) == True:
            lst_building_analisys[building_no][preference] = 0

        else:
            flag = False

    if flag == True:    
        return True
    else:
        print(f"All preferences do not exist in building {building_no}")
        return False

# Function for going to the right hand side of the building and checking for closest preferences!
def search_right_of_building(building_n,building):
    # If else statement to find if building is last or first
    if building_n < (len_lis_buildings - 1):

        # For loop will go from the building_no to the end
        for pre in pref_lst:
        
            for i in range((building_n + 1), len_lis_buildings, +1):

                building_facilities = lis_buildings[i].get('facilities')

                if building_facilities.get(pre) == True:
                    curr_val = lst_building_analisys[building_n][pre]

                    if curr_val != 0:
                        if curr_val == -1:
                            lst_building_analisys[building_n][pre] = (i - building_n)
                        else:
                            if (i - building_n) < curr_val:
                                lst_building_analisys[building_n][pre] = (i - building_n)
                                

                    # You have found the preferrence in one of the buildings to the right
                    # No need to search further for the same facility
                    # So break the loop and start searching for the next facility required by the user
                    break 


# Function for going to the left hand side of the building and checking for closest preferences!
def search_left_of_building(building_number,building):
    # If else statement to find if building is last or first
    if building_number > 0:

        # Forloop will go from the current building to the first building which on the LEFT
        for preference in pref_lst:

            for n in range((building_number-1),-1,-1):
                building_facilities = lis_buildings[n].get('facilities')

                if building_facilities.get(preference) == True:
                    if lst_building_analisys[building_number][preference] != 0:
                        lst_building_analisys[building_number][preference] = building_number - n
                    # You have found the preferred facility in one of the left buildings
                    # No need to search for the same facility any more to the left
                    # So break the loop and search for the next preference given by the user
                    break

                   

def analyse_building(building, build_no):
    
    
    curr_building = search_in_curr_building(building,build_no)
    left_of_building = search_left_of_building(build_no,building) 
    right_of_building = search_right_of_building(build_no,building)

    

build_no = 0

for building in lis_buildings:
    analyse_building(building.get('facilities'), building.get('building_number'))
    
    build_no += 1


print("==========================================================================================================")

for building_an in lst_building_analisys:
    print(building_an)
