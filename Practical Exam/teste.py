#Modulul teste.py
from business import Service
from infrastructura import Repo
from domain import Piesa
from validator import Valid
from erori import *
class Teste:
    """
    Clasa de obiecte de tip Teste- Domain: valid, Valid, repo, Repo, service, Service
    """
    def __init__(self):
        self.__valid=Valid()
        self.__repo=Repo("fisier_test.txt")
        self.__service=Service(self.__repo,self.__valid)

    def test_set_gen(self):
        piesa=Piesa("a","b","Comedie",12)
        piesa.set_gen("Satira")
        assert piesa.get_gen()=="Satira"

    def test_set_durata(self):
        piesa=Piesa("a","b","Comedie",12)
        piesa.set_durata(129)
        assert piesa.get_durata()==129

    def test_get_titlu(self):
        assert Piesa("a","b","Comedie",12).get_titlu()=="a"
        assert not Piesa("a", "b", "Comedie", 12).get_titlu()=="b"

    def test_get_regizor(self):
        assert Piesa("a","b","Comedie",12).get_regizor()=="b"
        assert not Piesa("a","b","Comedie",12).get_regizor()=="asfjf"

    def test_get_gen(self):
        assert Piesa("a","b","Comedie",12).get_gen()=="Comedie"
        assert not Piesa("a","b","Comedie",12).get_gen()=="Satira"

    def test_gen_durata(self):
        assert Piesa("a","b","Comedie",12).get_durata()==12
        assert not Piesa("a","b","Comedie",12).get_durata()==10

    def test_validare_piesa(self):
        self.__valid.validare_piesa(Piesa("a","b","Comedie",12))
        try:
            self.__valid.validare_piesa(Piesa("","","c",-12))
            assert False
        except ValidError as e:
            assert str(e)=="Titlu invalid\nRegizor invalid\nGen invalid\nDurata invalida\n"
        try:
            self.__valid.validare_piesa(Piesa("a","a","c",-12))
            assert False
        except ValidError as e:
            assert str(e)=="Gen invalid\nDurata invalida\n"

    def test_validare_titlu(self):
        assert self.__valid.validare_titlu(Piesa("a","b","Comedie",12))
        assert not self.__valid.validare_titlu(Piesa("","b","Comedie",12))

    def test_validare_regizor(self):
        assert self.__valid.validare_regizor(Piesa("a", "b", "Comedie", 12))
        assert not self.__valid.validare_regizor(Piesa("a","","Comedie",12))

    def test_validare_gen(self):
        assert self.__valid.validare_gen(Piesa("a","b","Comedie",12))
        assert self.__valid.validare_gen(Piesa("a", "b", "Drama", 12))
        assert self.__valid.validare_gen(Piesa("a", "b", "Satira", 12))
        assert self.__valid.validare_gen(Piesa("a", "b", "Altele", 12))
        assert not self.__valid.validare_gen(Piesa("a", "b", "comedy", 12))

    def test_validare_durata(self):
        assert self.__valid.validare_durata(Piesa("a", "b", "Comedie", 12))
        assert not self.__valid.validare_durata(Piesa("a", "b", "Comedie", -12))

    def test_service_adaugare(self):
        try:
            self.__service.service_adaugare("ana","are","Comedie",4)
            assert False
        except RepoError as e:
            assert str(e)=="Piesa a mai fost adaugata deja! "
        self.__service.service_adaugare("k","k","Comedie",5)
        assert Piesa("k","k","Comedie",5) in self.__repo.get_all()
        self.__repo.delete()
        try:
            self.__service.service_adaugare("","","",-5)
            assert False
        except ValidError as e:
            assert str(e)=="Titlu invalid\nRegizor invalid\nGen invalid\nDurata invalida\n"

    def test_service_get_all(self):
        assert self.__service.get_all()==[Piesa("ana","are","Comedie",4),Piesa("a","b","Drama",8),Piesa("d","e","Satira",19)]

    def test_repo_get_all(self):
        assert self.__repo.get_all()==[Piesa("ana", "are", "Comedie", 4), Piesa("a", "b", "Drama", 8),
                                          Piesa("d", "e", "Satira", 19)]

    def test_load_from_file(self):
        #load from file se apeleaza in inceputul programului
        assert self.__service.get_all()==[Piesa("ana", "are", "Comedie", 4), Piesa("a", "b", "Drama", 8),
                                          Piesa("d", "e", "Satira", 19)]

    def test_update_file(self):
        self.__repo.update_file()
        f=open("fisier_test.txt","r")
        assert f.read()=="ana,are,Comedie,4\na,b,Drama,8\nd,e,Satira,19\n"
        f.close()

    def test_repo_adaugare(self):
        try:
            self.__repo.repo_adaugare(Piesa("ana","are","Comedie",4))
            assert False
        except RepoError as e:
            assert str(e)=="Piesa a mai fost adaugata deja! "
        self.__repo.repo_adaugare(Piesa("k","k","Comedie",5))
        assert Piesa("k","k","Comedie",5) in self.__repo.get_all()
        self.__repo.delete()

    def test_validare_unicitate(self):
        try:
            self.__repo.validare_unicitate(Piesa("ana", "are", "Comedie", 4))
            assert False
        except RepoError as e:
            assert str(e)=="Piesa a mai fost adaugata deja! "
        self.__repo.validare_unicitate(Piesa("k", "k", "Comedie", 5))

    def test_delete(self):
        self.__repo.delete()
        assert not Piesa("d","e","Satira",19) in self.__repo.get_all()
        self.__repo.repo_adaugare(Piesa("d","e","Satira",19))

    def test_service_modificare(self):
        try:
            self.__service.modificare("aaaaa","Aaaaaa","Comedie",12)
            assert False
        except RepoError as e:
            assert str(e)=="Piesa nu exista! "
        try:
            self.__service.modificare("","","Comedie",12)
            assert False
        except ValidError as e:
            assert str(e)=="Titlu invalid\nRegizor invalid\n"
        self.__service.modificare("ana","are","Satira",5)
        for i in self.__service.get_all():
            if i==Piesa("ana","are","Satira",5):
                assert i.get_gen()=="Satira"
                assert i.get_durata()==5
                break
        self.__service.modificare("ana", "are", "Comedie", 4)

    def test_repo_modificare(self):
        try:
            self.__repo.repo_modificare(Piesa("aaaaa", "Aaaaaa", "Comedie", 12))
            assert False
        except RepoError as e:
            assert str(e)=="Piesa nu exista! "
        self.__repo.repo_modificare(Piesa("ana","are","Satira",5))
        for i in self.__repo.get_all():
            if i==Piesa("ana","are","Satira",5):
                assert i.get_gen()=="Satira"
                assert i.get_durata()==5
                break
        self.__repo.repo_modificare(Piesa("ana", "are", "Comedie", 4))

    def test_export(self):
        self.__service.exportare("export_test.txt")
        f=open("export_test.txt")
        assert f.read()=="are,ana,4,Comedie\nb,a,8,Drama\ne,d,19,Satira\n"
        f.close()
        self.__service.service_adaugare("aa","are","Comedie",5)
        self.__service.exportare("export_test.txt")
        self.__repo.delete()
        f=open("export_test.txt","r")
        assert f.read()=="are,aa,5,Comedie\nare,ana,4,Comedie\nb,a,8,Drama\ne,d,19,Satira\n"
        f.close()

    def test_generare_aleatoare(self):
        vocale = ["a", "e", "i", "o", "u"]
        consoane = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
                    "z"]
        string=list(self.__service.generare_aleatoare())
        assert " " in string
        assert len(string)>=8 and len(string)<=12
        string=list(string)
        for i in range(0,len(string)-1):
            if string[i] in vocale:
                assert string[i+1] in consoane or string[i+1]==" "
            else:
                assert string[i+1] in vocale or string[i+1]==" "

    def test_creare(self):
        lungime=len(self.__repo.get_all())
        assert len(self.__service.creare(4))==4
        assert len(self.__repo.get_all())==lungime+4
        for i in range(4):
            self.__repo.delete()


    def run_all(self):
        self.test_generare_aleatoare()
        self.test_set_durata()
        self.test_set_gen()
        self.test_gen_durata()
        self.test_get_gen()
        self.test_get_regizor()
        self.test_get_titlu()
        self.test_validare_durata()
        self.test_validare_gen()
        self.test_validare_regizor()
        self.test_validare_titlu()
        self.test_validare_piesa()
        self.test_service_adaugare()
        self.test_service_get_all()
        self.test_repo_get_all()
        self.test_load_from_file()
        self.test_update_file()
        self.test_repo_adaugare()
        self.test_validare_unicitate()
        self.test_delete()
        self.test_service_modificare()
        self.test_repo_modificare()
        self.test_export()
        self.test_creare()