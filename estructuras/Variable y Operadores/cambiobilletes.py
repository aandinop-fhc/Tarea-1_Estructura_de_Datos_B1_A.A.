#Taller 2
#IA
    #Bosquejo
    #monto = 87

    #$20: 87 // 20 = 4, sobra 7
    #$10:  7 // 10 = 0, sobra 7
    #$5 :  7 //  5 = 1, sobra 2
    #$1 :  2 //  1 = 2, sobra 0

monto = int(input("Monto: $"))
resto = monto

b20 = resto // 20; resto = resto % 20
b10 = resto // 10; resto = resto % 10
b5  = resto // 5;  resto = resto % 5
b1  = resto // 1;  resto = resto % 1

print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")

#Ampliado
    #Bosquejo
    #monto = 137.61  →  centavos_totales = 13761

    #$50: 13761 // 5000 = 2, sobra 3761
    #$20:  3761 // 2000 = 1, sobra 1761
    #$10:  1761 // 1000 = 1, sobra 761
    #$5 :   761 //  500 = 1, sobra 261
    #$1 :   261 //  100 = 2, sobra 61
    #25¢:    61 //   25 = 2, sobra 11
    #10¢:    11 //   10 = 1, sobra 1
    #5¢ :     1 //    5 = 0, sobra 1
    #1¢ :     1 //    1 = 1, sobra 0

monto = float(input("Monto: $"))
centavos = round(monto * 100)          

b50 = resto // 5000; resto = resto % 5000
b20 = resto // 2000; resto = resto % 2000
b10 = resto // 1000; resto = resto % 1000
b5  = resto //  500; resto = resto %  500
b1  = resto //  100; resto = resto %  100

m25 = resto //  25; resto = resto %  25
m10 = resto //  10; resto = resto %  10
m5  = resto //   5; resto = resto %   5
m1  = resto //   1; resto = resto %   1

print(f"$50  × {b50}")
print(f"$20  × {b20}")
print(f"$10  × {b10}")
print(f"$5   × {b5}")
print(f"$1   × {b1}")
print(f"25¢  × {m25}")
print(f"10¢  × {m10}")
print(f"5¢   × {m5}")
print(f"1¢   × {m1}")