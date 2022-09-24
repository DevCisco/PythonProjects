cars = ["Tucson", "Santa Fe", "Kona", "Elantra", "Palisade"]
print("These are Hyundai's models on sell in US:")
for i in range(0,5):
    if cars[i] == "Tucson":
        print(cars[i])
        print("Available in Hybrid, PHEV or N-Line")
    if cars[i] == "Santa Fe":
        print(cars[i])
        print("Available in Hybrid, PHEV or normal")
    if cars[i] == "Palisade":
        print(cars[i])
        print("Available on MY21 or MY22")
    if cars[i] == "Kona":
        print(cars[i])
        print("Available in Electric, N or N-Line")
    if cars[i] == "Elantra":
        print(cars[i])
        print("Available in Hybrid, N-Line or N")