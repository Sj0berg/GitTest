print(" Hej och Välkomen till JörgenBank ")
print("Meny\n"
+ "1. Visa Saldo\n"
+ "2. Gör Insättning\n"
+ "3. Gör Uttag\n"
+ "4. Logga Ut")
saldo = 0.0
meny = 0
while meny != 4:
    try:
        meny = float(input("Gör ett val från menyn:  "))
    except:
        print:("Du måste ange en siffra!")
    if meny == 1:
        print("ditt saldo är:  ", saldo)
    elif meny == 2:
        saldo += float (input("Gör Insättning:  "))
    elif meny == 3:
        saldo -= float (input("för Uttag:  "))
    elif meny == 4:
        print("Du är nu utloggad!\n" 
        + "Tack för att du använder JörgenBank")
        

