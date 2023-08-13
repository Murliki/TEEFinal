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




def triangle(U, Zab: complex, Zbc: complex, Zca: complex):
    """
    Входные данные:
    U - напряжение схемы
    Za, Zb, Zc(комплексные числа в арифтической форме)
    Из заданных U, Zab, Zbc, Zca возвращает полный ход решения задачи
    "Трехфазное симметричное сопротивление

    """

    res = "Рассчетной симметричной нагрузки\n"  # Переменная определяющая полный вывод решения задачи

    Uab = indic(U, 0)
    Ubc = indic(U, -120)
    Uca = indic(U, 120)

    res += f"Uab = {U}e^0°\nUbc = {U}e^-120°\nUca = {U}e^120°\n\n"

    varAB = (vector(Zab), angle(Zab))
    varBC = (vector(Zbc), angle(Zbc))
    varCA = (vector(Zca), angle(Zca))
    Zab1 = indic(varAB[0], round(varAB[1], 2))
    Zbc1 = indic(varBC[0], round(varBC[1], 2))
    Zca1 = indic(varCA[0], round(varCA[1], 2))

    res += (
        "Zab = "
        + str(Zab1.IndicPrint())
        + "\nZbc = "
        + str(Zbc1.IndicPrint())
        + "\nZca = "
        + str(Zca1.IndicPrint() + "\n\n")
    )

    Iab = Uab.division(Zab1)
    Ibc = Ubc.division(Zbc1)
    Ica = Uca.division(Zca1)

    res += (
        "Iab = Uab / Iab = {} / {} = ".format(Uab.IndicPrint(), Zab1.IndicPrint())
        + str(Iab.IndicPrint())
        + "\nIbc = Ubc / Ibc = {} / {}".format(Ubc.IndicPrint(), Zbc1.IndicPrint())
        + str(Ibc.IndicPrint())
        + "\nIca = Uca / Ica = {} / {}".format(Uca.IndicPrint(), Zca1.IndicPrint())
        + str(Ica.IndicPrint() + "\n\n")
    )

    Ia = Iab.subtraction(Ica)
    Ib = Ibc.subtraction(Iab)
    Ic = Ica.subtraction(Ibc)

    res += (
        "Ia = Iab - Ica = {} - {} = ".format(Iab.IndicPrint(), Ica.IndicPrint())
        + str(Ia.IndicPrint())
        + "\nIb = Ibc - Iab = {} - {} = ".format(Ibc.IndicPrint(), Iab.IndicPrint())
        + str(Ib.IndicPrint())
        + "\nIc = Ica - Ibc = {} - {} = ".format(Ica.IndicPrint(), Ibc.IndicPrint())
        + str(Ic.IndicPrint() + "\n\n")
    )

    FP = FullPower(Iab, Ibc, Ica, Uab, Ubc, Uca)

    AP = ActivePower(Iab, Ibc, Ica, Zab, Zbc, Zca)
    RP = ReactivePower(Iab, Ibc, Ica, Zab, Zbc, Zca)

    var = (
        (Iab.ReversedMultiplication(Uab)).arifm()
        + (Ibc.ReversedMultiplication(Ubc)).arifm()
        + (Ica.ReversedMultiplication(Uca)).arifm()
    )

    Uab = Uab.IndicPrint()
    Ubc = Ubc.IndicPrint()
    Uca = Uca.IndicPrint()

    res += f"S = Uab * Iab* + Ubc * Ibc* + Uca * Ica* = {Uab} * {vector(Iab.arifm())}^e{-angle(Iab.arifm())} + {Ubc} * {vector(Ibc.arifm())}^e{-angle(Ibc.arifm())}+ {Uca} * {vector(Ica.arifm())}^e{-angle(Ica.arifm())} = "

    res += (
        f"{vector(var)}*e^{angle(var)} = {round(FP.real, 2)} + {round(FP.imag, 2)}j\n"
    )
    res += f"P = {round(AP, 2)}\n"
    res += f"Q = {round(RP, 2)}"

    return res

