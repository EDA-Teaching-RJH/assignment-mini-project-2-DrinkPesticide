"""
Assignment 1: I can choose my own project but I must demonstrate basic knowledge of these topics:
concept: a librarian can use this software to perform book transaction and other function for users
1. [Covered] Strings, Ints and Floats [Floats not included so far, i hope you don't hold that against me]
2. [Covered] Inputs and outputs
3. [Covered] Definitions / modules
4. [Covered] Conditionals: = == != += * **
5. [Covered] Match statement and modulo 
6. [Covered] Loops
7. [Covered] Lists and dictionaries
8. [Covered] Error exceptions

Library book system:
    Allows a librarian to access various files about books and the people taking them out on loan.

Variables:
    - (dict) Books = [
        {name:"", author:"", genre:"", total_copies:0, copies_out:0}
        ]
    - (dict) Users: [
    {}
    ]
"""
Books = [
    {"name":"The Great Gatsby", "author":"F. Scott Fitzgerald", "genre":"classics", "total_copies":5, "copies_out":3, "Published": 1925},
    {"name":"Brave New World", "author":"Aldous Huxley", "genre":"classics", "total_copies":6, "copies_out":5, "Published": 1932},
    {"name":"Pride and Prejudice", "author":"Jane Austen", "genre":"classics", "total_copies":7, "copies_out":7, "Published": 1813},
    {"name":"Frankenstein", "author":"Mary Shelley", "genre":"classics", "total_copies":1, "copies_out":1, "Published": 1823},
    {"name":"Jane Eyre", "author":"Charlotte Bronte", "genre":"classics", "total_copies":4, "copies_out":3, "Published": 1847},
    # Classics
    {"name":"The Third Man", "author":"Graham Greene", "genre":"crime", "total_copies":5, "copies_out":4, "Published": 1950},
    {"name":"The Talented Mr Ripley", "author":"Patricia Highsmith", "genre":"crime", "total_copies":7, "copies_out":3, "Published": 1955},
    {"name":"Tishomingo Blues", "author":"Elmore Leonard", "genre":"crime", "total_copies":3, "copies_out":3, "Published": 2002},
    {"name":"Murder on the Orient Express", "author":"Agatha Christie", "genre":"crime", "total_copies":2, "copies_out":0, "Published": 1934},
    {"name":"The Stranger", "author":"Harlan Coben", "genre":"crime", "total_copies":5, "copies_out":4, "Published": 2015},
    # Crime
    {"name":"Children of Time", "author":"Adrian Tchaikovsky", "genre":"Science_fiction", "total_copies":5, "copies_out":0, "Published": 2015},
    {"name":"Fury", "author":"Henry Kuttner", "genre":"Science_fiction", "total_copies":3, "copies_out":1, "Published": 1947},
    {"name":"Dune", "author":"Frank Herbert", "genre":"Science_fiction", "total_copies":15, "copies_out":5, "Published": 1965},
    {"name":"The Difference Engine", "author":"Bruce Sterling and William Gibson", "genre":"Science_fiction", "total_copies":5, "copies_out":0, "Published": 1990},
    {"name":"A Scanner Darkly", "author":"Philip K. Dick", "genre":"Science_fiction", "total_copies":4, "copies_out":2, "Published": 1997},
    # Science Fiction    
    {"name":"Electronics A Systems Approach; 5th edition", "author":"Neil Storey", "genre":"Non_fiction", "total_copies":3, "copies_out":2, "Published": 1925},
    {"name":"The Hundred Years' War on Palestine", "author":"Rashid Khalidi", "genre":"Non_fiction", "total_copies":5, "copies_out":2, "Published": 2020},
    {"name":"Long Walk to Freedom", "author":"Nelson Mandela", "genre":"Non_fiction", "total_copies":2, "copies_out":0, "Published": 1994},
    {"name":"A History of the World", "author":"Andrew Marr", "genre":"Non_fiction", "total_copies":5, "copies_out":0, "Published": 2012},
    {"name":"A Promised Land", "author":"Barack Obama", "genre":"Non_fiction", "total_copies":4, "copies_out":0, "Published": 2020},
    {"name":"Bad Book", "author":"Jordan Peterson", "genre":"Non_fiction", "total_copies":4, "copies_out":1, "Published": 2018},
    # Non fiction
    {"name":"Hamlet", "author":"William Shakepeare", "genre":"plays_and_poetry", "total_copies":5, "copies_out":5, "Published": 1600},
    {"name":"King Lear", "author":"William Shakepeare", "genre":"plays_and_poetry", "total_copies":7, "copies_out":4, "Published": 1600},
    {"name":"Top Girls", "author":"Caryl Churchill", "genre":"plays_and_poetry", "total_copies":2, "copies_out":2, "Published": 1982},
    {"name":"Beautiful", "author":"Carol Ann Duffy", "genre":"plays_and_poetry", "total_copies":2, "copies_out":1, "Published": 1925},
    {"name":"Ariel", "author":"Sylvia Plath", "genre":"plays_and_poetry", "total_copies":1, "copies_out":0, "Published": 1925},
    # Plays and Poetry
    # All book publishing dates are accurate to the tolerance of wikipedia.
    ]

