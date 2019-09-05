"""
CREATE A CLASS 'PERSON'
representing a roommate
"""
class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.daily_chore = '0'
        self.weekly_chore = '0'
        self.score = 0

"""
GET ROOMMATE INFO
"""
number_of_roommates = int(input('How many roommates are there total? '))
list_of_roommates = []

for number in range(number_of_roommates):
    list_of_roommates.append(
        Person(str(input('What is the name of roommate #' + str(number + 1) + '? ')),
               str('+1' + input(
                   'What is the phone number (format XXX-XXX-XXXX) of roommate #' + str(number + 1) + '? '))))

"""
GET DAILY CHORES
"""
names_of_daily = []

# get number of daily chores, no more than number of roommates:
number_of_daily_chores = int(input('How many daily chores are there total? (max = ' + str(number_of_roommates) + ') '))
for number in range(number_of_daily_chores):
    chore = str(input('What is the name of chore #' + str(number + 1) + '? '))
    names_of_daily.append(chore)

"""
GET WEEKLY CHORES
"""
names_of_weekly = []

# get number of weekly chores, no more than number of roommates:
number_of_weekly_chores = int(input('How many weekly chores are there total? (max = ' + str(number_of_roommates) + ') '))
for number in range(number_of_weekly_chores):
    chore = str(input('What is the name of chore #' + str(number + 1) + '? '))
    names_of_weekly.append(chore)

"""
ASSIGN DAILY/WEEKLY CHORES
"""
def assign_daily_chores(names_of_daily, list_of_roommates, iterator):
    setattr(list_of_roommates[iterator], 'daily_chore', names_of_daily[iterator])
    return list_of_roommates

def assign_weekly_chores(names_of_weekly, list_of_roommates, iterator):
    setattr(list_of_roommates[iterator], 'weekly_chore', names_of_weekly[iterator])
    return list_of_roommates

"""
ROTATE CHORES LIST
"""
def rotate(chores_list):
    return chores_list[1:] + chores_list[:1]

"""
SENDING DAILY/WEEKLY CHORE MESSAGE
"""
def send_daily_message(list_of_roommates, iterator):
    if list_of_roommates[iterator].daily_chore != '0':
        response = input(str(list_of_roommates[iterator].name) + "! You chore today is to: " +
                         str(list_of_roommates[iterator].daily_chore) + ". Have you completed it? (Yes / No) ")
    else:
        response = input(str(list_of_roommates[iterator].name) + "! You have no chores today! :-) (type 'OK' to continue) ")
    return response

def send_weekly_message(list_of_roommates, iterator):
    if list_of_roommates[iterator].weekly_chore != '0':
        response = input(str(list_of_roommates[iterator].name) + "! Your chore this week is to: " +
                         str(list_of_roommates[iterator].weekly_chore) + ". Have you completed it? (Yes / No) ")
    else:
        response = input(str(list_of_roommates[iterator].name) + "! You have no chores this week! :-) (type 'OK' to continue) ")
    return response


"""
REASSIGN DAILY/WEEKLY CHORES
"""
# reassigning daily chores: (should be sent to iter+1)
def reassign_daily_chores(iterator, list_of_roommates):
    if iterator < number_of_roommates-1:
        print(str(list_of_roommates[iterator].name) + " has skipped their chore today. " +
              str(list_of_roommates[iterator + 1].name) + ", you will complete " +
              str(list_of_roommates[iterator].daily_chore) + ".")
        list_of_roommates[iterator + 1].score += 1
        print(str(list_of_roommates[iterator + 1].name) + ", your score is: " + str(list_of_roommates[iterator + 1].score) +
              ". " + str(list_of_roommates[iterator].name) + ", your score is: " + str(list_of_roommates[iterator].score) + ".")
    elif iterator == number_of_roommates-1:
        print(str(list_of_roommates[iterator].name) + " has skipped their chore today. " +
              str(list_of_roommates[0].name) + ", you will complete " +
              str(list_of_roommates[iterator].daily_chore) + ".")
        list_of_roommates[0].score += 1
        print(str(list_of_roommates[0].name) + ", your score is: " + str(list_of_roommates[0].score) +
              ". " + str(list_of_roommates[iterator].name) + ", your score is: " + str(list_of_roommates[iterator].score) + ".")


