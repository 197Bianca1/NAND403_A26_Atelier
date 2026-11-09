import os 
import sys

#on a obtenue le folder dans lequel il y a notre fichier courant
# __file__ = le fichier courant
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_file_path)
# ici on vient ajouter aobsolute_folder_path au path de python pour qu'il trouve
sys.path.append(absolute_folder_path)

import ui 
import importlib
importlib.reload(ui)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    random_animation_ui = ui.randomanimationUI
    random_animation_ui.show
 
main()