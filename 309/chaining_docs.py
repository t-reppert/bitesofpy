from __future__ import annotations

import string
from string import punctuation as punct


EOL_PUNCTUATION = ".!?"


class Document:
    def __init__(self) -> None:
        # it is up to you how to implement this method
        # feel free to alter this method and its parameters to your liking
        self.lines = []
        self._words = set()

    def add_line(self, line: str, index: int = None) -> Document:
        """Add a new line to the document.

        Args:
            line (str): The line,
                expected to end with some kind of punctuation.
            index (int, optional): The place where to add the line into the document.
                If None, the line is added at the end. Defaults to None.

        Returns:
            Document: The changed document with the new line.
        """
        if index is not None:
            self.lines.insert(index, line)
        else:
            self.lines.append(line)
        line = self._remove_punctuation(line)
        word_set = {word.lower() for word in line.split()}
        self._words = self._words.union(word_set)
        return self

    def swap_lines(self, index_one: int, index_two: int) -> Document:
        """Swap two lines.

        Args:
            index_one (int): The first line.
            index_two (int): The second line.

        Returns:
            Document: The changed document with the swapped lines.
        """
        if index_one == index_two:
            return self
        temp = self.lines[index_one]
        self.lines[index_one] = self.lines[index_two]
        self.lines[index_two] = temp
        return self

    def merge_lines(self, indices: list) -> Document:
        """Merge several lines into a single line.

        If indices are not in a row, the merged line is added at the first index.

        Args:
            indices (list): The lines to be merged.

        Returns:
            Document: The changed document with the merged lines.
        """
        if len(indices) == 1:
            return self
        new_line = ''
        index = indices[0]
        prev_value = 0
        for i in indices:
            if i < prev_value:
                index = 1
            prev_value = i
        start = True
        for i in indices:
            if start is True:
                new_line = self.lines[i]
                start = False
            else:
                new_line += f" {self.lines[i]}"
        for i in indices[1:]:
            del self.lines[i]
        self.lines[index] = new_line
        return self

    def add_punctuation(self, punctuation: str, index: int) -> Document:
        """Add punctuation to the end of a sentence.

        Overwrites existing punctuation.

        Args:
            punctuation (str): The punctuation. One of EOL_PUNCTUATION.
            index (int): The line to change.

        Returns:
            Document: The document with the changed line.
        """
        if punctuation in EOL_PUNCTUATION:
            line = self._remove_punctuation(self.lines[index])
            self.lines[index] = line + punctuation
        return self

    def word_count(self) -> int:
        """Return the total number of words in the document."""
        count = 0
        for line in self.lines:
            line = self._remove_punctuation(line)
            l = line.split()
            count += len(l)
        return count

    @property
    def words(self) -> list:
        """Return a list of unique words, sorted and case insensitive."""
        return sorted([word for word in self._words])


    def _remove_punctuation(self, line: str) -> str:
        """Remove punctuation from a line."""
        # you can use this function as helper method for
        # Document.word_count() and Document.words
        # or you can totally ignore it
        for x in punct:
            line = line.replace(x,'')
        return line

    def __len__(self):
        """Return the length of the document (i.e. line count)."""
        return len(self.lines)

    def __str__(self):
        """Return the content of the document as string."""
        return '\n'.join(self.lines)


if __name__ == "__main__":
    # this part is only executed when you run the file and is ignored by the tests
    # you can use this section for debugging and testing
    d = (
        Document()
        .add_line("My first sentence.")
        .add_line("My second sentence.")
        .add_line("Introduction", 0)
        .merge_lines([1, 2])
        .swap_lines(0,1)
    )

    print(d)
    print(len(d))
    print(d.word_count())
    print(d.words)