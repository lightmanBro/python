import csv
def main():
    with open('file_read\hymns.csv', 'rt') as csv_file:
        reader = csv.reader(csv_file)
        for row_list in reader:
            print(row_list)

    def read_files(filename):
        
if __name__ == '__main__':
    main()