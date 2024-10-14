from notifypy import Notify
def limiter ():
    f = open("Experimental Code/Limit.txt" , "r")
    limit = 0
    f.close()
    
    # Limit Selection Menu
    while True:
        try:
            print("Limit Menu:\n[1] Set Limit\n[2] See Limit\n[3] Exit")
            choice = int(input("\nChoice = "))
            match choice:
                case 1:
                    
                    # Set up the limit
                    def setup_limit():
                        try:
                            file2 = open("Experimental Code/Limit.txt" , "w")
                            while limit < 100 or limit > 100000 or limit != 0:
                                print("Set Limit [$100-$100000\n[$0 = No limit]")
                                limit = input("\n Amount: ")
                            else:
                                limit = int(limit)
                                if (100 <= limit <= 100000):
                                    file2.write(str(limit))
                                    file2.close()
                                    print("Changes Made")
                                elif 0 < limit < 100:
                                    print("Limit too low")
                                elif limit ==  0:
                                    file2.write("")
                                    file2.close()
                                    print("Limit Removed")
                                else:
                                    print("Limit Too High")
                        except Exception:
                            print("Invalid amount, please try again later")
                            return()
                        except KeyboardInterrupt:
                            print("Program terminated")
                            break
                    setup_limit()
                case 2:
                    
                    # To See the Limit
                    if limit == '':
                        print("limit not set\n")
                    else:
                        print(f'Limit : {limit}')
                case 3:
                    
                    # Returning to Main Menu
                    return()
                case _:
                    
                    # In case they enter an invalid number (e.g Choosing 4+ numbers)
                    print("Invalid Choice\n")
                    
        #In case they enter a symbols or Letters
        except Exception:
            print("Invalid Choice\n")
        # In case they use (Ctrl + C) AKA (keyboard interruption shortcut) to terminate program
        except KeyboardInterrupt:
            print("Program terminated\n")
            break
limiter()