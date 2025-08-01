# Gerekli kütüphaneleri içe aktar
from flask import Flask, render_template, request, jsonify
import subprocess
import os

# Flask uygulamasını başlat
app = Flask(__name__)

# Ana sayfa (http://127.0.0.1:5000) için rota
@app.route('/')
def index():
    # 'templates' klasöründeki 'index.html' dosyasını kullanıcıya göster
    return render_template('index.html')

# '/execute' adresine komut geldiğinde çalışacak rota
@app.route('/execute', methods=['POST'])
def execute_powershell():
    # Web sayfasındaki formdan 'command' adlı veriyi al
    command = request.form.get('command')

    # Komut boşsa hata döndür
    if not command:
        return jsonify({
            'success': False,
            'output': '',
            'error': 'Komut boş olamaz.'
        })

    try:
        # PowerShell'i harici bir işlem olarak çalıştır.
        # Bu, web sunucusu için en güvenli yoldur.
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", command], # -NoProfile başlangıcı hızlandırır
            capture_output=True,  # Çıktıyı yakala
            text=True,            # Çıktıyı metin olarak al
            timeout=30,           # 30 saniyeden uzun sürerse işlemi sonlandır
            check=False           # Hata durumunda Python'un çökmesini engelle
        )

        # Başarılı çıktı varsa stdout'u, yoksa stderr'i al
        output_message = result.stdout if result.stdout else result.stderr
        
        # Her şeyi JSON formatında web arayüzüne geri gönder
        return jsonify({
            'success': result.returncode == 0, # Komut başarılı ise True (çıkış kodu 0)
            'output': output_message
        })
        
    except subprocess.TimeoutExpired:
        # Zaman aşımı hatasını yakala
        return jsonify({
            'success': False,
            'output': 'HATA: Komut 30 saniyede tamamlanamadı ve zaman aşımına uğradı.'
        })
    except Exception as e:
        # Diğer tüm olası hataları yakala
        return jsonify({
            'success': False,
            'output': f'Sunucuda bir hata oluştu: {str(e)}'
        })

# Bu script doğrudan çalıştırıldığında...
if __name__ == '__main__':
    # Uygulamayı hata ayıklama modunda çalıştır (geliştirme için)
    app.run(debug=True)