# list = [1, 2, 3, 4, 5]

# for el in list:
#     print(el)


str = "granthsoni"

for char in str:
    if(char == 'o'):
        print('o found')
        break
    print(char)
else: #[ye jab likhte h tab hume character ko print nhi krvana ho{optional h }]
    print("END")