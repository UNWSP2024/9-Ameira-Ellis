# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
        total = 0
        with open('numbers.txt', 'r') as file:
                lines = file.readlines()
                if not lines:
                    print("The file is empty.")
                    return
                
        for line in lines:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                print(f"ValueError: Could not convert line to an integer: '{line.strip()}'")
            except IOError:
                print("IOError: An error occurred while reading the file.")
         
        print(f"The total sum of the numbers in the file is: {total}")

if __name__ == '__main__':
    sum_numbers_from_file()