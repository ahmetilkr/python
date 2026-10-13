

dictionary={"a":1,
            "b":2,
            "c":3,
            "d":4}

dictionary.keys()  #keylere erişen methot
dictionary.values()    #valuelere erişen methot
dictionary.items()     #key ve value değerleri ziplenmiş ve listenin içinde

{k:v**2 for (k,v) in dictionary.items()}
{k.upper():v for (k,v) in dictionary.items()}