# Created by: Scarlett Gao
# Created on: Sep 2017
# Created for: ICS3U
# This program is the Hello, World program, but with 3 buttons

import ui

def english_touch_up_inside(sender):
    # displays the English version
    view['hello_world_label'].text = ('Hello, World!')
    
def french_touch_up_inside(sender):
    # displays the French version
    view['hello_world_label'].text = ('Bonjour le monde!')
    
def spanish_touch_up_inside(sender):
    # displays the Spanish version
    view['hello_world_label'].text = ('¡Hola Mundo!')

# note that now the app runs full screen
view = ui.load_view()
view.present('full_screen')
