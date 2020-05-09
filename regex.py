""" /hello/ searches for string hello
\d indicates digit
\w indicates word
. indicates any character
+ indicates one or more occurences of precedint pattern
* indicates zero or more
? indicates zero or one """

import re
five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'

five_digit_expression = r'\d{5}'
print(re.search(five_digit_expression, five_digit_zip))
print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))