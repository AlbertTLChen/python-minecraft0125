from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=200
y=200
z=100
import time
mc.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

mc.player.setTilePos(x,y,z)
time.sleep(2)

x=x-50
y=y-50

mc.player.setTilePos(x,y,z)