Users = [
    {"surname": "Lurcook", "forename": "Callum", "id_number": 680129, "borrowed_items": ["Electronics A Systems Approach; 5th edition", "The Third Man", "The Talented Mr Ripley", "Murder on the Orient Express"],},
    {"surname": "King", "forename": "Charlie", "id_number": 678903, "borrowed_items": ["Electronics A Systems Approach; 5th edition", "Fury"]},
    {"surname": "Brown", "forename": "Andrew", "id_number": 614705, "borrowed_items": ["Bad Book", "The Hundred Years' War on Palestine"]},
    {"surname": "Rogers", "forename": "Natalya", "id_number": 110011, "borrowed_items": ["The Hundred Years' War on Palestine", "Brave New World"]},
    {"surname": "Russel", "forename": "Harry", "id_number": 657948, "borrowed_items": ["Dune", "The Difference Engine", "Fury", "A Scanner Darkly"]},
    ]
def shutdown():
# (1.) [Done] When get_user_action outputs a 0, this module is activated to display a shutdown message to user.
    message = "-=--=--=-\nYou are shutting down the program.\n-=--=--=-\n \n \n ... complete ..."
    return message

def book_search():
    """ 
When get_user_action outputs 1, this module is activated to:
(1.) [Complete] prompt the user for a book name.
(2.) [Complete] try-except error filtering on input and have the User reinput as necessary.
(3.) [Complete] search for the book name by iterating along the dict_list Books for "name". 
(4.) [Complete] if name does not yield results the user should be told.
(5.) [Complete] display book name and whether it is in stock or not.
"""
    i = 0
    while True:
            try: 
            # 2. implmentation of overall structure, with lots of messy loops
                input_book_name = str(input("Please enter the exact name of a book to see if we have it: "))
                # 1. & 2. expression attempts to convert action to an int object.
            except ValueError:
                print("Try again, specified inputs are string form book names")
                i = i + 0.1
                # floats used to control the loop.
                continue
            else:
                #this else branch covers the logic of searching for the book.
                c = 0
                for x in range(len(Books)):
                # for string iterates through every dictionary in the list.
                    if Books[x]["name"] == input_book_name: 
                        output_book_name = Books[x]["name"]
                        output_book_author = Books[x]["author"]
                        output_book_tcopies = Books[x]["total_copies"]
                        output_book_ocopies = Books[x]["copies_out"]
                        # saved as variables because f strings don't seem to like dict keys. 
                        in_stock = output_book_tcopies - output_book_ocopies
                        print(f"{in_stock}")
                        if in_stock <= 0:
                            return print(f"The library holds {output_book_tcopies} of {output_book_name},\nby {output_book_author}, but all of them are currently on loan.") 
                        elif in_stock > 0:
                            return print(f"The library holds {output_book_tcopies} of {output_book_name},\nby {output_book_author}. We have {in_stock} copies out of {output_book_tcopies} ready for loan.")                          
                    elif Books[x]["name"] != input_book_name:
                        # counting branch to keep track of how many times the id number did not match
                        c = c + 1            
                        if len(Books) == c:
                        # control to activate             
                            return print("-=--=--=--=--=-\nWe do not have this book.\n-=--=--=--=--=-")

