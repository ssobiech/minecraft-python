import mcpi.minecraft as minecraft
from os import environ
import mcpi.connection as conn
import sys
import logger

gracz = "Spock"
server ="spock.nazwa.pl"
port = 4711
environ["MINECRAFT_PLAYER_NAME"] = gracz

logger = logger.Logger()


def polacz():
    try:
        mc = minecraft.Minecraft.create(server, port)
        if mc.player.getName() == gracz:
            logger.info("użytkownik %s został podłączony do serwera %s" % (mc.player.getName(), server + ":" + str(port)))
            return mc
        else:
            '''logger.error("podlaczono, ale brak mozliwosci identyfikacji gracza %s " % gracz)'''
            raise conn.RequestError("podlaczono do niewlasciwego gracza %s " % mc.player.getName())
    except conn.RequestError as err:
        logger.error("problem z podlaczeniem do serwera. Błąd: " + err.__str__())
        raise

def podlacz():
    mc = polacz()
    return mc


if __name__ == "__main__":
    podlacz()
