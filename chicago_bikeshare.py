
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(20):
    print(data_list[i])

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]
#
# # We can access the features through index
# # E.g. sample[6] to print gender or sample[-2]
#
input("Press Enter to continue...")
# # TASK 2
# # TODO: Print the `gender` of the first 20 rows
#
print("\nTASK 2: Printing the genders of the first 20 samples")
for i in range(20):
    print(data_list[i][6])
#
#
input("Press Enter to continue...")
# # TASK 3
# # TODO: Create a function to add the columns (features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Function to add the columns (features) of a list in another list in the same order.
    Args:
          data: The data that is doing to be iterable.
          index: The index of the column desired.
    Returns:
           List of the values
    """

    column_list = []
    for index in range(len(data)):
        column_list.append(data[i][index])
    return column_list
#
#
# # Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# # -----------------------------------------------------
#
input("Press Enter to continue...")
# # Now we know how to access the features, let's count how many Males and Females the dataset have
# # TASK 4
# # TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for i in range(len(data_list)):
    if data_list[i][6] == "Male":
        male += 1

    elif data_list[i][6] == "Female":
        female += 1

# # Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# # -----------------------------------------------------
#
input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    Function to count the genders.
    Args:
          data_list: The data list that is doing to be iterable.
    Returns:
           List with the count values of males and females
    """

    male = 0
    female = 0

    for i in range(len(data_list)):
        if data_list[i][6] == "Male":
            male += 1

        elif data_list[i][6] == "Female":
            female += 1

    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# # -----------------------------------------------------
#
input("Press Enter to continue...")
# # Now we can count the users, which gender use it the most?
# # TASK 6
# # TODO: Create a function to get the most popular gender and print the gender as string.
# # We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Function to get the most popular gender and print the gender as string.
    Args:
          data_list: The data list that is doing to be iterable.
    Returns:
           A string with the popular gender.
    """

    answer = ""

    count_gender(data_list)

    if male > female:
        answer = "Male"

    elif male < female:
        answer = "Female"

    else:
        answer = "Equal"

    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# # -----------------------------------------------------
#
# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)
#

input("Press Enter to continue...")
# # TASK 7
# # TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_user(data_list):
    """
    Function count the users.
    Args:
          data_list: The data list that is doing to be iterable.
    Returns:
           A list with the count value of each user type.
    """

    customer = 0
    subscriber = 0

    for i in range(len(data_list)):
        if data_list[i][5] == "Customer":
            customer += 1

        elif data_list[i][5] == "Subscriber":
            subscriber += 1

    return [customer, subscriber]


gender_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Type')
plt.xticks(y_pos, types)
plt.title('Quantity by user type')
plt.show(block=True)


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because some samples have null values."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------
#
input("Press Enter to continue...")
# # Let's work with the trip_duration now. We cant get some values from it.
# # TASK 9
# # TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# # You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = list(map(int, trip_duration_list))
min_trip = 0.
max_trip = 0.
mean_trip = 0
median_trip = 0.
summ = 0
trip_duration_list.sort()
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]

for i in range(len(trip_duration_list)):
    summ += trip_duration_list[i]

mean_trip = summ/len(trip_duration_list)

if len(trip_duration_list) % 2 == 0:
    index1 = len(trip_duration_list)/2
    index2 = index1 - 1
    median_trip = (trip_duration_list[index1] + trip_duration_list[index2])/2

else:
    odd_index = (len(trip_duration_list) - 1)//2
    median_trip = trip_duration_list[odd_index]
#
#
# print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# # -----------------------------------------------------
#
input("Press Enter to continue...")
# # TASK 10
# # Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# # TODO: Check types how many start_stations do we have using set()
start_station_list = column_to_list(data_list, 3)

start_station = set(start_station_list)
#
print("\nTASK 10: Printing start stations:")
print(len(start_station))
print(start_station)
#
# # ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(start_station) == 582, "TASK 10: Wrong len of start stations."
# # -----------------------------------------------------
#
# input("Press Enter to continue...")
# # TASK 11
# # Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# # def new_function(param1: int, param2: str) -> list:
#       """
#       Example function with annotations.
#       Args:
#           param1: The first parameter.
#           param2: The second parameter.
#       Returns:
#           List of X values
#
#       """
#
input("Press Enter to continue...")
# # TASK 12 - Challenge! (Optional)
# # TODO: Create a function to count user types without hardcoding the types
# # so we can use this function with a different kind of data.
print("\nWill you face it? \n")
answer = "yes"


def count_items(column_list):

    """
    Function count the users.
    Args:
          column_list: The data list that is doing to be iterable.
    Returns:
           A list with the item types and another list with the count values.
    """

    item_types = []
    count_items = []
    new_count_list = []

    counting_list = Counter(column_list)

    for i in counting_list:
        new_count_list.append([i, counting_list[i]])

    item_types, count_items = zip(*new_count_list)

    return item_types, count_items
#
#
if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    #-----------------------------------------------------
