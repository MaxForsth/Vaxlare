#Exchange
#In: belopp som ska växlas, valör på en sedel eller mynt
#Out: antal sedlar/mynt man får ut i valör

def exchange(belopp, sedel):
    return int(belopp) // sedel

#get_exchange_dict
#
#
def get_exchange_dict(inbetalning, priset)