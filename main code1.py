#####################################################################################################
# First we define the class User, and create a function that allows new users to create their account.
#####################################################################################################
class User():
    def __init__(self, first_name, last_name, degree, year, contact, username, password, subscription, tutoring):
        self.first_name = first_name
        self.last_name = last_name
        self.degree = degree
        self.year = year
        self.contact = contact
        self.username = username
        self.password = password
        self.subscription = subscription
        self.tutoring = tutoring


def user_details(user_list):
    first_name = input("Please type your first name: ")
    last_name = input("Please type your last name: ")
    degree = input("What degree are you doing: "
                     "\n1 - Bachelor in Business Administration"
                     "\n2 - Bachelor in Behavior And Social Sciences"
                     "\n3 - Bachelor in Economics"
                     "\n4 - Bachelor in Data And Business Analytics"
                     "\n5 - Bachelor in Computer Science And Artificial Intelligence"
                     "\n6 - Bachelor in Communication And Digital Media"
                     "\n7 - Bachelor in Architectural Studies"
                     "\n8 - Bachelor in Design"
                     "\n9 - Bachelor in International Relations"
                     "\n10 - Bachelor in Philosophy, Politics, Law And Economics"
                     "\n11 - Bachelor in Laws"
                     "\n12 - Dual Degree in Business Administration + Data & Business Analytics"
                     "\n13 - Dual Degree in Business Administration + International Relations"
                     "\n14 - Dual Degree in Business Administration + Laws"
                     "\n15 - Dual Degree in Laws + International Relations"
                     "\n16 - Dual Degree in Philosophy, Politics, Law & Economics + Data & Business Analytics"
                     "\n17 - Dual Degree in Business Administration + Design"
                     "\n18 - Dual Degree in Economics + International Relations"
                     "\n\nPlease type the number corresponding to your degree: ")
    if degree == "1":
        degree = "Bachelor in Business Administration"
    elif degree == "2":
        degree = "Bachelor in Behavior And Social Sciences"
    elif degree == "3":
        degree = "Bachelor in Economics"
    elif degree == "4":
        degree = "Bachelor in Data And Business Analytics"
    elif degree == "5":
        degree = "Bachelor in Computer Science And Artificial Intelligence"
    elif degree == "6":
        degree = "Bachelor in Communication And Digital Media"
    elif degree == "7":
        degree = "Bachelor in Architectural Studies"
    elif degree == "8":
        degree = "Bachelor in Design"
    elif degree == "9":
        degree = "Bachelor in International Relations"
    elif degree == "10":
        degree = "Bachelor in Philosophy, Politics, Law And Economics"
    elif degree == "11":
        degree = "Bachelor in Laws"
    elif degree == "12":
        degree = "Dual Degree in Business Administration + Data & Business Analytics"
    elif degree == "13":
        degree = "Dual Degree in Business Administration + International Relations"
    elif degree == "14":
        degree = "Dual Degree in Business Administration + Laws"
    elif degree == "15":
        degree = "Dual Degree in Laws + International Relations"
    elif degree == "16":
        degree = "Dual Degree in Philosophy, Politics, Law & Economics + Data & Business Analytics"
    elif degree == "17":
        degree = "Dual Degree in Business Administration + Design"
    elif degree == "18":
        degree = "Dual Degree in Economics + International Relations"

    year = input("Please type the year you are in (1-5)? ")
    contact = input("Please type your email: ")
    username = input("Please type your username: ")
    password = input("Please type your password: ")
    subscription = input("We have monthly subscription plan for 19.99€. Do you want to subscribe? (yes or no): ")
    tutoring = input("Do you want to be a tutor? (yes or no): ")

    infile = open('accounts.txt','r')
    for line in infile:
        str = line

    infile = open('accounts.txt', 'w')

    print(str+";"+username+'='+password, file=infile, end='')

    infile.close()

    user = User(first_name, last_name, degree, year, contact, username, password, subscription, tutoring)
    user_list.append(user)
    return user

################################################
# Creating a function that allows users to login
################################################
def log_in(user_details, list, notes_list):
    username = input("Username: ")
    password = input("Password: ")

    infile = open('accounts.txt', 'r')

    for line in infile:
        str = line

    dictionary = dict(subString.split("=") for subString in str.split(";"))

    value = dictionary.get(username)

    if value:
        if password == dictionary[username]:
            print("Hello", username, "\nWelcome back to Student2Student")

            want_tutor = input("Do you want to find a tutor? (yes or no) ")

            if want_tutor == "yes":
                find_tutor()
            else:
                pass

            want_upload_notes = input("Do you want to upload your notes? (yes or no) ")

            if want_upload_notes == "yes":
                upload_notes(notes_list)
            else:
                pass

            want_download_notes = input("Do you want to download notes? (yes or no) ")

            if want_download_notes == "yes":
                download_notes()
            else:
                pass
            exit()
        else:
            print("Your password is incorrect, try again")
    else:
        print("This account does not exist.")

    initial = input("If you want to try again, type: 1.\nIf you want to create a new account, type: 2. ")

    if initial == "1":
        log_in(user_details, list)
    else:
        user_details(list)

