from Board import MostrarTablero
from CodeBreaker import minimax
from Evaluation import Evaluacion
import chess
import pygame as py

# Variables del minmax
MAX, MIN = 100000, -100000
Profundidad = 4

Tablero = chess.Board()
display = MostrarTablero(Tablero)


def Mover():
    Posible_Movimiento_Jugador = display.square_select(py.mouse.get_pos())
    if Posible_Movimiento_Jugador != None:
        try:
            eval = Evaluacion(Tablero, display.player_color)
            is_late_game = eval.is_late_game()

            if display.player_color == "W":
                MueveBlanco(Posible_Movimiento_Jugador, is_late_game)
                MueveNegro(Posible_Movimiento_Jugador, is_late_game)
            else:
                MueveNegro(Posible_Movimiento_Jugador, is_late_game)
                MueveBlanco(Posible_Movimiento_Jugador, is_late_game)
        except:
            print("Invalid Move")

def MueveBlanco(move, is_late_game):

    if display.player_color == "W":
        Tablero.push_uci(move)
    else:
        # El atributo para la profundidad debe ser impar
        if is_late_game:
            white = minimax(Profundidad + 1, True, MIN, MAX, Tablero, True)
        else:
            white = minimax(Profundidad + 1, True, MIN, MAX, Tablero, True)

        Tablero.push(white)

    display.update(Tablero)

def MueveNegro(move, is_late_game):

    if display.player_color == "B":
        Tablero.push_uci(move)
    else:
         # El atributo para la profundidad debe ser par
        if is_late_game:
            black = minimax(Profundidad + 2, False, MIN, MAX, Tablero, True)
        else:
            black = minimax(Profundidad, False, MIN, MAX, Tablero, True)
        Tablero.push(black)

    display.update(Tablero)

def is_game_over(board):
    if board.is_game_over():
        display.run = False
        display.game_over = True
        display.game_over_menu()

def Ejecutar():

    if display.player_color == "B":
        MueveBlanco(None, False)

    while display.run:
        events = py.event.get()
        for event in events:
            if event.type == py.QUIT:
                exit()

            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                Mover()
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 3:
                display.remove_square_select()

        display.update_screen()
        is_game_over(Tablero)

def ConfigurarJuego():
    Tablero.reset_board()
    display.main_menu()
    display.update(Tablero)
    Ejecutar()

while Ejecutar:
    ConfigurarJuego()

py.quit()
