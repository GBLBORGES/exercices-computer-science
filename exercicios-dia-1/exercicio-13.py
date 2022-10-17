def new_Rating_Method(listRatings):
    for index, numbers in enumerate(listRatings):
        listRatings[index] = numbers * 10
    print(listRatings)


new_Rating_Method([6, 8, 5, 9, 10])
