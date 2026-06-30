# python-for-devops
Python para projetos de automação do mundo de DevOps



###  Virtual Environment = .venv

.venv é um ambiente virtual do Python, que permite criar um espaço isolado para instalar pacotes e dependências sem afetar o sistema global.

instalação no teminal do Linux:
'sudo apt install python3.10-venv'

instalar pelo pip:
'pip install virtualenv'

setup inicial, chamada do modulo venv para criar o ambiente virtual:
'python3 -m venv .venv'

ativação do ambiente virtual:
'source .venv/bin/activate'

desativação do ambiente virtual:
'deactivate'

checa qual o ambiente virtual está sendo usado:
'which python'

ver os diretórios onde as libs estão instaladas
'pip list -v'
