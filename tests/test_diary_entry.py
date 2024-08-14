from lib.diary_entry import DiaryEntry

""""
When I initialise with title and contenets
I get back the title and content
"""
def test_entry_to_return_title_content():
    diary_entry = DiaryEntry("My_Title", "My_Content")
    assert diary_entry.title == "My_Title"
    assert diary_entry.contents == "My_Content"

"""
When I initialise with a 5 word content
then @count_words should reture count of 5
"""
def test_count_words_correctly_counts_words_in_contents():
    diary_entry = DiaryEntry("My_Title", "One two three four five")
    assert diary_entry.count_words() == 5

"""
Reading time returns how long it will take me to read DiaryEntry based on inputted WPM
"""
def test_reading_time_output_is_calculated_from_wpm_and_word_count():
    diary_entry = DiaryEntry("My_Title", "One two three four five six")
    assert diary_entry.reading_time(2) == 3

"""
Reading time returns how long it will take me to read larger DiaryEntry based on inputted WPM
"""
def test_reading_time_output_is_calculated_from_wpm_and_large_word_count():
    diary_entry = DiaryEntry("My_Title", "One two three four five six seven eight nine ten")
    assert diary_entry.reading_time(2.5) == 4


"""
@DiaryEntry
def reading_chunk()
Return chunk of contents based on critera (wpm * minutes), if called again, it will return the next chunk
"""
def test_return_reading_chunk_based_on_criteria():
    diary_entry = DiaryEntry("My_Title", "One two three four five six seven eight nine ten")
    assert diary_entry.reading_chunk(2,3) == "One two three four five six"
    assert diary_entry.reading_chunk(2,3) == "seven eight nine ten"

