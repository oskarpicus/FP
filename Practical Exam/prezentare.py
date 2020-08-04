#Modulul prezentare
from erori import *
class Console:
    """
    Clasa de obiecte de tip Console- Domain: service, Service, comenzi, dict
    """
    def __init__(self,service):
        """
        Initializeaza un obiect de tipul service
        :param service: Service
        """
        self.__service=service
        self.__comenzi={"1":self.ui_adaugare,"2":self.ui_modificare,"3":self.ui_creare,"4":self.ui_exportare,"5":self.ui_afisare}

    def run(self):
        """
        Afiseaza functionalitatile disponibile si primeste comenzi de la utilizator
        :return:
        """
        while True:
            print("1 - Adaugare piesa")
            print("2 - Modificare piesa")
            print("3 - Creeaza aleator piese de teatru")
            print("4 - Exporta piese de teatru sortate dupa regizor si titlu intr-un fisier")
            print("5 - Afisare piese de teatru")
            print("0 - Iesire din aplicatie")
            cmd=input()
            if cmd=="0":
                return
            elif cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError as e:
                    print("Eroare UI\n",str(e))
                except RepoError as e:
                    print("Eroare Repo\n",str(e))
                except ValidError as e:
                    print("Eroare Validator\n",str(e))
            else:
                print("Comanda invalida")

    def ui_adaugare(self):
        """
        Metoda in vederea adaugarii unei piese de teatru
        :return:
        """
        titlu=self.citire_titlu()
        regizor=self.citire_regizor()
        gen=self.citire_gen()
        durata=self.citire_durata()
        durata=self.tip_numeric(durata)
        self.__service.service_adaugare(titlu,regizor,gen,durata)
        print("Adaugarea a fost facuta cu succes! ")

    def ui_modificare(self):
        """
        Metoda in vederea modificarii unei piese de teatru
        :return:
        """
        titlu=self.citire_titlu()
        regizor=self.citire_regizor()
        gen = self.citire_gen()
        durata = self.citire_durata()
        durata = self.tip_numeric(durata)
        self.__service.modificare(titlu,regizor,gen,durata)
        print("Modificarea a fost facuta cu succes! ")

    def ui_creare(self):
        """
        Metoda in vederea crearii aleatoare a pieselor de teatru
        :return:
        """
        nr=self.citire_numar()
        nr=self.tip_numeric(nr)
        l=self.__service.creare(nr)
        print("Piesele adaugate sunt: ")
        for i in l:
            print(i)

    def ui_exportare(self):
        """
        Metoda in vederea exportarii pieselor de teatru intr-un fisier text
        :return:
        """
        fisier=self.citire_fisier()
        self.__service.exportare(fisier)
        print("Exportarea a fost facuta cu succes! ")

    def ui_afisare(self):
        """
        Metoda in vederea afisarii pieselor de teatru memorate
        :return:
        """
        l=self.__service.get_all()
        if l==[]:
            print("Nu exista nicio piesa memorata ")
        else:
            print("Piesele memorate: ")
            for i in l:
                print(i)

    def citire_titlu(self):
        """
        Metoda pentru citirea titlului unei piese
        :return: titlul piesei citite
        """
        return input("Dati titlul piesei ")

    def citire_regizor(self):
        """
        Metoda pentru citirea regizorului unei piese
        :return: regizorul piesei citite
        """
        return input("Dati regizorul piesei ")

    def citire_gen(self):
        """
        Metoda pentru citirea genului unei piese
        :return: genul citit
        """
        return input("Dati genul piesei ")

    def citire_durata(self):
        """
        Metoda pentru citirea duratei unei piese
        :return: durata citita
        """
        return input("Dati durata piesei ")

    def tip_numeric(self,x):
        """
        Metoda pentru validarea tipului numeric
        :param x: string
        :return: int(x)
        raises ValidError daca x nu se poate converti la int
        """
        try:
            return int(x)
        except ValueError:
            raise ValueError("Nu se verifica tipul numeric! ")

    def citire_fisier(self):
        """
        Metoda pentru citirea unui nume de fisier
        :return: numele de fisier citit
        """
        return input("Dati numele fisierului ")

    def citire_numar(self):
        """
        Metoda pentru citirea unui numar de piese de adaugat
        :return: numarul citit
        """
        return input("Dati numarul de piese de adaugat ")
