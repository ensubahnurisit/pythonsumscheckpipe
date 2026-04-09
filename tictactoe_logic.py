for i in range(3):
    for j in range(3):
        print(f'{i}{j}',end=" ")
    print("\n")

def func(val,choice,symbol):
    val[val.index(choice)] = symbol
    for i in range(0,9,3):
        print(val[i:i+3])
        print("\n")

def ifwin(done):
    if len(done)<3:
        return False
    else:
        if "00" in done and "01" in done and "02" in done:
            return True
        if "10" in done and "11" in done and "12" in done:
            return True
        if "20" in done and "21" in done and "22" in done:
            return True
        if "00" in done and "10" in done and "20" in done:
            return True
        if "01" in done and "11" in done and "21" in done:
            return True
        if "02" in done and "12" in done and "22" in done:
            return True
        if "00" in done and "11" in done and "22" in done:
            return True
        if "02" in done and "11" in done and "20" in done:
            return True
        
done1 = []
isdone1 = True
done2 = []
isdone2 = False
done = []
val = ["00","01","02","10","11","12","20","21","22"]
while(True):
    chance = "Player 1" if isdone1 else "Player 2"
    choice = input(f"{chance}, choose the position as per the diagram: ")
    if choice not in val:
        print("Invalid Option")
    if "quit" in choice:
        break
    else:
        if isdone1:
            done1.append(choice)
            func(val,choice,'X')
            if(ifwin(done1)):
                print("GAME OVER for Player 1")
                break
            isdone2,isdone1 = isdone1,isdone2
        else:
            done2.append(choice)
            func(val,choice,'O')
            if(ifwin(done2)):
                print("GAME OVER for Player 2")
                break
            isdone2,isdone1 = isdone1,isdone2