def user_withdrawals():
# When get_user_action outputs 2, this module is activated to  
# (1.) [complete] prompts the user to enter a valid id number for a user
# (2.) [complete] authenticate with try except
# (2.5.) [complete] authenticate it is 6 characters long.
# (3.) [complete] iterate through User ids until a user matches.
# (4.) [complete] if user_id does not match, reprompt. 
# (5.) [complete] if User does match, print(Users["borrowed_items"])
# (6.) [complete] 3 try fail system to system shutdown
# variables, a(for iterable), x(for iterable), i(control integer), id_no(input integer), c(another control int)
    i = 0
    while True:
        if i == 0.3:
            # 6. nested if added for shutdown functionality
            print(f"You have failed to correctly input 3 times.\nGo have a rest.")
            action = 0
            # 6. output 0 is linked to shutdown function in main()
            return action
            break
            # 6. command ends the infinite While loop and triggers output       
        else:        
            try: 
            # 2. implmentation of overall structure, with lots of messy loops
                id_no = int(input("Please enter a valid 6 letter id number: "))
                # 3. expression attempts to convert action to an int object.
            except ValueError:
                print("Try again, specified inputs are 6 character long numbers.")
                i = i + 0.1
                continue
            except TypeError:
                print("Try again, specified inputs are 6 character long numbers with no decimals.")
                i = i + 0.1
                continue

            else:
                if (id_no > 999999) | (id_no  <100000):
                    # if branch to ensure id_no is six figures long.
                    print("Try again, specified inputs are 6 character long numbers.")
                    i = i + 1
                    continue
                c = 0
                #this else branch covers the logic of searching for the book.
                for x in range(len(Users)):
                # for string iterates through every dictionary in the list.
                    if Users[x]["id_number"] == id_no: 
                        # held id numbers are referenced against the user input
                        print("-=--=--=--=--=-\nUser has these items on loan:")
                        for a in Users[x]["borrowed_items"]:
                            print(a)
                        return print("-=--=--=--=--=-")                 
                    elif Users[x]["id_number"] != id_no:
                        # counting branch to keep track of how many times the id number did not match
                        c = c + 1            
                        if len(Users) == c:
                            i = i + 1
                            print("Input is not a valid user id")

def book_list():
# [complete] When get_user_action outputs 3, this module is activated to list every book in the library collection
    print("-=--=--=--=--=-\nThe library holds these books ")
    for x in range(len(Books)):
        name = Books[x]["name"]  
        author = Books[x]["author"]
        date = Books[x]["Published"]       
        print(f"{name}, by {author}, published: {date}.")
    print("-=--=--=--=--=-")

def genre_list():
# When get_user_action outputs 4, this module is activated to  
# Classics, Crime, Science_fiction, Non_fiction, Plays_and_poetry
# (1.) [complete]take an input genre from the user
# (2.) [complete] 3 try fail system implemented
# (3.) [complete] try except verification
# (4.) [complete] compare internal variable with all the values for genre using for loops

    i = 0 
    while True: 
        if i == 0.3:
            # 6. nested if added for shutdown functionality 
            print(f"You have failed to correctly input 3 times.\nGo have a rest.")
            action = 0
            # 6. output 0 is linked to shutdown function in main()
            return action
            break
            # 6. command ends the infinite While loop and triggers output       
        else:       
            try:
                input_genre_name = str(input("Please enter the exact genre name to see our selection\nclassics, crime, science_fiction, non_fiction, plays_and_poetry: "))
                print(input_genre_name)
            except ValueError:
                print("Try again, specified inputs are classics, crime, science_fiction, non_fiction, plays_and_poetry:")
                i = i + 0.1
                continue 
            else:
                if (input_genre_name == "classics") or (input_genre_name == "crime") or (input_genre_name == "science_fiction") or (input_genre_name == "non_fiction") or (input_genre_name == "plays_and_poetry"):
                    print(f"-=--=--=--=--=-\nThe library holds these books in the {input_genre_name} genre: ")
                    for x in range(len(Books)):   
                        if Books[x]["genre"] == input_genre_name:   
                            name = Books[x]["name"]
                            author = Books[x]["author"]
                            date = Books[x]["Published"]     
                            print(f"{name}, by {author}, published: {date}")
                    return print("-=--=--=--=--=-")                     
                else: 
                    print("Try again, specified inputs are classics, crime, science_fiction, non_fiction, plays_and_poetry:")
                    i = i + 0.1
                    continue

