import unittest
from src.chatGPT.rpn import eval_rpn, RPNError


class TestRPN(unittest.TestCase):

    # ----- operaciones básicas -----

    def test_suma(self):
        self.assertEqual(eval_rpn("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(eval_rpn("5 1 2 + 4 * + 3 -"), 14)

    def test_multiplicacion(self):
        self.assertEqual(eval_rpn("2 3 4 * +"), 14)

    def test_floats(self):
        self.assertEqual(eval_rpn("2.5 2 *"), 5)

    def test_negativos(self):
        self.assertEqual(eval_rpn("-3 4 +"), 1)

    # ----- funciones -----

    def test_sqrt(self):
        self.assertEqual(eval_rpn("9 sqrt"), 3)

    def test_log(self):
        self.assertEqual(eval_rpn("100 log"), 2)

    def test_ln(self):
        result = eval_rpn("1 ln")
        self.assertAlmostEqual(result, 0)

    def test_ex(self):
        self.assertAlmostEqual(eval_rpn("1 ex"), 2.71828, places=3)

    # ----- trigonometría -----

    def test_sin(self):
        self.assertAlmostEqual(eval_rpn("90 sin"), 1, places=3)

    def test_cos(self):
        self.assertAlmostEqual(eval_rpn("0 cos"), 1, places=3)

    # ----- comandos de pila -----

    def test_dup(self):
        self.assertEqual(eval_rpn("5 dup *"), 25)

    def test_swap(self):
        self.assertEqual(eval_rpn("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(eval_rpn("3 4 drop"), 3)

    # ----- constantes -----

    def test_pi(self):
        import math
        self.assertAlmostEqual(eval_rpn("p"), math.pi)

    def test_e(self):
        import math
        self.assertAlmostEqual(eval_rpn("e"), math.e)

    # ----- errores -----

    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 4 foo")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            eval_rpn("+")

    def test_pila_final_incorrecta(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 4")

    def test_chs(self):
        self.assertEqual(eval_rpn("5 chs"), -5)


    def test_clear(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 4 clear")


    def test_10x(self):
        self.assertEqual(eval_rpn("2 10x"), 100)


    def test_reciproco(self):
        self.assertEqual(eval_rpn("4 1/x"), 0.25)


    def test_potencia(self):
        self.assertEqual(eval_rpn("2 3 yx"), 8)


    def test_asin(self):
        self.assertAlmostEqual(eval_rpn("1 asin"), 90, places=3)


    def test_acos(self):
        self.assertAlmostEqual(eval_rpn("1 acos"), 0, places=3)


    def test_atg(self):
        self.assertAlmostEqual(eval_rpn("1 atg"), 45, places=3)


    def test_memoria_sto_rcl(self):
        self.assertEqual(eval_rpn("5 0 sto 0 rcl"), 5)


if __name__ == "__main__":
    unittest.main()