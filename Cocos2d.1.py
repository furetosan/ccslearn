#!/usr/local/bin/python2.7
# coding: utf-8

# In[1]:

import cocos
import pyglet


# In[2]:

from cocos.actions import *


# In[3]:

class HelloWorld(cocos.layer.ColorLayer):
    def __init__(self):
        super(HelloWorld,self).__init__(64,64,224,255)
        label = cocos.text.Label('O MEU momento... do Fred!',
                                font_name='Arial',
                                 font_size=32,
                                 anchor_x='center',
                                 anchor_y='center'
                                )
        label.position = 320,240
        self.add(label)
        # This WILL take relative paths
        img = pyglet.image.load('grossini.png')
        sprite = cocos.sprite.Sprite(img)
        sprite.position = 320,240
        sprite.scale = 3
        scale = ScaleBy(3, duration=2)
        self.add(sprite, z=1)
        label.do(Repeat(scale+Reverse(scale)))
        sprite.do(Repeat(Reverse(scale)+scale))


cocos.director.director.init()
hello_layer = HelloWorld()
hello_layer.do(RotateBy(360, duration=10))
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)