def book_withdrawals():
# (1.) When get_user_action outputs 5, this module is called to 
# [complete] (2.) Prompt the user for the name of a book to take out 
# [complete] (3.) Prompt the user for id of a library user that is taking out the book.
# [complete] (4.) Authenticate both as preexisting in the system by iterating through Books and Users separately.
# [complete] (5.) If either are not in the program reprompt exit the system user out.
# [complete] (6.) Classic move: trigger shutdown after 3 tries.
# [complete] (7.) Ensure a user cannot take out a book if all copies are on loan
# variables: book_details_list["message string", response_bool, book_index], user_details_list["message string", response_bool, user_index], 
    print("Function chosen: withdrawals") 
    book_details_list = book_verification()
    if book_details_list[1] == True:
        # references response bool, this allows the loops to continue unabated. 
        print(book_details_list[0]) 
        # references message string
        book_index = book_details_list[2]
        # important reference variable when calling values from Books[]
        book_name = Books[book_index]["name"]
        in_stock = Books[book_index]["total_copies"]-Books[book_index]["copies_out"]
        print(f"-=--=--=--=--=-\nThere are currently {in_stock} copies of {book_name} available.\n-=--=--=--=--=-")
        # references the target index of the book as a variable    
    elif book_details_list[1] == False:
        return print(book_details_list[0])
        # the user either didn't input a book the library had, or failed to input correctly
    user_details_list = user_verification()
    if user_details_list[1] == False:
        return print(user_details_list[0])
        # references message string
    elif user_details_list[1] == True:
        # prime execution branch, both bools are true
        # copies_out must = it + 1
        # book name must be appended to Users"borrowed_items"
        user_index = user_details_list[2]
        # important reference variable when calling values from Users[]
        user_id = Users[user_index]["id_number"]
        user_name = Users[user_index]["forename"]
        users_books = Users[user_index]["borrowed_items"]
        # a bunch of variables assigned to list calls for use in end string
        Books[book_index]["copies_out"] = Books[book_index]["copies_out"] + 1 
        in_stock_2 = Books[book_index]["total_copies"]-Books[book_index]["copies_out"]
        Users[user_index]["borrowed_items"].append(book_name)
        # saves user index as a variable
        out_message = f"-=--=--=--=--=-\n User: {user_name}, {user_id} \n Books currently on loan: {users_books} \nNew withdrawal: {book_name} | Copies left: {in_stock_2}\n Enjoy your read!\n-=--=--=--=--=-"
        # end strings to serve as receipt of transaction
        return print(out_message)
       
def book_verification():
    i = 0
    while True:
    # sub module for separate book verification algorithm for use in the Book withdrawals 
    # variables: book_details_list["message string", bool, book_index] 
        # "message string" self explanatory, bool is used to decide what response the book_withdrawals() will have, True means the system has the book, False
        # book_index_number is a record of the index number where the book is recorded
        if i == .3: 
             # 6. nested if added for shutdown functionality
            # 6. output 0 is linked to shutdown function in main()
            return ["You have failed to correctly input 3 times.\nGo have a rest.", False, 0]
        else:
            try: 
            # 2. implmentation of overall structure, with lots of messy loops
                input_book_name = str(input("Please enter the exact name of a book to see if we have it on our system: "))
                # 1. & 2. expression attempts to convert action to an int object.
            except ValueError:
                print("Try again, specified inputs are string form book names")
                i = i + 0.1
                # floats used to control the loop.
                continue
            else:
                #this else branch covers the logic of searching for the book.
                c = 0
                for x in range(len(Books)):
                # for string iterates through every dictionary in the list.
                    if Books[x]["name"] == input_book_name: 
                        
                        output_book_tcopies = Books[x]["total_copies"]
                        output_book_ocopies = Books[x]["copies_out"]
                        # saved as variables because f strings don't seem to like dict keys. 
                        in_stock = output_book_tcopies - output_book_ocopies                       
                        if in_stock <= 0:
                        # not in stock branch
                            return ["The book is not available; all copies are on loan already.", False, x]
                        elif in_stock > 0:
                        # in stock, proceed
                            return ["We have the book on file.", True, x]                          
                    elif Books[x]["name"] != input_book_name:
                        # counting branch to keep track of how many times the id number did not match
                        c = c + 1            
                        if len(Books) == c:
                        # control decision reached that book is not on the system
                            i = i + 1             
                            return ["We do not have this book.", False, x]
                        