#######################################################################################################
# Now let's define the class Tutor, and the function that creates a Tutor instance from a user instance
#######################################################################################################
class Tutor():
    def __init__(self, first_name, last_name, degree, year, subject, contact):
        self.first_name = first_name
        self.last_name = last_name
        self.degree = degree
        self.year = year
        self.subject = subject
        self.contact = contact


def create_tutor(user):
    first_name = user.first_name
    last_name = user.last_name
    degree = user.degree
    year = user.year
    contact = user.contact
    subject = input("What class you can tutor other students in? (only 1 class) ")

    tutor = Tutor(first_name, last_name, degree, year, subject, contact)

    infile = open('tutors_list.txt', 'r')
    for line in infile:
        str = line

    infile = open('tutors_list.txt', 'w')

    print(str + ";" + tutor.last_name + '=' + subject, file=infile, end='')

    infile = open('tutors_contact.txt', 'r')
    for line in infile:
        str = line

    infile = open('tutors_contact.txt', 'w')

    print(str + ";" + tutor.last_name + '=' + contact, file=infile, end='')

    infile.close()

###################################################################
# Now let's define the function that allows a user to find a tutor.
###################################################################
def find_tutor():
    subject = input("What class do you want to be tutored in? (only 1 class) ")

    infile = open('tutors_contact.txt', 'r')
    for line in infile:
        str_contact = line

    dictionary_contact = dict(subString.split("=") for subString in str_contact.split(";"))

    infile = open('tutors_list.txt', 'r')
    for line in infile:
        str = line

    dictionary = dict(subString.split("=") for subString in str.split(";"))

    for tutors in dictionary:
        p = ""
        if dictionary[tutors] == subject:
            p = "yes"
            print(tutors, "can tutor you in", subject, ". You can contact him/her at:", dictionary_contact[tutors])
    if p != "yes":
        initial = input(
            "Sorry, no tutors are available for this class at the moment. If you want to try another class "
            "type yes. Otherwise press <Enter>: ")
        if initial == "yes":
            find_tutor()
        else:
            pass

###################################################
# Now we move on to the creation of the Notes Class
###################################################
class Notes():
    def __init__(self, subject, chapter, content):
        self.subject = subject
        self.chapter = chapter
        self.content = content

#####################################
# Creating a function to upload Notes
#####################################
def upload_notes(notes_list):
    subject = input("For which class do you want to upload notes? ")
    chapter = input("Which chapter are you uploading? (only 1 chapter) ")

    infileName = input("Okay, now what is the name of the file where the notes are? ")

    infile = open(infileName, "r")
    notes = infile.read()
    infile.close()
    mynotes = Notes(subject=subject, chapter=chapter, content=notes)

    infile = open('notes_list.txt', 'r')
    for line in infile:
        str = line

    infile = open('notes_list.txt', 'w')

    print(str + ";" + subject+chapter + '=' + infileName, file=infile, end='')

    infile.close()

    notes_list.append(mynotes)

#######################################
# Creating a function to download notes
#######################################
def download_notes():
    subject = input('For which class you want to download the notes? ')
    chapter = input('Which chapter from this class do you want to download? ')

    infile = open('notes_list.txt', 'r')
    for line in infile:
        str = line

    dictionary = dict(subString.split("=") for subString in str.split(";"))

    for notes in dictionary:
        p = ""
        if notes == subject+chapter:
            p = "yes"
            print("You can download", dictionary[notes], "for the class", subject, "chapter", chapter)
            initial = input("\nIf you want to download them, please type yes. Otherwise press <Enter> ")
            if initial == "yes":
                infile = open(dictionary[notes], 'r')
                data = infile.read()
                outfileName = input("What file should the notes go in? ")
                outfile = open(outfileName, 'w')
                print(data, file=outfile)
                outfile.close
                print("The notes have been saved under the name:", outfileName)
                break
    if p != "yes":
        initial = input("Sorry, there are no notes available for what you asked at the moment. If you want to try another class or chapter "
                        "type yes. Otherwise press <Enter>: ")
        if initial == "yes":
            download_notes()
        else:
            pass


def main():
    user_list = []
    tutors_list = []
    notes_list = []
    print("Hello and Welcome to Student2Student!")

    initial = input("If you already have an account and want to login, please press <Enter>.\nIf you don't have an account yet "
                    "and want to create one, type 1 ")

    if initial == "1":
        user = user_details(user_list)
    else:
        log_in(user_details, user_list, notes_list)


    if user.tutoring == "yes":
        create_tutor(user)
    else:
        pass


    if user.subscription == "yes":
        want_tutor = input("Do you want to find a tutor? (yes or no) ")

        if want_tutor == "yes":
            find_tutor()
        else:
            pass
    else:
        pass


    want_upload_notes = input("Do you want to upload your notes? (yes or no) ")

    if want_upload_notes == "yes":
        upload_notes(notes_list)
    else:
        pass

    want_download_notes = input("Do you want to download notes? (yes or no) ")

    if want_download_notes == "yes":
        download_notes()
    else:
        pass


main()
