# פונקציית בדיקה אם יש זכיה
def chk(cubic,C,R,P):
    # מוודא שורה אופקית מלאה
    for i in range(7):
        if(P == cubic[R][i] == cubic[R][i+1] == cubic[R][i+2] == cubic[R][i+3]):
            return True
    # מוודא שורה אנכית מלאה
    if((R<7) and P == cubic[R][C] == cubic[R+1][C] == cubic[R+2][C] == cubic[R+3][C]):
        return True
    # מוודא שורה אלכסונית יורדת לימין מלאה
    c = r = 0
    if(C>=R):
        c = C-R
    else:
        r = R-C
    while(c+3 < 10 and r+3 < 10):
        if(P == cubic[r][c] == cubic[r+1][c+1] == cubic[r+2][c+2] == cubic[r+3][c+3]):
            return True
        c += 1
        r += 1
    # מוודא שורה אלכסונית יורדת לשמאל מלאה 
    if(C+R<10):
        c = C+R
        r = 0
    else:
        c = 9
        r = R+C-9
    while(c-3 > -1 and r+3 < 10):
        if(P == cubic[r][c] == cubic[r+1][c-1] == cubic[r+2][c-2] == cubic[r+3][c-3]):
            return True
        c -= 1
        r += 1
    return False
# פונקציית הדפסת מבנה המשחק  
def printer(cubic):
    print(F'\n       ','_'*39)
    for i in range(10):
        print('       ', end = '')
        for j in range(10):
            if(cubic[i][j] == 1):
                print('| O ' ,end = '')
            elif(cubic[i][j] == 0):
                print('| X ' ,end = '')
            else:
                print('| - ' ,end = '')
        print('|')
    print(F'       | 1   2   3   4   5   6   7   8   9  10 |\n      /=========================================\\\n     |||||||||||||||||||||||||||||||||||||||||||||')

# פונקציית המשתמש
def user(cubic):
    print()
    a = input('First Player enter your name:  ')
    b = input('Second Player enter your name:  ')
    printer(cubic)
    player = j = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    while (j <100):
        # קבלת מיקום עמודה מהמשתמש
        if(player == 0):
            useIN = int(input(F'\n{a} enter the column you chose: '))
        else:
            useIN = int(input(F'\n{b} enter the column you chose: '))
        if(useIN > 0 or useIN < 0): useIN -= 1
        else: useIN = 9   
        # בדיקה שהערכים שהוזנו אפשריים - ובדיקה האם העמודה מלאה
        if (useIN > 9 or useIN < 0 or cubic[0][useIN] != -1):
            print('   >> Error !!!\n   - the selected column is already taken\n   - the number entered is greater than 10\n\ntry again >>')
            continue
        for i in range(9,-1,-1):
            if(cubic[i][useIN] == -1):
                # הצבה במערך במיקום הפנוי בעמודת בחירת המשתמש
                cubic[i][useIN] = player
                row = i
                printer(cubic)
                # בדיקת אפשרות זכיה מעל תור 7
                if(j >= 6 and chk(cubic,useIN,row,player)):
                    if(player == 0):    
                        print(F'\n\n{a} congratulation, you are the winer!\n')
                    else:
                        print(F'\n\n{b} congratulation, you are the winer!\n')
                    return 0
                break
                # בסיום הריצה ללא מנצחים
        player = (player + 1) %2
        j += 1
    print('\n   >> ther are no winers!\n\n   >> try again...\n\n')

# # # # Main # # # #       
cubic = [[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10]
user(cubic)
