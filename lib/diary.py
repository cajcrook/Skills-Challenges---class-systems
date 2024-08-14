# File: lib/diary.py

class Diary:
    def __init__(self):
        self.entries = []


    def add(self, entry):
        self.entries.append(entry)
        # self.add adds all diary entries to to self.entries[] list
    # tested

    def all(self):
        return self.entries
        # returns full [] list of all entries
    # tested
        
    def count_words(self):
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total
    # for each entry in self.entries, each word = 1, add each word to the total
# # # not elegant
    # tested


    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total / wpm
# # # not elegant
        # tested
        

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        time = wpm * minutes
        readable = []
        for entry in self.entries:
            if entry.count_words() <= time:
                readable.append(entry) 
        if readable == []:
            return None
        return readable[0]
        # for i in self.entries:
        #     if len(i) <= time:
        #         return self.entries
                


