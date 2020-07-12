import sys

f = open("students.txt", 'w', newline='')
f.close()

class Academy:
    courses = ('Python', 'Java', 'C', 'Ruby')

    def inquiry(self):
        option = input("Would you like more information about our program? Enter y or n : ")

        if option == "y":
            print('''\nIT Academy Institute has been providing quality education and hands-on training since its
            establishment in 2010. We offer courses in Python, Java, C, and Ruby. You will have the option to take 
            our courses either online or in class. Post course completion we also provide mock interviews and job 
            placement to the best performing candidates.\n''')
            reg = input("Would you like to register? Enter y or n : ")
            if reg == "y":
                self.register()
            elif reg == "n":
                print("Please visit us again!")

        elif option == "n":
            print("We hope to hear from you in the future. Thank you!")
    
    def register(self):

        print("Please fill out the following information to register : ")
        full_name = input("Full Name : ")
        dob = input("Date of Birth  (yyyy-mm-dd) : ")
        address = input("Address : ")
        phone = input("Phone number : ")
        email = input("Email : ")
        course = input("What course are you interested in : Python, Java, C or Ruby? ")
        balance = "N/A"

        filename = "students.txt"
        header = ("Full Name,", "Date of birth,", "Address,", "Phone,", "Email,", "Course,","Balance\n")
        data = [full_name, dob, address, phone, email, course,balance]
        self.save_data(header,data,filename,"write")
    
    def save_data(self,header,data,filename,option):
        filename = "students.txt"
        with open(filename,'a',newline="") as f:
            if option == 'write':
                f.writelines(header)
                f.write(','.join(data))
                f.close()
                self.payment()

            elif option == 'update':
                data[-1] = "Balance cleared"
                f.write(data[-1])
                self.completion()
            
            elif option == 'partial':
                data[-1] = "Balance: Rs. 10000"
                f.write(data[-1])
                self.clearbal()
            
    def updater(self,filename):
        filename = "students.txt"
        header = ("Full Name,", "Date of birth,", "Address,", "Phone,", "Email,", "Course,","Balance\n")
        f = open(filename,'r')
        read = f.readlines()
        f.close()

        self.save_data(header,read,filename,"update")
    
    def partial(self,filename):
        filename = "students.txt"
        header = ("Full Name,", "Date of birth,", "Address,", "Phone,", "Email,", "Course,","Balance\n")
        f = open(filename,'r')
        read = f.readlines()
        f.close()

        self.save_data(header,read,filename,"partial")
    
    def clearbal(self):
        clear = input("Are you ready to clear your balance? y or n ")
        if clear == "y":
            self.updater("students.txt")
        
        elif clear == "n":
            out = input("Do you want to drop out of the program? y or n ")
            if out == "n":
                print("Please contact our office immediately to clear the balance.")
            elif out == "y":
                print("You will be dropped from our program")
                self.delete("students.txt")
    
    def delete(self,filename):
        filename = "students.txt"
        # header = ("Full Name,", "Date of birth,", "Address,", "Phone,", "Email,", "Course,","Balance\n")
        f = open(filename,'r')
        read = f.readlines()
        f.close()
        
        del read[1]

    def payment(self):
        print("Thank you for registering. The next step is to make a payment.")
        print('''The deposit amount is Rs.20000. You can either pay the full deposit today or make a partial 
        payment of Rs.10000 today and the remaining balance in one week.''')
        choice = int(input("What amount would you like to pay? Please enter 1 for 10000 and 2 for 20000 : "))
        if choice == 2:
            print("Thank you. We will provide you information about the course materials shortly.")
            self.updater("students.txt")

        elif choice == 1:
            print("Thank you. Please pay the remaining balance in a week.")
            self.partial("students.txt")
        else:
            print("Request invalid")
    
    def completion(self):
        comp = input("If the student has completed the course, enter 'y'. If the student has dropped the course, enter 'n' : ")
        if comp == "y":
            print("Congratulations! You will now get your deposit back.")
        elif comp == "n":
            print("The student information will be removed from our program.")

x = Academy()
x.inquiry()
