# List, add, select journal, exit
import os.path


class Journal:
    """
    Journal class.  Methods to list, add and write entries to disk

    :param name
    Reads from and writes to __file__/journals/"name".jrnl
    """

    def __init__(self, name):
        self.name = name
        cwd = os.path.cwd()
        self.path = os.path.join(cwd, name, '.jrnl')
        if os.path.isfile(self.path):
            with open(journal_path, 'rt') as file:
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
                print('{}:  {}'.format(index + 1, entry))
            print()
        else:
            print('The "{}" journal does not yet have any entries.'.format(self.name))

    def add_entry(self):
        entry = input('New journal entry: ')
        self.entries.append(entry)
        # Journal is only written to disk on exit

    def write_to_disk(self):

        pass

