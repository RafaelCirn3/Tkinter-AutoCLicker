import tkinter as tk
from tkinter import ttk  # Usar ttk para widgets estilizados
import threading
import pyautogui
import time
import keyboard  # Biblioteca para detectar pressionamento de teclas

# Variáveis globais para controlar o estado do autoclicker
clicking = False
click_delay = 0.1  # Delay padrão de 0.1 segundos
click_count = 1    # Número padrão de cliques por execução
mouse_button = "left"  # Botão do mouse padrão

# Função que realiza o clique automático
def start_clicking():
    global clicking, click_delay, click_count, mouse_button
    while clicking:
        for _ in range(click_count):
            pyautogui.click(button=mouse_button)
            time.sleep(0.05)  # Pequeno intervalo entre múltiplos cliques
        time.sleep(click_delay)

# Função para iniciar o autoclicker
def start():
    global clicking, click_delay, click_count, mouse_button
    try:
        click_delay = float(delay_entry.get())
        click_count = int(click_choice.get())
        mouse_button = button_choice.get()
        clicking = True
        click_thread = threading.Thread(target=start_clicking)
        click_thread.start()
        status_label.config(text="Status: Running", foreground="green")
    except ValueError:
        status_label.config(text="Erro: Por favor, insira um valor válido para o delay.", foreground="red")

# Função para parar o autoclicker
def stop():
    global clicking
    clicking = False
    status_label.config(text="Status: Stopped", foreground="red")

# Função para alternar o estado do autoclicker usando uma tecla
def toggle_clicking():
    if clicking:
        stop()
    else:
        start()

# Iniciar um thread para monitorar a tecla de atalho
def start_keyboard_listener():
    keyboard.add_hotkey('F8', toggle_clicking)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Autoclicker com Tkinter")

# Frame principal
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill='x', expand=True)

# Campo para inserir o delay entre cliques
delay_label = ttk.Label(main_frame, text="Delay entre cliques (segundos):")
delay_label.pack(anchor='w')

delay_entry = ttk.Entry(main_frame)
delay_entry.insert(0, "0.1")  # Valor padrão
delay_entry.pack(fill='x', padx=5, pady=5)

# Opções para o número de cliques por execução
click_choice = tk.StringVar(value="1")  # Valor padrão

click_label = ttk.Label(main_frame, text="Número de cliques por execução:")
click_label.pack(anchor='w')

click_option_1 = ttk.Radiobutton(main_frame, text="1 Clique", variable=click_choice, value="1")
click_option_1.pack(anchor='w')

click_option_2 = ttk.Radiobutton(main_frame, text="2 Cliques", variable=click_choice, value="2")
click_option_2.pack(anchor='w')

# Opções para escolher o botão do mouse
button_choice = tk.StringVar(value="left")  # Valor padrão

button_label = ttk.Label(main_frame, text="Escolha o botão do mouse:")
button_label.pack(anchor='w')

left_button = ttk.Radiobutton(main_frame, text="Botão Esquerdo", variable=button_choice, value="left")
left_button.pack(anchor='w')

right_button = ttk.Radiobutton(main_frame, text="Botão Direito", variable=button_choice, value="right")
right_button.pack(anchor='w')

# Botões de controle
control_frame = ttk.Frame(main_frame)
control_frame.pack(fill='x', pady=10)

start_button = ttk.Button(control_frame, text="Start", command=start)
start_button.pack(side='left', expand=True, fill='x', padx=5)

stop_button = ttk.Button(control_frame, text="Stop", command=stop)
stop_button.pack(side='left', expand=True, fill='x', padx=5)

# Label para exibir o status do autoclicker
status_label = ttk.Label(main_frame, text="Status: Stopped", foreground="red")
status_label.pack(fill='x', pady=10)

# Iniciar o thread do listener de teclado
keyboard_listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
keyboard_listener_thread.start()

# Iniciar o loop principal do Tkinter
root.mainloop()
