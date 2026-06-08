from funkcijas import paradit_galdu, veikt_gajienu

galds = [
    ["T", "Z", "L", "D"],
    ["P", "P", "P", "P"],
    [" ", " ", " ", " "],
    ["p", "p", "p", "p"]
]

paradit_galdu(galds)

for speletajs in range(2):
    print()
    print("Spēlētājs", speletajs + 1)

    rinda = int(input("Ievadi rindu (0-3): "))
    kolonna = int(input("Ievadi kolonnu (0-3): "))

    veikt_gajienu(galds, rinda, kolonna)

    paradit_galdu(galds)

print("Spēle beigusies!")
