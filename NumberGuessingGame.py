import numpy as np

limite = 100
nb_myst = np.random.randint(1, limite + 1)
nb_user = ''

try:
    nb_user = int(input(f"Entrez un nombre inférieur ou égal à {limite} "))
except ValueError:
    print("Entrez un nombre !")

if nb_user > limite:
    raise Exception(f"Entrez un nombre inférieur à {limite}")

while nb_user != nb_myst:
    if nb_user < nb_myst:
        print("C'est plus !")
    elif nb_user > nb_myst:
        print("C'est moins !")
    nb_user = int(input(f"Entrez un nombre inférieur à {limite} "))
print("Vous avez gagné ! ")
