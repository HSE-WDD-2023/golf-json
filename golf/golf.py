from os import system
import json

system("clear")

# we want to load the data from the json file to a list in python
holes = []
with open("golf.json", "r") as data_file:
    # use the json lib to grab the data
    holes = json.load(data_file)

# print out the hole number and the par for each hole
for hole in holes:   # each hole is a dict in the holes list
    print(f"Hole {hole.get('hole_number')}:  Par {hole.get('par')}")

# take the above info and print it out to a text file
with open("course_info.txt", "w") as my_file:
    my_file.write(f"Fishel Country Club {chr(9971)}\n")
    for hole in holes:
        my_file.write(f"\tHole {hole.get('hole_number')}: Par {hole.get('par')}\n")

system("clear")
# how many holes are par 3's?
count = 0
for hole in holes: # loop through each hole
    if hole.get('par') == 3:
        count += 1  # increase count by 1
print(f"There are {count} par 3 holes on this course.")

# find out how many of each kind of par there is put that into a dict
par_dict = {}
for hole in holes:
    par = hole.get('par')
    key = f"par_{par}"
    # look up the count for par_n, if it doesn't exists, the make the count 0
    count = par_dict.get(key, 0)
    count += 1 #increace our count by 1
    par_dict[key] = count # update the dict with the new count value

# print out the par_dict to see
# print(par_dict)
# let's instead save this new dict as a json file
with open("pars.json", "w") as my_file:
    json.dump(par_dict, my_file, indent=4)
    # (what to dump, where to dump it, formatting)



# make a dictionary that will keep track of the distance by color
distances = {}
for hole in holes:
    distance_dict = hole.get("distances")
    for tee_color, dist in distance_dict.items():
        tot_dist = distances.get(tee_color, 0) # check the dict for the tee color
        tot_dist += dist  # add the current distance to the total
        #distances[tee_color] = tot_dist
        distances.update({tee_color: tot_dist})

#print(distances)
#use the json lib to print this all nice and fancy
print(json.dumps(distances, indent=4))

#now dump it to a json file
with open("distances.json", "w") as my_file:
    json.dump(distances, my_file, indent=2)





