book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)

voted = dict()

def check_voter(name):
    if voted.get(name):
        print ("kick them out")
    else:
        voted[name] = True
        print ("let them vote")

check_voter("Tom")
check_voter("Tom")