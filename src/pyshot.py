# ---------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------------
import pyscreenshot


#Valores adquiridos a partir do xdotool com o comando:

#CANTO SUPERIOR ESQUERDO
# Sem XCLIP
# eval $(xdotool getmouselocation --shell);echo X1=\"$X\"$'\n'Y1=\"$Y\" 
x1="37"
y1="332"

#CANTO INFERIOR DIREITO
# Sem XCLIP
# eval $(xdotool getmouselocation --shell);echo X2=\"$X\"$'\n'Y2=\"$Y\" 
x2="960"
y2="848"

# Ação da aplicação
im = pyscreenshot.grab(bbox=(x1, y1, x2, y2))  # X1,Y1,X2,Y2

# Nome da imagem salva
im.save("UltimaCaptura.png")
