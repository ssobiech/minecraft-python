import serwPol
import logger
from mcpi import block


def figura(pos, r, a, b):
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            for k in range(-r, r + 1):
                if ((i ** 2) / 1 ** 2 - (k ** 2) / a ** 2 <= j * 2) and (
                        (i ** 2) / 1 ** 2 - (k ** 2) / b ** 2 > j * 2 - 10):
                    mc.setBlock(pos.x + i, pos.y + j, pos.z + k, block.STONE.id, 2)


if __name__ == "__main__":
    mc = serwPol.podlacz()
    logger = logger.Logger()
    pos = mc.player.getTilePos()
    figura(pos, 10, 2, 2)
