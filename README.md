# flask-docker-projem
Günlük Alışkanlıklardan Kaynaklanan Hastalık Riski projesini 2 kişilik takım olarak yapmış bulunmaktayız.
# Günlük Alışkanlıklardan Kaynaklanan Hastalık Riski Analizi

Bu proje, bireylerin günlük yaşam alışkanlıklarının sağlık üzerindeki etkilerini analiz ederek, potansiyel hastalık risklerini tahmin etmeyi amaçlamaktadır. Veri seti Kaggle üzerinden temin edilmiştir ve proje içerisinde veri analizi, makine öğrenmesi, görselleştirme, otomasyon, web arayüzü, PDF raporlama ve konteynerleştirme gibi çeşitli bileşenler barındırmaktadır.

## 👥 Takım Üyeleri ve Katkılar

**Lena Keskin**
- Veri analizi ve görselleştirme (Power BI)
- Makine öğrenmesi modelleri (SVM, Naive Bayes, Karar Ağaçları)
- Özellik mühendisliği
- WSL 2 & Docker kurulumu ve yapılandırması
- Dockerfile oluşturma ve container çalıştırma

**Nehir Kurudere**
- Veri ön işleme (eksik verilerin giderilmesi, dönüştürmeler)
- Otomasyon sistemi (schedule/cron gibi zamanlama mekanizmaları)
- Web arayüzü (Flask tabanlı)
- PDF çıktısı ile raporlama

---

## 📁 Proje Yapısı

```bash
.
├── app/
│   ├── app.py              # Flask uygulaması
│   ├── static/             # CSS / JS / Görseller
│   ├── templates/          # HTML sayfaları
│   └── reports/            # Oluşturulan PDF raporları
├── dataset/
│   └── lifestyle_data.csv  # Kaggle'dan alınan veri seti
├── dockerfile              # Docker imajı oluşturmak için
├── requirements.txt        # Python bağımlılıkları
├── automation/
│   ├── schedule_script.py  # Zamanlanmış görev scripti
├── powerbi/
│   └── analysis.pbix       # Power BI görselleştirmeleri
├── README.md               # Bu dosya
Web Arayüzü
Web arayüzüne http://localhost:5000 adresinden erişilebilir.
