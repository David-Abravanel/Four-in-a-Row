# פונקציית בדיקה אם יש זכיה
def Check(current_column,current_row,current_player):
    # מוודא אופקית שורה בת 4 אברים מלאה
    for column in range(current_column-3,current_column+1):
        if(-1 < column < 7 and current_player == cubic[current_row][column] == cubic[current_row][column+1] == cubic[current_row][column+2] == cubic[current_row][column+3]):
            return True
    # מוודא שורה אנכית שורה בת 4 אברים מלאה
    if current_row<7 and (current_player == cubic[current_row][current_column] == cubic[current_row+1][current_column] == cubic[current_row+2][current_column] == cubic[current_row+3][current_column]):
        return True
    # מוודא שורה אלכסונית יורדת לימין שורה בת 4 אברים מלאה
    for row,column in zip(range(current_row-3,current_row+1), range(current_column-3,current_column+1)):
        if 7 > column > -1 and 7 > row > -1 and (current_player == cubic[row][column] == cubic[row+1][column+1] == cubic[row+2][column+2] == cubic[row+3][column+3]):
            return True
    # מוודא שורה אלכסונית יורדת לשמאלה שורה בת 4 אברים מלאה
    for row,column in zip(range(current_row-3,current_row+1), range(current_column+3,current_column-1,-1)):
        if 10 > column > -1 and 7 > row > -1 and (current_player == cubic[row][column] == cubic[row+1][column-1] == cubic[row+2][column-2] == cubic[row+3][column-3]):
            return True
    return False

# פונקציית הדפסת מבנה המשחק  
def Display():
    pice = [' ● ',' ○ ',' - ']
    # מבנה המשחק
    print('\n       ','_'*39,'\n       ',end = '')
    for row in range(10):
        for column in range(10):
                print('│'+pice[cubic[row][column]] ,end = '│\n       '*(column-8))
    # תחתית
    print('│ 1   2   3   4   5   6   7   8   9  10 │')

# מוודא קבלת ערך עמודה תקף מהמשתמש
def get_valid_column(players_name,player):
    while True:
        try:
            column = int(input(F'\n{players_name[player]} Chose a column between 1 and 10: ')) - 1
            if column < 0 or column > 9:
                print(" >> Invalid column. \nPlease enter a number between 1 and 10.")
            elif cubic[0][column] != -1:
                print(' >> column full. \nPlease chose anather column.')
            else:
                return column
        except ValueError:
            print(" >> Invalid input. \nPlease enter a number.")

# פונקציית הצבה במיקום הנבחר
def Placement(useIN,player):
    row = 9-chk[useIN]
    cubic[row][useIN] = player
    chk[useIN] += 1
    Display()
    return row

# פונקציית המשתמש
def User():
    players_name = [input('\nFirst player enter your name:  ') , input('second player enter your name:  ')]
    Display()
    player = 0
    # לולאת ריצה עד סיום המערך 10*10 או בניצחון
    for turn in range(100):
        # קבלת מיקום עמודה תקף מהמשתמש
        useIN = get_valid_column(players_name,player)
        # הצבה במקום הנבחר
        row = Placement(useIN,player)
        # בדיקת זכיה
        if(turn > 5 and Check(useIN,row,player)):
            print(F'\n\n{players_name[player]} congratulation, you are the winer!\n')
            return
        player = (player + 1) %2
    # בסיום הריצה ללא מנצחים
    print('\n   >> ther are no winers!\n    >> try again...\n\n')

# # # # Main # # # # 
chk = [0 for i in range(10)]      
cubic = [[-1 for j in range(10)] for i in range(10)]
User() 