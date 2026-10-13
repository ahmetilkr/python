#before --> hi my name is john and i am learning python
#after --> Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN

string="hi my name is john and i am learning python"

#1.yol
def string_değiştirme(string):
    boş_string=""
    yeni_string=[]
    for i in range(len(string)):
        if i%2==0:
            yeni_string.append(string[i].upper())
        if i%2==1:
            yeni_string.append(string[i])
    boş_string="".join(yeni_string)
    print(boş_string)
string_değiştirme(string)

#2.yol
def string_değiştirme2(string):
    boş_string=""
    for i in range(len(string)):
        #çift indeksli harfi büyütme
        if i%2==0:
            boş_string += string[i].upper()
        #tek indeksli harfi aynı bırakma
        else :
            boş_string += string[i]
    print(boş_string)
string_değiştirme2(string)

