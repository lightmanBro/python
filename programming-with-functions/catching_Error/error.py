# Example 4

def main():
    # ZERO DIVISION ERROR
    try:
        players = int(input("Enter the number of players: "))
        teams = int(input("Enter the number of teams: "))

        players_per_team = players / teams

        print(f"Each team should have {players_per_team} players")

    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)


    # KEY ERROR
    try:
        # Create a dictionary with student IDs as
        # the keys and student names as the values.
        students = {
            "42-039-4736": "Clint Huish",
            "61-315-0160": "Amelia Davis",
            "10-450-1203": "Ana Soares",
            "75-421-2310": "Abdul Ali",
            "07-103-5621": "Amelia Davis"
        }

        # Attempt to find the key "50-420-1021",
        # which is not in the dictionary. This will
        # cause the computer to raise a KeyError.
        name = students["50-420-1021"]

        print(name)

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)


        # INDEX ERROR 
        # Example 5
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to change the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        surnames[3] = "Olsen"

    except IndexError as index_err:
        print(index_err)
    # python index_error_write.py
    # list assignment index out of range



    # RANGE ERROR
    try:
        # Create a list that contains three family names.
        surnames = ["Smith", "Lopez", "Marsh"]

        # Attempt to print the surname at index 3. Because
        # there are only three names in the surnames list and
        # therefore the last index is 2, this statement will
        # fail and cause the computer to raise an IndexError.
        print(surnames[3])
    except IndexError as index_err:
        print(index_err)



        # FILE NOT FOUND ERROR
        try:
            with open("products.vcs", "rt") as products_file:
                for line in products_file:
                    print(line)

        except FileNotFoundError as not_found_err:
            print(not_found_err)

            # python file_not_found.py
            # [Errno 2] No such file or directory: 'products.vcs'


            # PERMISSION ERROR
            try:
                with open("contacts.csv", "rt") as contacts_file:
                    for line in contacts_file:
                        print(line)

            except PermissionError as perm_err:
                print(perm_err)

            # python permission_error.py
            # [Errno 13] Permission denied: 'contacts.csv'


        # READING form a FILE
        import csv
        DATE_INDEX = 0
        START_MILES_INDEX = 1
        END_MILES_INDEX = 2
        GALLONS_INDEX = 3

        try:
        # Open the fuel_usage.csv file.
            filename = "fuel_usage.csv"
            with open(filename, "rt") as usage_file:

                # Use the standard csv module to get
                # a reader object for the CSV file.
                reader = csv.reader(usage_file)

                # The first line of the CSV file contains
                # headings and not fuel usage data, so this
                # statement skips the first line of the file.
                next(reader)

                # Print headers for the three columns.
                print("Date,Start,End,Gallons,Miles/Gallon")

                # Process each row in the CSV file.
                for row_list in reader:

                    # From the current row of the CSV file, get
                    # the date, the starting and ending odometer
                    # readings, and the number of gallons used.
                    date = row_list[DATE_INDEX]
                    start_miles = float(row_list[START_MILES_INDEX])
                    end_miles = float(row_list[END_MILES_INDEX])
                    gallons = float(row_list[GALLONS_INDEX])

                    # Call the miles_per_gallon function.
                    mpg = miles_per_gallon(start_miles, end_miles, gallons)

                    # Display the results for one row.
                    mpg = round(mpg, 1)
                    print(date, start_miles, end_miles,
                            gallons, mpg, sep=",")

        except FileNotFoundError as not_found_err:
            print(f"Error: cannot open {filename}"
                    " because it doesn't exist.")

        except PermissionError as perm_err:
            print(f"Error: cannot read from {filename}"
                    " because you don't have permission.")

        except ZeroDivisionError as zero_div_err:
            print(f"Error: {filename} contains a"
                    " zero in the gallons column.")
        def miles_per_gallon(start_miles, end_miles, gallons):
            """Compute and return the average number of miles
            that a vehicle traveled per gallon of fuel.

            Parameters
                start_miles: starting odometer reading in miles.
                end_miles: ending odometer reading in miles.
                gallons: amount of fuel used in U.S. gallons.
            Return: miles per gallon
            """
            mpg = abs(end_miles - start_miles) / gallons
            return mpg




if __name__ == "__main__":
    main()
