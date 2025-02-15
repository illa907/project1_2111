def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Ми неможемо працювати з таким типом данних - {type(var1)}. Треба тип - str!")
    else:
        return var1


my_var = 10
m_var2 = "Vasya"
checker(my_var)
checker(my_var2)
