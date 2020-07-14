# import mydiary
#
#
# def main():
#     print_header()
#     run_event_loop() # asking the user for their inputs for different questions
#
#
# def print_header():
#     print('----------------------------')
#     print('         Dear Diary         ')
#     print('----------------------------')
#
#
# def run_event_loop():
#     print("What do you want to do with your journal? ")
#     cmd = 'EMPTY'
#     diary_name = 'default'
#     journal_data = mydiary.load(diary_name) # accessing from mydiary file. returns a new list from mydiary
#
#     while cmd != 'x' and cmd: # while cmd is not x and cmd is empty
#         cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
#
#         cmd = cmd.lower().strip()
#
#         if cmd == 'l':
#             list_entries(journal_data)
#
#         elif cmd == 'a':
#
#             add_entry(journal_data)
#         elif cmd != 'x' and cmd:
#             print("Sorry, '{}' is not valid! ".format(cmd))
#
#     print("Done, bye bye!!!")
#     mydiary.save(diary_name,journal_data)
#
#
# def list_entries(data): # journal_data
#     print("Your journal entries")
#     entries = reversed(data)
#     # for entry in data:
#     #for entry in entries:
#     #for entry in enumerate(entries): # enumerate modifies the collection that has returned. returns a tuple
#     for idx, entry in enumerate(entries): # working with the tuples that have returned
#         #print(entry)
#         print('* [{}], {}'.format(idx + 1,entry)) # items in the tuple are now assigned to the two vars - idx,entry. begins at 1 because of +1
#
#
# def add_entry(data): # journal_data
#     add_text = input("Type your entry, <enter> to exit: ") # ui
#     mydiary.add_entry(add_text,data)
#     #data.append(add_text) # being added to the journal list. working directly with the data
#
#
#
#
#
# if __name__ == '__main__':
#     main()


import mydiary


def main():
    print_header()
    journal_loop()


def print_header():
    print('--------------------------')
    print('      My Diary App        ')
    print('--------------------------')


def journal_loop():  # continuously asks user for inputs
    user_inputs = 'Empty'
    diary_name = 'default'
    my_journal = mydiary.load(diary_name)

    while user_inputs != 'x' and user_inputs:
        user_inputs = input("What would you like to do? [L]ist entries, [A]dd an entry, E[x]it journal: ")
        user_inputs = user_inputs.lower().strip()

        if user_inputs == 'l':
            list_entry(my_journal)

        elif user_inputs == 'a':
            add_entry(my_journal)

        elif user_inputs != 'x' and user_inputs:
            print(" '{}' is not a valid option".format(user_inputs))

    mydiary.save(diary_name, my_journal)


def list_entry(my_data):
    print("Your journal entries: ")
    my_data.reverse()
    for idx, entry in enumerate(my_data):
        print('* [{}], {}'.format(idx + 1, entry))


def add_entry(my_data):
    my_entry = input('Please add your entry: <enter> to exit: ')
    mydiary.add_entry(my_entry, my_data)
    # my_data.append(my_entry)


if __name__ == '__main__':
    main()
