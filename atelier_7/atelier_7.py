import maya.cmds as cmds

def animation_cvalry():

    cmds.playbackOptions(min = 0, max = 100)

    obj = cmds.ls(selection=True) 

    cmds.setKeyframe(obj, attribute = 'translateX', value = 0, time = 0)
    cmds.setKeyframe(obj, attribute = 'translateX', value = 10, time = 50)
    cmds.setKeyframe(obj, attribute = 'translateX', value = 20, time = 100)

animation_cvalry()


