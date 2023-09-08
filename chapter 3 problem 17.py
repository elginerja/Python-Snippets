# We are trying to make a program that helps a user connect to their wifi from their computer
# We are trying to tell the user the steps to use to do that
print("Reboot the computer and try to connect.\n(Y/N) Enter (Y or y) for yes or (N or n) for no.")

user_answer = input("Did that fix your problem? ")

if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
    if user_answer == "n" or user_answer == "N":
        print("Try and Reboot the router and try to connect.")
        user_answer = input("Did that fix your problem? ")

        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
            if user_answer == "n" or user_answer == "N":
                print("Make sure the cables inbetween the router & modem are plugged in firmly.")
                user_answer = input("Did that fix your problem? ")

                if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                    if user_answer == "n" or user_answer == "N":
                        print("Move the router to a new location and try to connect again. ")
                        user_answer = input("Did that fix your problem? ")

                        if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
                            print("Get a new router, you might be screwed. Sorry dawg. ")
                        else:
                            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
                else:
                    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
        else:
            print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
else:
    print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")