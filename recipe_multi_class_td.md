
## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

class Diary
Diary where you can:
    Returns a list of all entries.
    Returns how many words are within all entries.
    Returns est. of reading time in minutes of all entries based on 'words p/ min'.
    Returns best entry to read based on how much time they have & their wpm.

class DiaryEntry
    Title and content.
    Returns how many words are in entry (excluding title).
    Returns est. of reading time based on wpm and length of entry (excluding title).
    Returns chunk of content the user can read based on wpm and time available.
        If called again, the following chunk is returned until content is fully read.
        Next call will restart. 


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
### diary.py
"""
test def add() accepts 2 DiaryEntry(title,content) 
def all() returns with list of diary entries
"""
def test_two_diary_entries_return_in_list():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all

"""
Test that diary.count_words() counts all words (4) from multiple diary entries using diary_entry.countwords()
"""
def test_all_words_counted_from_all_entries():
    diary = Diary
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    diary.add("entry_1")
    diary.add("entry_2")
    assert diary.count_words() == 2

"""
Test that diary.reading_time() returns est. reading time of ALL entries based on users reading speed (WPM)
2 wpm, 2 words = 1 minute
"""
def test_total_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.reading_time(4)
    assert diary.reading_time() == 1

"""
Test that diary.reading_time() returns est. reading time of ALL entries based on users reading speed (WPM)
4 wpm, 16 words = 4 minute
"""
def test_total_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    entry_3 = DiaryEntry("Title_3", "Contents_3 has words")
    entry_4 = DiaryEntry("Title_4", "Contents_4 has more more words")
    entry_5 = DiaryEntry("Title_5", "Contents_5 has more more more words")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    diary.add(entry_5)
    diary.reading_time(4)
    assert diary.reading_time() == 4

"""
Test that shows DiaryEntry that can be read based on users reading speed (WPM) and minutes.
2 wpm, 3 minutes = 6 words = entry_4
"""
def test_total_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_1")
    entry_2 = DiaryEntry("Title_2", "Contents_2")
    entry_3 = DiaryEntry("Title_3", "Contents_3 has words")
    entry_4 = DiaryEntry("Title_4", "Contents_4 has more more words")
    entry_5 = DiaryEntry("Title_5", "Contents_5 has more more more words")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    diary.add(entry_5)
    diary.find_best_entry_for_reading_time(2, ):
    assert diary.reading_time() == entry_4


-------------------
### diary_entry.py

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
