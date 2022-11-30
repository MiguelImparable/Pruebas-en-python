import os

# Un programa que realice un juego de barajas según especificaciones técnicas.
def Exercise_RETO4():
    os.system ("cls"); print("\nExercise RETO4")

    def tiene_cartas_altas(cartas_siguientes):
        hay_cartas_altas = False

        for i in cartas_siguientes:
            if "A" in cartas_siguientes or "J" in cartas_siguientes or "Q" in cartas_siguientes or "K" in cartas_siguientes:
                hay_cartas_altas = True

        return hay_cartas_altas

    def juego(baraja):
        puntaje_jugador1 = 0; puntaje_jugador2 = 0; x = 0

        while x < (len(baraja)):

            if baraja[x] == "A":
                if tiene_cartas_altas(baraja[x + 1:x + 2]) == False:
                    if (x + 1) < (len(baraja)):
                        if x % 2 == 0:
                            puntaje_jugador1 += 1
                        elif x % 2 != 0:
                            puntaje_jugador2 += 1

            if baraja[x] == "J":
                if tiene_cartas_altas(baraja[x + 1:x + 3]) == False:
                    if (x + 2) < (len(baraja)):
                        if x % 2 == 0:
                            puntaje_jugador1 += 2
                        elif x % 2 != 0:
                            puntaje_jugador2 += 2

            if baraja[x] == "Q":
                if tiene_cartas_altas(baraja[x + 1:x + 4]) == False:
                    if (x + 3) < (len(baraja)):
                        if x % 2 == 0:
                            puntaje_jugador1 += 3
                        elif x % 2 != 0:
                            puntaje_jugador2 += 3

            if baraja[x]=="K":
                if tiene_cartas_altas(baraja[x+1:x+5])==False:
                    if (x+4)<(len(baraja)):
                        if x%2==0:
                            puntaje_jugador1+=4
                        elif x%2!=0:
                            puntaje_jugador2+=4

            x += 1

        return (puntaje_jugador1, puntaje_jugador2)

    baraja_=juego(['9', '6', '5', '7', 'J', '10', '10', 'K', '8', 'K', '9', 'A', '2', 'K', 'K', '4', 
                  '10', 'Q', '10', 'Q', '4', '3', '4', '2', 'A', '7', '2', 'J', '3', '6', '5', '5', 
                  'A','8','2','A','J','8','8','6','3','3','9','5','6','7','Q','9','Q','4','J','7'])

    print(baraja_)
    print("\nEnd of program\n")
    
if __name__ == "__main__":
    Exercise_RETO4()