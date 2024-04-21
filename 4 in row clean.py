# פונקציית בדיקה אם יש זכיה
def Check(C,R,P):
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
def Display():
    pices = ['| X ','| O ','| - ']
    print(F'\n       ','_'*39)
    for i in range(10):
        print('       ',end = '')
        for j in range(10):
                print(pices[cubic[i][j]],end = '')
        print('|')
    print('       | 1   2   3   4   5   6   7   8   9  10 |\n      /=========================================\\\n     |||||||||||||||||||||||||||||||||||||||||||||')

# פונקציית המשתמש
def User():
    players_name = [input('\nFirst Player enter your name:  '),input('Second Player enter your name:  ')]
    Display()
    player = j = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    while j in range(100):
        # קבלת מיקום עמודה מהמשתמש
        useIN = int(input(F'\n{players_name[player]} enter the column you chose: '))
        if(useIN > 0 or useIN < 0): useIN -= 1
        else: useIN = 9   
        # בדיקה שהערכים שהוזנו אפשריים - ובדיקה האם העמודה מלאה
        if (useIN > 9 or useIN < 0 or cubic[0][useIN] != -1):
            print('   >> Error !!!\n   - Either the column is already full\n   - Or the number entered is not between 1-10\n\ntry again >>')
            continue
        # לולאת הצבה במערך במיקום הפנוי בעמודת בחירת המשתמש
        for i in range(9,-1,-1):
            if(cubic[i][useIN] == -1):
                cubic[i][useIN] = player
                row = i
                Display()
                # בדיקת אפשרות זכיה מתור 7 ומעלה
                if(j >= 6 and Check(useIN,row,player)):
                    print(F'\n\n{players_name[player]} congratulation, you are the winer!\n')
                    return
                break
        player = (player + 1) %2
        j += 1
    # בסיום הריצה ללא מנצחים
    print('\n   >> ther are no winers!\n\n   >> try again...\n\n')

# # # # Main # # # #       
cubic = [[-1 for j in range(10)] for i in range(10)]
User()