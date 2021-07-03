x = 0
while x < 3:
    password = input('please inpout password:')
    if password == 'a12345':
    	print('yes you got it!')
    	break
    elif password != 'a12345':
    	print('wrong! you have', 3-(x+1), 'more shots!')
    	x = x + 1

