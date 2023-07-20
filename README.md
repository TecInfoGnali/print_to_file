# Aplicativo  - print_to_file -
Aplicativo utilizando linguagem de programação básica em Shell e Python 3.8 que:
 - Executa print screen utilizando o formato padrão do SO - .png
 - Verifica se há numeração pré existente de arquivos em uma pasta determinada
 - Define nomenclatura com incremento em relação ao maior numero encontrado na pasta
 - Gera um texto para o clipboard com formatação pré definida para colar no ambiente desejado

Aplicação desenvolvida e testada em **SO** Linux, **Distribuição** Ubuntu v.20.04.6 LTS em **ambiente** X11

## Requisitos:

 - Básico em shell script
 - Instalação do python
 - Instalação do xclip
 - Instalação do xdotool

### Bibliotecas utilizadas:
python:
pyscreenshot
os
sys

# 1 - Processo da primeira utilização:
## 1.1 Faça o git clone ou download ZIP

## 1.2 Primeiras ações:

Abra essa pasta no terminal e execute
~/.../print_to_file/$
```
cd src
chmod +x Print_to_File.sh
chmod +x exec.sh
```


## 1.3 - Para que seja possível criar um atalho no Linux para execução da aplicação, o próximo passo é imprescindivel. (Etapa não obrigatória)

Abra o arquivo **Print_to_File.sh** e altere o valor "$(pwd)" para o caminho até esta pasta.

exemplo:

de:
```
cd $(pwd)
./exec.sh
```
para:
```
cd /home/USER/Aplicativos/print_to_file/src
./exec.sh
```
# 2 - Alterações de pasta de destino, nomenclatura.
Abra o arquivo **exec.sh** e faça as seguintes alterações.

## 2.1 Definição de inicial do arquivo

de:
```
inicial_arquivo="XX"
```

para:
```
inicial_arquivo="AB"
```

## 2.2 Definição de pasta de destino

de:
```
pasta_destino=$(pwd)
```

para:
```
pasta_destino=/home/USER/Imagens/predeterminado
```

## 2.3 Definição de Formato

Altere de acordo com a sua necessidade, aqui está configurado com o padrão do meu SO:

```
format_print=".png"
```

## 2.4 Definição de clipboard

Altere de acordo com a sua necessidade, aqui está configurado para usar o clipboard em arquivo .md (markdown):

```
clipboardini="![](./"
clipboardfin=".png)"
```



