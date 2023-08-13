from THREEPHASE import *

from THREERES import *


def count(TYPE, R11, R22, R33, method='', E11=0, E22=0, E33=0, UU=0, code1=''):
    """Переменная TYPE определяет тип задачи, принимает в себя значения OTHER, THREEPHASE, THREERES.
    method выбирает ход решения задачи, для OTHER переменная не принимает в себя никакие значения
    для THREEPHASE принимает в себя значения STARNEUTRAL, STARNONEUTRAL, TRIANGLE, преобразуя значения
    R1, R2, R3 xd комплексную форму.
    Для THREERES принимает в себя значения NODAL, CONTUR, Kirchhoff, так же требует code и вызывает сответсвующий метод решения"""
    try:
        if TYPE == 'OTHER':
            pass
        elif TYPE == 'THREEPHASE':
            try:
                R1 = complex(R11)
                R2 = complex(R22)
                R3 = complex(R33)
                U = float(UU)
                if method == 'STARNEUTRAL':
                    return StarWithNeutral(U=UU, Za=R1, Zb=R2, Zc=R3)
                elif method == 'STARNONEUTRAL':
                    return star_without_neutral(U=UU, Za=R1, Zb=R2, Zc=R3)
                elif method == 'TRIANGLE':
                    return triangle(U=UU, Zab=R1, Zbc=R2, Zca=R3)
                else:
                    return 'Ошибка метода'
            except:
                return f'Ошибка трехфазной цепи\n U = {U}, Za = {R1}, Zb = {R2}, Zc = {R3}, method = {method}'
        elif TYPE == 'THREERES':
            try:
                R11 = float(R11)
                R22 = float(R22)
                R33 = float(R33)
                E11 = float(E11)
                E22 = float(E22)
                E33 = float(E33)

            except:
                return f'{R11}, {R22}, {R33}'
            if method == 'CONTUR':
                return contur(code1, R11, R22, R33, E1=E11, E2=E22, E3 = E33)
            elif method == 'Kirchhoff':
                return kirghofh(code=code1, R1=R11, R2=R22, R3=R33, E1=E11, E2=E22, E3=E33)
            elif method == 'NODAL':
                if code1 == '001':
                    return nodal_potential_001(E33, R11, R22, R33) 
                elif code1 == '00m':
                    return nodal_potential_00m(E33, R11, R22, R33)
                elif code1 == '010':
                    return nodal_potential_010(E22, R11, R22, R33)
                elif code1 == '011':
                    return nodal_potential_011(E22, E33, R11, R22, R33)
                elif code1 == '01m':
                    return nodal_potential_01m(E22, E33, R11, R22, R33)
                elif code1 == '0m0':
                    return nodal_potential_0m0(E22, R11, R22, R33)
                elif code1 == '0m1':
                    return nodal_potential_0m1(E22, E33, R11, R22, R33)
                elif code1 == '0mm':
                    return nodal_potential_0mm(E22, E33, R11, R22, R33)
                elif code1 == '100':
                    return nodal_potential_100(E11, R11, R22, R33)
                elif code1 == '101':
                    return nodal_potential_101(E11, E33, R11, R22, R33)
                elif code1 == '10m':
                    return nodal_potential_10m(E11, E33, R11, R22, R33)
                elif code1 == '110':
                    return nodal_potential_110(E11, E22,  R11, R22, R33)
                elif code1 == '111':
                    return nodal_potential_111(E11, E22, E33, R11, R22, R33)
                elif code1 == '11m':
                    return nodal_potential_11m(E11, E22, E33, R11, R22, R33)
                elif code1 == '1m0':
                    return nodal_potential_1m0(E11, E22, R11, R22, R33)
                elif code1 == '1m1':
                    return nodal_potential_1m1(E11, E22, E33, R11, R22, R33)
                elif code1 == '1mm':
                    return nodal_potential_1mm(E11, E22, E33, R11, R22, R33)
                elif code1 == 'm00':
                    return nodal_potential_m00(E11, R11, R22, R33)
                elif code1 =='m01':
                    return nodal_potential_m01(E11, E33, R11, R22, R33)
                elif code1 =='m0m':
                    return nodal_potential_m0m(E11, E33, R11, R22, R33)
                elif code1 =='m10':
                    return nodal_potential_m10(E11, E22,  R11, R22, R33)
                elif code1 =='m11':
                    return nodal_potential_m11(E11, E22, E33, R11, R22, R33)
                elif code1 =='m1m':
                    return nodal_potential_m1m(E11, E22, E33, R11, R22, R33)
                elif code1 =='mm0':
                    return nodal_potential_mm0(E11, E22, R11, R22, R33)
                elif code1 =='mm1':
                    return nodal_potential_mm1(E11, E22, E33, R11, R22, R33)
                elif code1 =='mmm':
                    return nodal_potential_mmm(E11, E22, E33, R11, R22, R33)
                else:
                    return 'Ошибка кодировки для узловых потенциалов'

        return 'Ошибка выполнения, неправильно введен тип задачи'
    except:
        return f'Неизвестная ошибка, возможно вы ввели недействительные значенияn\nR1 = {R11}, R2 = {R22}, R3 = {R33}, E1 = {E11}, E2 = {E22}, E3 = {E33}, code = {code1}'


# print(triangle(2.0, (2+7j), (3+0j), 4j))