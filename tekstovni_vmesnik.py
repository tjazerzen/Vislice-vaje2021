import model

def izpis_igre(igra):
    return (
        f"Igraš igro vislic:\n" +
        f"Narobe ugibane črke so: {igra.nepravilni_ugibi()}\n" +
        f"Trenutno stanje besede: {igra.pravilni_del_gesla()}\n"
    )

def izpis_poraza(igra):
    return (
        f"Izgubil si. Več sreče prihodnjič.\n" +
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n" +
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"
        f"Pravilno geslo je bilo: {igra.geslo}\n"

    )

def izpis_zmage(igra):
    return (
        f"Zmagal si. Bravo!\n" +
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n" +
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n"
        f"Pravilno geslo je bilo: {igra.geslo}\n"

    )

def se_enkrat():
    vnos = input("vnesi X, če želiš igrati še enkrat, in Y, če ne. ")
    if vnos == "X":
        return True
    elif vnos == "Y":
        return False
    else:
        print("Niste vnesli ne X ne Y. Vnesite še enkrat :) ")
        return se_enkrat()

def pozeni_vmesnik():
    igra = model.nova_igra(model.bazen_besed)

    while True:
        if igra.zmaga():
            print(izpis_zmage(igra))
        elif igra.poraz():
            print(izpis_poraza(igra))
        else:
            print(izpis_igre(igra))
            vnos = input("Vnesi novo črko: ")
            igra.ugibaj(vnos)

    se_enkrat_bool = se_enkrat()
    if se_enkrat_bool:
        pozeni_vmesnik()



pozeni_vmesnik()