import os
import Växla

def main():
    os.system('cls' if os.name == 'nt' else 'cls')
    print("\n\t Växlare \n")

    pris = input("\t Mata in pris på varan (i kronor):")
    inbet = input("\t Inbetalt belopp (i kronor):")

    #Anropar växlings-funktioner
    ExchangeNow(int(pris), int (inbet))

#Definierar växlings-funktion som skirver ut växling
def ExchangeNow(priset, inbetalning):
        print("jbkbj" + str(priset))


main()