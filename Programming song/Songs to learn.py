"""
Luke Maclean
1/9/2017

This program tracks songs the user wants to learn and has learned.

Github
https://github.com/CP1404-2017-2/a1-JCULukeM

"""


# Prints the menu choice
def print_menu():
    print("Menu: ")
    print("L - List songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")


# Asks the user for the details for the song and writes to the list
def add_song(song_list):
    new_list = []
    title = input("Title: ")
    new_list.append(title)
    artist = input("Artist: ")
    new_list.append(artist)
    year = input("Year: ")
    new_list.append(str(year))
    new_list.append('y')
    song_list.append(new_list)


# Load song. Appends each song to the master list and returns the song count and new updated list.
def load_song(in_file):
    song_list = []
    song_count = 0
    for song in in_file:
        record = song.strip("\n").split(",")
        song_count += 1
        song_list.append(record)

    return song_list, song_count

#Checks how many songs are left
def songs_left(song_list):
    songs_learned = 0
    song_left = 0
    for i in range(0, len(song_list), 1):
        if song_list[i][len(song_list[i]) - 1] == 'y':
            song_left += 1
    for i in range(0, len(song_list), 1):
        if song_list[i][len(song_list[i]) - 1] == 'n':
            songs_learned += 1
    if song_left > 0:
        print(songs_learned, "Songs learned,", song_left, "songs still to learn")
    else:
        print("No more songs to learn!")
        return True


# complete a song
# marks a song complete. Asks user for song number. error checks for valid input.
#Goes through list of songs noting whether the chosen song is already learned.
#If it is not learned it then marks it as learned.
def complete_song(song_list):
    songs_left(song_list)
    valid_input = False
    if songs_left == True:
        valid_input = True
    while not valid_input:
        try:
            song_number = int(input("Enter the number of song to mark as learned: "))
            if song_number < 0:
                print("Number must be >= 0")
                break
            if song_list[song_number][len(song_list[song_number])-1] == 'y':
                song_list[song_number][len(song_list[song_number]) - 1] = 'n'
                print((song_list[song_number]), "learned")
                valid_input = True
            else:
                print("you have already learned", (song_list[song_number]))

        except ValueError:
            print("Invalid input; enter a valid number")
        except:
            print("Invalid song number")


# Reads the csv file and prints out each line
def list_songs(song_list):
    for i in range(0, len(song_list), 1):
        print("{:2}.".format(i), end=' ')
        if song_list[i][len(song_list[i]) - 1] == 'y':
            print(" * ", end=' ')
        else:
            print("   ", end=' ')
        for j in range(0, len(song_list[i]) - 1, 1):
            if j < len(song_list[i]) - 2:
                print("{:32}-".format(song_list[i][j]), end=' ')
            else:
                print("({:4})".format(song_list[i][j]), end=' ')

        print()
    songs_left(song_list)


def save_songs(out_file, song_list):
    for i in range(0, len(song_list), 1):
        for j in range(0, len(song_list[i]), 1):
            print(song_list[i][j], file=out_file, end='')
            if j < len(song_list[i]) - 1:
                print(",", file=out_file, end='')

        print(file=out_file, )


def main():
    in_file = open("songs.csv", "r")
    song_list, song_num = load_song(in_file)
    in_file.close()
    songs_loaded = 6
    songs_saved = 7
    print("Songs to learn 1.0 - by Luke maclean")
    print(songs_loaded, " songs loaded")
    choice = "y"
    while choice != "Q":
        print_menu()
        choice = input(str("Choose menu option: ")).upper()
        if choice == "L":
            list_songs(song_list)
        elif choice == "A":
            add_song(song_list)
        elif choice == "C":
            complete_song(song_list)
        else:
            print("Invalid menu choice")
    out_file = open("songs.csv", "w")
    save_songs(out_file, song_list)
    out_file.close()
    print(songs_saved, "songs saved to songs.csv")
    print("Have a nice day :)")

main()
