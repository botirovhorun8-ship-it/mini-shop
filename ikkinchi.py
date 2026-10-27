
# name = [12 , 56, "Horun"]
# for nnn in name:
#     print(nnn)
# a = int(input("son kirit? "))
# for i in range(1, a+1): 
#     if i % 2 == 0: 
#         print(f"{i} bu juft son")
#     else: 
#         print(f"{i} bu toq son")
    
# name = [12 , 56, "Horun"]
# for i in name:
#     print(i)
# a = int(input("son kirit? "))
# if i % 2 == 0: 
#     print(f"{i} bu juft son")
# else: 
#     print(f"{i} bu toq son")


# products = {
#     "olma": {"narx": 12000, "soni": 20},
#     "banan": {"narx": 18000, "soni": 15},
#     "non": {"narx": 4000, "soni": 30}
# }

# while True:
#     print("\n1. Mahsulotlarni ko'rish")
#     print("2. Mahsulot qo'shish")
#     print("3. Mahsulot qidirish")
#     print("4. Mahsulot sonini o'zgartirish")
#     print("5. Umumiy qiymat")
#     print("6. Chiqish")

#     tanlov = input("Tanlov: ")

#     if tanlov == "1":
#         for nom, malumot in products.items():
#             print(nom, malumot)

#     elif tanlov == "2":
#         nom = input("Mahsulot nomi: ").lower()
#         if nom in products:
#             print("Bu mahsulot mavjud!")
#         else:
#             narx = int(input("Narxi: "))
#             soni = int(input("Soni: "))
#             if narx > 0 and soni >= 0:
#                 products[nom] = {"narx": narx, "soni": soni}
#                 print("Mahsulot qo'shildi!")
#             else:
#                 print("Narx yoki son noto'g'ri!")

#     elif tanlov == "3":
#         nom = input("Mahsulot nomi: ").lower()
#         if nom in products:
#             print(products[nom])
#         else:
#             print("Mahsulot topilmadi!")

#     elif tanlov == "4":
#         nom = input("Mahsulot nomi: ").lower()
#         if nom in products:
#             soni = int(input("Yangi soni: "))
#             if soni >= 0:
#                 products[nom]["soni"] = soni
#                 print("Soni o'zgartirildi!")
#             else:
#                 print("Soni manfiy bo'lmasin!")
#         else:
#             print("Mahsulot topilmadi!")

#     elif tanlov == "5":
#         jami = 0
#         for malumot in products.values():
#             jami += malumot["narx"] * malumot["soni"]
#         print("Umumiy qiymat:", jami, "so'm")

#     elif tanlov == "6":
#         print("Xayr, bro!")
#         break

#     else:
#         print("Noto'g'ri tanlov!")



# import tkinter as tk

# oyna = tk.Tk()
# oyna.title("Kalkulyator")
# oyna.geometry("300x400")
# oyna.configure(bg="#0A3A29")

# ekran = tk.Entry(oyna, font=("Arial", 24), justify="right")
# ekran.pack(fill="x", padx=10, pady=10)

# def bos(b):
#     if b == "C":
#         ekran.delete(0, tk.END)
#     elif b == "=":
#         try:
#             natija = eval(ekran.get())
#             ekran.delete(0, tk.END)
#             ekran.insert(0, str(natija))
#         except:
#             ekran.delete(0, tk.END)
#             ekran.insert(0, "Xato")
#     else:
#         ekran.insert(tk.END, b)

# tugmalar = [
#     ["7", "8", "9", "/"],
#     ["4", "5", "6", "*"],
#     ["1", "2", "3", "-"],
#     ["C", "0", "=", "+"]
# ]

# for qator in tugmalar:
#     ramka = tk.Frame(oyna)
#     ramka.pack(expand=True, fill="both")
#     for b in qator:
#         tk.Button(
#             ramka, text=b, font=("Arial", 18),
#             command=lambda x=b: bos(x)
#         ).pack(side="left", expand=True, fill="both")

# oyna.mainloop()

