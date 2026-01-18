

# 1a
first_number = input("Skriv in ett heltal: ")
first_int = int(first_number)
print(first_int)

# 1b
second_number = input("Skriv in ett till heltal: ")
second_int = int(second_number)
print(second_int)
sum = first_int + second_int
print(sum)

# 2a
pris_jacka = 2000
rea_procent = 75.0
slut_pris = int(pris_jacka * rea_procent / 100)
#sum = int(slut_pris / 100)
#print("Du behöver betala: " + str(sum) + "kr.")
print("Du behöver betala: " + str(slut_pris) + "kr.")

# 2b
skriv_procent = input("Skriv in procentsats: ")
skriv_procent_int = float(skriv_procent)
pris_jacka = 2000
# procent_av_pris = float(pris_jacka * skriv_procent_int / 100)
procent_av_pris = pris_jacka * skriv_procent_int / 100
slut_pris = pris_jacka - procent_av_pris
print("Du behöver betala: " + str(slut_pris) + "kr.")