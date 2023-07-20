# Aplicativo  - print_to_file -
Aplicativo utilizando linguagem de programação básica de Shell e Python 3.8 que executa um printscreen em uma área pré determinada e salva em uma pasta pré determinada.

## Requisitos:

### Básico em shell script:
python
xclip
xdotool

### Bibliotecas utilizadas:
python:
pyscreenshot
os
sys

# 1 - Processo da primeira utilização:
Faça o git clone ou download ZIP

Abra essa pasta no terminal e execute
~/.../print_to_file/$
```
cd src
chmod +x Print_to_File.sh
chmod +x exec.sh
```

_Caso não queira criar um atalho, pule esta etapa:_
## 1.1 - Para que seja possível criar um atalho no Linux para execução da aplicação, o próximo passo é imprescindivel.

Abra o arquivo **Print_to_File.sh** e altere o valor "/complete/path/to/this/archive" para o caminho até esta pasta.

exemplo:

de:
```
cd /complete/path/to/this/archive
./exec.sh
```
para:
```
cd /home/USER/Aplicativos/print_to_file/src
./exec.sh
```

Abra o arquivo **exec.sh** e faça as seguintes alterações

