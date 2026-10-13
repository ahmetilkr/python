#conda create -n sanal_ortam_ismi -->sanal ortamı conda ile oluşturur

#conda env remove -n SalanOrtamınİsmi --> Sanal ortamı siler

#conda env create -f environment.yaml --> yaml dosyasını indirir ve bu yaml dosyası hangi sanal ortamda indirildiyse diyelim ki ismi myenv yaml dosyasını indirirken myenvide kurar conda

#conda env list --> pcdeki sanal ortamların listesi

#conda activate myenv --> oluşturulan sanal ortamı aktif eder yani içine girer

#conda deactivate --> sanal ortamdan çıkış yapar

#conda list --> indirilen paketleri listeler

#conda install paketin_ismi --> paketi indirir

#conda install paket1 paket2 paket3 --> aynı anda birden fazla pkaeti yükleme

#conda remove paketin_ismi --> paketi siler

#conda install paket_ismi=version --> belirli versiyondaki paketi yükler

#conda upgrade paketin_ismi --> paketin en güncel versiyonunu indir

#conda upgrade -all --> tüm kütüphanelerin güncellenmesi

#conda env export > environment.yaml --> paket süümlerini başka sanal ortamda kullanmak için yaml dosyasına aktarmak




