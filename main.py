

# 1a
first_number = int(input("Skriv in ett heltal: "))
print(first_number)

# 1b
second_number = int(input("Skriv in ett till heltal: "))
#second_int = int(second_number)
print(second_number)
sum = first_number + second_number
print(sum)

# 2a
pris_jacka = 2000
rea_procent = 75.0
slut_pris = int(pris_jacka * rea_procent / 100)
#sum = int(slut_pris / 100)
#print("Du behöver betala: " + str(sum) + "kr.")
print("Du behöver betala: " + str(slut_pris) + "kr.")

#  2b
skriv_procent = int(input("Skriv in procentsats: "))
pris_jacka = 2000
# procent_av_pris = float(pris_jacka * skriv_procent_int / 100)
procent_av_pris = pris_jacka * skriv_procent / 100
slut_pris = int(pris_jacka - procent_av_pris)
print("Du behöver betala: " + str(slut_pris) + "kr.")

# ada