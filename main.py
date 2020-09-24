dia = int(input())
mes = int(input())

if mes == 1:
        if dia>=1 and dia<=20:
            print("capricornio")
        elif dia>=21 and dia<=31:
            print("acuario")
        else:
            print("Introduce un dia valido para este mes.")

elif mes == 2:
    if dia>=1 and dia<=18:
            print("acuario")
    elif dia>=18 and dia<=28:
            print("piscis")
    else:
            print("Introduce un dia valido para este mes.")

elif mes == 3:
    if dia>=1 and dia<=20:
         print("piscis")
    elif dia>=21 and dia<=31:
        print("aries")
    else:
         print("Introduce un dia valido para este mes.")

elif mes == 4:
    if dia>=1 and dia<=19:
        print("aries")
    elif dia>=20 and dia<=30:
        print("tauro")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 5:
    if dia>=1 and dia<=20:
        print("tauro")
    elif dia>=21 and dia<=31:
        print("geminis")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 6:
    if dia>=1 and dia<=20:
        print("geminis")
    elif dia>=21 and dia<=30:
        print("cancer")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 7:
    if dia>=1 and dia<=22:
        print("cancer")
    elif dia>=23 and dia<=31:
        print("leo")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 8:
    if dia>=1 and dia<=22:
        print("leo")
    elif dia>=23 and dia<=31:
        print("virgo")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 9:
    if dia>=1 and dia<=22:
        print("virgo")
    elif dia>=23 and dia<=30:
        print("libra")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 10:
    if dia>=1 and dia<=22:
        print("libra")
    elif dia>=23 and dia<=31:
        print("escorpio")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 11:
    if dia>=1 and dia<=21:
        print("escorpio")
    elif dia>=22 and dia<=30:
        print("sagitario")
    else:
        print("Introduce un dia valido para este mes.")

elif mes == 12:
    if dia>=1 and dia<=21:
        print("sagitario")
    elif dia>=22 and dia<=31:
        print("capricornio")
    else:
        print("Introduce un dia valido para este mes.")

else:
    print("Introduce un mes valido.")