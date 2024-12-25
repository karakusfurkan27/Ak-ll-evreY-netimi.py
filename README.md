### **Çevre İzleme ve Analiz Uygulaması - README**

Bu proje, çevresel verilerin simülasyonu, analizi, uyarılar oluşturma, e-posta bildirimleri gönderme, API entegrasyonu, makine öğrenimi ile tahminler yapma, veri saklama ve görselleştirme gibi işlemleri gerçekleştiren bir Python uygulamasıdır.

---

### **Projenin Amacı**

Uygulama, çevresel koşulları izleyerek belirli eşik değerlerini aşan durumlar için uyarılar oluşturur ve gerekirse e-posta bildirimi gönderir. Ayrıca, gerçek hava durumu verilerini entegre etmek ve makine öğrenimi kullanarak gelecekteki sıcaklık tahminleri yapmak için tasarlanmıştır.

---

### **Kullanılan Kütüphaneler**

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:
- **random**: Çevresel veri simülasyonu için.
- **time**: Döngüsel işlemler için.
- **smtplib**: E-posta gönderimi için.
- **matplotlib**: Veri görselleştirme için.
- **numpy**: Sayısal işlemler için.
- **requests**: Hava durumu API'sine istek göndermek için.
- **pandas**: Verilerin CSV dosyasına kaydedilmesi için.
- **sklearn.linear_model (LinearRegression)**: Makine öğrenimi ile sıcaklık tahminleri yapmak için.

---

### **Fonksiyonlar**

#### 1. **Çevre Verisi Simülasyonu**
- `generate_temperature()`: Sıcaklık verisi üretir.
- `generate_humidity()`: Nem oranı verisi üretir.
- `generate_air_quality()`: Hava kalitesi indeksi üretir.
- `generate_wind_speed()`: Rüzgar hızı verisi üretir.
- `generate_sunlight()`: Güneş ışığı yoğunluğu verisi üretir.

#### 2. **Çevre Analizi ve Uyarılar**
- `analyze_environment(temperature, humidity, air_quality, wind_speed, sunlight)`: Çevresel koşulları analiz eder ve uyarılar oluşturur.

#### 3. **E-posta Bildirimi**
- `send_email(subject, body, to_email)`: Kullanıcıya uyarı e-postası gönderir.

#### 4. **Hava Durumu ve Hava Kalitesi API Entegrasyonu**
- `get_weather(city)`: Belirtilen şehir için gerçek zamanlı hava durumu verilerini alır. **Not**: Gerçek bir API anahtarına ihtiyaç duyulmaktadır.

#### 5. **Makine Öğrenimi ile Tahmin**
- `predict_temperature(historical_data)`: Geçmiş sıcaklık verilerine dayanarak bir sonraki sıcaklığı tahmin eder.

#### 6. **Veri Saklama**
- `save_data_to_csv(data, filename)`: Çevresel verileri bir CSV dosyasına kaydeder.

#### 7. **Veri Görselleştirme**
- `plot_data(temperature_data, humidity_data, air_quality_data, wind_speed_data, sunlight_data)`: Çevresel verileri grafiklerle görselleştirir.

#### 8. **Ana Uygulama**
- `main()`: Tüm işlemleri bir döngü içinde birleştirir. Simülasyon verilerini oluşturur, analiz eder, e-posta gönderir, tahmin yapar ve sonuçları görselleştirir.

---

### **Kurulum ve Çalıştırma**

1. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install matplotlib numpy pandas scikit-learn requests
   ```

2. **API Anahtarını Güncelleyin:**
   `get_weather` fonksiyonunda, `api_key` değişkenine kendi OpenWeatherMap API anahtarınızı ekleyin.

3. **E-posta Bilgilerini Güncelleyin:**
   `send_email` fonksiyonunda, gönderen e-posta adresi ve şifre bilgilerini kendi bilgilerinizle değiştirin.

4. **Uygulamayı Başlatın:**
   ```bash
   python main.py
   ```

---

### **Uyarılar**
- Hava durumu API'si entegrasyonu için internet bağlantısı gereklidir.
- E-posta gönderimi için SMTP ayarlarını doğru yapılandırmanız gerekmektedir.
- Veri simülasyonu ve grafikler için düzenli veri toplama döngüsü (10 saniyelik aralıklarla) çalıştırılmaktadır.

---

### **Projeyi Geliştirme Fikirleri**
- Yeni çevresel parametreler eklenebilir (örneğin, karbon emisyonu).
- Makine öğrenimi modelleri geliştirilebilir ve farklı algoritmalar entegre edilebilir.
- Kullanıcı arayüzü oluşturularak uygulama daha kullanıcı dostu hale getirilebilir.
