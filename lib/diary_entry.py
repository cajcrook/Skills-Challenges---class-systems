# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.read_so_far = 0
    # tested

    def count_words(self):
        return len(self.contents.split())
    #tested

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        word_count = self.count_words()
        time = word_count / wpm
        return time
    # tested
        
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far +words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return " ".join(chunk_words)
    # tested

