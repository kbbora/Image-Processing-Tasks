# ÖZELLİK ALGILAMA VE EŞLEŞTİRME
Özellik algılama ve eşleştirme, görüntü işleme alanında hareketli yapıları incelemede, nesne tespiti ve görüntü tanıma gibi uygulamalarda önemli bir algoritmadır. Bu algoritma, bir görüntüde belirli özellik noktalarını veya desenleri bulmayı ve bunları başka bir görüntüdeki benzer özelliklerle eşleştirmeyi sağlar.
- 	Özellik algılama, bir görüntüdeki belirgin noktaları, kenarları, köşeleri veya desenleri belirleme işlemidir. Bu özellikler, görüntüler arasın da ilişkiler kurmak için kullanılır. Bu yöntem için kullanılan algoritma örnekleri ise  ‘Harris Köşe Algılayıcı’, ‘SIFT (Scale-Invariant Feature Transform)’, ‘SURF ( Speeded-Up Robust Features)’ ve ‘ORB (Oriented FAST and Rotated BRIEF)’ şeklindedir.
- 	Özellik eşleştirme, bir görüntüde algılanan özellik noktalarının, başka bir görüntüdeki benzer özellik noktalarıyla eşleştirilmesi işlemidir. Bu işlem, görüntüler arasında ortak noktaları ve benzerlikleri bulmak için kullanılır. Bu yöntem için kullanılan algoritma örnekleri ise ‘Brute-Force Eşleştirme’, FLANN (Fast Library for Approximate Nearest Neighbors), KNN (K-Nearest Neighbors) şeklindedir.
## Harris Köşe Algılama
Harris köşe algılama algoritması, köşe noktalarını tespit etmek için kullanılan bir görüntü işleme uygulamasıdır. Bu algoritma, köşe noktalarının yoğun bir şekilde değişen kenarların kesiştiği noktalarda bulunduğunu varsayar. Görüntüdeki her pikselin etrafındaki yoğunluğa göre bu yoğunluğu yorumlayarak bir köşe noktası olup olmadığını hesaplar.
![image](https://github.com/user-attachments/assets/aa988f8b-4ab6-44ce-b4f7-f77a0a880f91)
Harris köşe algılama algoritmasını kullanmak için  cv2.cornerHarris() fonksiyonunu kullanarak basit bir uygulama örneği yaptık. Ve sonuç olarak bu algoritma satranç tahtası üzerindeki tüm köşeleri tespit etmeyi başarılı bir şekilde gerçekleştirdi.
![image](https://github.com/user-attachments/assets/ba9701f3-5076-4f73-9e84-22a66b17b37f)
## SIFT ( Scale-Invraiant Feature Transform )
Makineler ölçek veya perspektifinde farklılıklar olan görüntüleri tanımakta zorlanır. SIFT, görüntülerden ayırt edici özellikler çıkararak makinelerin bu özellikleri aynı nesnenin yeni görüntüleriyle eşleştirmesine olanak tanır. Bu sayede görüntü tanıma, nesne tespiti gibi görüntü işleme uygulamalarının gerçekleştirilmesini sağlar. SIFT algoritmasının tüm bunları yapabilmesinin sebebi görüntülerdeki anahtar noktalar yani ‘key-point’ lerdir. Bu key-pointler bilgisayarlı görü uygulamaları için kullanılabilen ölçek ve dönüş değişmezleridir. SIFT kullanılarak oluşturulan bu keypoint’ler görüntülerdeki boyut, açı ve perspektif değişimlerinden etkilenmezler ve bu sayede makineler aynı nesnenin farklı açılardan çekilmiş görüntüleri arasında ilişki kurarak onları tanıyabilir.

![image](https://github.com/user-attachments/assets/959c0c7e-5a61-41dc-8c9f-fe927b40ce91)

İki farklı perspektife sahip Pisa Kulesi için basit bir SIFT uygulaması yaparsak;
![image](https://github.com/user-attachments/assets/37fb6047-6532-484e-a592-188b2fed487e)
![image](https://github.com/user-attachments/assets/5c0afb66-68f1-4c2b-bc1c-5fac8aada90f)

![image](https://github.com/user-attachments/assets/68ed0f33-9dc2-41eb-afd0-486b7bf04cf0)

- Sonuç görseli
![image](https://github.com/user-attachments/assets/1b0b359f-6d01-465f-a05b-d3f77afdddeb)

## SURF (Speeded-Up Robust Features)
SURF, görüntü işleme alanında kullanılan bir özellik algılama ve eşleştirme algoritmasıdır. 2006 yılında Herbert Bay et al. tarafından geliştirilmiştir. SURF, özellikle SIFT (Scale-Invariant Feature Transform) algoritmasının hızını artırmak ve hesaplama maliyetini düşürmek amacıyla tasarlanmıştır.
- Hesaplama Hızı ve Verimlilik: SURF, integral görüntü kullanarak hesaplama süresini önemli ölçüde azaltır. Bu, özellikle büyük veri setleri veya gerçek zamanlı uygulamalar için önemlidir. SIFT ise daha karmaşık hesaplama yöntemleri kullanarak daha yüksek hesaplama maliyetine sahiptir.
- Ölçek Uyumlu Özelliklerin Bulunması: SIFT, görüntülerdeki özellikleri farklı ölçeklerde tarayarak bulur ve bu sayede ölçek değişikliklerine karşı invariyant özellikler elde eder. SURF ise bu özellikleri bulurken daha hızlı bir yöntem kullanır ve bu da genellikle daha hızlı eşleştirme sağlar.
- Özellik Vektörü Boyutları: SIFT, her bir özellik noktası için 128 boyutlu bir vektör üretir. Bu vektörler, özellik noktasının etrafındaki gradient bilgilerini temsil eder. SURF ise genellikle daha küçük boyutlu vektörler kullanır (örneğin 64 boyutlu). Bu, bellek kullanımı ve hesaplama maliyeti açısından fark yaratabilir.
- Yönelim İnvariyansı ve Robustluk: Her iki algoritma da özelliklerin yönelimine karşı invariyans sağlar. Ancak SURF, bu özelliği sağlarken daha hızlı ve verimli olabilir. Ayrıca SURF, görüntülerdeki ışık değişikliklerine ve gürültülere karşı da SIFT'e göre daha dirençli olabilir.
- Uygulama Alanları: SURF genellikle gerçek zamanlı sistemlerde ve hızlı işlem gerektiren uygulamalarda tercih edilirken, SIFT genellikle daha geniş bir uygulama yelpazesine sahiptir. Özellikle detaylı ve hassas eşleştirme gerektiren uygulamalarda SIFT tercih edilebilir.

![image](https://github.com/user-attachments/assets/664fae35-b54e-43ba-828f-5bcbe8381a5b)

Bu algoritma patentli olduğundan maalesef bir uygulama örneği yapamıyoruz.

## ORB (Oriented FAST and Rotated BRIEF)
ORB, esas olarak SIFT ve SURF’ ün patentli uygulamalar olması sebebiyle tasarlandı. Temel işlevi anlamında bu uygulamalardan çok daha iyi performans gösterir. ORB, iyi bilinen FAST anahtar nokta dedektörü ve BRIEF tanımlayıcısı üzerine kuruludur. Bu tekniklerin her ikisi de iyi performansları ve düşük maliyetleri nedeniyle ORB algoritmasını daha kullanışlı kılar.
- Kıyas olması açısından aynı Pisa Kulesi görüntüleri üzerinde ORB algoritmasını çalıştıralım.

![image](https://github.com/user-attachments/assets/db7aa1ec-7de2-4a72-b159-90b755644237)

![image](https://github.com/user-attachments/assets/984373d1-d98d-4b2d-a9e2-48182f40dbef)

Bu sonuç görselinde eşleşmelerin daha tutarlı olduğunu görüyoruz.
