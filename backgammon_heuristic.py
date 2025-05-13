class heuristic:
    def evaluate_heuristic(self, board, side):
        vw = [-18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
        vb = [6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18]
        w1 = 8
        w3 = -2
        w4 = -1
        K = -12
        sumPosW = 0
        pedineMinacciateW = []
        for i in range(24):
            if (board.myBoard[i] > 0):
                for j in range(board.myBoard[i]):
                    sumPosW += vw[i]
        for i in range(24):
            temp = False
            if (board.myBoard[i] == 1):
                for j in range(23 - i):
                    if (board.myBoard[j + i] < 0):
                        temp = True
            if (temp == True):
                pedineMinacciateW.append(1 + (int)((i + 1) / 2))
        somMinW = 0
        for pedina in pedineMinacciateW:
            somMinW += pedina
        numCasOccW = 0
        for i in range(6):
            if (board.myBoard[i] < -1):
                numCasOccW += 1
        # caso nero
        sumPosB = 0
        pedineMinacciateB = []
        for i in range(24):
            if (board.myBoard[i] < 0):
                for j in range(-board.myBoard[i]):
                    sumPosB += vb[i]
        for i in range(24):
            temp = False
            if (board.myBoard[i] == -1):
                for j in range(i):
                    if (board.myBoard[j] > 0):
                        temp = True
            if (temp == True):
                pedineMinacciateB.append(1 + (int)((24 - i) / 2))
        somMinB = 0
        for pedina in pedineMinacciateB:
            somMinB += pedina
        numCasOccB = 0
        for i in range(6):
            if (board.myBoard[i] > 1):
                numCasOccB += 1
        HW = sumPosW + (w1 * board.wFree) - somMinW + board.wJail * (w3 * numCasOccW + w4 * (6 - numCasOccW) + K)
        HB = sumPosB + (w1 * board.bFree) - somMinB + board.bJail * (w3 * numCasOccB + w4 * (6 - numCasOccB) + K)
        if (side):
            HW += 3
            return HW - HB
        else:
            HB += 3
            return HB - HW

