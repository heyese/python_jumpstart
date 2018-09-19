# List, add, select journal, exit
import os.path


class Journal:
    """
    Journal class.  Methods to list, add and write entries to disk

    :param name
    Reads from and writes to __file__/journals/"name".jrnl
    """

    journals_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'journals')

    def __init__(self, name):
        self.name = name
        self.path = os.path.join(self.journals_dir, name + '.jrnl')
        if os.path.isfile(self.path):
            with open(self.path, 'rt') as file:
                self.entries = file.readlines()
        else:
            self.entries = []

    def list_entries(self):
        # Print entries in reverse order
        n = len(self.entries)
        if n:
            print('The {} entries for the "{}" journal:\n'.format(n, self.name))
            for index, entry in enumerate(self.entries[::-1]):
                # Index starts at 0
                print('{}:  {}'.format(index + 1, entry.rstrip('\n')))
            print()
        else:
            print('The "{}" journal does not yet have any entries.\n'.format(self.name))

    def add_entry(self):
        entry = input('New journal entry: ')
        self.entries.append(entry)
        # Journal is only written to disk on exit
        print()

    def write_to_disk(self):
        if not os.path.isdir(self.journals_dir):
            os.mkdir(self.journals_dir)
        with open(self.path, 'wt') as file:
            for entry in self.entries:
                # want to ensure only one newline on each entry
                entry = entry.rstrip()
                file.write(entry+'\n')

