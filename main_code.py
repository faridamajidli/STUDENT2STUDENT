#####################################################################################################
# First we define the class User, and create a function that allows new users to create their account.
#####################################################################################################
import os
from operator import add


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

    acc_path = os.path.join("data", "accounts.txt")
    infile = open(acc_path,'r')
    for line in infile:
        str = line

    infile = open(acc_path, 'w')

    print(str+";"+username+'='+password, file=infile, end='')

    infile.close()

    user = User(first_name, last_name, degree, year, contact, username, password, subscription, tutoring)
    user_list.append(user)
    return user

################################################
# Creating a function that allows users to login
################################################
def log_in(user_details, list):
    username = input("Username: ")
    password = input("Password: ")
    acc_path = os.path.join("data", "accounts.txt")
    infile = open(acc_path, 'r')

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
            want_check_availability = input("Do you want to check the availability of a tutor? (yes or no): ")
            if want_check_availability == "yes":
                bfs()
            else:
                pass

            want_upload_notes = input("Do you want to upload your notes? (yes or no) ")

            if want_upload_notes == "yes":
                upload_notes()
            else:
                pass

            want_download_notes = input("Do you want to download notes? (yes or no) ")

            if want_download_notes == "yes":
                download_notes()
            else:
                pass

            initial_loop = input("If you want to quit the program press <Enter>.\nIf you want to find another tutor "
                                 "please type 1.\nIf you want to check the availability of a tutor press 2."
                                 "\nIf you want to upload notes press 3."
                                 "\nIf you want to download notes press 4.")

            if initial_loop == "":
                exit()
            elif initial_loop == "1":
                find_tutor()
            elif initial_loop == "2":
                bfs()
            elif initial_loop == "3":
                upload_notes()
            elif initial_loop == "4":
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

    tutors_path = os.path.join('data', 'tutors_list.txt')
    infile = open(tutors_path, 'r')
    for line in infile:
        str = line

    infile = open(tutors_path, 'w')

    print(str + ";" + tutor.last_name + '=' + subject, file=infile, end='')

    contact_path = os.path.join('data', 'tutors_contact.txt')
    infile = open(contact_path, 'r')
    for line in infile:
        str = line

    infile = open(contact_path, 'w')

    print(str + ";" + tutor.last_name + '=' + contact, file=infile, end='')

    infile.close()

###################################################################
# Now let's define the function that allows a user to find a tutor.
###################################################################
def find_tutor():
    subject = input("What class do you want to be tutored in? (only 1 class) ")

    contact_path = os.path.join('data', 'tutors_contact.txt')
    infile = open(contact_path, 'r')
    for line in infile:
        str_contact = line

    dictionary_contact = dict(subString.split("=") for subString in str_contact.split(";"))

    tutors_path = os.path.join('data', 'tutors_list.txt')
    infile = open(tutors_path, 'r')
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
def upload_notes():
    subject = input("For which class do you want to upload notes? ")
    chapter = input("Which chapter are you uploading? (only 1 chapter) ")

    infileName = input("Okay, now what is the name of the file where the notes are? ")

    infile = open(infileName, "r")
    notes = infile.read()
    infile.close()
    mynotes = Notes(subject=subject, chapter=chapter, content=notes)

    notes_path = os.path.join('data', 'notes_list.txt')
    infile = open(notes_path, 'r')
    for line in infile:
        str = line

    infile = open(notes_path, 'w')

    print(str + ";" + subject+chapter + '=' + infileName, file=infile, end='')

    infile.close()


#######################################
# Creating a function to download notes
#######################################
def download_notes():
    subject = input('For which class you want to download the notes? ')
    chapter = input('Which chapter from this class do you want to download? ')

    notes_path = os.path.join('data', 'notes_list.txt')
    infile = open(notes_path, 'r')
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

