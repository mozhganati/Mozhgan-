# Arrays of people and animals
people = ["Mozhgan", "Yaser", "Atena", "Anita","Mahtab","Ali"]
animals = ["Giraffe","Lion", "Tiger", "Elephant","Dog" ,"Cat"]

# check which array the input belongs to
def identify_name(name):
    if name in people:
        return "It is a person's name."
    elif name in animals:
        return "It is an animal's name."
    else:
        return "There is not the name in arrays."

# Test the function
name = input("Enter a name: ")
result = identify_name(name)
print(result)
    