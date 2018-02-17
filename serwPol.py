import mcpi.minecraft as minecraft
from os import environ
import logger

gracz = "souza539"
server ="spock.nazwa.pl"
port = 4711
environ["MINECRAFT_PLAYER_NAME"] = gracz

logger = logger.Logger()


def polacz():
    mc = minecraft.Minecraft.create(server, port)
    logger.info("użytkownik " + mc.player.getName() + " został podłączony do serwera " + server + ":" + str(port))
    return mc


def podlacz():
    mc = polacz()
    return mc


if __name__ == "__main__":
    podlacz()
