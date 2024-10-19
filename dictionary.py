num = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}
n=input("Enter a number :")
for i in n:
    if i in num:
        print(num[i])
    else:
        print(f"unknown character :{i}")