# reassigning weekly chores: (should be sent to iter+1)
def reassign_weekly_chores(iterator, list_of_roommates):
    if iterator < number_of_roommates - 1:
        print(str(list_of_roommates[iterator].name) + " has skipped their chore today. " +
              str(list_of_roommates[iterator + 1].name) + ", you will complete " +
              str(list_of_roommates[iterator].weekly_chore) + ".")
        list_of_roommates[iterator + 1].score += 1
        print(str(list_of_roommates[iterator + 1].name) + ", your score is: " + str(
            list_of_roommates[iterator + 1].score) + ". " + str(list_of_roommates[iterator].name) +
              ", your score is: " + str(list_of_roommates[iterator].score) + ".")
    elif iterator == number_of_roommates - 1:
        print(str(list_of_roommates[iterator].name) + " has skipped their chore today. " +
              str(list_of_roommates[0].name) + ", you will complete " +
              str(list_of_roommates[iterator].weekly_chore) + ".")
        print(str(list_of_roommates[0].name) + ", your score is: " + str(list_of_roommates[0].score) +
              ". " + str(list_of_roommates[iterator].name) + ", your score is: " + str(list_of_roommates[iterator].score) + ".")

"""
DAILY/WEEKLY RUNTHROUGH
"""
def daily_runthrough(names_of_daily, list_of_roommates, iterator):
    # assign round of daily chores
    assign_daily_chores(names_of_daily, list_of_roommates, iterator)

    # send roommate daily chore
    user_daily_response = send_daily_message(list_of_roommates, iterator).upper()

    # chore response
    if user_daily_response == 'YES':
        list_of_roommates[iterator].score += 1
        print(str(list_of_roommates[iterator].name) + ", your score is: " + str(list_of_roommates[iterator].score) + ".")
    elif user_daily_response == 'NO':
        reassign_daily_chores(iterator, list_of_roommates)

def weekly_runthrough(names_of_weekly, list_of_roommates, iterator):
    # assign round of weekly chores
    assign_weekly_chores(names_of_weekly, list_of_roommates, iterator)

    # send roommate weekly chore
    user_weekly_response = send_weekly_message(list_of_roommates, iterator).upper()

    # chore response
    if user_weekly_response == 'YES':
        list_of_roommates[iterator].score += 1
        print(str(list_of_roommates[iterator].name) + ", your score is: " + str(list_of_roommates[iterator].score) + ".")
    elif user_weekly_response == 'NO':
        reassign_weekly_chores(iterator, list_of_roommates)

"""
DAILY/ WEEKLY PROGRAM
"""
def execute_daily_program(list_of_roommates):
    global names_of_daily

    # assign chores
    ITERATOR = 0
    while ITERATOR < len(list_of_roommates):
        daily_runthrough(names_of_daily, list_of_roommates, ITERATOR)
        ITERATOR += 1

    # rotate chores list
    names_of_daily = rotate(names_of_daily)

def execute_weekly_program(list_of_roommates):
    global names_of_weekly

    ITERATOR = 0
    while ITERATOR < len(list_of_roommates):
        weekly_runthrough(names_of_weekly, list_of_roommates, ITERATOR)
        ITERATOR += 1

    # rotate chores list
    names_of_weekly = rotate(names_of_weekly)

"""
MAIN PROGRAM
"""
program_weeks = int(input("How many weeks will this program go for? "))
for week in range(program_weeks):
    print("\n-------- Chores for week", week + 1, "--------")

    # daily chores
    for day in range(7):
        print("\n[Day " + str(day + 1) + " Chore]")
        execute_daily_program(list_of_roommates)

    # weekly chore
    print("\n[Week " + str(week + 1) + " Chore]")
    execute_weekly_program(list_of_roommates)

print("\nCongratulations! You have completed all of your chores!")
print("\n-------- YOUR FINAL SCORES --------")
for roommate in list_of_roommates:
    print(str(roommate.name) + ": " + str(roommate.score))