# Core functions only

def func(val, choice, symbol):
    """Place symbol on the board list"""
    val[val.index(choice)] = symbol
    # return a copy of the 3x3 board for testing
    return [val[i:i+3] for i in range(0, 9, 3)]

def ifwin(done):
    """Check if the player has won"""
    if len(done) < 3:
        return False
    # Rows
    if "00" in done and "01" in done and "02" in done:
        return True
    if "10" in done and "11" in done and "12" in done:
        return True
    if "20" in done and "21" in done and "22" in done:
        return True
    # Columns
    if "00" in done and "10" in done and "20" in done:
        return True
    if "01" in done and "11" in done and "21" in done:
        return True
    if "02" in done and "12" in done and "22" in done:
        return True
    # Diagonals
    if "00" in done and "11" in done and "22" in done:
        return True
    if "02" in done and "11" in done and "20" in done:
        return True
    return False

# Interactive loop only runs when executed directly
if __name__ == "__main__":
    done1 = []
    done2 = []
    val = ["00","01","02","10","11","12","20","21","22"]
    isdone1 = True
    isdone2 = False

    while True:
        chance = "Player 1" if isdone1 else "Player 2"
        choice = input(f"{chance}, choose position (or 'quit'): ")
        if choice not in val:
            print("Invalid Option")
            continue
        if choice == "quit":
            break
        if isdone1:
            done1.append(choice)
            board = func(val, choice, "X")
            for row in board: print(row)
            if ifwin(done1):
                print("GAME OVER for Player 1")
                break
            isdone1, isdone2 = False, True
        else:
            done2.append(choice)
            board = func(val, choice, "O")
            for row in board: print(row)
            if ifwin(done2):
                print("GAME OVER for Player 2")
                break
            isdone1, isdone2 = True, False
