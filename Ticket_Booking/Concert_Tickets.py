def Promoter():
    print("Which artist schedule would u like to Change?")
    Pro_ch=input();
    if Pro_ch not in Stadiums.keys():
        print("Sorry The Artist is not in List\nWould You Like To Add A New Performance?[y/n]")
        ch3=input();
        if "y" in ch3:
            artist=input("Enter Artist Names:")
            perform=input("Enter The performance:")
            Stadiums[artist]=perform
            print("Changes have Been Made")
            return
    elif Pro_ch in Stadiums.keys():
        print("Please Be Accurate With Names")
        print("Enter The Changes\nArtist:")
        artist=input()
        print("Performing On/at:")
        perform=input()
        print(artist + "\tIs performing At/On\t" + perform)
        Stadiums[artist]=perform
        print("Changes Have Been Made")
        for Key, val in Stadiums.items():
            print(Key + "\tIs Performing On/At\t " + val)
        return
            

def Consumer():   
        print("This is the is list of Artist performing...")
        for key ,val in Stadiums.items():
            print(key + "\tIs Performing On/At\t" + val)
        print("\nWhose Show Would U like to attend?:")
        artist=input()
        if artist not in Stadiums.keys():
            print("Sorry this Artist Is not Performing")
            
        if artist in Stadiums.keys():
            print(artist + "\tIs performing On/at\t" + Stadiums.get(artist))
            print("\nCan U Confirm?:")
            Ch=input().lower()
            if "y" in Ch:
                print("Showing Tickets"+"\n1.Front Row-500"+"\n2.Sides-300"+"\n3.Back Row-200")
                ch3=input().lower()
                if('1' in ch3 or 'f' in ch3):
                    print("Your Seat For Front Row is Booked!!!")
                if('2' in ch3 or 's' in ch3):
                    print("Your Seat For Sides Row is Booked!!!")
                if('3' in ch3 or 'b' in ch3):
                    print("Your Seat For Back Row is Booked!!!")
            else:
                print("Thank You!!")
                return
            print("Enjoy The Show!!!")
            return


Stadiums={"Ariana":"16th Decemeber GND","Shawn":"10th December GND","Michelle":"25th Decemeber GND"}
while(True):
    print("Hello Sire!! How can I Help You?");
    user=input("Who am i Talking to?\n");
    print("HI!!"+user+"\nWould U like to Login as \n1.Promoter\n2.Consumer");
    user_ch=input().lower();
    if('1' in user_ch or 'p' in user_ch ):
          print("You Have Logged In as Promoter")
          Promoter();

    if('2' in user_ch or 'c' in user_ch):
           print("You Have Logged In as Consumer")
           Consumer();
            
    print("Would U like To Continue?[1/0]")
    End_ch=input().lower()
    if('0' in End_ch or 'n' in End_ch):
        break
        

