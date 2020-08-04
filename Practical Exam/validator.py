#Modulul validator
from erori import ValidError
class Valid:
    """
    Clasa de obiecte de tip Valid- Domain: -
    """
    def validare_piesa(self,piesa):
        """
        Metoda pentru validarea unei piese de teatru
        :param: piesa, Piesa
        :return: -
        raises ValidError daca piesa nu este corecta logic
        """
        mesaj=""
        if not self.validare_titlu(piesa):
            mesaj+="Titlu invalid\n"
        if not self.validare_regizor(piesa):
            mesaj+="Regizor invalid\n"
        if not self.validare_gen(piesa):
            mesaj+="Gen invalid\n"
        if not self.validare_durata(piesa):
            mesaj+="Durata invalida\n"
        if mesaj!="":
            raise ValidError(mesaj)

    def validare_titlu(self,piesa):
        """
        Metoda pentru validarea titlului unei piese
        :param: piesa, Piesa
        :return: True, daca titlul piesei este ok, False, in caz contrar
        """
        if piesa.get_titlu()=="":
            return False
        return True

    def validare_regizor(self,piesa):
        """
        Metoda pentru validarea regizorului unei piese
        :param: piesa, Piesa
        :return: True, daca regizorul piesei este ok, False, in caz contrar
        """
        if piesa.get_regizor()=="":
            return False
        return True

    def validare_durata(self,piesa):
        """
        Metoda pentru validarea duratei unei piese
        :param: piesa, Piesa
        :return: True, daca durata piesei este ok, False, in caz contrar
        """
        if piesa.get_durata()>=0:
            return True
        return False

    def validare_gen(self,piesa):
        """
        Metoda pentru validarea genului unei piese
        :param: piesa, Piesa
        :return: True, daca genul piesei este ok, False, in caz contrar
        """
        genuri=["Comedie","Drama","Satira","Altele"]
        if piesa.get_gen() in genuri:
            return True
        return False