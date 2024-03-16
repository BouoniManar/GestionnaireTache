import tkinter as tk
from tkinter import messagebox, simpledialog

fenetre = tk.Tk()
fenetre.title("Liste de taches")

listbox = tk.Listbox(fenetre, font=("Arial", 12), selectbackground="#4286f4", selectforeground="white")
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(fenetre, font=("Arial", 12))
entry.pack(pady=5, padx=10)

frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(pady=5)

def ajouter_tache():
    tache = entry.get()
    if tache:
        listbox.insert(tk.END, tache)
        entry.delete(0, tk.END)

def supprimer_tache():
    index = listbox.curselection()
    if index:
        selection = listbox.get(index)
        confirmation = messagebox.askyesno("Confirmation", f"Etes-vous sûr de vouloir supprimer la tache '{selection}' ?")
        if confirmation:
            listbox.delete(index)

def modifier_tache():
    index = listbox.curselection()
    if index:
        ancienne_tache = listbox.get(index)
        nouvelle_tache = simpledialog.askstring("Modifier la tache", "Nouvelle tache :", initialvalue=ancienne_tache)
        if nouvelle_tache:
            listbox.delete(index)
            listbox.insert(index, nouvelle_tache)

bouton_ajouter = tk.Button(frame_boutons, text="Ajouter", command=ajouter_tache, font=("Arial", 12), bg="#4286f4", fg="white", relief="flat", padx="10")
bouton_ajouter.pack(side=tk.LEFT, padx=5)

bouton_supprimer = tk.Button(frame_boutons, text="Supprimer", command=supprimer_tache, font=("Arial", 12), bg="#f44336", fg="white", relief="flat", padx="10")
bouton_supprimer.pack(side=tk.LEFT, padx=5)

bouton_modifier = tk.Button(frame_boutons, text="Modifier", command=modifier_tache, font=("Arial", 12), bg="#4caf50", fg="white", relief="flat", padx="10")
bouton_modifier.pack(side=tk.LEFT, padx=5)

fenetre.mainloop()