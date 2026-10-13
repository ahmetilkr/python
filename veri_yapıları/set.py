#değiştirilebilir
#sırasızdır
#kapsayıcıdır

set1=set([1,3,5])
set2=set([1,2,3,5])

set1.difference(set2)  #set1 in set2 den farkı     set1-set2 ile aynı şey

set1.symmetric_difference(set2)   #iki kümede de birbirine göre olmayanlar
set2.symmetric_difference(set1)   #iki kümede de birbirine göre olmayanlar yukarıdakiyle aynı

set1.intersection(set2)  #kesişim
set2.intersection(set1)  #yukarıdakiyle aynı

set1.union(set2)  #birleşim
set2.union(set1)  #yukarıdaki ile aynı

set1.isdisjoint(set2)   #kesişimleri boş mu

set1.issubset(set2)   #set1 set2 nin alt kümesi mi




