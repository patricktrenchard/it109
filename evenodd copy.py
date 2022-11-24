import os 

counter = 1
tottalalaal = 0
countcount = 0

cart={}
newcart={}
def itemMenu (category, itemList):
    """itemMenu function - displays menu of variable number of shopping items.
       Inputs: category (books, etc.), list of item descriptions and prices.
       Returns: selected menu item (integer, 1 to n), s, or x
       ---------------------------------------------------------------------"""  
    #os.system('clear')    # clear screen if in MS Windows OS, 'clear' for Macs
    print ('\n\n\t\t ' + category + ' menu')
    print ('\n\t\t Select from the following items, display cart, or checkout: ')
    print('\n\t\t\t {0:3s}  {1:30s}  {2:9s}'.format('No.', 'Item Description', 'Price '))
    print('\t\t\t {0:3s}  {1:30s} {2:9s}'
          .format('===', '===============================', '========='))
    for n in range(0, len(itemList)):
        print('\t\t\t {0:>2s} - {1:30s}  ${2:8.2f}'.format(str(n+1), itemList[n][0], itemList [n][1]))
    print('\n\t\t\t {0:>2s} - {1:30s} '.format('s',  'display cart contents '))
    print('\t\t\t {0:>2s} - {1:30s} '.format('x', 'return to category menu '))
    menuPic = input('\n\nEnter Selection (1 to {0:>2s}, "s", or "x"): '.format(str(len(itemList))))
    return menuPic 
def scart(newcart):
    for key, value in newcart.items():
        print('{0:25s}'.format(key),'$','{0:8.2f}'.format(value))

def display_cart(newcart, temp):
    for key, value in newcart.items():
        print('{0:25s}'.format(key),'$','{0:8.2f}'.format(value))
    
    
def final_cart(cart,countcount):
    countcount += int((len(cart)) / 2)
    for key, value in cart.items():
        print('{0:25s}'.format(key),'$','{0:8.2f}'.format(value))
def process (x,cart,countcount,tottalalaal,ting,newting,y,newcart):
        select = ''
        select = x
        x = ''

        if select == '1'or '2' or '3' or '4' or 'c' or 's':
           
            while select not in 'x' or 'X':
            
                if select != 'n':
                    
                    select = itemMenu(ting,newting)
                
                if select in ('s', 'S'):
                    #os.system('clear')
                    scart(newcart)
                elif select in ('x','X'):
                    break

                
                    
                #elif select in ('x', 'X'): 
                    
                elif select in ('1', '2' ,'3', '4'):
                    if y not in 'n' or 'n':
                        
                        cheese = int(select)
                        item_item = input('Add ' + str(newting[cheese - 1][0]) + " to the cart(y/n)?")          
                        if item_item =='y':
                            print(str(newting[cheese-1][0]) +" added to cart")
                        
                        
                            title = newting[int(select) - 1][0]
                            price = newting[int(select) - 1][1]

                            tottalalaal+= float(newting[int(select) - 1][1])
                            cart[title] = price
                            newcart[title] = price
                            print(cart)

                            continue
                        else:
                            continue
                    else:
                        continue
        x = 'x'
        
        return(cart)         
def checkout(cart, yorn,counter,x,newcart):
    #while True:
    display_cart(newcart,2)
    if option == 'c' or 'C':
        x = str(input('Do you want another cart y or n  : '))
    yorn = x
    counter += 1
    if yorn != 'n':
        return
    return cart


#def processItems(item_cat, item_list, valid_list, p1_cart):
  #  item_pic = ''
  #  while item_pic != 'x':
  #      os.system('clear')
   #     item_pic = 


category_menu = """\n\n
             Select an item from the following menu or checkout:
             
               1 = books 
               2 = clothing
               3 = electronics
               4 - travel
               s = show cart contents
               c = checkout
        
        """

# category items tuples/lists - one per category ---------------------------

newting =[]
newlistting = ''
book_list = [['Our Missing Hearts', 29.00], ['Grant', 24.95], ['Lucy by the Sea', 28.00],
             ['Confidence Man', 32.00], ['Crying in H Mart', 26.95], ['Atomic Habits', 27.00]]
cloth_list = [['Armani Suit', 750.0], ['Shoes', 45.00], ['SmartWool Socks', 20.00], ['Nationals Hat', 32.00],
              ['Vasque Hiking Boots', 120.0]]
elect_list = [['Dell Latitude Laptop', 895.00], ['EyePhone 14 Pro', 995.00],
              ['Bose 20 Speakers', 220.00], ['Sharp 70 inch TV', 575.00] ]
travel_list = [['Ocean City, MD', 495.00], ['Disney World', 825.50], ['National Parks', 650.95],
               ['New York City', 550.00], ['Paris and the Ile de France', 1495.00]]
bookoptions = """
    1 - “Our Missing Hearts”, $29.00
    2 - “Grant”, $24.95
    3 - “Lucy by the Sea”, $28.00
    4 - “Confidence Man”, 32.00
    5 – “Crying in H Mart”, 26.95
    6 – “Atomic Habits”, 27.00
    s – show cart contents
    x – return to category menu
    """
clothingoptions="""
    1 – Armani Suit, $750.00
    2 - Shoes, $45.00
    3 – SmartWool Socks, $20.00
    4 - Nationals Hat, $32.00
    5 - Vasque Hiking Boots, $120.00
    s – show cart contents
    x - no selection
 """
electronicsoptions="""
    1 – Dell Latitude Laptop, $895.00
    2 - EyePhone 14 Pro, $995.00
    3 - Bose 20 Speakers, $220.00
    4 – Sharp 70 inch TV, $575.00
    s – show cart contents
    x – return to category menu
 """
traveloptions="""
    1 – Ocean City, MD, $495.00
    2 – Disney World, $825.00
    3 – National Parks, $690.95
    4 – New York City, $550.00
    5 – Paris and the Ile de France, $1,495.00
    s – show cart contents
    x – return to category menu
 """
 
yorn = 'y'
while yorn == 'y':
    option = ''
    newoption = ''
    select = ''
    x = ''
    print(category_menu)
    newoption = str(input('Please Input an option from the list above  : '))
    

    newting =[]
    ting = ''
    if newoption == '1':
        newting += book_list
        newlistting = bookoptions
        ting = 'Books'
    if newoption == '2':
        newting += cloth_list
        newlistting = clothingoptions
        ting = 'Clothing'
    if newoption == '3':
        newting += elect_list
        newlistting = electronicsoptions
        ting = 'Electronics'
    if newoption == '4':
        newting += travel_list
        newlistting = traveloptions
        ting = 'Travel'
    else:
        newoption = newoption
    
    
    if newoption == '1' or '2' or '3' or '4' or 's' or 'c':
       
        select = x
        
        if newoption in ('s', 'S'):
            
            #os.system('clear')
            scart(newcart)
        if newoption == ' c' or '':
            
            checkout(newcart, yorn,counter,x,cart)
        if newoption == ' c':
            
            checkout(newcart, yorn,counter,x,cart)
        print (select)
        x= newoption

        y=''
        if select != 'x':
            
            
            process (x,cart,countcount,tottalalaal,ting,newting,y,newcart)
            if x == 's':
                
                scart(newcart)

        
        if select in 'x' or 'X':
           
            continue
            
        
    if select == 'c' or 'C':
        
        checkout(newcart, yorn,counter,x,cart)
        newcart.clear()
    
    elif yorn == 'n' or 'N':
        final_cart(cart,countcount) 
        print("total cost of ",countcount, " items in ", counter, "cart(s): $", tottalalaal)
        break
    
    
        



input ('\n\nHit Enter to end program')