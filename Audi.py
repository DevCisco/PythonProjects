def electric():
    cars = ["Q4", "e-Tron", "e-Tron GT"]
    print("These are Audi's models on sell in US:")
    for i in range(0,3):
        if cars[i] == "Q4":
            print(cars[i].title())
            print("Available also Sportback")
        if cars[i] == "e-Tron":
            print(cars[i])
            print("Available also Sportback and S")
        if cars[i] == "e-Tron GT":
            print(cars[i])
            print("Available also RS")
def petrol():
    cars = ["A3", "A4", "A5", "A6", "A7", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "R8"]
    print("These are Audi's models on sell in US:")
    for i in range(0, 11):
        if cars[i] == "A3":
            print(cars[i])
            print("Available also S and RS")
        if cars[i] == "A4":
            print(cars[i])
            print("Available also allroad and S")
        if cars[i] == "A5":
            print(cars[i])
            print("Available also S, RS, Cabriolet and Sportback")
        if cars[i] == "A6":
            print(cars[i])
            print("Available also S, allroad and Avant")
        if cars[i] == "A7":
            print(cars[i])
            print("Available also S and RS")
        if cars[i] == "A8":
            print(cars[i])
            print("Available also S")
        if cars[i] == "Q3":
            print(cars[i])
        if cars[i] == "Q5":
            print(cars[i])
            print("Available also Sportback and S")
        if cars[i] == "Q7":
            print(cars[i])
            print("Available also S")
        if cars[i] == "Q8":
            print(cars[i])
            print("Available also S andRS")
        if cars[i] == "TT":
            print(cars[i])
            print("Available also S, RS and Roadster")
        if cars[i] == "R8":
            print(cars[i])
            print("Available also Spyder")
answer = input("Choose your motor, P for Petrol and E for electric: ")
if answer == "P":
    petrol()
if answer == "E":
    electric()