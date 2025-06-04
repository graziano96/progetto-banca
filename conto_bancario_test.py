import unittest

from conto_bancario import ContoBancario


class TestContoBancario(unittest.TestCase):
    def setUp(self):
        self.conto = ContoBancario("Mario Rossi", 100)

    def test_creazione_conto(self):
        self.assertEqual(self.conto.nome, "Mario Rossi")
        self.assertEqual(self.conto.saldo, 100)

    def test_deposita_conto(self):
        self.conto.deposita(50)
        self.assertEqual(self.conto.saldo, 150)

    def test_deposito_negativo(self):
        with self.assertRaises(ValueError):
            self.conto.deposita(-20)

        self.assertEqual(self.conto.saldo, 100)

    def test_prelievo_conto(self):
        self.conto.prelievo(20)
        self.assertEqual(self.conto.saldo, 80)

    def test_prelievo_eccessivo(self):
        with self.assertRaises(ValueError):
            self.conto.prelievo(101)

        self.assertEqual(self.conto.saldo, 100)

    def test_prelievo_negativo(self):
        with self.assertRaises(ValueError):
            self.conto.prelievo(-50)

        self.assertEqual(self.conto.saldo, 100)

    def test_tipo_errato_prelievo(self):
        with self.assertRaises(TypeError):
            self.conto.prelievo([2, 4, 7])

        with self.assertRaises(TypeError):
            self.conto.prelievo("dieci")
            

    def test_str(self):
        self.assertEqual(str(self.conto), "Conto di Mario Rossi - Saldo: €100.00")




if __name__ == '__main__':
    unittest.main()

