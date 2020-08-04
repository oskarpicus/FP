#Modulul domain.py
class Piesa:
    """
    Clasa de obiecte de tip Piesa de teatru- Domain: titlu, string, regizor, string, gen, string, durata, int
    """
    def __init__(self,titlu,regizor,gen,durata):
        """
        Initializeaza un obiect de tipul Piesa
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        """
        self.__titlu=titlu
        self.__regizor=regizor
        self.__gen=gen
        self.__durata=durata

    def get_titlu(self):
        """
        Getter pentru titlul unei piese
        :return: titlul piesei
        """
        return self.__titlu

    def get_regizor(self):
        """
        Getter pentru regizorul unei piese
        :return: regizorul piesei
        """
        return self.__regizor

    def get_gen(self):
        """
        Getter pentru genul unei piese
        :return: genul piesei
        """
        return self.__gen

    def get_durata(self):
        """
        Getter pentru durata unei piese
        :return: durata piesei
        """
        return self.__durata

    def __eq__(self, other):
        """
        Defineste relatia de egalitate dintre 2 piese
        :param other: Piesa
        :return: True, daca titlul si regizorul lui self si other sunt egale
        """
        return self.get_regizor()==other.get_regizor() and self.get_titlu()==other.get_titlu()

    def __str__(self):
        """
        Defineste modul in care sunt afisate piesele
        :return: formatul de afisare al piesei
        """
        return self.get_titlu()+","+self.get_regizor()+","+self.get_gen()+","+str(self.get_durata())

    def set_gen(self,gen):
        """
        Setter pentru genul unei piese
        :param gen: string
        :return:
        """
        self.__gen=gen

    def set_durata(self,durata):
        """
        Setter pentru durata unei piese
        :param durata: int
        :return:
        """
        self.__durata=durata