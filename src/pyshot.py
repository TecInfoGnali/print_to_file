# ---------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------------
import pyscreenshot


#Valores adquiridos a partir do xdotool com o comando:

#CANTO SUPERIOR ESQUERDO
# Sem XCLIP
# eval $(xdotool getmouselocation --shell);echo X1=\"$X\"$'\n'Y1=\"$Y\" 
X1="37"
Y1="332"

#CANTO INFERIOR DIREITO
# Sem XCLIP
# eval $(xdotool getmouselocation --shell);echo X2=\"$X\"$'\n'Y2=\"$Y\" 
X2="960"
Y2="848"

# part of the screen
im = pyscreenshot.grab(bbox=(X1, Y1, X2, Y2))  # X1,Y1,X2,Y2

# save image file
im.save("UltimaCaptura.png")
