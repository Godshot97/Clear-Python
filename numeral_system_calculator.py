logo = ''' 
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||               NUMERICAL SYSTEMS CALCULATOR                 |||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||                                                            |||
|||   CHOOSE FROM WHICH SYSTEM YOU WANT TO MAKE A CONVERSION   |||
|||                                                            |||
|||   [1] DECIMAL                                              |||
|||   [2] BINARY                                               |||
|||   [3] OCTAL                                                |||
|||   [4] HEXADECIMAL                                          |||
|||                                                            |||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

print(logo)
choice = input('||| CHOICE: ')

# FUNKCJE
def from2to10(l_bin):
    x = len(l_bin)
    l_dec = 0
    for i in range(0,x):
        l_dec += int(l_bin[i]) * pow(2,x-1)
        x -= 1
    return print('DECIMAL: ',l_dec)


def from2to8(l_bin):
    okt = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}
    
    if len(l_bin) % 3 == 1:
        l_bin = '00' + l_bin
    elif len(l_bin) % 3 == 2:
        l_bin = '0' + l_bin
        
    tab = []
    x = 0
    y = 3
    for i in range(int(len(l_bin) / 3)):
        tab.append(l_bin[x:y])
        x += 3
        y += 3
    
    result = ''
    for i in tab:
        result += okt[i]
    return print('OKTAL: ',result)  
 
def from2to16(l_bin):
    hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    
    if len(l_bin) % 4 == 1:
        l_bin = '000' + l_bin
    elif len(l_bin) % 4 == 2:
        l_bin = '00' + l_bin
    elif len(l_bin) % 4 == 3:
        l_bin = '0' + l_bin
        
    tab = []
    x = 0
    y = 4
    for i in range(int(len(l_bin) / 4)):
        tab.append(l_bin[x:y])
        x += 4
        y += 4
    
    result = ''    
    for i in tab:
        result += hex[i]
    return print('HEXADECIMAL: ',result)
    
def from10to2(l_dec):
    l_dec = int(l_dec)
    #ustalenie liczby bitow w zapisie binarnym (domyslnie 8 dla liczb z zakresu 0-255)
    counter = 9
    while True:
       if l_dec <= 255:
           length = 8
           break
       elif l_dec < pow(2,counter):
           length = counter
           break
       else:
           counter += 1
        
    tab = []
    for i in range(length):
        tab.append(l_dec % 2)
        l_dec = l_dec // 2
    tab2 = tab[::-1]
    
    result = ''
    for i in tab2:
        result += str(i)
    return print('BINARY: ',result)

def from10to8(l_dec):
    l_dec = int(l_dec)
    #ustalenie dlugosciu zapisu oktalnego
    counter = 1
    while True:
       if l_dec < pow(8,counter):
           length = counter
           break
       else:
           counter += 1
    
    tab = []
    for i in range(length):
        tab.append(l_dec % 8)
        l_dec = l_dec // 8
    tab2 = tab[::-1]
    
    result = ''
    for i in tab2:
        result += str(i)
    return print('OKTAL: ',result)
    
def from10to16(l_dec):    
    l_dec = int(l_dec)
    #ustalenie dlugosciu zapisu heksadecymalnego
    counter = 1
    while True:
       if l_dec < pow(16,counter):
           length = counter
           break
       else:
           counter += 1
    
    tab = []
    for i in range(length):
        tab.append(l_dec % 16)
        l_dec = l_dec // 16
    tab2 = tab[::-1]
    
    #zamiana liczb z zakresu 10-15 na A-F
    hex = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    b=0
    for i in tab2:
        if i in hex:
            tab2[b] = hex[i] #podmiana elementu w tab2
        b += 1
    
    result = ''
    for i in tab2:
        result += str(i)
    return print('HEXADECIMAL: ',result)
        
def from8to10(l_okt):
    x = len(l_okt)
    result = 0
    for i in range(0,x):
        result += int(l_okt[i]) * pow(8,x-1)
        x -= 1
    return print('DECIMAL: ',result)     
    
def from8to2(l_okt):    
    okt = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    
    lista = []
    for i in range(len(l_okt)):
        x = l_okt[i]
        lista.append(okt[x])
    
    #usuniecie zer z poczatku napisu
    if lista[0] == '001':
        lista[0] = lista[0].replace('0','',2)
    elif lista[0] in ('010','011'):
        lista[0] = lista[0].replace('0','',1)
    
    result = ''
    for i in range(0,len(l_okt)):
        result += lista[i]
    return print('BINARY: ',result)       
    
def from8to16(l_okt):
    okt = {'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
    hex = {'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7','1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    
    #zamiana na trojki binarne i polaczenie w 1 napis
    string = ''
    for i in range(0,len(l_okt)):
        x = l_okt[i]
        string += okt[x]
    
    #uzupełnienie brakujacych zer z przodu przed podzialem na czworki    
    if len(string) % 4 == 1:
        string = '000' + string
    elif len(string) % 4 == 2:
        string = '00' + string
    elif len(string) % 4 == 3:
        string = '0' + string
    
    #obciecie poczatku stringa w sytuacji gdy string zaczynal sie od 4 zer    
    if string[0:4] == '0000':
        string = string[4:]
    
    #podzial na czworki binarne i konwersja na zapis heksadecymalny
    tab = []
    x = 0
    y = 4
    for i in range(int(len(string) / 4)):
        tab.append(string[x:y])
        x += 4
        y += 4
        
    result = ''
    for i in tab:
        result += hex[i]
    return print('HEXADECIMAL: ',result)    
    
def from16to10(l_hex):
    x = len(l_hex)
    hex = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    result = 0
    for i in range(0,x):
        result += hex[l_hex[i]] * pow(16,x-1)
        x -= 1
    print('DECIMAL: ',result)

def from16to2(l_hex): 
    hex = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    
    lista = []
    for i in range(len(l_hex)):
        x = l_hex[i]
        lista.append(hex[x])
    
    #usuniecie zer z poczatku napisu
    if lista[0] == '0001':
        lista[0] = lista[0].replace('0','',3)
    elif lista[0] in ('0010','0011'):
        lista[0] = lista[0].replace('0','',2)
    elif lista[0] in ('0100','0101','0110','0111'):
        lista[0] = lista[0].replace('0','',1)
    
    result = ''
    for i in range(0,len(l_hex)):
        result += lista[i]
    return print('BINARY: ',result) 
    
def from16to8(l_hex):
    hex = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    okt = {'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}

    #zamiana na czworki binarne i polaczenie w 1 napis
    string = ''
    for i in range(0,len(l_hex)):
        x = l_hex[i]
        string += hex[x]
    
    #uzupełnienie brakujacych zer przed podzialem na trojki    
    if len(string) % 3 == 1:
        string = '00' + string
    elif len(string) % 3 == 2:
        string = '0' + string
    
    #obciecie poczatku stringa w sytuacji gdy string zaczynal sie od 3 zer
    if string[0:3] == '000':
        string = string[3:]
        
    #podzial na trojki binarne i konwersja na zapis oktalny
    tab = []
    x = 0
    y = 3
    for i in range(int(len(string) / 3)):
        tab.append(string[x:y])
        x += 3
        y += 3
    
    result = ''
    for i in tab:
        result += okt[i]
    return print('OKTAL: ',result) 

#funkcje sprawdzające poprawnosc wprowadzanych przez urzytkownka liczb
def check_l_dec(x):
    chars = ['0','1','2','3','4','5','6','7','8','9']
    check = True
    for i in x:
        if i in chars:
            check = check
        else:
            check = False
    return check

def check_l_bin(x):
    chars = ['0','1']
    check = True
    for i in x:
        if i in chars:
            check = check
        else:
            check = False
    return check

def check_l_okt(x):
    chars = ['0','1','2','3','4','5','6','7']
    check = True
    for i in x:
        if i in chars:
            check = check
        else:
            check = False
    return check

def check_l_hex(x):
    chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    check = True
    for i in x:
        if i in chars:
            check = check
        else:
            check = False
    return check

#ponowny wybór w przypadku wyboru poza zakresem 1-4       
while choice != '1' and choice != '2' and choice != '3' and choice != '4':
    choice = input('||| Choose again from 1-4! \n||| CHOICE: ')
    if choice == '1': 
        break
    elif choice == '2':
        break
    elif choice == '3':
        break
    elif choice == '4':
        break
    else:
        continue

 
if choice == '1':
    l_dec = input('Enter decimal number: ')
    if check_l_dec(l_dec):
        from10to2(l_dec)
        from10to8(l_dec)
        from10to16(l_dec)
    else:
        print('You entered wrong number! You can use only numbers 0-9.')
    
elif choice == '2':
    l_bin = input('Enter binary number: ')
    if check_l_bin(l_bin):
        from2to10(l_bin)
        from2to8(l_bin)
        from2to16(l_bin)
    else:
        print('You entered wrong number! You can use only numbers 0 and 1.')
            
elif choice == '3':
    l_okt = input('Enter oktal number: ')
    if check_l_okt(l_okt):
        from8to10(l_okt)
        from8to2(l_okt)
        from8to16(l_okt)
    else:
        print('You entered wrong number! You can use only numbers 0-7.')
            
elif choice == '4':
    l_hex = input('Enter hexadecimal number: ')
    if check_l_hex(l_hex):
        from16to10(l_hex)
        from16to2(l_hex)
        from16to8(l_hex)
    else:
        print('You entered wrong number! You can use only numbers 0-9 and chars A-F.')
        


     