def user_verification():
    # a sub module for the verification of the user id entered
    # variables: book_details_list["message string", bool, user_index]
    i = 0 
    while True:
        if i == .3: 
             # 6. nested if added for shutdown functionality
            # 6. output 0 is linked to shutdown function in main()
            return ["You have failed to correctly input 3 times.\nGo have a rest.", False, 0]
        else:
            try: 
            # 2. implmentation of overall structure, with lots of messy loops
                input_id_number = int(input("Please enter the exact 6 letter id-number of a user: "))
                # 1. & 2. expression attempts to convert action to an int object.
            except TypeError:
                print("Try again, specified inputs are 6 letter integers")
                i = i + 0.1
                # floats used to control the loop.
                continue
                #continue used in control to proceed ahead.
            else:
                #this else branch covers the logic of searching for the user id and returning the string.
                if (input_id_number > 999999) | (input_id_number < 100000):
                    # if branch to ensure id_no is six figures long.
                    print("Try again, specified inputs are 6 character long numbers.")
                    i = i + 0.1
                    continue
                c = 0
                for x in range(len(Users)):
                # for string iterates through every dictionary in the list.
                    if Users[x]["id_number"] == input_id_number: 
                            return ["The user is on file.", True, x]                          
                    elif Users[x]["id_number"] != input_id_number:
                        # counting branch to keep track of how many times the id number did not match
                        c = c + 1            
                        if len(Users) == c:
                        # control to activate end branch.
                            i = i + 1             
                            return ["We do not have this id number on file.", False, 0]
                        
def book_returns():
    # When get_user_action outputs 6, this module is called to 
    # (2.) Prompt the user for the name of a book to return 
    # (3.) Prompt the user for id of a library user that is returning the book.
    # (4.) Authenticate both as preexisting in the system by iterating through Books and Users separately.
    # (5.) If either are not in the program reprompt the user to enter that value.
    # (6.) Classic move: trigger shutdown after 3  failed tries.
    # (7.) Ensure a user cannot take return a book if copies_out = 0
    print("Function chosen: returns") 
    book_details_list = book_verification()
    if book_details_list[1] == True:
        # references response bool, this allows the loops to continue unabated. 
        print(book_details_list[0]) 
        # references message string
        book_index = book_details_list[2]
        # important reference variable when calling values from Books[]
        book_name = Books[book_index]["name"]
        in_stock = Books[book_index]["total_copies"]-Books[book_index]["copies_out"]
        print(f"-=--=--=--=--=-\nThere are currently {in_stock} copies of {book_name} available.\n-=--=--=--=--=-")
        # references the target index of the book as a variable    
    elif book_details_list[1] == False:
        return print(book_details_list[0])
        # the user either didn't input a book the library had, or failed to input correctly
    user_details_list = user_verification()
    if user_details_list[1] == False:
        return print(user_details_list[0])
        # references message string
    elif user_details_list[1] == True:
        # prime execution branch, both bools are true
        # copies_out must = it + 1
        # book name must be appended to Users"borrowed_items"
        user_index = user_details_list[2]
        # important reference variable when calling values from Users[]
        user_id = Users[user_index]["id_number"]
        user_name = Users[user_index]["forename"]
        # a bunch of variables assigned to list calls for use in end string
        Books[book_index]["copies_out"] = Books[book_index]["copies_out"] - 1 
        in_stock_2 = Books[book_index]["total_copies"]-Books[book_index]["copies_out"]
        c = 0 
        for x in range(len(Users[user_index]["borrowed_items"])):
            book_on_loan = Users[user_index]["borrowed_items"][x]    
            if book_on_loan == book_name:
                loan_index = x
                print(Books[book_index]["total_copies"])
                print(Books[book_index]["copies_out"])
                break
            elif book_on_loan != book_name:
                c = c + 1 
                print(Users[user_index]["borrowed_items"][x])
                if len(Users[3]["borrowed_items"]) == c:
                        # control to activate end branch.
               
                            return print("The user does not have this book on loan.")
                # control to activate end branch.
        try:
            del Users[user_index]["borrowed_items"][loan_index]
        except ValueError:
            return print("User does not have the book on loan. Aborting...")
        else:
            users_books = Users[user_index]["borrowed_items"]
            # saves user index as a variable
            out_message = f"-=--=--=--=--=-\n User: {user_name}, {user_id} \n Books still on loan: {users_books} \n Returned: {book_name} | Copies available now: {in_stock_2}\nSay: We hope you enjoyed your read, thanks for return it safely!\n-=--=--=--=--=-"
            # end strings to serve as receipt of transaction
            return print(out_message)

