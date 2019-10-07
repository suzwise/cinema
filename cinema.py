films={
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
}

while True:
    choice = input("what film will you like to watch? ").strip().title()
    if choice in films:

        #check user's age
        age=int(input("how old are you? "))
        if age >=films[choice][0]:
             
            # check enough seats
            num_seats = films[choice][1]
            if num_seats>0:
                print("enjoy the film!")
                films[choice][1] = films[choice][1] -1
            else :
                print("we are out of seats")
        else:
            print("you are too young to watch the film!")

    else:
        print ("we dont have that film ...")
