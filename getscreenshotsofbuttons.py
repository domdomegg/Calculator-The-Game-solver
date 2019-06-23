import warnings
warnings.filterwarnings("ignore")

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gdk

# TODO: not this
#warnings.filterwarnings("default")


window = Gdk.get_default_root_window()
screen = window.get_screen()
typ = window.get_type_hint()
for i, w in enumerate(screen.get_window_stack()):
	if w.get_height() > 1400 and w.get_height() < 1600:
		pb = Gdk.pixbuf_get_from_window(w, *w.get_geometry())
		pb.savev("game.png".format(i), "png", (), ())


from PIL import Image
img = Image.open("game.png")

button1img = img.crop((270, 630, 270+200, 630+130))
button1img.save("button1img.png")

button2img = img.crop((270, 630+192, 270+200, 630+192+130))
button2img.save("button2img.png")

button3img = img.crop((270, 630+192*2, 270+200, 630+192*2+130))
button3img.save("button3img.png")

button4img = img.crop((270+234, 630+192, 270+234+200, 630+192+130))
button4img.save("button4img.png")

button5img = img.crop((270+234, 630+192*2, 270+234+200, 630+192*2+130))
button5img.save("button5img.png")

movesimg = img.crop((394,186,394+36,186+36))
movesimg.save("movesimg.png")

goalimg = img.crop((475,190,475+178,190+27))
goalimg.save("goalimg.png")

startimg = img.crop((303,275,303+365,275+155))
startimg.save("startimg.png")