def get_user_action():
    # 1. [complete] design this module to get an int value for the action, then output that number back into main(). 
    # 2. [Complete] use try:, except:, else:, finally: loop to except non integer values and prompt the user for a new int input.
    # 3. [complete]close program if user fails after prompting 3 times. Have the output equal zero and use this to trigger a 'shutdown' for the program in main()
    # 4. [Unfinished] add function options strings in the input on line 23
    i = 0
    # 3. i(int) used to provide shutdown branch
    while True:
        if i == 0.3:
            # 3. nested if added for shutdown functionality 
            print(f"You have failed to correctly input 3 times.\nGo have a rest.")
            action = 0
            # 3. output 0 is linked to shutdown function in main()
            break
            # 1. command ends the infinite While loop and triggers output       
        else:
            try: 
            # 2. implmentation of overall structure, with lots of messy loops
                action = int(input("Select which function you'd like to use:\n(0.) Shutdown the system.\n(1.) Search the system for a book.\n(2.) Search the system for the items a user has on loan.\n(3.) List all the titles the library holds.\n(4.) Lists all the titles of one genre the library holds\n(5.) Borrow books\n(6.) Return books\nEnter Input number: "))
                # 1. & 2. expression attempts to convert action to an int object.
            except ValueError:
                print("Try again, specified inputs are (1-6):")
                i = i + 0.1
                # 3. false inputs add to i to trigger shutdown
                continue
            else:
                if 0 <= action <= 6:
                    break
                # successful branch kills the while loop
                else:
                    print("Try again, specified inputs are (0-6):")
                    i = i + 0.1
                    continue
    return action

# The main point of these two dictionaries is to give the program something to do operations on. 
def main():
    # def main() is for executing of the main program. It need to take an input and use that input to initiate a module.
    # [complete] def get_user_action is the central decision making module of the program.
    # [Functional] def 0: def shutdown(): shutdown output from get_user_action command.
    # [Functional] def 1: def book_search(): Check if the library has a book in stock. 
    # [Functional] def 2: def user_withdrawals(): See which books a user has on loan.
    # [Unfinished] def 3: def book_list(): List all books
    # [Unfinished] def 4: def genre_list(): List all genres. Then list all books of a certain genre
    # [Unfinished] def 5: def book_withdrawals(): Take a book out for a user using the name of the book and the user ID.
    # [Unfinished] def 6: def book_returns(): Return a book for a user using the name of the book and the user ID.
    while True:
        command = get_user_action()
        match command:
            case command if (command%-7 == 0):
                print(shutdown())
                break
                # while loop breaks here to end the program. 
            case command if (command%-7 == -6):
                book_search()
                continue
            case command if (command%-7 == -5):
                user_withdrawals()
                continue
            case command if (command%-7 == -4):
                book_list()
                continue
            case command if (command%-7 == -3):
                genre_list()
                continue
            case command if (command%-7 == -2):
                book_withdrawals()
                continue
            case command if (command%-7 == -1):
                book_returns()
                continue
        print("")

main()