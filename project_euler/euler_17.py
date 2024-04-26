# =================================
# Euler Project. Problem 16
# =================================

"""
The numbers 1 to 5 written out in words are One, Two, Three, Four and Five. First character of each word will be capital letter for example: 104 382 426 112 is
One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty Six Thousand One Hundred Twelve.

Given a number, you have to write it in words.

Input format
------------
The first line contains an integer T i.e. the number of test cases.

Next T lines will contain an integer N.

Constraints
-----------
1 <= T <= 10
0 <= N <= 10^12

Output format
-------------
Print the values corresponding to each test case.
"""


diferents_dict = {
    '0': '',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten',
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'Fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'Nineteen'
}

decens = {
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Forty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety'
}

def triad_numeral(triad:str)->str:

    """
    Function to convert to words a number below 1000.

    Parameter
    ---------
    triad: str
        number between 0 and 999 inclusive, casted as string.

    Return
    ------
    str
    """

    if len(triad)==1: triad = '00'+triad        
    if len(triad)==2: triad = '0'+triad
    
    numeral = ''
    
    if triad[0] != '0':
        numeral+= (diferents_dict[triad[0]] + ' Hundred ')
    if triad[1] not in ['0', '1']:
        numeral+= (decens[triad[1]] + ' ' + diferents_dict[triad[2]])
    elif triad[1] == '0':
        numeral+=diferents_dict[triad[2]]
    else:
        numeral+=diferents_dict[triad[1:]]
    return numeral.strip()

def number_to_words(number:int)->str:

    """
    Function to convert a number to words

    Parameter
    ---------
    number: int
        integer with 13 digits at most

    Return
    ------
    str
    """

    nmbr_str = str(number)
    text = ''

    if number==0:
        return 'Zero'
    
    if len(nmbr_str)>12:
        word = triad_numeral(nmbr_str[:-12])
        if word!='':
            text += (word + ' Trillion ')
        nmbr_str = nmbr_str[-12:]
    if len(nmbr_str)>9:
        word = triad_numeral(nmbr_str[:-9])
        if word!='':
            text += (word + ' Billion ')
        nmbr_str = nmbr_str[-9:]
    if len(nmbr_str)>6:
        word = triad_numeral(nmbr_str[:-6])
        if word!='':
            text += (word + ' Million ')
        nmbr_str = nmbr_str[-6:]
    if len(nmbr_str)>3:
        word = triad_numeral(nmbr_str[:-3])
        if word !='':
            text += (word + ' Thousand ')
        nmbr_str = nmbr_str[-3:]
    
    text += triad_numeral(nmbr_str)

    return text.strip().replace('  ', ' ')
