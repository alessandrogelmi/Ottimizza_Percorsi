from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import requests

root = Tk()
root.geometry("415x535")
root.title("Ottimizza percorsi")

def getResult():
    text=entry.get("1.0", END)
    if text=='\n' or text==None:
        messagebox.showerror(title="Errore", message="Errore, inserire almeno 2 località")
    else:
        locations = text.splitlines()
        payload = {'locations': locations}
        response = requests.get('http://www.mapquestapi.com/directions/v2/optimizedroute?key=yourkey', json=payload)
        result = response.json()

        if response.status_code==200:
            return result
        else:
            return messagebox.showerror(title="Errore", message="Errore API")

def ottimizza():
    data = getResult()
    j=1
    for i in data['route']['locations']:
        output.insert(END, f"#{str(j)} " + i['adminArea5'] + '\n')
        j+=1

def infoViaggio():
    KM_TO_MILES = 0.62137 
    info = getResult()

    time = info['route']['formattedTime']
    distance = round(((info['route']['distance'])/KM_TO_MILES),2)
    if(info['route']['hasHighway']==True):
        autostrade = "SI"
    else:
        autostrade = "NO"

    messagebox.showinfo(title="Info viaggio", message=f"Tempo percorrenza: {time} \nLunghezza totale percorso: {distance} km \nAutostrade: {autostrade}")    

foto = PhotoImage(file=r"C:\\Users\\Utente\\Documents\\Ottimizza distanza\\Icon\\info2.png")

#WIDGET
enter = StringVar()
l1 = Label(root, text="Inserisci le località seprandole andando a capo: ")
entry = Text(root, width=50, height=12, wrap=WORD)
button = Button(root, text="Ottimizza", width=20)
l2 = Label(root, text="Percorso ottimizzato:")
output = Text(root, width=50, height=12, wrap=WORD)
buttonInfo = Button(root, text="Info", image=foto)

#POSITION
l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button.grid(row=3, column=1, columnspan=2, pady=5)
l2.grid(row=4, column=1, padx=5, sticky=W)
output.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))
buttonInfo.grid(row=6, column=1, columnspan=2, pady=5, padx=5, sticky=E)

#BUTTON COMMAND
button.configure(command=ottimizza)
buttonInfo.config(command=infoViaggio)

if __name__ == "__main__":
    root.mainloop()
