#Det fantastiska pizzaprogrammet
print("*** Hej och välkommen till Pizzamakaren ***")
print("1. Skriv in ditt val av topping\n"
+ "2. Skriv ut ditt val av topping\n"
+ "3. Skicka Beställning\n"
+"4. Avsluta")
topping = ""
meny = 0
while meny != 4: 
    try:
        meny = int(input("Gör ett val från menyn: "))
    except:
        print("Du måste ange en siffra!") 
    
    if meny == 1:
        topping += input("Skriv in den topping du önskar: ") + "," 
    elif meny == 2:
        print("Din valda topping är: ", topping)
    elif meny == 3:
        print("Din beställning tillagas nu!") 
    elif meny == 4:
        print("Smaklig måltid")    
    else:
        print("Du gjorde inte ett korrekt val, prova igen.") 