def StarWithNeutral(U, Za: complex, Zb: complex, Zc: complex):
    """
    Входные данные:
    U - напряжение схемы
    Za, Zb, Zc(комплексные числа в арифтической форме)
    Из заданных U, Zab, Zbc, Zca возвращает полный ход решения задачи
    "Трехфазное симметричное сопротивление

    """

    res = "Рассчетной звездообразной нагрузки\n"  # Переменная определяющая полный вывод решения задачи

    Ua = indic(round((U / 1.732), 2), 0)
    Ub = indic(round((U / 1.732), 2), -120)
    Uc = indic(round((U / 1.732), 2), 120)

    res += f"Ua = {U / 1.732}e^0°\nUb = {U / 1.732}e^-120°\nUc = {U / 1.732}e^120°\n\n"

    varA = (vector(Za), angle(Za))
    varB = (vector(Zb), angle(Zb))
    varC = (vector(Zc), angle(Zc))
    Za1 = indic(varA[0], round(varA[1], 2))
    Zb1 = indic(varB[0], round(varB[1], 2))
    Zc1 = indic(varC[0], round(varC[1], 2))

    res += (
        "Za = "
        + str(Za1.IndicPrint())
        + "\nZb = "
        + str(Zb1.IndicPrint())
        + "\nZc = "
        + str(Zc1.IndicPrint() + "\n\n")
    )

    Ia = Ua.division(Za1)
    Ib = Ub.division(Zb1)
    Ic = Uc.division(Zc1)

    res += (
        "Ia = Ia / Za = {} / {} = ".format(Ua.IndicPrint(), Za1.IndicPrint())
        + str(Ia.IndicPrint())
        + "\nIb = Ib / Zb = {} / {} = ".format(Ub.IndicPrint(), Zb1.IndicPrint())
        + str(Ib.IndicPrint())
        + "\nIc = Ic / Zc = {} / {} = ".format(Uc.IndicPrint(), Zc1.IndicPrint())
        + str(Ic.IndicPrint() + "\n\n")
    )

    In = Ia.arifm() + Ib.arifm() + Ic.arifm()

    res += (
        f"In = Ia + Ib + Ic = {Ia.IndicPrint()} + {Ib.IndicPrint()} + {Ic.IndicPrint()} = {(indic(vector(In), angle(In))).IndicPrint()}"
        
        + "\n\n"
    )

    FP = FullPower(Ia, Ib, Ic, Ua, Ub, Uc)
    AP = ActivePower(Ia, Ib, Ic, Za, Zb, Zc)
    RP = ReactivePower(Ia, Ib, Ic, Za, Zb, Zc)


    var = (
        (Ia.ReversedMultiplication(Ua)).arifm()
        + (Ib.ReversedMultiplication(Ub)).arifm()
        + (Ic.ReversedMultiplication(Uc)).arifm()
    )

    Ua = Ua.IndicPrint()
    Ub = Ub.IndicPrint()
    Uc = Uc.IndicPrint()

    res += f"S = Ua * Ia* + Ub * Ib* + Uc * Ic* = {Ua} * {vector(Ia.arifm())}^e{-angle(Ia.arifm())} + {Ub} * {vector(Ib.arifm())}^e{-angle(Ib.arifm())}+ {Uc} * {vector(Ic.arifm())}^e{-angle(Ic.arifm())} = "

    res += (
        f"{vector(var)}*e^{angle(var)} = {round(FP.real, 2)} + {round(FP.imag, 2)}j\n"
    )
    res += f"P = {round(AP, 2)}\n"
    res += f"Q = {round(RP, 2)}"

    return res

