import csv
import os
import random

cwd_path = os.getcwd()

def read_row(file_name):
    """
    Reads one row for a CSV file and returns numeric data.
    :param file_name: (str), name of CSV file
    :return: (list, int),
    """

    with open(file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')

        for line in reader:
            line = [int(number) for number in line]

        return line


def read_rows(file_name, row_number):
    """
    Reads selected row for a CSV file and returns selected numeric data.
    :param file_name: (str), name of CSV file
    :param row_number: (int), number of selected row
    :return: (list, int),
    """

    with open(file_name, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        for line_idx, line in enumerate(reader):
            if line_idx == row_number:
                row = [int(number) for number in line]

        return row


def selection_sort(number_array, direction='ascending'):
    """
        Sorts and returns selected numeric data with Selection Sort.
        :param number_array: (list,int), list with numeric array
        :return: (list, int), sorted numeric array
    """

    # hlavní cyklus procházení sekvence - v první iteraci ukazuju na prvni prvek
    for count, _ in enumerate(number_array):
        extreme_idx = count

        for num_idx, num in enumerate(number_array[count:]):
            if direction == 'ascending':
                if num < number_array[extreme_idx]:                      # pokud otočím porovnávací znamínko, čísla se seřadí sestupně
                    extreme_idx = num_idx + count

            elif direction == 'descending':
                if num > number_array[extreme_idx]:                      # pokud otočím porovnávací znamínko, čísla se seřadí sestupně
                    extreme_idx = num_idx + count

        number_array[count], number_array[extreme_idx] = number_array[extreme_idx], number_array[count]

    return number_array


def bubble_sort(number_array):
    """
       Sorts and returns selected numeric data with Bubble Sort.
       :param number_array: (list,int), list with numeric array
       :return: (list, int), sorted numeric array
    """

    for i in range(len(number_array)):
        if number_array[i] < number_array[i+1]:
            number_array[i], number_array[i+1] = number_array[i+1], number_array[i]


    return number_array


def main():

    # Ukol: Selection Sort
    result_1 = read_row('numbers_one.csv')
    # print(result_1)

    # Ukol: Selection Sort - se smerem razeni
    result_2 = selection_sort(result_1, 'ascending')  # ascending/descending
    # print(result_2)
    

    # Ukol: Bubble Sort
    selected_row = read_rows('numbers_two.csv', 0)
    result_3 = bubble_sort(selected_row)
    print(selected_row)


    # příklad výpisu hodnot seřazené řady
    # print ("Seřazená řada čísel je:")
    # for i in range(len(number_array)):
    #	print ("%d" %number_array[i]),


if __name__ == '__main__':
    main()

