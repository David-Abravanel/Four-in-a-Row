from colorama import init, Fore, Style
init()

# פונקציית בדיקה אם יש זכיה
def chk(C,R,P):
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
    r = 0
    c = 9
    if(C+R<10):
        c = C+R
    else:
        r = R+C-9
    while(c-3 > -1 and r+3 < 10):
        if(P == cubic[r][c] == cubic[r+1][c-1] == cubic[r+2][c-2] == cubic[r+3][c-3]):
            return True
        c -= 1
        r += 1
    return False

# פונקציית הדפסת מבנה המשחק  
def Display():
    pice = [Fore.RED + ' O ',Fore.GREEN + ' O ',Fore.YELLOW + ' - ']
    # מבנה המשחק
    print(F'\n       ',Fore.CYAN +'_'*39)
    for i in range(10):
        print('       ', end = '')
        for j in range(10):
                print(Fore.CYAN + '|'+pice[cubic[i][j]] ,end = '')
        print(Fore.CYAN +'|')
    # תחתית
    print('       |',Fore.YELLOW +'1   2   3   4   5   6   7   8   9  10', Fore.CYAN + '|\n      /','='*39,'\\\n     ','|'*43)

# פונקציית המשתמש
def user():
    players_name = [Fore.RED + input('\nFirst player enter your name:  ' + Fore.RED) + Style.RESET_ALL  ,  Fore.GREEN + input(Style.RESET_ALL + 'second player enter your name:  '+ Fore.GREEN) + Style.RESET_ALL]
    Display()
    player = turn = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    while(turn < 100):
        # קבלת מיקום עמודה מהמשתמש
        try:
            useIN = int(input(F'\n{players_name[player]} enter the column you chose:  '))-1
            if useIN == -1: useIN = 9
        except ValueError:
            print('wirde...')
            continue
        # בדיקה שהערכים שהוזנו בטווח האפשרי - והאם העמודה מלאה
        if (useIN > 9 or useIN < 0 or cubic[0][useIN] != -1):
            print(Fore.RED + '   >> Error !!!'+ Fore.BLUE + '\n   - Either the column is already full\n   - or the number entered is not between 1-10\n\ntry again >>')
            continue
        # לולאת הצבה במערך במיקום הפנוי בעמודת בחירת המשתמש
        for i in range(9,-1,-1):
            if(cubic[i][useIN] == -1):
                cubic[i][useIN] = player
                row = i
                Display()
                # בדיקת אפשרות זכיה מתור 7 ומעלה
                if(turn > 5 and chk(useIN,row,player)):
                    print(F'\n\n{players_name[player]} congratulation, you are the winer!\n')
                    return
                break
        player = (player + 1) %2
        turn += 1
    # בסיום הריצה ללא מנצחים
    print(Style.RESET_ALL + '\n   >> ther are no winers!\n\n  ',Fore.GREEN + '>> try again...\n\n')

# # # # Main # # # #       
cubic = [[-1 for j in range(10)] for i in range(10)]
user()