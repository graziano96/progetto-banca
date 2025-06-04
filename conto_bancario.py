
class ContoBancario:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def __str__(self):
        return f"Conto di {self.nome} - Saldo: €{self.saldo:.2f}"

    def deposita(self, importo):

        if importo <= 0:
            raise ValueError("L'importo deve essere positivo!")

        self.saldo += importo

    def prelievo(self, importo):
        if not isinstance(importo, (int, float)):
            raise TypeError("Tipo non supportato!")

        if importo < 0:
            raise ValueError("L'importo non può essere negativo!")

        elif self.saldo >= importo:
            self.saldo -= importo
        else:
            raise ValueError("Non hai abbastanza soldi!")

if __name__ == "__main__":

    c = ContoBancario("Luigi Neri", 1000)
    c.deposita(10)
    print(c)