#Creating a Breadth First Search Algorithm to find a timeslot with matched tutor
#First defining the function where tutors can put their availability
def tutors_schedule():
    date = input("Please type all the days where you are available for, seperated by a comma in "
                     "the format dd/mm (for example >>):"
                     "\n29/11,01/12,04/12..."
                     "\n(Don't put spaces before or after the commas please: ")
    date = date.split(',')

    time = input("Please for each day you wrote in the previous input, write at what time you are available (seperated by a comma) "
                 "in the following form:"
                 "\n11:00am,05:00pm,09:00pm...")

    time = time.split(',')

    date_time = list(map(add, date, time))
    date_time_str = ' '.join(map(str, date_time))

    last_name = input("Please write your last name: ")


    subject = input("Please type which class you can tutor in (only one subject)")

    contact = input("Please write where you want to be contacted if a student is matched with you (write your email or your phone number): ")

    schedules_path = os.path.join("data", "schedules.txt")
    infile = open(schedules_path, 'r')
    for line in infile:
        string = line

    infile = open(schedules_path, 'w')

    print(string + ";" + last_name+"_date_time" + '=' + date_time_str + ";" + last_name+"_subject" + '=' + subject +
          ";" + last_name+"_contact" + '=' + contact, file=infile, end='')

    infile.close()

#then, defining a function that searches through the availability of a given tutor and prints the time slot that match the
#availability of the tutor with the availability of the student
def bfs():
    last_name = input("Please write the last name of the tutor that you want to check the availability for: ")

    schedules_path = os.path.join("data", "schedules.txt")
    infile = open(schedules_path, 'r')

    for line in infile:
        string = line

    dictionary = dict(subString.split("=") for subString in string.split(";"))

    if last_name+"_date_time" in dictionary:

        date_time = dictionary.get(last_name+"_date_time")
        date_time = date_time.split()
        subject = dictionary.get(last_name+"_subject")
        contact = dictionary.get(last_name+"_contact")

        #Creation of the graph
        graph = {}
        graph[last_name] = date_time
        for i in date_time:
            graph[i] = []


        date_student = input("Which day do you want to be tutored in? Please write in the format dd/mm: ")
        time_student = input("At what time in that day do you want to be tutored? Please write a time like 11:00am or 03:00pm: ")
        subject_student = input("What class do you want to be tutored in at that time?")

        date_time_student = date_student+time_student
        search_queue = graph[last_name]
        already_searched = [last_name]

        result = False

        while search_queue:
            currentDate = search_queue.pop(0)
            if not currentDate in already_searched:
                if currentDate == date_time_student and subject_student == subject:
                    result = True
                    print(last_name, "can tutor you for", subject, ". You can contact him at", contact)
                    search_queue.extend(graph[currentDate])
                    already_searched.append(currentDate)

        if result:
            pass
        else:
            print("Sorry, no tutors are available at that time for", subject_student)
    else:
        try_again = input("Sorry, this tutor has not registered the data of his schedule. Do you want to try again? (yes or no) ")
        if try_again == "yes":
            bfs()
        else:
            pass



def main():
    user_list = []
    notes_list = []
    print("Hello and Welcome to Student2Student!")


    initial = input("If you already have an account and want to login, please press <Enter>.\nIf you don't have an account yet "
                    "and want to create one, type 1 ")

    if initial == "1":
        user = user_details(user_list)
    else:
        log_in(user_details, user_list)


    if user.tutoring == "yes":
        create_tutor(user)
        initial_schedule = input("Do you want to set your schedule to show other students when you are available? (yes or no): ")
        if initial_schedule == "yes":
            tutors_schedule()
        else:
            pass
    else:
        pass


    if user.subscription == "yes":
        want_tutor = input("Do you want to find a tutor? (yes or no) ")

        if want_tutor == "yes":
            find_tutor()
            initial_bfs = input("Do you want to check the availability of a tutor? (yes or no): ")
            if initial_bfs == "yes":
                bfs()
            else:
                pass
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

    initial_loop = input("If you want to quit the program press <Enter>.\nIf you want to find another tutor "
                         "please type 1.\nIf you want to check the availability of a tutor press 2."
                         "\nIf you want to upload notes press 3."
                         "\nIf you want to download notes press 4.")

    if initial_loop == "":
        exit()
    elif initial_loop == "1":
        find_tutor()
    elif initial_loop == "2":
        bfs()
    elif initial_loop == "3":
        upload_notes()
    elif initial_loop == "4":
        download_notes()
    else:
        pass
        #all the else statements with pass mean that we need to do error handling)


main()
