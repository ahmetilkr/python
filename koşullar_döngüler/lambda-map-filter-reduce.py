
#normal bir şekilde fonksiyon
def summer(a,b):
    return a+b

summer(1,3)



#normal fonksiyon gibi kısa ve tek satır kullan at özelliği var
new_sum=lambda a,b : a+b
new_sum(4,5)


salaries=[1000,2000,3000,4000]

def new_salary(x):
    return (x*20/100)+x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))


#map fonksiyonu for yazmaktan bizi kurtarır ilk parametresine fonksiyonu verirsin ikincisine vereceğin listeyi (listenin elemanları dolaşıp lambda fonksiyonuna gönderir)
list(map(new_salary,salaries))


#lambda fonksiyonuna kullan at özelliği kazandırdık
list(map(lambda x:x*20/100+x,salaries))



