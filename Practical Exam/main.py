#Modulul principal
from teste import Teste
from prezentare import Console
from business import Service
from infrastructura import Repo
from validator import Valid
teste=Teste()
teste.run_all()
repo=Repo("fisier.txt")
valid=Valid()
service=Service(repo,valid)
ui=Console(service)
ui.run()
