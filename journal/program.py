import journal as j
import os

def main():
    """
    The journal app!
    """

    # print header
    header()

    # Get user to choose an existing journal or give the name for a new one
    name = choose_journal()

    # Create the journal instance
    journal = j.Journal(name)

    # Enter select loop
    while True:
        choice = input('What do you want to do?  [L]ist, [A]dd or E[x]it? ')
        choice_l = choice.lower()
        if choice_l not in 'lax':
            print('Sorry, I do not understand that choice: "{}".'.format(choice))
        elif choice_l == 'l':
            journal.list_entries()
        elif choice_l == 'a':
            journal.add_entry()
        elif choice_l == 'x':
            print('Saving the "{}" journal ...'.format(name))
            journal.write_to_disk()
            print('... and exiting.  Bye!!')
            break


def header():
    hyphens = '-'*30
    print('{0}\n{1:^30}\n{0}'.format(hyphens, 'PERSONAL JOURNAL APP'))

def choose_journal():
    if os.path.exists(j.Journal.journals_dir):
        print('These are the journals found in the {} directory:'.format(j.Journal.journals_dir))
        with os.scandir(j.Journal.journals_dir) as files:
            for f in files:
                if f.name.endswith('.jrnl') and f.is_file():
                    print(f.name.rstrip('.jrnl'))
        print()
        journal_name = input('Type the name of the journal you wish to open.  '
                             'If it does not exist, a new journal will be started: ')
    else:
        journal_name = input('No journals exist in directory {}.\n'
                             'Please type a journal name to create a new one: '.format(j.Journal.journals_dir))
        print()
    return journal_name

if __name__ == '__main__':
    main()

