#Modulul business
from domain import Piesa
from random import randint,choice
class Service:
    """
    Clasa de obiecte de tip Service- Domain: repo, Repo, valid, Valid
    """
    def __init__(self,repo,valid):
        """
        Initializeaza un obiect de tip Service
        :param repo: Repo
        :param valid: Valid
        """
        self.__repo=repo
        self.__valid=valid

    def service_adaugare(self,titlu,regizor,gen,durata):
        """
        Metoda in vederea adaugarii unei noi piese de teatru
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        :return:
        """
        piesa=Piesa(titlu,regizor,gen,durata)
        self.__valid.validare_piesa(piesa)
        self.__repo.repo_adaugare(piesa)

    def modificare(self,titlu,regizor,gen,durata):
        """
        Metoda pentru modificarea unei piese de teatru
        :param titlu: string
        :param regizor: string
        :param gen: string
        :param durata: int
        :return:
        """
        piesa=Piesa(titlu,regizor,gen,durata)
        self.__valid.validare_piesa(piesa)
        self.__repo.repo_modificare(piesa)

    def get_all(self):
        """
        Metoda pentru accesarea listei de piese
        :return: lista de piese
        """
        return self.__repo.get_all()

    def exportare(self,fisier):
        """
        Metoda pentru exportarea pieselor intr-un fisier, sortate dupa titlu si regizor
        :param fisier:
        :return:
        """
        l=self.get_all()[:]
        l.sort(key=lambda x:(x.get_regizor(),x.get_titlu()))
        f=open(fisier,"w")
        for i in l:
            f.write(i.get_regizor()+","+i.get_titlu()+","+str(i.get_durata())+","+i.get_gen()+"\n")
        f.close()

    def generare_aleatoare(self):
        """
        Genereaza aleator un cuvant dupa criteriile: lungime intre 8 si 12, exista un spatiu si consoanele si vocalele alterneaza
        :return: cuvantul generat
        """
        vocale = ["a", "e", "i", "o", "u"]
        litere=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        consoane=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
        rezultat=[]
        l = randint(8, 11)  # lungimea cuvantului
        n=randint(1,l-1) #pozitia spatiului
        for i in range(0,l+1):
            if i==0:
                rezultat.append(choice(litere))
            elif i==n:
                rezultat.append(" ")
            else:
                if rezultat[i-1] in vocale:
                    rezultat.append(choice(consoane))
                else:
                    rezultat.append(choice(vocale))
        return "".join(rezultat)

    def creare(self,nr):
        """
        Metoda pentru crearea unui numar de piese cu date aleatorii
        :param nr: int
        :return: lista cu piesele nou adaugate
        """
        genuri=["Comedie","Drama","Satira","Altele"]
        l=[]
        for i in range(0,nr):
            piesa=Piesa(self.generare_aleatoare(),self.generare_aleatoare(),choice(genuri),randint(1,10000))
            try:
                self.__repo.repo_adaugare(piesa)
                l.append(piesa)
            except:
                i-=1
        return l