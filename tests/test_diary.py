from lib.diary import Diary


"""
Initial list is empyy
"""
def test_initial_list_is_empty():
    diary = Diary()
    assert diary.all() == []

""""
Initial word count is zero
"""
def test_initial_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0