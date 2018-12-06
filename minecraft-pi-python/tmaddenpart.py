from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

def init():
	#change 10.183.0.68 to 127.0.0.1 or your ip
	mc = Minecraft.create("127.0.0.1", 4711)
	x,y,z = mc.player.getPos()
	return mc
	
#main
def clear_with_air():
	mc = init()
	air = 0
	mc.setBlocks(x-h, y-k, z-l, x+h, y+k, z+l, air)
	return mc	
def main():	
	mc = init()
	x, y, z = mc.player.getPos()
	a, b, c = mc.player.getPos()
	while(int(x)+int(z) == int(a)+int(c)):
		a, b, c =mc.player.getPos()
	z+=4
	y+=0
	
	#stating out with sand
	mc.setBlocks(x+40,y-7,z,x-10,y,z+20, 12)
	
	#outline of upper
	mc.setBlocks(x-2, y, z, x-2, y+6, z+6, 24)
	mc.setBlocks(x-1, y, z, x-1, y+6, z+6, 24)
	mc.setBlocks(x, y, z, x, y+6, z+6, 24)
	mc.setBlocks(x+1, y, z,x+1,y+6,z+6, 24)
	mc.setBlocks(x+2,y,z,x+2,y+6,z+6, 24)
	mc.setBlocks(x-5,y,z+7,x+7,y+6,z+7, 24)
	mc.setBlocks(x+8,y,z+8,x+20,y+7,z+8, 24)
	
	#upper
	mc.setBlocks(x-5,y,z+7,x+7,y+6,z+8,24)
	mc.setBlocks(x-5,y,z+9,x+19,y+7,z+14,24)
	mc.setBlocks(x+9,y,z+15,x+5,y+6,z+19,24)
	#air for tunnels
	mc.setBlocks(x-1,y,z,x,y+3,z+10, 0)
	mc.setBlocks(x,y,z,x,y+4,z+10, 0)
	mc.setBlocks(x+1,y,z,x,y+3,z+10, 0)
	mc.setBlocks(x+6,y,z+14,x+6,y+3,z+18, 0)
	mc.setBlocks(x+7,y,z+14,x+7,y+4,z+18, 0)
	mc.setBlocks(x+8,y,z+14,x+8,y+3,z+18, 0)

	#air for upper
	mc.setBlocks(x-4,y,z+8,x+6,y+5,z+8,0)
	mc.setBlocks(x-4,y,z+9,x+18,y+5,z+13,0)
	mc.setBlocks(x-4,y,z+15,x-8,y+5,z+18,0)
	mc.setBlocks(x-6,y,z+15,x-6,y+5,z+18,0)
	mc.setBlocks(x+7,y+6,z+11,x+8,y+14,z+12, 0)
	mc.setBlocks(x+16,y+6,z+11,x+16,y+14,z+13, 0)
	mc.setBlocks(x+15,y+6,z+11,x+15,y+14,z+12, 0)
	
	#things inside uppers
	mc.setBlocks(x-2,y,z+8,x-3,y+3,z+9, 5)
	mc.setBlocks(x-4,y,z+8,x-4,y+3,z+9, 17)
	
	mc.setBlocks(x,y,z+13,x,y+3,z+13, 1)
	mc.setBlocks(x,y+4,z+13,x,y+4,z+13, 89)
	mc.setBlocks(x,y+5,z+13,x,y+5,z+13, 4)
	
	mc.setBlocks(x-4,y,z+13,x-4,y+3,z+13, 1)
	mc.setBlocks(x-4,y+4,z+13,x-4,y+4,z+13, 89)
	mc.setBlocks(x-4,y+5,z+13,x-4,y+5,z+13, 4)
	
	mc.setBlocks(x+4,y,z+13,x+4,y+3,z+13, 1)
	mc.setBlocks(x+4,y+4,z+13,x+4,y+4,z+13, 89)
	mc.setBlocks(x+4,y+5,z+13,x+4,y+5,z+13, 4)
	
	mc.setBlocks(x+12,y,z+13,x+12,y+3,z+13, 1)
	mc.setBlocks(x+12,y+4,z+13,x+12,y+4,z+13, 89)
	mc.setBlocks(x+12,y+5,z+13,x+12,y+5,z+13, 4)
	
	mc.setBlocks(x+5,y,z+9,x+5,y+3,z+9, 1)
	mc.setBlocks(x+5,y+4,z+9,x+5,y+4,z+9, 89)
	mc.setBlocks(x+5,y+5,z+9,x+5,y+5,z+9, 4)
	
	mc.setBlocks(x+9,y,z+9,x+9,y+3,z+9, 1)
	mc.setBlocks(x+9,y+4,z+9,x+9,y+4,z+9, 89)
	mc.setBlocks(x+9,y+5,z+9,x+9,y+5,z+9, 4)
	
	mc.setBlocks(x+4,y,z+9,x+4,y,z+10, 5)
	mc.setBlocks(x+12,y,z+9,x+12,y,z+10, 5)
	mc.setBlocks(x+13,y,z+9,x+14,y+1,z+10, 5)
	
	#stairs into lower aired out
	
	mc.setBlocks(x+17,y,z+13,x+18,y-3,z+9, 0)
	mc.setBlocks(x+15,y-1,z+6,x+26,y-3,z+8, 0)
	

	#stairs
	
	mc.setBlocks(x+16,y-1,z+9,x+16,y-1,z+13, 53,1)
	
	mc.setBlocks(x+17,y-1,z+13,x+18,y-1,z+13, 53,2)
	mc.setBlocks(x+17,y-2,z+12,x+18,y-2,z+12, 53,2)
	mc.setBlocks(x+17,y-3,z+11,x+18,y-3,z+11, 53,2)
	
	#outline of lowers
	
	mc.setBlocks(x+15,y,z+6,x+27,y,z+8, 24)
	mc.setBlocks(x+27,y,z+6,x+27,y-3,z+8, 24)
	mc.setBlocks(x+15,y,z+5,x+27,y-3,z+5, 24)
	
	
	mc.setBlocks(x+19,y,z+6,x+21,y,z+6, 0)
	mc.setBlocks(x+20,y,z+6,x+20,y,z+7, 0)
	mc.setBlocks(x+24,y,z+6,x+25,y,z+7, 0)
	
	
	
	#lower items
	
	mc.setBlocks(x+16,y-3,z+8,x+15,y-2,z+8, 1)
	mc.setBlocks(x+16,y-1,z+8,x+15,y-1,z+8, 89)
	
	mc.setBlocks(x+15,y-3,z+6,x+15,y-3,z+6, 24)
	
	mc.setBlocks(x+22,y-2,z+8,x+23,y-3,z+8, 5)
	
	block = ['sandy','other']
	if(mc.getBlock(x,y,z)>0):
		mc.postToChat("not very sandy floor")
	else:
		mc.postToChat("very sandy floor")

