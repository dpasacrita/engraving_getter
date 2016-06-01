#!/usr/bin/python3.3
import os
import sys
__author__ = 'Daniel Pasacrita'
__date__ = '5/31/2016'


def retrieve_envraving_data(filename, directory):
    """
    Retrieves the engraving from a file placed in the directory.
    :param filename: The text file with the engraving
    :param directory: the directory the script is working in
    :return: engraving_data: The raw engraving data from the text file, as a string
    """

    # Convert the file to a string
    filepath = directory + filename
    with open(filepath, "r") as file:
        engraving_data = file.read().replace('\n', '')

    # Return the string
    return engraving_data

def strip_and_format(data):
    """
    This function takes the raw engraving data and formats it into a list of lists, with all the engraving perfectly formatted
    :param data: the raw engraving data
    :return:
    """
    # First split it into an array based on the items
    item_array = data.split("sequence")
    item_array.pop(0)

    # Then Split into a list of lists, by item/engraving
    count = 0
    split_array = []
    line_array = []
    for item in item_array:
        split_data = item.split('{"text":"')
        split_data.pop(0)
        new = []
        split_array.append(new)
        secondcount = 0
        for item2 in split_data:
            split_array[count].append(split_data[secondcount])
            secondcount += 1
        count += 1
    count = 0
    for item3 in split_array:
        finalcount = 0
        for item4 in split_array[count]:
            # print(item4)
            head, sep, tail = item4.partition('"}')
            split_array[count][finalcount] = head
            finalcount += 1
        count += 1

    return split_array

def write_to_file(englist):
    """
    This function will finally write all the engraving to a file.
    :param englist: the engraving list
    :return: nothing.
    """

    # Output to text file
    text_file = open("engraving_output.txt", "w")
    count = 0

    # Write to the text file
    text_file.write("_ = empty line if present.")
    text_file.write("\n")
    text_file.write("\n")
    for x in englist:
        text_file.write("ITEM " + str(count + 1) + "\n")
        for y in x:
            if not y:
                text_file.write("_")
            else:
                text_file.write(y + "\n")
        text_file.write("\n")
        text_file.write("\n")
        count += 1

    # Close text file
    text_file.close()

if __name__ == "__main__":
    # Grab present working directory
    pwd = os.path.dirname(os.path.realpath(__file__)) + "/"

    # Check first that the file name is there
    if len(sys.argv) == 1:
        print("Enter the file name as a parameter stupid!")
        sys.exit(1)
    # Get the engraving filename
    engraving_file = sys.argv[1]

    # Grab engraving data from file
    engdata = retrieve_envraving_data(engraving_file, pwd)

    # Format engraving data
    final_array = strip_and_format(engdata)

    # Output to text file
    write_to_file(final_array)

    # Finish up
    print("Engraving output to: engraving_output.txt")