from Document import Document
from DateTime import DateTime
from Address import Address
from Phone import Phone
import re

# DOCUMENT
###########################################
### CPF - DOCUMENT FOR PERSON
# input = 33277848094

### CNPJ - DOCUMENT FOR COMPANY
input = 76713750000172

output = Document.create_document(input)
print(output)
###########################################


# PHONE
#########################
phone = "552126481234"

output = Phone(phone)
print(output)
#########################


# DATE - TIME
#####################
output = DateTime()
print(output)
#####################


# CEP - DOCUMENT FOR ADDRESS
#####################
cep = 93030060

output = Address(cep)
print(output.get_address())
#####################


# REGULAR EXPRESSIONS
##################################################################################################################
# default = "[0-9][a-z][0-9]" ## one number, one char, one number
# default = "[0-9][a-z]{2}[0-9]" ## one number, two char, one number
# text = "123 1a2 1cc1 aa1 xxx y3r"

### EMAIL

## anything from 5 to 50 characters + @ + char from 3 to 10 + . + anything from 2 to 3 + . + anything from 2 to 3
default = "\w{5,50}@[a-z]{3,10}.\w{2,3}.\w{2,3}"
text = "ajowiejrfd python@gmail.com.br zaozkpdjfdfds hgfjkdkwpe"

output = re.search(default, text) ## return one result
print(output.group())
###################################################################################################################