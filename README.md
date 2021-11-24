# STUDENT2STUDENT
ADS Group Project

Student2Student is a platform for connecting students to student for tutoring purposes and providing notes exclusive to IE students 
* it allows students to interact, share notes, and receive tutoring
* it ensures students get their knowledge from approved students who have experience and are informed about the university's methodology

# Installation

To be able to run our main program, you have to have the Python programming language (versions between 3.6 and 3.8) installed. When you launch Python, create a new project and make sure you have these files created in your project with following texts written in them:

* accounts.txt: username1=password1
* notes_list.txt: classachapter1=textfile.txt
* tutors_list.txt: tutor1=subject1
* tutors_contact.txt: tutor1=contact1

Note: These text files help us to store the inputted data by the user as dictionaries.

To be able to run our scheduling program, you have to use Google Colaboratory.

You do not need to install any packages or libraries.

Now, that you have everything set up, create 2 new python files called student2student.py and scheduling.py and run them, respectfully.

# Usage

Main Code:

After running the main code, you will officially access our platform. You will be welcomed and asked several questions on the following 3 sections:

* The Account: Sign up or Log in
* Giving and Receiving Tutoring
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
            * OUTPUT: You are saved to tutors_list.txt and tutors_contact.txt as a tutor for potential students.
         * Receiving Tutoring: You can only receive tutoring if you have a subscription.
            * USER INPUT: yes or no for Receiving Tutoring and Class Desired to Learn
            * OUTPUT: Last Name and Email of an available tutor for that particular class. (if no available tutor, then message is displayed)
   3.  
           
  




# Credits

The authors of this project are:
1. Mahika Vats
2. Mehdi Zaid
3. Maria Al-Sawalha
4. Delphine Troje
5. Fernando Pascual
6. Farida Majidli
