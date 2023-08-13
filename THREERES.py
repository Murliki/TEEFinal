def PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=0, E2=0, E3=0):
    res = 'Pист = '
    if E1 != 0:
        res += 'E1 * I1'
        if E2 != 0:
            res += ' + '  
        else:
            if E3 != 0:
                res += ' + '  
    if E2 != 0:
        res += 'E2 * I2'
        if E3 != 0:
            res += ' + '  
    if E3 != 0:
        res += 'E3 * I3'

    res += f' = {round(E1 * I1 + E2 * I2 + E3 * I3, 2)}\n'

    res += f'Rпр = I1^2 * R1 + I2^2 * R2 + I3^2 * R3 = {round(I1, 2)}^2 * {R1} + {round(I2, 2)}^2 * {R2} + {round(I3, 2)}^2 * {R3} = {round(I1 ** 2 * R1 + I2 ** 2 * R2 + I3 ** 2 * R3, 2)}' 

    return res


#nodal

def nodal_potential_100(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой ветке \n\n"

    u1 = (E * (1 / R1)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E1/R1) / (1/R1 + 1/R2 + 1/R3) = {round(E/R1, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (E - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({round(E, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u1 - u2) / R2
    res += f"I2 = (u1 - u2) / R2 = ({round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E))

    return res

def nodal_potential_010(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в центральной ветке \n\n"

    u1 = (E * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E2/R2\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(E/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({round(E, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 + u2) / R3 = ({round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E))

    return res

def nodal_potential_001(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой ветке \n\n"

    u1 = (E * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E3/R3\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u1 - u2) / R2
    res += f"I2 = (u1 - u2) / R2 = ({round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E - u1 + u2) / R3
    res += f"I3 = (E - u1 + u2) / R3 = ({round(E, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E3=E))

    return res

def nodal_potential_m00(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой ветке \n\n"

    u2 = (E * (1 / R1)) / (1 / R1 + 1 / R2 + 1 / R3)
    u1 = 0

    res += "u2 * (1/R1 + 1/R2 + 1/R3) = E1/R1\n"
    res +='u1 = 0\n\n'
    res += f"u2 = (E1/R1) / (1/R1 + 1/R2 + 1/R3) = {round(E/R1, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u2, 2)}\n"
    res +='u1 = 0\n\n'


    I1 = (E - u2 + u1) / R1
    res += f"I1 = (E1 - u2 + u1) / R1 = ({round(E, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u2 - u1) / R2
    res += f"I2 = (u2 - u1) / R2 = ({round(u2, 2)} - {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u2 - u1) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u2, 2)} - {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E))

    return res

def nodal_potential_0m0(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в центральной ветке \n\n"

    u2 = (E * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u1 = 0
    res += f"u2 * (1/R1 + 1/R2 + 1/R3) = E2/R2 => u2 = (E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(E/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u2, 2)}\nu1 = 0\n"
    res += 'u1 = 0\n\n'
    I1 = (u2 - u1) / R1
    res += f"I1 = (u2 - u1) / R1 = ({round(u2, 2)} - {round(u1, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E - u2 + u1) / R2
    res += f"I2 = (E - u2 + u1) / R2 = ({round(E, 2)} - {round(u2, 2)} + {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u2 - u1) / R3
    res += f"I3 = (u2 - u1) / R3 = ({round(u2, 2)} - {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E))

    return res

def nodal_potential_00m(E, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = 'ЭДС в правой ветке направлено вверх, заземленный угол сверху\n'
    u2 = (E * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u1 = 0
    res += f"u2 * (1/R1 + 1/R2 + 1/R3) = E3/R3 => u2 = (E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u2, 2)}\nu1 = 0\n"
    I1 = (u2 - u1) / R1
    res += f"I1 = (u2 - u1) / R1 = ({round(u2, 2)} - {round(u1, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u2 - u1) / R2
    res += f"I2 = (u2 - u1) / R2 = ({round(u2, 2)} - {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E - u2 + u1) / R3
    res += f"I3 = (E3 - u2 + u1) / R3 = ({round(E, 2)} - {round(u2, 2)} + {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E3=E))

    return res




def nodal_potential_110(E1, E2, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой и центральной ветке \n\n"

    u1 = (E1 * (1 / R1) + E2 * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 + E2/R2\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E1/R1 + E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 + E2/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({round(E1, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2))

    return res

def nodal_potential_m10(E1, E2, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой и вверхсмотрящим центральной ветке \n\n"

    u1 = (-E1 * (1 / R1) + E2 * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 + E2/R2\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (-E1/R1 + E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 + E2/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2))

    return res

def nodal_potential_mm0(E1, E2, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой центральной ветке \n\n"

    u1 = (E1 * (1 / R1) - E2 * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 + E2/R2\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E1/R1 - E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E2/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2))

    return res

def nodal_potential_mm0(E1, E2, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой и центральной ветке \n\n"

    u1 = (-E1 * (1 / R1) - E2 * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 + E2/R2\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (-E1/R1 - E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 - E2/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2))

    return res

def nodal_potential_011(E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральном и правом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой и центральной ветке \n\n"

    u1 = (E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E2/R2 + E3/R3\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E2/R2 + E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E2, E3=E3))

    return res

def nodal_potential_01m(E2, E3, R1, R2, R3):

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в правой и вверхсмотрящим в центральной ветке\n\n"

    u1 = (E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E2/R2 - E3/R3\n"
    res +='u2 = 0\n\n'
    res += f"u1 = (E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res +='u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u2 + u1) / R3

    res += f"I3 = (E3 - u2 + u1) / R3 = ({round(E3, 2)} - {round(u2, 2)} + {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E2, E3=E3))

    return res

def nodal_potential_0m1(E2, E3, R1, R2, R3):

    res = "ЭДС центральной ветки направлен вниз, правой - вверх\n\n"

    u1 = (-E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E2/R2 + E3/R3\n"
    res += 'u2 = 0\n\n'
    res += f"u1 = (-E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E2/R2 + E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u2 + u1) / R2
    res += f"I2 = (E2 - u2 + u1) / R2 = ({E2} - {round(u2, 2)} + {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u2 - u1) / R3

    res += f"I3 = (E3 + u2 - u1) / R3 = ({round(E3, 2)} + {round(u2, 2)} - {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E2, E3=E3))

    return res

def nodal_potential_0mm(E2, E3, R1, R2, R3):

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в правой и центральной ветке \n\n"

    u1 = (-E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E2/R2 - E3/R3\n"
    res += 'u2 = 0\n\n'

    res += f"u1 = (-E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'

    I1 = (u1 - u2) / R1
    res += f"I1 = (u1 - u2) / R1 = ({round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u2 + u1) / R2
    res += f"I2 = (E2 - u2 + u1) / R2 = ({E2} - {round(u2, 2)} + {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u2 + u1) / R3

    res += f"I3 = (E3 - u2 + u1) / R3 = ({round(E3, 2)} - {round(u2, 2)} + {round(u1, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E2=E2, E3=E3))

    return res

def nodal_potential_101(E1, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральном и правом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой и правой ветке \n\n"

    u1 = (E1 * (1 / R1) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 + E3/R3\n"
    res += 'u2 = 0\n\n'

    res += f"u1 = (E1/R1 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 + E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'


    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({round(E1, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u1 - u2) / R2
    res += f"I2 = (u1 - u2) / R2 = ({round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E3=E3))

    return res

def nodal_potential_m01(E1, E3, R1, R2, R3):


    res = "Решение задачи методом узловых потенциалов с внизсмотрящим ЭДС в левой вверхсмотрящим в правой ветке \n\n"

    u1 = (E1 * (1 / R1) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (E1/R1 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({E1} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u2 - u1) / R2
    res += f"I2 = (u2 - u1) / R2 = ({round(u2, 2)} - {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=0, E3=E3))

    return res

def nodal_potential_10m(E1, E3, R1, R2, R3):


    res = "Решение задачи методом узловых потенциалов с внизсмотрящим в правой и вверхсмотрящим в левой ветке \n\n"

    u1 = (E1 * (1 / R1) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (E1/R1 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({E1} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u2 - u1) / R2
    res += f"I2 = (u2 - u1) / R2 = ({round(u2, 2)} - {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=0, E3=E3))

    return res

def nodal_potential_m0m(E1, E3, R1, R2, R3):


    res = "Решение задачи методом узловых потенциалов с внизсмотрящим в левой и правой ветках \n\n"

    u1 = (-E1 * (1 / R1) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (-E1/R1 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n\n"
    res += 'u2 = 0\n\n'


    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (u2 - u1) / R2
    res += f"I2 = (u2 - u1) / R2 = ({round(u2, 2)} - {round(u1, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=0, E3=E3))

    return res

def nodal_potential_1m0(E1, E2, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в левом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой и внизсмотрящим в центральной ветке \n\n"

    u1 = (E1 * (1 / R1) - E2 * (1 / R2)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 - E2/R2\n"
    res += 'u2 = 0\n\n'

    res += f"u1 = (E1/R1 - E2/R2) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E2/R2, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'


    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({round(E1, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (u1 - u2) / R3
    res += f"I3 = (u1 - u2) / R3 = ({round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2))

    return res

def nodal_potential_111(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральном и правом узле
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой, центральной и правой ветке \n\n"

    u1 = (E1 * (1 / R1) + E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 + E2/R2 + E3/R3\n"
    res += 'u2 = 0\n\n'

    res += f"u1 = (E1/R1 + E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 + E2/R2 + E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'


    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({round(E1, 2)} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_m11(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой и центрольной и внизмотрящим в левой ветке \n\n"

    u1 = (-E1 * (1 / R1) + E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 + E2/R2 + E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (-E1/R1 + E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 + E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += 'u2 = 0\n\n'


    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_mm1(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой и внизмотрящим в левой и центрольной ветке \n\n"

    u1 = (-E1 * (1 / R1) + -E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 - E2/R2 + E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (-E1/R1 - E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 - E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_m1m(E1, E2, E3, R1, R2, R3):

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой и правой ветке, вверхсотрящим в центральной\n\n"

    u1 = (-E1 * (1 / R1) + E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 + E2/R2 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (-E1/R1 + E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 + E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_mmm(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с внизсмотрящим источником в левой, в центральной и в правой ветке \n\n"

    u1 = (-E1 * (1 / R1) - E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = -E1/R1 - E2/R2 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (-E1/R1 - E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(-E1/R1 - E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 + u1 - u2) / R1
    res += f"I1 = (E1 + u1 - u2) / R1 = ({E1} + {round(u1, 2)} - {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_1m1(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой и левой и внизмотрящим в центральной ветке \n\n"

    u1 = (E1 * (1 / R1) - E2 * (1 / R2) + E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 - E2/R2 + E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (E1/R1 - E2/R2 + E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E2/R2 + E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({E1} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 - u1 + u2) / R3
    res += f"I3 = (E3 - u1 + u2) / R3 = ({E3} - {round(u1, 2)} + {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_11m(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в правой и центральной, внизсмотрящим в левой\n\n"

    u1 = (E1 * (1 / R1) + E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 + E2/R2 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (E1/R1 + E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 + E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({E1} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 - u1 + u2) / R2
    res += f"I2 = (E2 - u1 + u2) / R2 = ({E2} - {round(u1, 2)} + {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res

def nodal_potential_1mm(E1, E2, E3, R1, R2, R3):
    """Возвращает полный ход решения задачи методом узловых
    потенциалов для задач с источников энергии в центаральномб левом и правом узле
    направления токов совпадают с направлениями ЭДС
    """

    res = "Решение задачи методом узловых потенциалов с вверхсмотрящим источником в левой, и внизмотрящим в центральной ветке и правой ветке \n\n"

    u1 = (E1 * (1 / R1) - E2 * (1 / R2) - E3 * (1 / R3)) / (1 / R1 + 1 / R2 + 1 / R3)
    u2 = 0

    res += "u1 * (1/R1 + 1/R2 + 1/R3) = E1/R1 - E2/R2 - E3/R3\n"
    res += "u2 = 0\n\n"
    res += f"u1 = (E1/R1 - E2/R2 - E3/R3) / (1/R1 + 1/R2 + 1/R3) = {round(E1/R1 - E2/R2 - E3/R3, 2)} / ({round(1/R1, 2)} + {round(1/R2, 2)} + {round(1/R3, 2)}) = {round(u1, 2)}\n"
    res += "u2 = 0\n\n"

    I1 = (E1 - u1 + u2) / R1
    res += f"I1 = (E1 - u1 + u2) / R1 = ({E1} - {round(u1, 2)} + {round(u2, 2)}) /  {R1} = {round(I1, 2)}\n"

    I2 = (E2 + u1 - u2) / R2
    res += f"I2 = (E2 + u1 - u2) / R2 = ({E2} + {round(u1, 2)} - {round(u2, 2)}) /  {R2} = {round(I2, 2)}\n"

    I3 = (E3 + u1 - u2) / R3
    res += f"I3 = (E3 + u1 - u2) / R3 = ({E3} + {round(u1, 2)} - {round(u2, 2)}) /  {R3} = {round(I3, 2)}\n\n"

    res += str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1=E1, E2=E2, E3=E3))

    return res






def kirghofh(code:str, R1, R2, R3, E1=0, E2=0, E3=0):
    if E1 < 0 or E2 < 0 or E3 < 0 or R1 < 0 or R2 < 0 or R3 < 0:
        return 'Все значения ввода должны быть положительными'
    
    wR1 = R1; wR2 = R2; wR3 = R3
    wE1 = E1; wE2 = E2; wE3 = E3

    res = 'Решение задачи с '

    if code[0] == 'm':
        wE1 = -E1
        wR1 = R1
        res += 'внизсмотрящим ЭДС в левой ветке'
    elif code[0] == '0':
        wE1 = 0
        wR1 = R1
        res += ''
    elif code[0] == '1':
        wE1 = E1
        wR1 = R1
        res += 'вверхсмотрящим ЭДС в левой ветке'
    else:
        return 'Ошибка внутренней кодировки, свяжитесь с поддержкой' 

    res += f'{", " if code[1] != 0 or code[2] != 0 else ""}'
    

    if code[1] == 'm':
        wE2 = E2
        wR2 = -R2
        res += 'внизсмотрящим ЭДС в центральной ветке'
    elif code[1] == '0':
        wE2 = 0
        wR2 = -R2
        res += ''
    elif code[1] == '1':
        wE2 = -E2
        wR2 = -R2
        res += 'вверхсмотрящим ЭДС в центральной ветке'
    else:
        return 'Ошибка внутренней кодировки, свяжитесь с поддержкой' 
    
    if code[1] != '0' and code[2] != '0':
        res += ', '


    if code[2] == 'm':
        wE3 = E3
        wR3 = -R3
        res += 'внизсмотрящим ЭДС в правой ветке'
    elif code[2] == '0':
        wE3 = 0
        wR3 = -R3
        res += ''
    elif code[2] == '1':
        wE3 = -E3
        wR3 = -R3
        res += 'вверхсмотрящим ЭДС в правой ветке'
    else:
        return 'Ошибка внутренней кодировки, свяжитесь с поддержкой' 
    

    res += '\n\n'
    
    res += f'В замкнутом контуре сумма падений напряжений равна сумме "ЭДС\nВыбраны контуры: R1R3, R1R2, все токи направлены вверх\n\nСистема уравнений:\n'
    if wE3 < 0:
        E1E3symbol = '-'
    elif wE3 > 0:
        E1E3symbol = '+'
    else:
        E1E3symbol = ''

    if wE2 < 0:
        E1E2symbol = '-'
    elif wE2 > 0:
        E1E2symbol = '+'
    else:
        E1E2symbol = ''

    

    res += f'{"-" if wR1<0 else ""}{R1}I1 {"-" if wR3 < 0 else "+"} {R3}I3 = {wE1 if wE1 != 0 else ""}{E1E3symbol}{E3 if wE3 != 0 else ""} = {wE3 + wE1}\n'
    res += f'{"-" if wR1<0 else ""}{R1}I1 {"-" if wR2 < 0 else "+"} {R2}I2 = {wE1 if wE1 != 0 else ""}{E1E2symbol}{E2 if wE2 != 0 else ""} = {wE2 + wE1}\n'
    res += f'I1 + I2 + I3 = 0\n\n'
    
    res += 'Система уравнений будет решена методом Краммера\n\n'
    res += f'{wR1}  0  {wR3} | {wE3 + wE1}\n{wR1}  {wR2}  0 | {wE2 + wE1}\n1  1  1 | 0\n'

    m11, m12, m13 = wR1, 0, wR3
    m21, m22, m23 = wR1, wR2, 0
    m31, m32, m33 = 1, 1, 1



    m1 = wE3 + wE1
    m2 = wE2 + wE1
    m3 = 0

    det = m11*m22*m33 + m12*m23*m31 + m21*m32*m13 - (m13*m22*m31) - (m11*m23*m32) - (m21*m12*m33)

    res += f'Δ = ({m11})*({m22})*({m33}) + ({m12})*({m23})*({m31}) + ({m21})*({m32})*({m13}) - ({m13})*({m22})*({m31}) - ({m11})*({m23})*({m32}) - ({m21})*({m12})*({m33}) = {det}' 
    res += '\n\n\n\n\n'

    if det == 0:
        return str(res) + f'Возникла ошибка выполнения, Δ = 0, вычисление матрицы невозможно\nwR1 = {wR1}, wR2 = {wR2}, wR3 = {wR3}\nwE1 = {wE1}, wE2 = {wE2}, wE3 = {wE3}'


    res += f'Столбец 1 заменен на столбец ответов\n{m1}  {m12}  {m13}\n{m2}  {m22}  {m23}\n{m3}  {m32}  {m33}\n'
    detI1 = m1*m22*m33 + m12*m23*m3 + m2*m32*m13 - (m13*m22*m3) - (m1*m23*m32) - (m2*m12*m33)
    res += f'ΔI1 = ({m1})*({m22})*({m33}) + ({m12})*({m23})*({m3}) + ({m2})*({m32})*({m13}) - ({m13})*({m22})*({m3}) - ({m1})*({m23})*({m32}) - ({m2})*({m12})*({m33}) = {detI1}\n\n\n\n\n'


    res += f'Столбец 2 заменен на столбец ответов\n{m11}  {m1}  {m13}\n{m21}  {m2}  {m23}\n{m31}  {m3}  {m33}\n'
    detI2 = m11*m2*m33 + m1*m23*m31 + m21*m3*m31 - (m13*m2*m31) - (m11*m23*m3) - (m21*m1*m33)
    res += f'ΔI2 = ({m11})*({m2})*({m33}) + ({m1})*({m23})*({m31}) + ({m21})*({m3})*({m13}) - ({m13})*({m2})*({m31}) - ({m11})*({m23})*({m3}) - ({m21})*({m1})*({m33}) = {detI2}\n\n\n\n\n'

    res += f'Столбец 3 заменен на столбец ответов\n{m11}  {m12}  {m1}\n{m21}  {m22}  {m2}\n{m31}  {m32}  {m3}\n'
    detI3 = m11*m22*m3 + m12*m2*m31 + m21*m32*m1 - (m1*m22*m31) - (m11*m2*m32) - (m21*m12*m3)
    res += f'ΔI3 = ({m11})*({m22})*({m3}) + ({m12})*({m2})*({m31}) + ({m21})*({m32})*({m1}) - ({m1})*({m22})*({m31}) - ({m11})*({m2})*({m32}) - ({m21})*({m12})*({m3}) = {detI3}\n\n'

    I1 = round(detI1/det, 2)
    I2 = round(detI2/det, 2)
    I3 = round(detI3/det, 2)

    res += f'I1 = ΔI1/Δ = {round(detI1, 2)} / {round(det, 2)} = {I1}\n'
    res += f'I2 = ΔI2/Δ = {round(detI2, 2)} / {round(det, 2)} = {I2}\n'
    res += f'I3 = ΔI3/Δ = {round(detI3, 2)} / {round(det, 2)} = {I3}\n\n'



    if code[0] == 'm':
        E1 = -E1
    if code[1] == 'm':
        E2 = -E2
    if code[2] == 'm':
        E3 = -E3

    res += PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1, E2, E3)
    
    
    return res

def contur(code:str, R1, R2, R3, E1=0, E2=0, E3=0):

    if len(code) == 3:
        if code[0] == '0':
            wE1 = 0
            wR1 = 0
            sign11 = ''
            sign12 = ''
        elif code[0] == '1':
            wE1 = E1
            wR1 = R1    
            sign11 = ''
            sign12 = '-'
        elif code[0] == 'm':
            wE1 = -E1
            wR1 = -R1
            sign11 = '-'
            sign12 = '+'
        else:
            return 'Ошибка кодировки первого символа' 
        

        if code[1] == '0':
            wE2 = 0
            wR2 = 0
            wwE2 = 0
            wwR2 = 0
            sign21 = ''
            sign22 = ''
        elif code[1] == '1':
            wE2 = -E2
            wR2 = -R2
            wwE2 = E2
            wwR2 = R2
            sign21 = '-'
            sign22 = '+'
        elif code[1] =='m':
            wE2 = E2
            wR2 = R2
            wwE2 = -E2
            wwR2 = -R2
            sign21 = '+'
            sign22 = '-'
        else:
            return 'Ошибка кодировки второго символа'


        if code[2] == '0':
            wE3 = 0
            wR3 = 0
            sign31 = ''
            sign32 = ''
        elif code[2] == '1':
            wE3 = -E3
            wR3 = -R3
            sign31 = '-'
            sign32 = '-'
        elif code[2] =='m':
            wE3 = E3
            wR3 = R3
            sign31 = '-'
            sign32 = '+'
        else:
            return 'Ошибка кодировки третьего символа'
        
    else: 
        return 'Бро эта штука не умеет считать больше или меньше трех резисторов, да и не надо оно тебе))'
    
    res = 'Составим систему уравнений для контурных токов:\n\nДрузья, в силу своей лени я не писал код пропуска нулевых значений, так что будьте благоразумны их не переписывать))\n\n'

    res += f'Ik1(R1+R2) - R2 * Ik2 = {sign11}E1 {sign21} E2\n'
    res += f'Ik2(R2+R3) - R2 * Ik1 = {sign22 if sign22 == "-" else ""}{"E2" if wE3 != 0 else ""} {sign32} {"E3" if wE3 != 0 else ""}\n\n'

    res += 'Подставим значения\n'
    res += f'{R1 + R2}Ik1 - {R2}Ik2 = {wE1 + wE2}\n'
    res += f'{R2 + R3}Ik2 - {R2}Ik1 = {wwE2 + wE3}\n\n'

    res += 'Выразим и упростим Ik2\n'
    res += f'{R1 + R2}Ik1 - {R2}Ik2 = {wE1 + wE2}\n'
    res += f'Ik2 = ({wwE2 + wE3} + {R2}Ik1)/{R2+R3} = {round((wwE2 + wE3)/(R2+R3), 2)} + {round(R2/(R2+R3), 2)}Ik1\n\n'

    var = f'{round((wwE2 + wE3)/(R2+R3), 2)} + {round(R2/(R2+R3), 2)}Ik1'

    res += 'Подставим Ik2 в первое уравнение\n'

    res += f'{R1 + R2}Ik1 - {R2}({var}) = {wE1 + wE2}\n'
    res += f'Ik2 = {var}\n\n'

    res += 'Упростим первое уравнение\n'

    res += f'{R1 + R2}Ik1 - {round(R2 * round((wwE2 + wE3)/(R2+R3), 2), 2)} {"+" if round(R2/(R2+R3), 2) < 0 else "-"} {round(R2 * (R2/(R2+R3)), 2)}Ik1 = {wE1 + wE2}\n'
    res += f'Ik2 = {var}\n\n'

    res += 'Выразим и найдем Ik1\n'

    Ik1 = round(round(wE1 + wE2 + round(R2 * round((wwE2 + wE3)/(R2+R3), 2), 2), 2)/round(R1 + R2 - round(R2 * (R2/(R2+R3)), 2), 2), 2)

    res += f'Ik1  = {round(wE1 + wE2 + round(R2 * round((wwE2 + wE3)/(R2+R3), 2), 2), 2)}/{round(R1 + R2 - round(R2 * (R2/(R2+R3)), 2), 2)} = {Ik1}\n'
    res += f'Ik2 = {var}\n\n'

    res += 'Найдем Ik2\n'
    res += f'Ik1 = {Ik1}\n'
    res += f'Ik2 = {round(round((wwE2 + wE3)/(R2+R3), 2) + round(R2/(R2+R3), 2) * Ik1, 2)}\n\n'

    Ik2 = round((wwE2 + wE3)/(R2+R3) + (R2/(R2+R3) * Ik1), 2)
    I1 = Ik1
    I2 = Ik2 - Ik1
    I3 = -Ik2

    res += f'Найдем токи:\nНаправление обхода с направлением I1, соответвенно I1 = {Ik1}\nНаправление обхода Ik1 не совпадает с направлением I2, в отличии от направления обхода Ik2, следовательно I2 = Ik2 - Ik1 = {round(I2, 2)}\n'
    res += f'Направление обхода Ik2 не совпадает с направление тока I3, отсюда следует что I3 = -Ik2 = {-Ik2}\n\n'

    if code[0] == 'm':
        E1 = -E1
    if code[1] == 'm':
        E2 = -E2
    if code[2] == 'm':
        E3 = -E3

    res += str(str(PowerBalance_DC(I1, I2, I3, R1, R2, R3, E1, E2, E3)))
    
    return res
