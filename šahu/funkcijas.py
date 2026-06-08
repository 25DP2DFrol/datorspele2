def paradit_galdu(galds):
    print("\nŠaha galds:")
    for rinda in galds:
        print(rinda)

def veikt_gajienu(galds, rinda, kolonna):
    if 0 <= rinda < len(galds) and 0 <= kolonna < len(galds[0]):
        galds[rinda][kolonna] = "*"
    else:
        print("Nepareizas koordinātas!")
