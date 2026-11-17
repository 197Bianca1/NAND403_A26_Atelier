import random

import maya.cmds as cmds

from tp3 import ui


class animator:
   def __init__(self):
    super().__init__()

    self.ui = ui
 
    self.animation()

    def animation(self):

       ob = cmds.ls(selection=True, type='transform')

       if not ob:
           cmds.warning("No object selected. Please select an object to animate.")
           return

       duration = self.ui.duration_spinbox.value()

       interval = self.ui.interval_spinbox.value()

       cmds.playbackOptions(min=0, max=duration)

       attribute = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ']

       cmds.undoInfo(openChunk=True, chunkName='Animation')

      
