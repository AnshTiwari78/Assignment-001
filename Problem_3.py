def reflection(user_string):
    empty_str = " " 
    new_list = [] 
    for i in user_string:
        if(i==','):  
            new_list.append(empty_str.strip())  
            empty_str = " " 
        else:
            empty_str = empty_str+i
    if(empty_str!=''):
        new_list.append(empty_str.strip()) 
    x = new_list[::-1]  
    for k in x:
        print(k)
M = input()
a = input()
reflection(a)