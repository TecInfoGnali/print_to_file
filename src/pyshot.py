# ---------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------------
import pyscreenshot

# part of the screen
im = pyscreenshot.grab(bbox=(37, 332, 960, 848))  # X1,Y1,X2,Y2

# save image file
im.save("UltimaCaptura.png")