import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

list_message = []

def tanya_ai(pertanyaan):
    list_message.append({"role": "user", "content": pertanyaan})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages= list_message
    )
    return response.choices[0].message.content


print("Halo! Nice To meet you")

while True:
    print("========================")
    print("Please Select an option below!")
    print("1. Tanya AI")
    print("2. Exit")
    print("3. Tambahkan Personalisasi")
    user_input = int(input("Masukkan Pilihan Anda: "))

    if user_input == 1:
        pertanyaan = input("Masukkan Pertanyaan: ")
        jawaban = tanya_ai(pertanyaan)
        list_message.append({"role": "assistant", "content": jawaban})
        print(f"\nAI: {jawaban}")
    elif user_input == 2:
        break
    elif user_input == 3:
        personalisasi = input("Masukkan personalisasi yang anda inginkan: ")
        list_message.append({"role": "system", "content": personalisasi})
    else :
        print("Invalid Option!")
    
print("Thank You!!!")