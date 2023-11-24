class BoardValues:

    def __init__(self):
        self.Pawn = [0,  0,   0,   0,   0,   0,  0, 0,
                     5, 10,  10, -20, -20,  10, 10, 5,
                     5, -5, -10,   0,   0, -10, -5, 5,
                     0,  0,   0,  20,  20,   0,  0, 0,
                     5,  5,  10,  25,  25,  10,  5, 5,
                     10,10,  20,  30,  30,  20, 10,10,
                     50,50,  50,  50,  50,  50, 50,50,
                     0,  0,  0,    0,   0,   0,  0, 0
                     ]

        self.Knight = [-50, -40, -30, -30, -30, -30, -40, -50,
                       -40, -20,   0,   0,   0,   0, -20, -40,
                       -30,   5,  10,  15,  15,  10,   5, -30,
                       -30,   0,  15,  20,  20,  15,   0, -30,
                       -30,   5,  15,  20,  20,  15,   5, -30,
                       -30,   0,  10,  15,  15,  10,   0, -30,
                       -40, -20,   0,   5,   5,   0, -20, -40,
                       -50, -40, -30, -30, -30, -30, -40, -50
                       ]

        self.Bishop = [-20,-10,-10,-10,-10,-10,-10,-20,
                       -10,  5,  0,  0,  0,  0,  5,-10,
                       -10, 10, 10, 10, 10, 10, 10,-10,
                       -10,  0, 10, 10, 10, 10,  0,-10,
                       -10,  5,  5, 10, 10,  5,  5,-10,
                       -10,  0,  5, 10, 10,  5,  0,-10,
                       -10,  0,  0,  0,  0,  0,  0,-10,
                       -20,-10,-10,-10,-10,-10,-10,-20
                       ]

        self.Rook = [ 0, 0,  0,  5,  5,  0,  0,  0,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                     -5, 0,  0,  0,  0,  0,  0, -5,
                      5,10, 10, 10, 10, 10, 10,  5,
                      0, 0,  0,  0,  0,  0,  0,  0
                     ]

        self.Queen = [-10,   5,   5,  5,  5,   5,   0, -10,
                      -10,   0,   5,  0,  0,   0,   0, -10,
                        0,   0,   5,  5,  5,   5,   0,  -5,
                       -5,   0,   5,  5,  5,   5,   0,  -5,
                      -10,   0,   0,  0,  0,   0,   0, -10,
                      -10,   0,   5,  5,  5,   5,   0, -10,
                      -20, -10, -10, -5, -5, -10, -10, -20,
                      -20, -10, -10, -5, -5, -10, -10, -20
                      ]

        self.KingEarly = [ 20,  30,  10,   0,   0,  10,  30,  20,
                           20,  20,   0,   0,   0,   0,  20,  20,
                          -10, -20, -20, -20, -20, -20, -20, -10,
                          -20, -30, -30, -40, -40, -30, -30, -20,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30,
                          -30, -40, -40, -50, -50, -40, -40, -30
                          ]

        self.KingLate = [-50, -30,-30,-30,-30,-30, -30, -50,
                         -30, -30,  0,  0,  0,  0, -30, -30,
                         -30, -10, 20, 30, 30, 20, -10, -30,
                         -30, -10, 30, 40, 40, 30, -10, -30,
                         -30, -10, 30, 40, 40, 30, -10, -30,
                         -30, -10, 20, 30, 30, 20, -10, -30,
                         -30, -20,-10,  0,  0,-10, -20, -30,
                         -50, -40,-30,-20,-20,-30, -40, -50
                         ]


class Evaluacion():

    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.boardValues = BoardValues()
        self.lateGameWhite = False
        self.lateGameBlack = False


        self.boardLayout = [None] * 64


        self.populate()

    def populate(self):

        boardString = self.board.fen()


        boardString = boardString[0:boardString.find(' ')]
        boardString = boardString + '/'


        counter = 0

        for y in range(8):
            dash = boardString.find('/')
            rawCode = boardString[0:dash]
            boardString = boardString[dash + 1:len(boardString)]

            for char in rawCode:
                if char.isdigit():
                    counter += int(char)
                else:
                    self.boardLayout[counter] = char
                    counter += 1

    def materialComp(self):

        total = 0
        boardString = self.board.fen()


        boardString = boardString[0:boardString.find(' ')]


        for i in boardString:
            if str(i) == "P": total += 100
            elif str(i) == "N": total += 320
            elif str(i) == "B": total += 330
            elif str(i) == "R": total += 500
            elif str(i) == "Q": total += 900
            elif str(i) == "K": total += 20000

            elif str(i) == "p": total -= 100
            elif str(i) == "n": total -= 320
            elif str(i) == "b": total -= 330
            elif str(i) == "r": total -= 500
            elif str(i) == "q": total -= 900
            elif str(i) == "k": total -= 20000
            else: pass

        return total

    def development(self):
        total = 0
        counter = 0


        numberOfMinorPiecesWhite = 0
        numberOfMinorPiecesBlack = 0

        for piece in self.boardLayout:
            if piece != None:
                if str(piece) == "P":
                    total += self.boardValues.Pawn[-(counter-63)]
                elif str(piece) == "N":
                    total += self.boardValues.Knight[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "B":
                    total += self.boardValues.Bishop[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "R":
                    total += self.boardValues.Rook[-(counter-63)]
                    numberOfMinorPiecesWhite += 1
                elif str(piece) == "Q":
                    total += self.boardValues.Queen[-(counter-63)]
                    numberOfMinorPiecesWhite += 1

                #######################################################################

                elif str(piece) == "p":
                    total -= self.boardValues.Pawn[counter]
                elif str(piece) == "n":
                    total += self.boardValues.Knight[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "b":
                    total += self.boardValues.Bishop[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "r":
                    total += self.boardValues.Rook[counter]
                    numberOfMinorPiecesBlack += 1
                elif str(piece) == "q":
                    total += self.boardValues.Queen[counter]
                    numberOfMinorPiecesBlack += 1

            counter += 1

        counter = 0
        for piece in self.boardLayout:
            if piece != None:
                # If True it is still early game.
                if str(piece) == "k":
                    if (numberOfMinorPiecesBlack >= 3):
                        total += self.boardValues.KingEarly[counter]
                    else:
                        total += self.boardValues.KingLate[counter]
                        self.lateGameBlack = True
                        print("Black LAte")

                # If True it is still early game.
                elif str(piece) == "K":
                    if (numberOfMinorPiecesWhite >= 3):
                        total += self.boardValues.KingEarly[-(counter - 63)]
                    else:
                        total += self.boardValues.KingLate[-(counter - 63)]
                        self.lateGameWhite = True

            counter += 1

        return total

    def checkmate(self):

        total = 0

        if self.board.is_checkmate:
            if self.color == "W":
                total += 50000
            else:
                total -= 50000

        return total

    def is_late_game(self):
        self.development()
        if (self.lateGameBlack) and (self.lateGameWhite):
            return True
        else:
            return False

    def result(self):
        total = 0

        total += self.materialComp()

        total += self.development()
        
        total += self.checkmate()

        return total

