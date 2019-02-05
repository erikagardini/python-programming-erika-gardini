#ALGORITHMS FOR COMPUTING AND EVALUATING SEQUENCE ALIGNMENTS

match_award = 10
mismatch_penalty = -5
gap_penalty = -2

def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval


def match_score(alpha, beta):

    matrix = {"AA": 2,"AC": -1,"AT": -1,"AG": 0,"CA": -1,"CC": 2,"CT": 0,"CG": -1,"TA": -1,"TC": 0,"TT": 2,"TG": -1,"GA": 0,"GC": -1,"GT": -1,"GG": 2}

    s = ""

    if alpha == '-' or beta == '-':
        return gap_penalty
    else:
        s = s + alpha + beta
        return matrix.get(s)


def finalize(align1, align2):
    align1 = align1[::-1]    #reverse sequence 1
    align2 = align2[::-1]    #reverse sequence 2

    score = 0
    for i in range(0,len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:                
            score += match_score(align1[i], align2[i])
    
        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-': 
            score += match_score(align1[i], align2[i])

        #if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':          
            score += gap_penalty
    

    print('Score =', score)
    print(align1)
    print(align2)

#Needleman and Wunsch algorithm
def needle(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences
    
    # Generate DP table and traceback path pointer matrix
    score = zeros((m+1, n+1))      # the DP table
   
    # Calculate DP table
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + match_score(seq1[i-1], seq2[j-1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            score[i][j] = max(match, delete, insert)

    # Traceback and compute the alignment 
    align1, align2 = '', ''
    i,j = m,n # start from the bottom right cell
    while i > 0 and j > 0: # end toching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i-1][j-1]
        score_up = score[i][j-1]
        score_left = score[i-1][j]

        if score_current == score_diagonal + match_score(seq1[i-1], seq2[j-1]):
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1

    # Finish tracing up to the top left cell
    while i > 0:
        align1 += seq1[i-1]
        align2 += '-'
        i -= 1
    while j > 0:
        align1 += '-'
        align2 += seq2[j-1]
        j -= 1

    finalize(align1, align2)


#Needleman and Wunsch algorithm without end gaps


#Smith and Waterman algorithm
def water(seq1, seq2):
    m, n = len(seq1), len(seq2)  # length of two sequences
    
    # Generate DP table and traceback path pointer matrix
    score = zeros((m+1, n+1))      # the DP table
    pointer = zeros((m+1, n+1))    # to store the traceback path
    
    max_score = 0        # initial maximum score in DP table
    # Calculate DP table and mark pointers
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score_diagonal = score[i-1][j-1] + match_score(seq1[i-1], seq2[j-1])
            score_up = score[i][j-1] + gap_penalty
            score_left = score[i-1][j] + gap_penalty
            score[i][j] = max(0,score_left, score_up, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0 # 0 means end of the path
            if score[i][j] == score_left:
                pointer[i][j] = 1 # 1 means trace up
            if score[i][j] == score_up:
                pointer[i][j] = 2 # 2 means trace left
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3 # 3 means trace diagonal
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j]
    
    align1, align2 = '', ''    # initial sequences
    
    i,j = max_i,max_j    # indices of path starting point
    
    #traceback, follow pointers
    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 += seq1[i-1]
            align2 += seq2[j-1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1
        elif pointer[i][j] == 1:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1

    finalize(align1, align2)


import sys, math


def affine_gap(seq1, seq2):
    gap_open = -1.
    gap_extend = -0.1
    match = 1.
    mismatch = -1.

    #### initiate and calculate value
    lseq1 = len(seq1);
    lseq2 = len(seq2)
    row = lseq2 + 1;
    col = lseq1 + 1

    xval = [[0. for j in range(col)] for i in range(row)]
    yval = [[0. for j in range(col)] for i in range(row)]
    val = [[0. for j in range(col)] for i in range(row)]

    for i in range(row):
        val[i][0] = gap_open + i * gap_extend
        yval[i][0] = -10000.

    for j in range(col):
        val[0][j] = gap_open + j * gap_extend
        xval[0][j] = -10000.  # assign -INF

    val[0][0] = 0.

    for i in range(1, row):
        for j in range(1, col):
            xval[i][j] = max(xval[i - 1][j] + gap_extend, val[i - 1][j] + gap_open + gap_extend)
            yval[i][j] = max(yval[i][j - 1] + gap_extend, val[i][j - 1] + gap_open + gap_extend)
            cople = 0.
            if (seq1[j - 1] == seq2[i - 1]):
                cople = val[i - 1][j - 1] + match
            else:
                cople = val[i - 1][j - 1] + mismatch

            val[i][j] = max(cople, xval[i][j], yval[i][j])

    #### print value
    for i in range(row):
        for j in range(col):
            print(val[i][j], '\t')
        print('')

    #### traceback
    sequ1 = ''
    sequ2 = ''
    i = lseq2
    j = lseq1
    ITER_MAX = 1000000
    iteration = 0
    while ((i > 0 or j > 0) and iteration < ITER_MAX):
        if (i > 0 and j > 0 and val[i][j] == val[i - 1][j - 1] + (match if seq2[i - 1] == seq1[j - 1] else mismatch)):
            sequ1 += seq1[j - 1]
            sequ2 += seq2[i - 1]
            i -= 1;
            j -= 1
        elif (i > 0 and val[i][j] == xval[i][j]):
            sequ1 += '_'
            sequ2 += seq2[i - 1]
            i -= 1
        elif (j > 0 and val[i][j] == yval[i][j]):
            sequ1 += seq1[j - 1]
            sequ2 += '_'
            j -= 1

        iteration += 1

    sequ1r = ' '.join([sequ1[j] for j in range(-1, -(len(sequ1) + 1), -1)])
    sequ2r = ' '.join([sequ2[j] for j in range(-1, -(len(sequ2) + 1), -1)])

    score = 0.
    for j in range(len(sequ1)):
        if (sequ1[j] == sequ2[j]):
            score += match
        else:
            score += mismatch

    print("Sequence 1: ", sequ1r)
    print("Sequence 2: ", sequ2r)
    print("Score     : ", score)

#Main

seq1 = "ACTCT"
seq2 = "ATTAA"

needle(seq1, seq2)
water(seq1, seq2)

#affine_gap(seq1, seq2)