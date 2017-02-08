#! python3
# Concatenate different clipboard items for easy pasting
# requirements: pip install pyperclip

import pyperclip

entry = []
n = int(input('Enter the number of entries to concatenate from clipboard: '))

for i in range(n):
    input('Copy new entry and press enter\n')
    # Read from clipboard and it to list named 'entry'
    entry.append(pyperclip.paste())

text = '\n'.join(entry)
# Write it back to the clipboard
pyperclip.copy(text)
print('All the entries have been copied to your clip board')
