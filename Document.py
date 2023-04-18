from validate_docbr import CPF
from validate_docbr import CNPJ


class Document:

    @staticmethod
    def create_document(document):
        document = str(document)
        if len(document) == 11:
            return Cpf(document)
        elif len(document) == 14:
            return Cnpj(document)
        else:
            raise ValueError("Document length invalid")


# CPF - DOCUMENT FOR PERSON
class Cpf:
    def __init__(self, document):
        if self.validate(document):
            self.cpf = document
        else:
            raise ValueError("CPF invalid")

    def __str__(self):
        return self.format()

    def validate(self, document):
        cpf = CPF()
        return cpf.validate(document)

    def format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)


# CNPJ - DOCUMENT FOR COMPANY
class Cnpj:
    def __init__(self, document):
        if self.validate(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ invalid")

    def __str__(self):
        return self.format()

    def validate(self, document):
        cnpj = CNPJ()
        return cnpj.validate(document)

    def format(self):
        cnpj = CNPJ()
        return cnpj.mask(self.cnpj)
