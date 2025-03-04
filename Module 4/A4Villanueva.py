# Alex Villanueva

#==================================

##################### algorithm

import sys


### First, initialize variables:
#    counts for egg weights - jumbo, extra_large, large, medium, and small - initialized to 0
#     full egg (count) and total_weight initialized as 0
#     (max_weight) and (min_weight) set to -sys.maxsize - 1 and sys.maxsize, respectively

total_weight = 0 #for computing average
count = 0 # same
small_count = 0
medium_count = 0
large_count = 0
xl_count = 0
jumbo_count = 0

# ### Initialize min and max weights ###
min_weight = sys.maxsize
max_weight = -sys.maxsize - 1


### next, initialize egg weight minimums as constants
JUMBO_MIN = 2.5
XL_MIN = 2.25
LARGE_MIN = 2.0
MEDIUM_MIN = 1.75
SMALL_MIN = 1.5


# take input with "Enter egg weight (or 0 to quit)" as priming read, save as (weight input)
weight_input = float(input("Enter egg weight (or enter 0 to quit): "))


while weight_input != 0:
#      if weight input < 0:
#         print "please enter a positive weight or 0 if you're finished"
    if weight_input < 0:
        print("Please enter a positive weight or 0 if you're finished")
#      else: (update total weight and count)
#         add weight input to total weight and save it as total weight
#         add 1 to the count and save it as count
    else:
        total_weight += weight_input
        count += 1

# ### update min/max ###
        if weight_input < min_weight:
            min_weight = weight_input
        if weight_input > max_weight:
            max_weight = weight_input

# ### update category counts ###
        if weight_input >= JUMBO_MIN:
            jumbo_count += 1
        elif weight_input >= XL_MIN:
            xl_count += 1
        elif weight_input >= LARGE_MIN:
            large_count += 1
        elif weight_input >= MEDIUM_MIN:
            medium_count += 1
        elif weight_input >= SMALL_MIN:
            small_count += 1
        else:
            print("The weight entered is below minimum")
# ### ask for the next input at the bottom of the while loop ###
    weight_input = float(input("Enter egg weight (or enter 0 to quit): "))

# ### OUTPUTS ###

# if count == 0:
#   print "No eggs entered"
# else:
#   print (f"{category:<30s}{count:<10s}")
# print(-*40)
# print (f"{Jumbo:<30}{jumbo count:<10}")
# print (f"{XL:<30}{XL count:<10}")
# print (f"{large:<30}{large count:<10}")
# print (f"{medium:<30}{medium count:<10}")
# print (f"{small:<30}{small count:<10}")
#print (f"Total Eggs: {count}")
# print Total weight?
# print average weight
# print min weight
# print max weight

if count == 0:
    print("No eggs entered")
else:
    average_weight = total_weight / count
    print()
    print() # for a lil space between input and output
    print(f"{'Category':<30s}{'Count':<10s}")
    print("-" * 40) # for some nice separation
    print(f"{'Jumbo':<30}{jumbo_count:<10}")
    print(f"{'XL':<30}{xl_count:<10}")
    print(f"{'Large':<30}{large_count:<10}")
    print(f"{'Medium':<30}{medium_count:<10}")
    print(f"{'Small':<30}{small_count:<10}")
    print("-" * 40) # more nice separation
    print()
    print(f"Total Eggs: {count}")
    print()
    print(f"{'Total Weight':<30}{total_weight:<10.2f} oz")
    print(f"{'Average Weight':<30}{average_weight:<10.2f} oz")
    print(f"{'Min Weight (Lightest Egg)':<30}{min_weight:<10.2f} oz")
    print(f"{'Max Weight (Heaviest Egg)':<30}{max_weight:<10.2f} oz")





