import requests
import os

KM_TO_MILES = 0.62137
clear = lambda: os.system('cls')
clear()

input_location = input("Inserisci i paesi con provincia e separati da un punto e virgola: (xx,pr; yy,pr;...): ")
clear()
locations = input_location.split(";")
print(f"Località inserite: {locations}")

payload = {'locations': locations}
response = requests.get('http://www.mapquestapi.com/directions/v2/optimizedroute?key=yourkey', json=payload)
result = response.json()

if response.status_code == 200:
    j = 1
    print("\nPercorso ottimizzato: ")
    for i in result['route']['locations']:
        print(f"#{j} {i['adminArea5']}")
        j+=1

    print("\nInfo viaggio:")
    print(f"Tot. tempo: {result['route']['formattedTime']}")
    print(f"Tot. {round(((result['route']['distance'])/KM_TO_MILES),2)} km")
    if(result['route']['hasHighway']==True):
        print("Autostrade: SI")
    else:
        print("Autostrade: NO")
else: 
    print(response.status_code)