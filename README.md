# ! EM DESENVOLVIMENTO !



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
 - pyscreenshot
 - os
 - sys

# 1 - Processo da primeira utilização:
## 1.1 Faça o git clone ou download ZIP

Vá para a pasta ou extraia do ZIP

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
clipboardfin=")"
```

# 3 Definições do printscren com o pyscreenshot, 
Como exemplo, para fazer a próximas alterações, utilizei o programa xdotool para encontrar valores da posição do mouse e utilizei o xclip para copiar o arquivo automaticamente

## 3.1 Adquirindo as informações da posição do mouse: (COM XCLIP INSTALADO)
Para um print screen são necessários 4 pontos de localização do mouse, por conveniencia separamos em:
 - Canto Superior Esquerdo
 - Canto Inferior Direito

### Coloque a posição do mouse **NO CANTO SUPERIOR ESQUERDO** onde você quer e **Execute**:
```
eval $(xdotool getmouselocation --shell);echo X1=\"$X\"$'\n'Y1=\"$Y\" | xclip -selection clipboard 
```
Abra o arquivo **pyshot.py** com um editor de texto e substitua as linhas 11 e 12 pelos valores no clipboard (ctrl+v)

### Coloque a posição do mouse **NO CANTO INFERIOR DIREITO** onde você quer e **Execute**:
```
eval $(xdotool getmouselocation --shell);echo X2=\"$X\"$'\n'Y2=\"$Y\" | xclip -selection clipboard 
```
No arquivo **pyshot.py** substitua as linhas 16 e 17 pelos valores no clipboard (ctrl+v)

## 3.2 Adquirindo as informações da posição do mouse: (SEM XCLIP INSTALADO)
Para um print screen são necessários 4 pontos de localização do mouse, por conveniencia separamos em:
 - Canto Superior Esquerdo
 - Canto Inferior Direito

### Coloque a posição do mouse **NO CANTO SUPERIOR ESQUERDO** onde você quer e **Execute**:
```
eval $(xdotool getmouselocation --shell);echo X1=\"$X\"$'\n'Y1=\"$Y\" 
```
Abra o arquivo **pyshot.py** com um editor de texto e substitua as linhas 11 e 12 pelos valores no shell

### Coloque a posição do mouse **NO CANTO INFERIOR DIREITO** onde você quer e **Execute**:
```
eval $(xdotool getmouselocation --shell);echo X2=\"$X\"$'\n'Y2=\"$Y\"
```
No arquivo **pyshot.py** substitua as linhas 16 e 17 pelos valores no shell

