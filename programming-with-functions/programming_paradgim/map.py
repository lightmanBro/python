

# Example 5

# def main():
#     # Create a list that contains the names of Canadian provinces.
#     provinces_list = [
#         "Alberta", "Ontario", "Prince Edward Island", "Ontario",
#         "Quebec", "Saskatchewan", "AB", "Nova Scotia", "Alberta",
#         "Northwest Territories", "Saskatchewan", "Nunavut",
#         "Nova Scotia", "Prince Edward Island", "Alberta",
#         "Nova Scotia", "Prince Edward Island", "Saskatchewan",
#         "Nova Scotia", "Newfoundland and Labrador", "Ontario",
#         "Ontario", "Ontario", "British Columbia", "Ontario",
#         "Nova Scotia", "Prince Edward Island", "Saskatchewan",
#         "Newfoundland and Labrador", "Ontario", "Ontario",
#         "Manitoba", "British Columbia", "Ontario", "Alberta",
#         "Saskatchewan", "Ontario", "Manitoba", "Ontario",
#         "New Brunswick", "Yukon", "British Columbia", "Yukon",
#         "Newfoundland and Labrador", "Manitoba", "Ontario",
#         "Yukon", "British Columbia", "Yukon", "Ontario", "AB",
#         "Newfoundland and Labrador", "Nova Scotia", "Yukon",
#         "Northwest Territories", "Nunavut", "Yukon", "Nunavut",
#         "Ontario", "British Columbia", "AB", "Saskatchewan",
#         "Prince Edward Island", "Saskatchewan",
#         "Prince Edward Island", "Alberta", "Ontario", "Alberta",
#         "Manitoba", "AB", "British Columbia", "Alberta"
#     ]

#     # As a debugging aid, print the entire list.
#     print("Original list of provinces:")
#     print(provinces_list)
#     print()

#     # Define a nested function that converts AB to Alberta.
#     def alberta_from_ab(province_name):
#         if province_name == "AB":
#             province_name = "Alberta"
#         return province_name

#     # Replace all occurrences of "AB" with "Alberta" by
#     # calling the map function and passing the ablerta_from_ab
#     # function and provinces_list into the map function.
#     new_list = list(map(alberta_from_ab, provinces_list))
#     print("List of provinces after AB was changed to Alberta:")
#     print(new_list)
#     print()

#     # Define a nested function that returns True if
#     # province_name is Alberta and returns False otherwise.
#     def is_alberta(province_name):
#         return province_name == "Alberta"

#     # Filter the new list to only those provinces that
#     # are "Alberta" by calling the filter function and
#     # passing the is_alberta function and new_list.


#     filtered_list = list(filter(is_alberta, new_list))
#     print("List filtered to Alberta only:")
#     print(filtered_list)
#     print()

#     # Because all the elements in filtered_list are
#     # "Alberta", we can count how many elements are
#     # "Alberta" by simply calling the len function.
#     count = len(filtered_list)

#     print(f"Alberta occurs {count} times in the modified list.")


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


# Example 7

def main():
    # Create a list that contains data about countries.
    countries = [
        # [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]

    # Print the unsorted list.
    print("Original unsorted list of countries")
    for country in countries:
        print(country)
    print()

    # Define a lambda function that will be used as the
    # key function by the sorted function. The lambda
    # function extracts the population data from a
    # country so that the population will be used for
    # sorting the list of countries.
    POPULATION_INDEX = 2
    
    popul_func = lambda country: country[POPULATION_INDEX]
    # Sort the list of countries by the population.
    sorted_list = sorted(countries, key=popul_func)

    # Print the sorted list.
    print("List of countries sorted by population")
    for country in sorted_list:
        print(country)


# Call main to start this program.
if __name__ == "__main__":
    main()