from lib.diary import Diary
from lib.diary_entry import DiaryEntry
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
# """
def test_all_words_counted_from_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "Contents_2 Contents_3")
    entry_2 = DiaryEntry("Title_2", "Contents_4 Contents_5")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 4

"""
# class Diary
# def reading_tiME()
# Test to calculate full reading time if user reads all DiaryEntry
# """
def test_calculate_total_reading_time_for_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four")
    entry_2 = DiaryEntry("Title_2", "Five six seven")
    entry_3 = DiaryEntry("Title_3", "Eight nine ten")
    entry_4 = DiaryEntry("Title_4", "Eleven twelve")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    assert diary.reading_time(3) == 4

"""
# class Diary
# def reading_tiMe()
# Test to calculate full reading time if user reads MORE all DiaryEntry
# """
def test_calculate_total_reading_time_for_all_entries_MORE():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four")
    entry_2 = DiaryEntry("Title_2", "Five six seven")
    entry_3 = DiaryEntry("Title_3", "Eight nine ten")
    entry_4 = DiaryEntry("Title_4", "Eleven twelve")
    entry_5 = DiaryEntry("Title_5", "Thirteen")
    entry_6 = DiaryEntry("Title_6", "Fourteen fifteen")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.add(entry_4)
    diary.add(entry_5)
    diary.add(entry_6)
    assert diary.reading_time(5) == 3


"""
Test to find best DiaryEntry to read base on the time available, wpm and length of entry
"""
def test_find_best_diary_entry():
    diary = Diary()
    entry_1 = DiaryEntry("Title_1", "One two three four")
    entry_2 = DiaryEntry("Title_2", "Five six seven eight nine ten")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(1, 5) == entry_1

"""
Test to find best reading time when no entry is eligible
"""
def test_returns_none_when_no_entry_is_readable():
    diary = Diary()
    entry_1 = DiaryEntry("Title_2", "Five six seven eight nine ten")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(1, 5) == None
