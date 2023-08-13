j = 1j
import math
from cmath import polar, rect

def vector(number: complex):
    """
    Функция поиска вектора комплесного числа
    """
    vector = math.sqrt(number.real**2 + number.imag**2)
    vector = round(vector, 2)
    return round(vector, 2)


def angle(number: complex):
    """Функция поиска угла комплексного числа"""
    vect, ang = polar(number)
    return round(math.degrees(ang), 2)


def indicative(number):
    """Возвращает комплексное число в виде строки в показательной форме. Не пригодно для вычислений"""
    return vector(number), angle(number)


class indic:
    def __init__(self, vect, ang):
        """Функция-конструктор"""
        self.vect = vect
        self.ang = ang

    def division(self, num):
        """Делит комплесное число в показательной форме на другое в формате:
        основание.division(делитель)
        """
        return indic(self.vect / num.vect, self.ang - num.ang)

    def arifm(self):
        """Переводит из показательной формы в арифметическую"""
        return rect(self.vect, math.radians(self.ang))

    def subtraction(self, number):
        """Отнимает комплексное число в показательной форме от комплексного числа в показательной форме"""
        var = self.arifm() - number.arifm()
        return indic(vector(var), angle(var))

    def additional(self, number):
        """Складывает 2 комплексных числа в показательной форме"""
        var = self.arifm() + number.arifm()
        return indic(vector(var), angle(var))

    def multiplication(self, num):
        """Умножает комплесное число в показательной форме на другое в формате:
        множитель0.division(множитель1)
        """
        return indic(self.vect * num.vect, self.ang + num.ang)

    def ReversedMultiplication(self, num):
        """Умножает комплесное число в показательной форме на другое в формате:
        множитель0.division(множитель1) c возведением угла в минус первую степень
        """
        return indic(self.vect * num.vect, -1 * self.ang + num.ang)

    def Squaring(self):
        return indic(self.vect * self.vect, self.ang + self.ang)

    def ReturnVector(self):
        """Возвращает вектор комплексного числа в показательной форме"""
        return float(self.vect)

    def ReturnAngle(self):
        """Возвращает вектор комплексного числа в показательной форме"""
        return float(self.ang)

    def IndicPrint(self):
        vvect = round(self.vect, 2)
        vang = round(self.ang, 2)
        if vang == 0:
            return str(f"{vvect}")
        else:
            return str(f"{vvect}*e^{vang}°")


def FullPower(Ia: indic, Ib: indic, Ic: indic, Ua: indic, Ub: indic, Uc: indic):
    """Высчитывает полную мощность трехфазной цепи из заданных трех токов и напряжений"""
    global var0, var1, var2, var3
    var0 = Ia.ReversedMultiplication(Ua)
    var1 = Ib.ReversedMultiplication(Ub)
    var2 = Ic.ReversedMultiplication(Uc)
    var3 = var0.arifm() + var1.arifm() + var2.arifm()
    return var3


def ActivePower(Ia: indic, Ib: indic, Ic: indic, Za: complex, Zb: complex, Zc: complex):
    """Из комплексных токов в показательной форме и сопротивлений в арифметической форме возвращает"""
    global var01, var11, var21, var31
    if Za.real < 0.05 and Za.real > -0.05:
        var01 = 0
    else:
        var01 = Za.real * Ia.ReturnVector() ** 2
    if Zb.real < 0.05 and Zb.real > -0.05:
        var11 = 0
    else:
        var11 = Zb.real * Ib.ReturnVector() ** 2
    if Zc.real < 0.05 and Zc.real > -0.05:
        var21 = 0
    else:
        var21 = Zc.real * Ic.ReturnVector() ** 2

    var31 = var01 + var11 + var21
    return var31


def ReactivePower(
    Ia: indic, Ib: indic, Ic: indic, Za: complex, Zb: complex, Zc: complex
):
    global var02, var12, var22, var32
    if Za.imag < 0.05 and Za.imag > -0.05:
        var02 = 0
    else:
        var02 = Za.imag * Ia.ReturnVector() ** 2
    if Zb.imag < 0.05 and Zb.imag > -0.05:
        var12 = 0
    else:
        var12 = Zb.imag * Ib.ReturnVector() ** 2
    if Zc.imag < 0.05 and Zc.imag > -0.05:
        var22 = 0
    else:
        var22 = Zc.imag * Ic.ReturnVector() ** 2

    var32 = var02 + var12 + var22
    return var32


def nonsuited_sinus(U, Z:complex, u=0):

    res = 'Если емкостные и индуктивные сопротивления заданы не в "рабочих значениях(в основном испульзуются значения от 1 до 10) а в мГн или мкфФ воспользуйтесь функцией перевода индуктивности для катушек и функцией перевода емкостей для конденсатора иначе введите значения так как они заданы\n\n'
    #Сюда надо запилить ссылки так же на переводчики
    #Полное сопротивление цепи можно просто сложив сопротивление всех резисторов и добавив к ним реактивное сопротивления, для рассчета которого нужно сложить сопротивления катушек и конденсаторов(сопротивление конденсаторов с минусом)
    

    U = indic(U, u)
    Z1 = indic(vector(Z), angle(Z))
    I1 = U.division(Z1)
    I1.ang = -I1.ang
    res += f'I = U / Z = {U.IndicPrint()} / {Z} = {U.IndicPrint()} / {Z1.IndicPrint()} = {(U.division(Z1)).IndicPrint()}\n\n'
    var = (U.division(Z1))
    var1 = U.multiplication(I1).arifm()
    res += f'S = U * I* = {U.IndicPrint()} * {I1.IndicPrint()} = {round(var1.real, 1)} + {round(var1.imag, 1)}j\n'
    res += f'P = (Cумма всех ваших резисторов, по типу R1 + R2 ...) * I^2 = {round(Z.real)} * {round(var.vect, 2)}^2 = {round(Z.real)} {round(var.vect ** 2, 2)} = {round((Z.real * var.vect ** 2), 2)}\n'
    res += f'Q = (Cумма всех ваших реактивных состовляющий по типу L1 - C1 + L2... (Напоминание:Конденсаторы с минусов, катушки с плюсом) * I^2 = {round(Z.imag)} * {round(var.vect, 2)}^2 = {round(Z.imag)} {round(var.vect ** 2, 2)} = {round(Z.imag * var.vect ** 2, 2)}'

    return res

def translation_for_inductance(inductance):
    """Переводит заданное сопротивление в рабочую форму(Катушка)
    сопротивление должно быть задано в мГн"""
    return (round(((314 * inductance)/1000), 2))

def translation_for_capatitance(capatitance):
    """Переводит заданное сопротивление в рабочую форму(Конденсатор)
    сопротивление должно быть задано в мкФ"""
    return (round(((1 / (capatitance * 314)) * 1000000), 2))






