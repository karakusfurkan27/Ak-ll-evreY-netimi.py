import random
import time
import smtplib
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sklearn.linear_model import LinearRegression

# 1. Çevre Verisi Simülasyonu
def generate_temperature():
    return round(random.uniform(15.0, 35.0), 2)

def generate_humidity():
    return round(random.uniform(30.0, 80.0), 2)

def generate_air_quality():
    return random.randint(50, 200)

def generate_wind_speed():
    return round(random.uniform(0.0, 25.0), 2)

def generate_sunlight():
    return round(random.uniform(0.0, 100.0), 2)

# 2. Çevre Analizi ve Uyarılar
def analyze_environment(temperature, humidity, air_quality, wind_speed, sunlight):
    warnings = []
    if temperature > 30.0:
        warnings.append("Sıcaklık yüksek! Soğutma cihazlarını kontrol edin.")
    if humidity > 70.0:
        warnings.append("Nem oranı yüksek! Havalandırma yapın.")
    if air_quality > 150:
        warnings.append("Hava kalitesi kötü! Filtreleri temizleyin.")
    if wind_speed > 20.0:
        warnings.append("Rüzgar hızı çok yüksek! Dışarı çıkarken dikkatli olun.")
    if sunlight < 10.0:
        warnings.append("Güneş ışığı düşük! Enerji verimliliğinizi artırın.")
    
    if not warnings:
        return "Çevresel koşullar iyi."
    else:
        return "Uyarılar: " + ", ".join(warnings)

# 3. E-posta Bildirimi
def send_email(subject, body, to_email):
    sender_email = "your_email@example.com"  # Gönderen e-posta adresi
    receiver_email = to_email  # Alıcı e-posta adresi
    password = "your_email_password"  # Gönderenin e-posta şifresi
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("E-posta gönderildi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# 4. Hava Durumu ve Hava Kalitesi API Entegrasyonu
def get_weather(city):
    api_key = "your_actual_api_key_here"  # Gerçek API anahtarınızı buraya ekleyin
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if data.get("cod") == 200:
                main = data["main"]
                weather_desc = data["weather"][0]["description"]
                temperature = main["temp"] - 273.15  # Kelvin'den Celsius'a dönüştür
                humidity = main["humidity"]
                wind_speed = data["wind"]["speed"]
                sunlight = data["clouds"]["all"]  # Güneş ışığı yoğunluğu için bulut yoğunluğu verisini alıyoruz
                return {
                    "city": city,
                    "description": weather_desc,
                    "temperature": temperature,
                    "humidity": humidity,
                    "wind_speed": wind_speed,
                    "sunlight": sunlight
                }
            else:
                return f"Hata: Hava durumu verisi alınamadı. API'den gelen hata: {data.get('message', 'Bilinmeyen hata')}"
        else:
            return f"API hatası: {response.status_code}. Lütfen API anahtarınızı kontrol edin ve bağlantıyı doğrulayın."

    except requests.exceptions.RequestException as e:
        return f"İstek hatası: {e}. Lütfen internet bağlantınızı kontrol edin ve tekrar deneyin."

# 5. Makine Öğrenimi ile Çevresel Öngörü
def predict_temperature(historical_data):
    if len(historical_data) < 2:
        return "Veri yetersiz. Daha fazla veri ekleyin."
    
    model = LinearRegression()
    X = np.array(range(len(historical_data))).reshape(-1, 1)
    y = np.array(historical_data)
    model.fit(X, y)
    prediction = model.predict([[len(historical_data) + 1]])
    return f"Gelecek sıcaklık tahmini: {prediction[0]:.2f}°C"

# 6. Veri Saklama (CSV'ye Kaydetme)
def save_data_to_csv(data, filename="environment_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=False, index=False)

# 7. Veri Görselleştirme (Grafikler)
def plot_data(temperature_data, humidity_data, air_quality_data, wind_speed_data, sunlight_data):
    time_data = list(range(len(temperature_data)))
    plt.figure(figsize=(10,8))

    plt.subplot(3, 1, 1)
    plt.plot(time_data, temperature_data, label='Sıcaklık (°C)', color='red')
    plt.title('Zamanla Sıcaklık')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Sıcaklık (°C)')

    plt.subplot(3, 1, 2)
    plt.plot(time_data, humidity_data, label='Nem (%)', color='blue')
    plt.title('Zamanla Nem')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Nem (%)')

    plt.subplot(3, 1, 3)
    plt.plot(time_data, air_quality_data, label='Hava Kalitesi (AQI)', color='green')
    plt.title('Zamanla Hava Kalitesi')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Hava Kalitesi (AQI)')

    plt.tight_layout()
    plt.show()

# 8. Ana Uygulama
def main():
    temperature_data = []
    humidity_data = []
    air_quality_data = []
    wind_speed_data = []
    sunlight_data = []

    while True:
        # Gerçek çevresel verileri simüle et
        temperature = generate_temperature()
        humidity = generate_humidity()
        air_quality = generate_air_quality()
        wind_speed = generate_wind_speed()
        sunlight = generate_sunlight()

        # Çevresel koşulları analiz et
        result = analyze_environment(temperature, humidity, air_quality, wind_speed, sunlight)
        print(f"Sıcaklık: {temperature}°C, Nem: {humidity}%, Hava Kalitesi: {air_quality}, Rüzgar Hızı: {wind_speed} km/h, Güneş Işığı: {sunlight}%")
        print(result)

        # E-posta bildirim gönderme (örnek olarak)
        if air_quality > 150:
            send_email("Hava Kalitesi Uyarısı", "Hava kalitesi seviyeniz yüksek!", "user_email@example.com")

        # Hava durumu API'si entegrasyonu (örnek olarak)
        weather_info = get_weather("Istanbul")
        print(weather_info)

        # Makine öğrenimi ile tahmin
        prediction = predict_temperature(temperature_data)
        print(prediction)

        # Veriyi CSV dosyasına kaydet
        data = {
            "temperature": temperature,
            "humidity": humidity,
            "air_quality": air_quality,
            "wind_speed": wind_speed,
            "sunlight": sunlight
        }
        save_data_to_csv([data])

        # Verileri listeye ekle
        temperature_data.append(temperature)
        humidity_data.append(humidity)
        air_quality_data.append(air_quality)
        wind_speed_data.append(wind_speed)
        sunlight_data.append(sunlight)

        # 10 saniye sonra tekrar veri al
        time.sleep(10)

        # Veri görselleştirme
        plot_data(temperature_data, humidity_data, air_quality_data, wind_speed_data, sunlight_data)

if __name__ == "__main__":
    main()
