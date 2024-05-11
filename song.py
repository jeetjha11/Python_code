def display_song(song_container):
    print("Song Name::::\n")
    for song in song_container:
        print(song)

    print("\n")


def update_by_index(song_index, song_container):
    new_song = input("Enter the Song: ")
    song_container[song_index] = new_song
    display_song(song_container)


def update_by_name(old_song, song_container):
    if old_song in song_container:
        new_song = input("Enter the new value>>>> ")
        index = song_container.index(old_song)
        song_container[index] = new_song
        print("Song Updated Success")
        display_song(song_container)

    else:
        print("Invalid Song Name Please Try Again!!")


def insert_song(song_name, song_container):
    if song_name in song_container:
        print(f"Song->{song_name}  is already Present in the list")

    song_container.append(song_name)
    print("Song added Success")
    display_song(song_container)


def main():
    song_container = []
    print("Welcome to the program......")
    while True:
        print("1. Insert song\n"
              "2. Update/edit Song \n"
              "3. Delete Song \n"
              "4. view All Song \n "
              "5. Exit")

        choice = int(input("Please Select a Operation>>>: "))
        if choice == 1:
            song_name = input("Enter the song: ")
            insert_song(song_name, song_container)


        elif choice == 2:
            while True:
                print("1. Update by Song Name\n"
                      "2. Update by song Index\n"
                      "3. Exit")

                update_choice = int(input("Please choose one option"))
                if update_choice == 1:
                    old_song = input("Enter the song name which you want to update>>> ")
                    update_by_name(old_song, song_container)

                elif update_choice == 2:
                    song_index = int(input("Please Enter the Index od the song"))
                    while True:
                        if song_index < 0 or song_index > len(song_container) - 1:
                            print(
                                f"Given Index is invalid Please Enter the valid index which lie between 0 to{len(song_container) - 1} \n ")

                            song_index = int(input("Please Enter the Index od the song"))
                        else:
                            break
                    update_by_index(song_index, song_container)
                elif update_choice == 3:
                    print("Thanks")
                    break


if __name__ == '__main__':
    main()
