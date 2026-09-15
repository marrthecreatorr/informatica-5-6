import time
def main():
    playlist = ["Boston", "Dracula", "I knew It, I knew You", "hate that i made you love me", "Risk It All"]
    playlist.append("Be By You")
    print(playlist)

    playlist.insert(0,"Bohemian Rhaosody")
    print(playlist)

    playlist.pop(4)
    print(playlist)

    print(playlist.index("Risk It All"))
    print("Number of songs un playlist:", len(playlist))
    playlist.reverse()
    print(playlist)
    playlist.sort()
    print(playlist)

    # Challenge
    repeat = len(playlist)
    while repeat > 0:
        print(playlist)
        song = playlist[0]
        playlist.append(song)
        repeat -= 1
        time.sleep(3)

if __name__ == "__main__":
    main()
