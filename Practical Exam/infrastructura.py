#Modulul infrastructura
from domain import Piesa
from erori import RepoError
class Repo:
    """
    Clasa de obiecte de tip Repo- Domain: lista, list, fisier, string
    """
    def __init__(self,fisier):
        """
        Initializeaza un obiect de tip Repo
        :param fisier: string
        """
        self.__lista=[]
        self.__fisier=fisier
        self.load_from_file()

    def load_from_file(self):
        """
        Metoda pentru incarcarea datelor din fisier
        :return:
        """
        f=open(self.__fisier,"r")
        for linie in f:
            linie=linie.split(",")
            if len(linie)==4:
                piesa=Piesa(linie[0],linie[1],linie[2],int(linie[3]))
                self.__lista.append(piesa)
        f.close()

    def update_file(self):
        """
        Metoda pentru actualizarea fisierului de piese
        :return:
        """
        f=open(self.__fisier,"w")
        for i in self.__lista:
            f.write(i.get_titlu()+","+i.get_regizor()+","+i.get_gen()+","+str(i.get_durata())+"\n")
        f.close()

    def repo_adaugare(self,piesa):
        """
        Metoda pentru adaugarea unei noi piese de teatru
        :param piesa: Piesa
        :return:
        """
        self.validare_unicitate(piesa)
        self.__lista.append(piesa)
        self.update_file()

    def validare_unicitate(self, piesa):
        """
        Verifica unicitatea unei piese
        :param piesa: Piesa
        :return:
        raises RepoError daca piesa exista deja in lista
        """
        if piesa in self.__lista:
            raise RepoError("Piesa a mai fost adaugata deja! ")

    def get_all(self):
        """
        Metoda pentru accesarea listei de piese
        :return: lista de piese
        """
        return self.__lista

    def delete(self):
        """
        Metoda pentru stergerea ultimului element din lista de piese
        :return:
        """
        self.__lista.pop()
        self.update_file()

    def repo_modificare(self,piesa):
        """
        Metoda pentru modificarea piesei
        :param piesa: Piesa
        :return:
        """
        ok=False
        for i in self.__lista:
            if i==piesa:
                ok=True
                i.set_gen(piesa.get_gen())
                i.set_durata(piesa.get_durata())
                break
        if not ok:
            raise RepoError("Piesa nu exista! ")
        self.update_file()