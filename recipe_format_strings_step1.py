# input data
data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]
# PRINT THE HEADER FOR REFERENCES
print('REVENUE | PROFIT | PERCENT')

# USING A TEMPLATE TO ALIGN AND DISPLAYS THE DATA IN THE PROPER FORMAT.
TEMPLATE = '{revenue:>7} | {profit:>+6} | {percent:>7.2%}'

# PRINT THE DATA ROWS
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit/revenue)
    print(row)

# ---------------------------------------------------------------------------- #
#                             Manipulating strings                             #
# ---------------------------------------------------------------------------- #
INPUT_TEXT = '''
AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
WITH THE OBJECTIVES FOR THE YEAR. 
THE MAIN DRIVER OF THE SALES HAS BEEN THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING 
DEPARTMENT.
OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH THE BOARD
CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS SATISFACTORY
AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD EXPECTS
AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
'''
# split it into individual words
words = INPUT_TEXT.split()

# replace any numerical digits with an 'X' character
redacted = [''.join('X' if character.isdigit() else character for character in word) for word in words]
# transform the text into pure ASCII.
ascii_text = [word.encode('ascii', errors='replace').decode('ascii') for word in redacted]
# group the words into 80 character lines
newlines = [word + '\n' if word.endswith('.') else word for word in ascii_text]
LINE_SIZE = 80
lines = []
line = ''
for word in newlines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ''
    line = f'{line} {word}'
# format all of the lines as title and join them as a single piece of text
lines = [line.title() for line in lines]
result = '\n'.join(lines)
print(result)



