# STUDENT2STUDENT
ADS Group Project

Student2Student is a platform for connecting students to student for tutoring purposes and providing notes exclusive to IE students 
* it allows students to interact, share notes, and receive tutoring
* it ensures students get their knowledge from approved students who have experience and are informed about the university's methodology

# Installation

To be able to run our main program, you have to have the Python programming language (versions between 3.6 and 3.8) installed. When you launch Python, create a new project and make sure you have these files that we have published above opened in your project:

* accounts.txt: username1=password1
* notes_list.txt: classachapter1=textfile.txt
* tutors_list.txt: tutor1=subject1
* tutors_contact.txt: tutor1=contact1
* schedules.txt: name=info
* marketing_notes_chapter1.txt: some notes for marketing chapter 1 (this is sample notes for you to try our 'Upload Notes' service) 

Note: These text files help us to store the inputted data by the user as dictionaries. 

To be able to run our scheduling program, you have to use Google Colaboratory.

Packages and Libraries:
You will need to run these 2 lines (already included in the code) without installing any package.
* import os
* from operator import add

Now, that you have everything set up, download the python files called main_code.py and run it.

# Usage

Main Code:

After running the main code, you will officially access our platform. You will be welcomed and asked several questions on the following 4 sections:

* The Account: Sign up or Log in
* Giving and Receiving Tutoring
* Inserting Schedule and Searching Availability 
* Uploading and Downloading Notes 

You will have to input you choices. After the choices are validated, the respective action will be carried out and you will be asked more questions based on your choice.

   1. The Account: Sign up or Log in. This part makes sure if you already have an account or not. If want to log in, you press Enter. If you want sign up, you type 1
         * Sign Up
            * USER INPUT: First Name, Last Name, Degree, Year, Email, Username, Password, Subscription Plan (19.99€ per month)
            * OUTPUT: Your username and password is now saved in accounts.txt. The program continues with the remaining functions which means the inputs are validated and the account has been created
         * Log In
            * USER INPUT: Username, Password
            * OUTPUT: You are welcomed and program continues with the remaining functions
   2. Giving and Receiving Tutoring: Depending on your choices in the previous stage of the program (subscription), you are asked to input more information
         * Giving Tutoring: You can be a tutor no matter if you have a subscription or not.
            * USER INPUT: yes or no for Giving Tutoring and Class Desired to Teach
            * OUTPUT: Your last name, email and class you are teaching are now saved to tutors_list.txt and tutors_contact.txt as a tutor for potential students.
         * Receiving Tutoring: You can only receive tutoring if you have a subscription.
            * USER INPUT: yes or no for Receiving Tutoring and Class Desired to Learn
            * OUTPUT: Last Name and Email of an available tutor for that particular class. (if no available tutor, then message is displayed)
   3. Inserting Schedule and Searching Availability: If you sign up as a Tutor, you can choose to set up your schedule of availability.
         * Inserting Schedule: If you sign up as a tutor, you can insert the days and times during which you are available for tutoring
            * USER INPUT: List of days and corresponding times of availability, last name, subject of tutoring, and contact information.
            * OUTPUT: These inputs are saved as a string in the file "schedules.txt", which will be potentially retrieved and transformed intro a dictionnary to run the next function.
         * Searching Availability: As a user of the app, you can search for the availability of the tutor of your choice, provided he has already set up his schedule on the app.
            * USER INPUT: Last name of tutor of interest, day and time for which you want to check availability, and subject you want to be tutored in.
            * OUTPUT: A confirmation that the tutor is available at that day and time for that subject and his contact information, or a disconfirmation.
   5. Uploading and Downloading Notes: You have an access to the notes no matter if you have a subscription or not.
         * Uploading Notes:
            *  USER INPUT: yes or no for Uploading Notes, Class, Chapter (enter only the chapter number), Name of the text file the notes are in (create a text file in your python project and put the notes in that file)
            *  OUTPUT: The class, chapter number and file name for your notes are now saved in notes_list.txt
         *  Downloading Notes:
            *  USER INPUT: yes or no for Downloading Notes, Class, Chapter (enter only the chapter number), Name of the text file you want the notes to be saved (if there are any)
            *  OUTPUT: The name of the text file that the notes are originally in. Downloads the notes after asking you if you want to download them.

# Additional Information about The Code

The main code that we created does not have pre-stored data for the accounts, available list of tutors and uploaded notes of courses. It actually saves information in real-time. Meaning it saves the user's credentials, uploads, tutoring status in a text file right after input in a separate file. As new information is inputted by the user, the text file gets updated.

In order to carry out our objective, we have used the following data structure:

1. Dictionaries: Storing accounts, tutors, notes

And following Algorithms:

1. Breadth-first Search: Creating an algorithm that helped us with scheduling sessions
2. Insertion: Appending relevant inputs to the Dictionaries

# Credits

The authors of this project are:
1. Al-Sawalha, Maria
2. Majidli, Farida
3. Pascual, Fernando 
4. Troje, Delphine 
5. Vats, Mahika
6. Zaid, Mehdi
