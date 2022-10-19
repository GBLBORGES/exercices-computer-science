def inverted_ladder(name: str):
    while len(name) >= 1:
        print(name)
        name = name[:-1]


inverted_ladder('gabriel')
