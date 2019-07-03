COL_WIDTH = 20
from itertools import zip_longest as ZL
import textwrap as tw

def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    t_split = text.split('\n\n')
    paragraphs = [ tw.wrap(paragraph,width=COL_WIDTH) for 
                  paragraph in t_split]
    zipped = list(ZL(*paragraphs, fillvalue=' '*20))
    final_text = ''
    for text in zipped:
        for i in range(len(text)):
            final_text += f'{text[i].strip():<20}      '
        final_text += '\n'
    return final_text
    