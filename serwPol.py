import mcpi.minecraft as minecraft
from os import environ

gracz = "Wurtexoi"
server ="172.20.10.2"

def setUser():
    environ["MINECRAFT_PLAYER_NAME"] = gracz
    print("ustawiono gracza o nicku: "+ environ["MINECRAFT_PLAYER_NAME"])


def polacz():
    mc = minecraft.Minecraft.create(server,4711)
    print("podlaczono do serwera: " + str(server))
    return mc

def podlacz():
    setUser()
    mc = polacz()
    return mc
    
if __name__ == "__main__":
    podlacz()
