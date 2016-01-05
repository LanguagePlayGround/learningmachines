import MySQLdb as mdb 
import MySQLdb.cursors
import sys
import os.path as path
import csv


try:
    # X is a matrix with the features for our training data (what information we know about each row, without the answers)
    X = []
    # y is the answer for each row
    y = []

    with open('titanic.csv', 'rU') as openInputFile:
        # csv.DictReader will take a csv file, and read it in as an array of python dictionaries (similar to JavaScript objects, or hashes)
        inputRows = csv.DictReader(openInputFile)
        # ignore the header row
        firstRow = False
        for row in inputRows:
            if(firstRow):
                # if possible, read in the data as floats (numbers with decimal points) rather than strings
                for key, val in enumerate(row):
                    try:
                        row[key] = float(val)
                    rowAsFloats.append( val )
                X.append(row)
            else:
                headerRow = row
                firstRow = True

    allData = []

    # transform:
        # name
        # sex
        # ticket
            # take only the letters in front of ticket. categorize that
            # if there is a good ticket number, include that

        # cabin
            # definitely parse out the leading letter here. that denotes the deck they're on. 
            # possibly parse out the number of cabins they have as well?
        # embarked
    # TODO: binarize the categorical data in the categorical fields
    # information like 'embarked' represents a category (which city did you embark in?) rather than a number (how much money did you pay for your fare?)
    # a common way to format categorical data for machine learning is to turn it into binary values
    # so if we have three categories ('C','Q',and 'S'), we would turn that into something like separate columns for 'embarkedC', 'embarkedQ', and 'embarkedS', with a value of either 0 or 1
    # define your own binarize function here, that will take in categorical data, and turn it into a single binary representation of which category is present for this row
    def binarize(columnName, columnValue):


    # SOLUTION CODE BELOW
    for row in data:
        # {'fare': 7.25, 'passenger': 'Braund, Mr. Owen Harris', 'embarked': 'S', 'age': 22L, 'pClass': 3L, 'sex': 'male', 'parents': 0L, 'survived': 0L, 'siblings': 1L, 'ticket': 'A/5 21171', 'passengerId': 1L, 'cabin': ''}

        passenger = {}

        if row['sex'] == 'female':
            passenger['is_female'] = 1
        else:
            passenger['is_male'] = 1

        passenger['age'] = row['age']

        pasenger['fare'] = row['fare']


        allData.append(passenger)
    # END SOLUTION CODE
