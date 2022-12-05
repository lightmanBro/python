import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    try:
       students_list = read_compound_list('programming-with-functions\people\pupils.csv')
       
       sorted_list_3 = sort_by_month_day(students_list)
       print("Ordered by Birth Month and Day")
       print_list(sorted_list_3)


       sorted_list_2 = sort_by_given_name(students_list)
       print('Sorted by given name')
       print(sorted_list_2)
       
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")


def sort_by_given_name(students_list):
    # Using lambda to sort the student by name
    sort_by_name = lambda student: student[GIVEN_NAME_INDEX]
    #  call the sorted function to sort the list by name index
    sort_by_name = sorted(students_list, key=sort_by_name)
    return sort_by_name


def sort_by_month_day(students_list):
    """Sort a list of students by their birth month and day.
    In other words sort the list by their birthdate but ignore
    the year of their birthdate.

    Parameter
        students_list: a list that contains small lists.
            Each small list contains the given name,
            surname, and birthdate of one student.
    Return: a new list of students that is sorted by birth
        month and day.
    """

    # Define a nested function that extracts
    # a student's birthdate without the year.
    def extract_month_and_day(student):
        birthday_string = student[BIRTHDATE_INDEX]
        month_and_day = birthday_string[5:]
        return month_and_day

    # Call the sorted function to sort the list
    # of students by their birth month and day.
    sorted_list = sorted(students_list, key=extract_month_and_day)
    return sorted_list

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    for names in compound_list:
        print(names)
        print()



if __name__ == '__main__':
    main()