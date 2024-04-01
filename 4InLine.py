from colorama import init, Fore, Style
init()

# פונקציית בדיקה אם יש זכיה
def chk(cubic,C,R,P):
    # מוודא שורה אופקית מלאה
    for i in range(7):
        if(cubic[R][i] == P and cubic[R][i+1] == P and cubic[R][i+2] == P and cubic[R][i+3] == P):
            return 1
    # מוודא שורה אנכית מלאה
    if((R<7) and cubic[R][C] == P and cubic[R+1][C] == P and cubic[R+2][C] == P and cubic[R+3][C] == P):
        return 1
    # מוודא שורה אלכסונית יורדת לימין מלאה
    c = r = 0
    if(C>=R):
        c = C-R
    else:
        r = R-C
    while(c+3 < 10 and r+3 < 10):
        if(cubic[r][c] == P and cubic[r+1][c+1] == P and cubic[r+2][c+2] == P and cubic[r+3][c+3] == P):
            return 1
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
        if(cubic[r][c] == P and cubic[r+1][c-1] == P and cubic[r+2][c-2] == P and cubic[r+3][c-3] == P):
            return 1
        c -= 1
        r += 1

# פונקציית הדפסת מבנה המשחק  
def printer(cubic):
    print(F'\n       ',Fore.CYAN +'_'*39)
    for i in range(10):
        print('       ', end = '')
        for j in range(10):
            if(cubic[i][j] == 1):
                print(Fore.CYAN + '|',Fore.GREEN + 'O ' ,end = '')
            elif(cubic[i][j] == 0):
                print(Fore.CYAN + '|',Fore.RED + 'O ' ,end = '')
            else:
                print(Fore.CYAN + '|',Fore.YELLOW + '- ' ,end = '')
        print(Fore.CYAN +'|')
    print(F'       ',Fore.YELLOW +'_1___2___3___4___5___6___7___8___9__10_', Style.RESET_ALL + '')

# פונקציית המשתמש
def user(cubic):
    print()
    a = input('First player enter your name:  ' + Fore.RED)
    b = input(Style.RESET_ALL + 'second player enter your name:  '+ Fore.GREEN)
    printer(cubic)
    player = j = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    while (j <100):
        # קבלת מיקום עמודה מהמשתמש
        if(player == 0):
            useIN = int(input('\n' + Fore.RED + F'{a}' + Style.RESET_ALL + ' enter the column you chose: '))
        else:
            useIN = int(input('\n' + Fore.GREEN + F'{b}' + Style.RESET_ALL + ' enter the column you chose: '))
        if(useIN > 0 or useIN < 0): useIN -= 1
        else: useIN = 9   
        # בדיקה שהערכים שהוזנו אפשריים - ובדיקה האם העמודה מלאה
        if (useIN > 9 or useIN < 0 or cubic[0][useIN] != -1):
            print(Fore.RED + '   >> Error !!!'+ Fore.BLUE + '\n   - the selected column is already taken\n   - the number entered is greater than 10\n\ntry again >>')
            continue
        for i in range(9,-1,-1):
            if(cubic[i][useIN] == -1):
                # הצבה במערך במיקום הפנוי בעמודת בחירת המשתמש
                cubic[i][useIN] = player
                row = i
                printer(cubic)
                # בדיקת אפשרות זכיה מעל תור 7
                if(j >= 6 and chk(cubic,useIN,row,player) == 1):
                    if(player == 0):    
                        print(Fore.RED + F'\n\n{a}',Style.RESET_ALL + ' congratulation, you are the winer!\n')
                    else:
                        print(Fore.GREEN + F'\n\n{b}',Style.RESET_ALL + ' congratulation, you are the winer!\n')
                    j = 99
                    break
                # בסיום הריצה ללא מנצחים
                elif(j == 99):
                    print(Style.RESET_ALL + '\n   >> ther are no winers!\n\n  ',Fore.GREEN + '>> try again...\n\n')
                break
        player = (player + 1) %2
        j += 1

# # # # Main # # # #       
cubic = [[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10,[-1]*10]
user(cubic)