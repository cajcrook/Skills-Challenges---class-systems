class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 0

        for char in self.text:
            if not char.isalpha():
                continue
            # if char is not alphanumeric, 'continue onto next char
            counter[char] = counter.get(char,0)+1
            #
            if counter[char] > most_common_count:
            #if counter is more the current count...
                most_common = char
            # then most common letter = char
                most_common_count = counter[char]
            # and most_common_count is the count of char

        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
    