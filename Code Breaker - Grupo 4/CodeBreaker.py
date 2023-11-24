from Evaluation import Evaluacion

MAX, MIN = 100000, -100000

# Devuelve el valor óptimo para el jugador actual
# (Inicialmente llamado para raíz y maximizador)
def minimax(Profundidad, JugadorMaximizado, alpha, beta, board, PrimerMovimiento):

    # Condición de terminación.
    # se alcanza el nodo hoja
    if (Profundidad == 0) or (board.is_game_over()):

        if JugadorMaximizado:
            eval = Evaluacion(board, "W")
        else:
            eval = Evaluacion(board, "B")

        return eval.result()

    # Todo el código a partir de aquí sólo se ejecuta si el árbol aún no ha alcanzado el nodo hoja

    if JugadorMaximizado:

        Mejor = MIN
        # Recurre para los hijos izquierdo y derecho
        for i in board.legal_moves:

            board.push(i)

            if JaqueMate(board) and PrimerMovimiento:
                return i

            val = minimax(Profundidad - 1, False, alpha, beta, board, False)
            board.pop()

            if val > Mejor:
                Mejor = val
                best_move_white = i

            alpha = max(alpha, Mejor)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        if PrimerMovimiento:
            print(best_move_white)
            return best_move_white
        else:
            return Mejor

    else:

        Mejor = MAX
        for i in board.legal_moves:

            board.push(i)

            if JaqueMate(board) and PrimerMovimiento:
                return i

            val = minimax(Profundidad - 1, True, alpha, beta, board, False)
            board.pop()

            if val < Mejor:
                Mejor = val
                MejorMovimientoNegro = i

            beta = min(beta, Mejor)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        if PrimerMovimiento:
            return MejorMovimientoNegro
        else:
            return Mejor

def JaqueMate(board):
    if board.is_checkmate():
        return True
    else:
        return False