main()


# multiple line comment
"""
AIR                   0
STONE                 1
GRASS                 2
DIRT                  3
COBBLESTONE           4
WOOD_PLANKS           5
SAPLING               6
BEDROCK               7
WATER_FLOWING         8
WATER                 8
WATER_STATIONARY      9
LAVA_FLOWING         10
LAVA                 10
LAVA_STATIONARY      11
SAND                 12
GRAVEL               13
GOLD_ORE             14
IRON_ORE             15
COAL_ORE             16
WOOD                 17
LEAVES               18
GLASS                20
LAPIS_LAZULI_ORE     21
LAPIS_LAZULI_BLOCK   22
SANDSTONE            24
BED                  26
COBWEB               30
GRASS_TALL           31
WOOL                 35
FLOWER_YELLOW        37
FLOWER_CYAN          38
MUSHROOM_BROWN       39
MUSHROOM_RED         40
GOLD_BLOCK           41
IRON_BLOCK           42
STONE_SLAB_DOUBLE    43
STONE_SLAB           44
BRICK_BLOCK          45
TNT                  46
BOOKSHELF            47
MOSS_STONE           48
OBSIDIAN             49
TORCH                50
FIRE                 51
STAIRS_WOOD          53
CHEST                54
DIAMOND_ORE          56
DIAMOND_BLOCK        57
CRAFTING_TABLE       58
FARMLAND             60
FURNACE_INACTIVE     61
FURNACE_ACTIVE       62
DOOR_WOOD            64
LADDER               65
STAIRS_COBBLESTONE   67
DOOR_IRON            71
REDSTONE_ORE         73
SNOW                 78
ICE                  79
SNOW_BLOCK           80
CACTUS               81
CLAY                 82
SUGAR_CANE           83
FENCE                85
GLOWSTONE_BLOCK      89
BEDROCK_INVISIBLE    95
STONE_BRICK          98
GLASS_PANE          102
MELON               103
FENCE_GATE          107
GLOWING_OBSIDIAN    246
NETHER_REACTOR_CORE 247
"""

