
def search(phrase):
    list = []
    with open("twss.txt", "r") as f:
        list = f.readlines()
    #print(list)

    for word in list:
        if phrase in word:
            return True