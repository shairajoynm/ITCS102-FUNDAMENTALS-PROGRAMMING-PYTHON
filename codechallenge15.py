print("\nHi! Welcome to your anime list compiler\n")

anime = []

while True:
    name = input("\nInput the name of anime, type 's' to stop the compiler:  ").lower()
    print("Anime title added to the list")

    if name == "s":
        break

    anime.append(name)

print("\nYour compiled anime list:")
for title in anime:
    print(title)