# oyna = tk.Tk()
# oyna.title("Mening kalkulyatorim")
# oyna.geometry("300x400")
# oyna.configure(bg="#202020")
# ekran = tk.Entry(oyna, font=("Arial",24),justify="right")
# ekran.pack(fill="x", padx=10, pady=10)
# tugma = tk.Button(oyna , text="7")
# tugma.pack(command=lambda: ekran.insert(tk.END, "7"))
# tugma.pack(fill="both" , expand=True)
# import tkinter as tk 
# oyna = tk.Tk()
# oyna.title("Mening kalkulyatorim")
# oyna.geometry("300x400")
# oyna.configure(bg="#202020")
# ekran = tk.Entry(oyna, font=("Arial",24),justify="right")
# ekran.pack(fill="x", padx=10, pady=10)
# tugmalar_joyi = tk.Frame (bg= "#202020")
# tugmalar_joyi.pack(fill="both" , expand=True)
# for i in range(4):
#     tugmalar_joyi.columnconfigure(i, weight=1)
# for i in range(5):
#     tugmalar_joyi.rowconfigure(i, weight=1)
# tugma = tk.Button(tugmalar_joyi,text="7",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "7"))
# tugma.grid(row=1, column=0, sticky="nsew")
# tugma8 = tk.Button(tugmalar_joyi,text="8",font=("Arial", 16),bg="#00A86B",fg="white",activebackground="#00CC88",command=lambda: ekran.insert(tk.END, "8"))
# tugma8.grid(row=1, column=1, sticky="nsew")
# tugma9 = tk.Button(tugmalar_joyi,text="9",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "9"))
# tugma9.grid(row=1, column=2, sticky="nsew")
# tugma4 = tk.Button(tugmalar_joyi,text="4",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "4"))
# tugma4.grid(row=2, column=0, sticky="nsew")
# tugma5 = tk.Button(tugmalar_joyi,text="5",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "5"))
# tugma5.grid(row=2, column=1, sticky="nsew")
# tugma6 = tk.Button(tugmalar_joyi,text="6",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "6"))
# tugma6.grid(row=2, column=2, sticky="nsew")
# tugma_qoshish = tk.Button(tugmalar_joyi,text="+",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.insert(tk.END, "+"))
# tugma_qoshish.grid(row=3, column=3, sticky="nsew")
# def hisobla():
#     if "+" in ekran.get():
#         sonlar = ekran.get().split("+")
#         natija = int(sonlar[0]) + int(sonlar[1])
#     elif "-" in ekran.get():    
#         sonlar = ekran.get().split("-")
#         natija = int(sonlar[0]) - int(sonlar[1])
#     elif "*" in ekran.get():    
#         sonlar = ekran.get().split("*")
#         natija = int(sonlar[0]) * int(sonlar[1])  
#     elif "/" in ekran.get():    
#         sonlar = ekran.get().split("/")
#         natija = int(sonlar[0]) / int(sonlar[1])    
#     else:
#         return
#     ekran.delete(0, tk.END)
#     ekran.insert(0, str(natija))

# tugma_teng = tk.Button(tugmalar_joyi,text="=",font=("Arial", 16),bg="#404040",fg="white",command=hisobla)
# tugma_teng.grid(row=4, column=3, sticky="nsew")
# tugma_ayirish = tk.Button(tugmalar_joyi,text="-",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.insert(tk.END, "-"))
# tugma_ayirish.grid(row=2, column=3, sticky="nsew")
# tugma_kopaytirish = tk.Button(tugmalar_joyi,text="×",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.insert(tk.END, "*"))
# tugma_kopaytirish.grid(row=1, column=3, sticky="nsew")
# tugma_bolish = tk.Button(tugmalar_joyi,text="/",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.insert(tk.END, "/"))
# tugma_bolish.grid(row=0, column=3, sticky="nsew")
# tugma_tozalash = tk.Button(tugmalar_joyi,text="C",font=("Arial", 16),bg="#E53935",fg="white",command=lambda: ekran.delete(0, tk.END))
# tugma_tozalash.grid(row=0, column=0, sticky="nsew")
# tugma0 = tk.Button(tugmalar_joyi,text="0",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "0"))
# tugma0.grid(row=4, column=1, sticky="nsew")
# tugma1 = tk.Button(tugmalar_joyi,text="1",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "1"))
# tugma1.grid(row=3, column=0, sticky="nsew")
# tugma2 = tk.Button(tugmalar_joyi,text="2",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "2"))
# tugma2.grid(row=3, column=1, sticky="nsew")
# tugma3 = tk.Button(tugmalar_joyi,text="3",font=("Arial", 16),bg="#00A86B",fg="white",command=lambda: ekran.insert(tk.END, "3"))
# tugma3.grid(row=3, column=2, sticky="nsew")
# tugma_nuqta = tk.Button(tugmalar_joyi,text=".",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.insert(tk.END, "."))
# tugma_nuqta.grid(row=4, column=2, sticky="nsew")
# tugma_ochirish = tk.Button(tugmalar_joyi,text="⌫",font=("Arial", 16),bg="#404040",fg="white",command=lambda: ekran.delete(len(ekran.get())-1, tk.END))
# tugma_ochirish.grid(row=0, column=1, sticky="nsew")
# oyna.mainloop()

