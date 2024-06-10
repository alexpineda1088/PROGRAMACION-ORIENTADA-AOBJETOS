def daño(self, enemigo):
    raise NotImplementedError("Este método debe ser implementado por las subclases")


def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida -= daño
    print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
    if enemigo.esta_vivo():
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
    else:
        enemigo.morir()