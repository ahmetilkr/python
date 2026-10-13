from torch.distributed import group

öğrenciler=["ahmet","mehmet","mahmut","ali"]

#enumerate hem idexi hem de o indexteki öğrenciyi verir
for index,öğrenci in enumerate(öğrenciler):
    print(index,öğrenci)


#uygulama
#divide_students fonksiyonu yazınız
#çift indexte yer alan öğrencileri bir listeye ekleyin
#tek indexte yer alan öğrencileri başka bir listeye ekleyin
#ama bu iki liste tek bir liste olarak return olsun


students=["john","mark","venessa","mariam"]
def divide_students(students):
    groups=[[],[]]
    for index,student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else :
            groups[1].append(student)
    return groups


st=divide_students(students)
st[0]
st[1]


