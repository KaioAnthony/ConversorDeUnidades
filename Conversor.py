import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Conversor de Unidades")
root.geometry("450x400")

def converter():
    try:
        valor = float(entry.get()) 
        de = origem.get()  
        para = destino.get()

        if de == "megabyte" and para == "kilobyte":
            resultado_valor = valor * 1024
        elif de == "megabyte" and para == "byte":
            resultado_valor = valor * 1024 * 1024 
        elif de == "megabyte" and para == "gigabyte":
            resultado_valor = valor / 1024
        elif de == "megabyte" and para == "terabyte":
            resultado_valor = valor / 1024 / 1024
        elif de == "kilobyte" and para == "megabyte":
            resultado_valor = valor / 1024
        elif de == "kilobyte" and para == "byte":
            resultado_valor = valor * 1024  
        elif de == "kilobyte" and para == "gigabyte":
            resultado_valor = valor / 1024 / 1024
        elif de == "kilobyte" and para == "terabyte":
            resultado_valor = valor / 1024 / 1024 / 1024
        elif de == "gigabyte" and para == "megabyte":
            resultado_valor = valor * 1024
        elif de == "gigabyte" and para == "kilobyte":
            resultado_valor = valor * 1024 * 1024
        elif de == "gigabyte" and para == "byte":
            resultado_valor = valor * 1024 * 1024 * 1024 
        elif de == "gigabyte" and para == "terabyte":
            resultado_valor = valor / 1024
        elif de == "terabyte" and para == "kilobyte":
            resultado_valor = valor * 1024 * 1024 * 1024 * 1024
        elif de == "terabyte" and para == "megabyte":
            resultado_valor = valor * 1024 * 1024 * 1024
        elif de == "terabyte" and para == "byte":
            resultado_valor = valor * 1024 * 1024 * 1024 * 1024 * 1024
        elif de == "terabyte" and para == "gigabyte":
            resultado_valor = valor * 1024
        elif de == "byte" and para == "kilobyte":
            resultado_valor = valor / 1024
        elif de == "byte" and para == "megabyte":
            resultado_valor = valor / 1024 / 1024
        elif de == "byte" and para == "gigabyte":
            resultado_valor = valor / 1024 / 1024 / 1024
        elif de == "byte" and para == "terabyte":
            resultado_valor = valor / 1024 / 1024 / 1024 / 1024
        else:
            resultado_valor = "Unidades inválidas ou não suportadas"

        resultado.set(f"{resultado_valor:.2f} {para}")  
    except ValueError:
        resultado.set("Valor inválido") 
    except Exception as e:
        resultado.set(f"Erro: {str(e)}") 

label = ctk.CTkLabel(root, text="Digite o valor:", font=("Arial", 20))
label.pack(pady=10)

entry = ctk.CTkEntry(root, font=("Arial", 14), width=200, justify="center")
entry.pack(pady=5)

label_unidade_de = ctk.CTkLabel(root, text="De:", font=("Arial", 15))
label_unidade_de.pack(pady=5)

origem = ctk.StringVar(value="byte")
menu_unidade_de = ctk.CTkOptionMenu(root, values=["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"], variable=origem)
menu_unidade_de.pack(pady=5)

label_destino = ctk.CTkLabel(root, text="Para:", font=("Arial", 15))
label_destino.pack(pady=5)

destino = ctk.StringVar(value="kilobyte")
menu_destino = ctk.CTkOptionMenu(root, values=["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"], variable=destino)
menu_destino.pack(pady=5)

botao_converter = ctk.CTkButton(root, text="Converter", command=converter)
botao_converter.pack(pady=10)

resultado = ctk.StringVar() 

label_resultado = ctk.CTkLabel(root, textvariable=resultado, font=("Arial", 16, "bold"))
label_resultado.pack(pady=10)

def trocar_modo():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

botao_tema = ctk.CTkButton(root, text="Trocar Tema", command=trocar_modo)
botao_tema.pack(pady=5)

root.mainloop()