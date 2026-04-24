import requests

def get_cuaca(nama_kota):
    url_kota = "https://geocoding-api.open-meteo.com/v1/search?name=" + nama_kota
    url = "https://api.open-meteo.com/v1/forecast"
    
    response_url_kota = requests.get(url_kota)

    if response_url_kota.status_code == 200:
        geocoding_result = response_url_kota.json()
        latitude_kota = geocoding_result["results"][0]["latitude"]
        longitude_kota = geocoding_result["results"][0]["longitude"]
    else:
        print(f"Error: {response_url_kota.status_code}")
        return

    params = {
        "latitude": latitude_kota,
        "longitude": longitude_kota,
        "current": "temperature_2m,windspeed_10m",
        "timezone": "Asia/Jakarta"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        cuaca_result = response.json()
        suhu = cuaca_result["current"]["temperature_2m"]
        angin = cuaca_result["current"]["windspeed_10m"]
        print(f"Cuaca di {nama_kota}:")
        print(f"  Suhu   : {suhu}°C")
        print(f"  Angin  : {angin} km/h")
    else:
        print(f"Error: {response.status_code}")

input_kota = input("Masukkan nama kota: ")

get_cuaca(input_kota)