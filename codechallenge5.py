print("Hi, Welcome to Manga Recommender!")
print("\nAnswer a few questions to find your next read.")

genre = input("\nWhat genre do you like? (action, romance, horror): ")

#action
if genre == "action":
    duration = input("\nHow long should the manga be? (short, medium, long): ")
    if duration == "short":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can only recommend:\n\tAll You Need Is Kill by Hiroshi Sakurazaka & Takeshi Obata")
        elif decade == "2010s":
            print("\nI can recommend:\n\tTokyo Ghoul by Sui Ishida\n\tOne Punch Man by ONE & Yusuke Murata")
    elif duration == "medium":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\n\tThere is no medium duration manga in the 2000s.")
        elif decade == "2010s":
            print("\nI can recommend:\n\tMy Hero Academia by Kohei Horikoshi")
    elif duration == "long":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tOne Piece by Eiichiro Oda\n\tNaruto by Masashi Kishimoto\n\tBleach by Tite Kubo")
        elif decade == "2010s":
            print("\nI can recommend:\n\tAttack on Titan by Hajime Isayama")

#romance
elif genre == "romance":
    duration = input("\nHow long should the manga be? (short, medium, long): ")
    if duration == "short":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tLovely★Complex by Aya Nakahara")
        elif decade == "2010s":
            print("\nI can recommend:\n\tMy Little Monster by Robico")
    elif duration == "medium":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nThere is no medium-length duration romance manga in the 2000s.")
        elif decade == "2010s":
            print("\nI can recommend:\n\tAo Haru Ride by Io Sakisaka")
    elif duration == "long":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tBoys Over Flowers by Yoko Kamio")
        elif decade == "2010s":
            print("\nI can recommend:\n\tKimi ni Todoke by Karuho Shiina")

#horror
elif genre == "horror":
    duration = input("\nHow long should the manga be? (short, medium, long): ")
    if duration == "short":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tThe Enigma of Amigara Fault by Junji Ito")
        elif decade == "2010s":
            print("\nI can recommend:\n\tFragments of Horror by Junji Ito")
    elif duration == "medium":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tThe Drifting Classroom by Kazuo Umezu")
        elif decade == "2010s":
            print("\nI can recommend:\n\tI Am a Hero by Kengo Hanazawa")
    elif duration == "long":
        decade = input("\nWhich decade? (2000s, 2010s): ")
        if decade == "2000s":
            print("\nI can recommend:\n\tHellsing by Kouta Hirano")
        elif decade == "2010s":
            print("\nI can recommend:\n\tAjin: Demi-Human by Gamon Sakurai")

else:
    print("\n\tSorry but that genre isn't available. Please try again.")
