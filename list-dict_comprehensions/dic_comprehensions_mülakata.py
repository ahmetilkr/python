
#çift sayıların akresi alınarak sözlüğe eklenecek

new_dict={}
numbers=range(10)

for n in numbers:
    if n % 2 ==0:
        new_dict[n]=n**2


#diğer yöntem

{n:n**2 for n in numbers if n % 2 == 0}