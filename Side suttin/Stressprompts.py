import time

def first_phase():
    response_to_first_message = input("You have reached Nii's automated message service. "
                                      "Select from the following options: \n"
                                      "A - An apology \n"
                                      "B - An explanation  \n"
                                      "C - You're bored \n"
                                      "D - Other(Specify) \n").upper()
    if response_to_first_message == "A":
        input("What do you want to apologise for? ")
    elif response_to_first_message == "B":
        input("What do you want to explain? ")
    elif response_to_first_message == "C":
        input("What would you want to do (specify) ")
    elif response_to_first_message == "D":
        input("Talk to us: ")
        print("I see...")

    print("You are in line to be connected to Nii in a live chat please wait. "
          "While waiting, what song would you like to listen to? ")
    song_choice = input("")
    print(f"Oh you have a nice taste in music. {song_choice} coming right up")


def reconnect():
    while True:
        again = input("Live session has ended. You had like eternity to say whatever you wanted to say but you didn't."
                      "Any would you like to reconnect?[y/n] ").lower()
        if again == "y":
            first_phase()
        elif again == "n":
            print("Oh I see have a nice day. Hmph!")
            break
        else:
            print("I don't seem to understand.")


first_phase()
time.sleep(15)
reconnect()

