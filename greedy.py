def main():
    while True:
        summa = float(input("Enter the sum: "))
        if summa >= 0:
            break

    change = int(round(summa * 100))
    coins = 0
    while change > 0:
        if (change - 25) >= 0: 
         
            change = change - 25 
            coins +=1
        
        elif (change - 10) >= 0:
         
            change = change - 10
            coins +=1
        
        elif (change - 5) >= 0:
         
            change = change - 5
            coins +=1
        
        elif (change - 1) >= 0:
         
            change = change - 1 
            coins +=1 
               
    print(coins) 
if __name__ == "__main__":
    main()    
