from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint
def init():
	# change 192.168.0.68 to 127.0.0.1 or your ip
	mc = Minecraft.creat("127.0.0.1", 4711)
	x,y,x = mc.player.getPos()
	return mc
	
#main
def main():
	mc = init()
	mc.player.setPos(0,0,0)
	x, y, z = mc.player.getPos()
	mc.setBlocks(x-50, y-20, z, x+50, y+50, z+25, 0)
	mc.setBlocks(x-2, y, z+3, x, y+5, z+5, 24)
