import requests

class Address:

    def __init__(self, document):
        document = str(document)
        if self.validade(document):
            self.cep = document
        else:
            raise ValueError("Document invalid")

    def __str__(self):
        return self.format()

    def validade(self, document):
        if len(document) == 8:
            return True
        else:
            return False

    def format(self):
        format_cep = "{}-{}".format(self.cep[:5], self.cep[5:])
        return format_cep

    def get_address(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)

        request = requests.get(url)
        datas = request.json()

        return (
            datas["uf"],  # state
            datas["localidade"],  # city
            datas["bairro"],  # district
        )



