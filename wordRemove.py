import re
import os
from decoractor import timing


class wordRemove(object):
    def __init__(self, remove_filepath, remove_word, new_filepath):
        self.file_path = remove_filepath
        self.remove_word = remove_word
        self.new_path = new_filepath

    @timing
    def FindWordAndRemove(self):
        if (not os.path.exists(remove_filepath)) or remove_word == "":
            return "path is empty or remove_word is not vaild"

        new_wordline_list = []
        with open(self.file_path, "r") as f:
            wordlines = f.readlines()
            for wordline in wordlines:
                words = re.findall(r"xyz", wordline)
                if len(words) < 1:
                    new_wordline_list.append(wordline)

        with open(self.new_path, "w") as f:
            for wordline in new_wordline_list:
                f.write(wordline)


if __name__ == '__main__':
    remove_filepath = "file1.txt"
    remove_word = "xyz"
    new_filepath = "file2.txt"
    word_remove = wordRemove(remove_filepath, remove_word, new_filepath)
    word_remove.FindWordAndRemove()
