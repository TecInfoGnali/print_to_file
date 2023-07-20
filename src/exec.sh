#!/bin/bash


#---------------------------------------------------------------------------------------------#
# DEFINIÇÃO DE INICIAL DO ARQUIVO                                                             #
#---------------------------------------------------------------------------------------------#

#Substitua XX pela inicial que irá usar
inicial_arquivo="XX"

#Substitua $(pwd) pelo endereço da pasta onde estão seus prints numerados
pasta_destino=$(pwd)

#Define a pasta de origem como a pasta atual
pasta_origem=$(pwd)

#Definição de formato do print
format_print=".png"

#Define a pasta de origem como a pasta atual
#antes no nome do arquivo
clipboardini="![](./"
#depois do nome do arquivo
clipboardfin=")"

#
#  EXECUÇÃO DE APLICAÇÕES EM PYTHON
#

#executa a aplicação de printscreen em Python
#Caso sua versão seja diferente, verifique sua versão digitando python e pressionando Tab duas vezes
print=$(python3.8 $pasta_origem/pyshot.py)

proxima_seq=$(python3.8 $pasta_origem/proxima_seq.py $pasta_destino)

# Verifica se retornou uma sequência inteira positiva e cria o arquivo
if [[ $proxima_seq =~ ^[0-9]+$ ]]; then
   if [ $proxima_seq -gt -1 ]; then
       mv $pasta_origem/UltimaCaptura$format_prin $pasta_destino/$inicial_arquivo$proxima_seq$format_prin     
   fi
else
   echo "ERRO: "$proxima_seq >&2; exit 1 
fi 

# # Para habilitar o salvamento do caminho para o arquivo no clipboard, retire o Comentário do ítem abaixo
# echo $clipboardini$inicial_arquivo$proxima_seq$format_print$clipboardfin | xclip -selection clipboard

sleep 0.1







