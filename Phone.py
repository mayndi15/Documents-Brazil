import re


class Phone:

    def __init__(self, phone):
        phone = str(phone)

        if self.validate(phone):
            self.number = phone
        else:
            raise ValueError("Phone invalid")

    def __str__(self):
        return self.format()

    def validate(self, phone):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        validate = re.findall(default, phone)

        if validate:
            return True
        else:
            return False

    def format(self):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        format = re.search(default, self.number)

        format_phone = "+{}({}){}-{}".format(
            format.group(1),
            format.group(2),
            format.group(3),
            format.group(4))

        return format_phone