def star_without_neutral(U, Za: complex, Zb: complex, Zc: complex):
    """Из заданного входного напряжения и комплексных сопротивлей возвращает полный ход решения
    задачи 'Звезда с обрывом нейтрали'"""
    res = "Рассчетной звездообразной нагрузки c обрывом нейтрали\n"  # Переменная определяющая полный вывод решения задачи

    Ua = indic(round((U / 1.732), 2), 0)
    Ub = indic(round((U / 1.732), 2), -120)
    Uc = indic(round((U / 1.732), 2), 120)

    res += f"Ua = {round((U / 1.732), 2)}e^0°\nUb = {U / 1.732}e^-120°\nUc = {U / 1.732}e^120°\n\n"

    varA = (vector(Za), angle(Za))
    varB = (vector(Zb), angle(Zb))
    varC = (vector(Zc), angle(Zc))
    Za1 = indic(varA[0], round(varA[1], 2))
    Zb1 = indic(varB[0], round(varB[1], 2))
    Zc1 = indic(varC[0], round(varC[1], 2))

    res += (
        "Za = "
        + str(Za1.IndicPrint())
        + "\nZb = "
        + str(Zb1.IndicPrint())
        + "\nZc = "
        + str(Zc1.IndicPrint() + "\n\n")
    )

    Ia = Ua.division(Za1)
    Ib = Ub.division(Zb1)
    Ic = Uc.division(Zc1)

    res += (
        "Ia = Ia / Za = {} / {} = ".format(Ua.IndicPrint(), Za1.IndicPrint())
        + str(Ia.IndicPrint())
        + "\nIb = Ib / Zb = {} / {} = ".format(Ub.IndicPrint(), Zb1.IndicPrint())
        + str(Ib.IndicPrint())
        + "\nIc = Ic / Zc = {} / {} = ".format(Uc.IndicPrint(), Zc1.IndicPrint())
        + str(Ic.IndicPrint() + "\n\n")
    )
    In = Ia.arifm() + Ib.arifm()
    In1 = (indic(vector(In), angle(In)))
    Zn = (1 / Zc1.arifm() + 1 / Zb1.arifm() + 1 / Za1.arifm())
    res += f"Un = (Ia + Ib + Ic) / (1/Za + 1/Zb + 1/Zc) = ({Ia.IndicPrint()} + {Ib.IndicPrint()} + {Ic.IndicPrint()}) / (1/{Za1.IndicPrint()} + 1/{Zb1.IndicPrint()} + 1/{Zc1.IndicPrint()}) = ({In1.IndicPrint()} + {Ic.IndicPrint()}) / ({(indic(vector(1 / Za), angle(1 / Za))).IndicPrint()} + {(indic(vector(1 / Zb), angle(1 / Zb))).IndicPrint()} + {(indic(vector(1 / Zc), angle(1 / Zc))).IndicPrint()}) = {(indic(vector(In1.arifm() + Ic.arifm()), angle(In1.arifm() + Ic.arifm()))).IndicPrint()} / {indic(vector(Zn), angle(Zn)).IndicPrint()} = {(indic(vector(In1.arifm() + Ic.arifm()), angle(In1.arifm() + Ic.arifm()))).division(indic(vector(Zn), angle(Zn))).IndicPrint()}\n\n"
    
    Un = (indic(vector(In1.arifm() + Ic.arifm()), angle(In1.arifm() + Ic.arifm()))).division(indic(vector(Zn), angle(Zn)))
    Ua1 = indic(vector(Ua.arifm() - Un.arifm()), angle(Ua.arifm() - Un.arifm()))
    Ub1 = indic(vector(Ub.arifm() - Un.arifm()), angle(Ub.arifm() - Un.arifm()))
    Uc1 = indic(vector(Uc.arifm() - Un.arifm()), angle(Uc.arifm() - Un.arifm()))

    res += f"U'a = Ua - Un = {Ua.IndicPrint()} - {Un.IndicPrint()} = {Ua1.IndicPrint()}\n"
    res += f"U'b = Ub - Un = {Ub.IndicPrint()} - {Un.IndicPrint()} = {Ub1.IndicPrint()}\n"
    res += f"U'c = Uc - Un = {Uc.IndicPrint()} - {Un.IndicPrint()} = {Uc1.IndicPrint()}\n\n"

    Ia1 = Ua1.division(Za1)
    Ib1 = Ub1.division(Zb1)
    Ic1 = Uc1.division(Zc1)

    res += f"I'a = U'a / Za = {Ua1.IndicPrint()} / {Za1.IndicPrint()} = {Ia1.IndicPrint()}\n"
    res += f"I'b = U'b / Zb = {Ub1.IndicPrint()} / {Zb1.IndicPrint()} = {Ib1.IndicPrint()}\n"
    res += f"I'c = U'c / Zc = {Uc1.IndicPrint()} / {Zc1.IndicPrint()} = {Ic1.IndicPrint()}\n\n"

    TrueIn = Ia1.arifm() + Ib1.arifm() + Ic1.arifm()
    TrueInTrue = indic(vector(TrueIn), angle(TrueIn))
    res += f"In = I'a + I'b + I'c = {Ia1.IndicPrint()} + {Ib1.IndicPrint()} + {Ic1.IndicPrint()} = {(indic(vector(Ia1.arifm() + Ib1.arifm()), angle(Ia1.arifm() + Ib1.arifm()))).IndicPrint()} + {Ic1.IndicPrint()} = {TrueInTrue.IndicPrint()} = {round((TrueInTrue.arifm()).real, 2)} + {round((TrueInTrue.arifm()).imag, 2)}j\n\n"

    FP = FullPower(Ia1, Ib1, Ic1, Ua1, Ub1, Uc1)
    AP = ActivePower(Ia1, Ib1, Ic1, Za, Zb, Zc)
    RP = ReactivePower(Ia1, Ib1, Ic1, Za, Zb, Zc)

    var = (
        (Ia1.ReversedMultiplication(Ua1)).arifm()
        + (Ib1.ReversedMultiplication(Ub1)).arifm()
        + (Ic1.ReversedMultiplication(Uc1)).arifm()
    )



    res += f"S = Ua * Ia* + Ub * Ib* + Uc * Ic* = {Ua1.IndicPrint()} * {vector(Ia1.arifm())}^e{-angle(Ia1.arifm())} + {Ub1.IndicPrint()} * {vector(Ib1.arifm())}^e{-angle(Ib1.arifm())}+ {Uc1.IndicPrint()} * {vector(Ic1.arifm())}^e{-angle(Ic1.arifm())} = "
    res += (
        f"{vector(var)}*e^{angle(var)} = {round(FP.real, 2)} + {round(FP.imag, 2)}j\n"
    )

    res += f"P = {round(AP, 2)}\n"
    res += f"Q = {round(RP, 2)}"
        
    return res

