import os


def load(name):  # name of journal
    # todo: populate from file if it exists
    """
    This method creates and loads a new journal entry

    :param name: The base name of the journal to load
    :return: a new data structure populated with the file data
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as file_input:
            for entry in file_input.readlines():
                data.append(entry.rstrip())  # added a journal entry at the end
                # print('would load:' + entry.rstrip())
    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print('......saving to: {}'.format(filename))
    # file = open(filename, 'w')  # 'w' - write
    with open(filename, 'w') as file:  # context manager

        for entry in journal_data:
            file.write(entry + '\n')

    # file.close() file closes after the above block of code because of the context manager


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'Journals', name + '.jrl'))
    return filename


def add_entries(text, journal_data):
    journal_data.append(text)
