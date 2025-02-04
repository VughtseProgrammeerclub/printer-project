# Belangrijk: Zorg ervoor dat de pinnen 2 t/m 9 laag (off) worden gemaakt als ze niet worden gebruikt
#             Dit om inbranden van het papier te voorkomen.
#             Dit s extra belangrijk omdat de GPIO-pinnen van de Raspberry Pico standaard hoog lijken 
#             te zijn. Dit in tegenstelling tot de Arduino waar de pinnen laag zijn.

# De schakelaar op de print staat in de stand 11. Dit betekent dat de motor start als er een puls wordt gegeven op GPIO 11,
# Als de motor draait krijgt deze de voeding via het verbreekcontact van het printerloopwerk. De motor stopt dus automatisch.
import machine
import time
import random

led = machine.Pin("LED", machine.Pin.OUT)
led.on()
# Configureer GPIO-pinnen 2 t/m 9 als output en zet ze laag
# Let op! De volgorde van de pinnen is omgedraaid omdat de tekst op de print verkeerd-om staat
pin_2 = machine.Pin(9, machine.Pin.OUT)
pin_3 = machine.Pin(8, machine.Pin.OUT)
pin_4 = machine.Pin(7, machine.Pin.OUT)
pin_5 = machine.Pin(6, machine.Pin.OUT)
pin_6 = machine.Pin(5, machine.Pin.OUT)
pin_7 = machine.Pin(4, machine.Pin.OUT)
pin_8 = machine.Pin(3, machine.Pin.OUT)
pin_9 = machine.Pin(2, machine.Pin.OUT)

for pin in [pin_2, pin_3, pin_4, pin_5, pin_6, pin_7, pin_8, pin_9]:
    pin.off()

# Configureer de motor op GPIO 11
motor_pin = machine.Pin(11, machine.Pin.OUT)
motor_pin.off()  # Zorg ervoor dat de motor bij aanvang uit staat

# Configureer de startknop op GPIO 13
button_rood = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configureer de startknop op GPIO 15
button_blauw = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configureer de paperfeed-knop op GPIO 14
button_wit = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Timing- en statusvariabelen
start_signal_duration = 100  # Duur van het startsignaal in milliseconden
timing_high = 0.004          # Tijd dat een pin hoog blijft in seconden
button_debounce_time = 0.2   # Minimale tijd tussen knopactiveringen in seconden
last_button_press = 0        # Tijdstip van de laatste knopdruk

# Definieer letterpatronen als functies die rijen retourneren
def letter_A():
    return [
        ".XXX..",
        "X...X.",
        "X...X.",
        "XXXXX.",
        "X...X.",
        "X...X.",
        "X...X.",
        "......",
    ]

def letter_B():
    return [
        "XXXX..",
        "X...X.",
        "X...X.",
        "XXXX..",
        "X...X.",
        "X...X.",
        "XXXX..",
        "......",
    ]

def letter_C():
    return [
        ".XXX..",
        "X...X.",
        "X.....",
        "X.....",
        "X.....",
        "X...X.",
        ".XXX..",
        "......",
    ]

def letter_D():
    return [
        "XXXXX.",
        "X....X",
        "X....X",
        "X....X",
        "X....X",
        "X....X",
        "XXXXX.",
        "......",
    ]

def letter_E():
    return [
        "XXXXX.",
        "X.....",
        "X.....",
        "XXXXX.",
        "X.....",
        "X.....",
        "XXXXX.",
        "......",
    ]

def letter_G():
    return [
        ".XXX..",
        "X...X.",
        "X.....",
        "X.XXX.",
        "X...X.",
        "X...X.",
        "XXXX..",
        "......",
    ]

def letter_H():
    return [
        "X...X.",
        "X...X.",
        "X...X.",
        "XXXXX.",
        "X...X.",
        "X...X.",
        "X...X.",
        "......",
    ]

def letter_I():
    return [
        "XXXXX.",
        "..X...",
        "..X...",
        "..X...",
        "..X...",
        "..X...",
        "XXXXX.",
        "......",
    ]

def letter_J():
    return [
        ".XXXX.",
        "....X.",
        "....X.",
        "....X.",
        "....X.",
        "X...X.",
        ".XXX..",
        "......",
    ]

def letter_K():
    return [
        "X...X.",
        "X..X..",
        "X.X...",
        "XX....",
        "X.X...",
        "X..X..",
        "X...X.",
        "......",
    ]

def letter_L():
    return [
        "X.....",
        "X.....",
        "X.....",
        "X.....",
        "X.....",
        "X.....",
        "XXXXX.",
        "......",
    ]

def letter_M():
    return [
        "X...X.",
        "XX.XX.",
        "X.X.X.",
        "X...X.",
        "X...X.",
        "X...X.",
        "X...X.",
        "......",
    ]

def letter_N():
    return [
        "X...X.",
        "X...X.",
        "XX..X.",
        "X.X.X.",
        "X..XX.",
        "X...X.",
        "X...X.",
        "......",
    ]
def letter_O():
    return [
        ".XXX..",
        "X...X.",
        "X...X.",
        "X...X.",
        "X...X.",
        "X...X.",
        ".XXX..",
        "......",
    ]

def letter_P():
    return [
        "XXXX..",
        "X...X.",
        "X...X.",
        "XXXX..",
        "X.....",
        "X.....",
        "X.....",
        "......",
    ]

def letter_R():
    return [
        "XXXX..",
        "X...X.",
        "X...X.",
        "XXXX..",
        "X...X.",
        "X...X.",
        "X...X.",
        "......",
    ]

def letter_S():
    return [
        ".XXX..",
        "X...X..",
        "X.....",
        ".XXX..",
        "....X.",
        "X...X.",
        ".XXX..",
        "......",
    ]
def letter_T():
    return [
        "XXXXX.",
        "..X...",
        "..X...",
        "..X...",
        "..X...",
        "..X...",
        "..X...",
        "......",
    ]

def letter_U():
    return [
        "X...X.",
        "X...X.",
        "X...X.",
        "X...x.",
        "X...X.",
        "X...X.",
        ".XXX..",
        "......",
    ]

def letter_V():
    return [
        "X...X.",
        "X...X.",
        "X...X.",
        "X...X.",
        "X...X.",
        ".X.X..",
        "..X...",
        "......",
    ]

def letter_W():
    return [
        "X...X.",
        "X...X.",
        "X...X.",
        "X.X.X.",
        "X.X.X.",
        "X.X.X.",
        "XX.XX.",
        "......",
    ]

def letter_Z():
    return [
        "XXXXX.",
        "....X.",
        "...X..",
        "..X...",
        ".X....",
        "X.....",
        "XXXXX.",
        "......",
    ]

def space():
    return [
        "......",
        "......",
        "......",
        "......",
        "......",
        "......",
        "......",
        "......",
    ]
def uit():
    return [
        "...X..",
        "...X..",
        "...X..",
        "...X..",
        "...X..",
        "......",
        "...X..",
        "......",
    ]

def SPEL(knop):
    if knop == computer_keuze:
        print_text("HET IS GELIJKSPEL!")
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
    if knop == 'STEEN':
        if computer_keuze == 'PAPIER':
            print_text("JIJ VERLIEST, HELAAS!")
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()
        elif computer_keuze == 'SCHAAR':
            print_text("JIJ WINT!")
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()
    if knop == 'PAPIER':
        if computer_keuze == 'SCHAAR':
            print_text('JE VERLIEST, HELAAS!')
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()
        elif computer_keuze == 'STEEN':
            print_text('JIJ HEBT GEWONNEN!')
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()
    if knop == 'SCHAAR':
        if computer_keuze == 'STEEN':
            print_text('JIJ VERLIEST, HELAAS!')
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()
        elif computer_keuze == 'PAPIER':
            print_text('JE HEBT GEWONNEN!')
            time.sleep(1.5)
            motor_pin.on()
            time.sleep(0.05)
            motor_pin.off()

def print_letter(letter_function):
    pattern = letter_function()

    for col_index in range(len(pattern[0])):  # Itereer over kolommen
        # Zet alle pinnen uit
        for pin in [pin_2, pin_3, pin_4, pin_5, pin_6, pin_7, pin_8, pin_9]:
            pin.off()

        # Zet alleen de relevante pinnen aan
        if pattern[0][col_index] == 'X':
            pin_2.on()
        if pattern[1][col_index] == 'X':
            pin_3.on()
        if pattern[2][col_index] == 'X':
            pin_4.on()
        if pattern[3][col_index] == 'X':
            pin_5.on()
        if pattern[4][col_index] == 'X':
            pin_6.on()
        if pattern[5][col_index] == 'X':
            pin_7.on()
        if pattern[6][col_index] == 'X':
            pin_8.on()
        if pattern[7][col_index] == 'X':
            pin_9.on()

        time.sleep(timing_high * 2)  # 4 ms per kolom
        for pin in [pin_2, pin_3, pin_4, pin_5, pin_6, pin_7, pin_8, pin_9]:
            pin.off()

def print_text(text):
    letter_map = {
        'A': letter_A,
        'B': letter_B,
        'C': letter_C,
        'D': letter_D,
        'E': letter_E,
        'G': letter_G,
        'H': letter_H,
        'I': letter_I,
        'J': letter_J,
        'K': letter_K,
        'L': letter_L,
        'M': letter_M,
        'N': letter_N,
        'O': letter_O,
        'P': letter_P,
        'R': letter_R,
        'S': letter_S,
        'T': letter_T,
        'U': letter_U,
        'V': letter_V,
        'W': letter_W,
        'Z': letter_Z,
        ' ': space,
        '!': uit,
    }
    for char in text:
        if char in letter_map:
            print_letter(letter_map[char])
            time.sleep(timing_high * 2)  # Ruimte tussen letters

while True:
    current_time = time.time()
    mogelijkheden = ['STEEN', 'PAPIER', 'SCHAAR']
    computer_keuze = random.choice(mogelijkheden)
    # Controleer of de startknop is ingedrukt
    if button_rood.value() == 1 and current_time - last_button_press > button_debounce_time:
        last_button_press = current_time  # Update de tijd van de laatste knopdruk
        keuze = "STEEN"
        # Start het motorsignaal
        motor_pin.on()
        #print("Startpuls rood begin")
        time.sleep(0.05)
        motor_pin.off()
        #print("Startpuls rood eind")
        print_text("JOUW KEUZE IS STEEN")
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        TEKST = "PRINTER IS " + computer_keuze
        print_text(TEKST)
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        SPEL(keuze)


    if button_blauw.value() == 1 and current_time - last_button_press > button_debounce_time:
        last_button_press = current_time  # Update de tijd van de laatste knopdruk
        keuze = "SCHAAR"
        # Start het motorsignaal
        motor_pin.on()
        #print("Startpuls blauw begin")
        time.sleep(0.05)
        motor_pin.off()
        #print("Startpuls blauw eind")
        print_text("JOUW KEUZE IS SCHAAR")
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        TEKST = "PRINTER IS " + computer_keuze
        print_text(TEKST)
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        SPEL(keuze)

        # Print de tekst 'SCHAAR'
        #print_text("SCHAAR")
        
    if button_wit.value() == 1 and current_time - last_button_press > button_debounce_time:
        last_button_press = current_time  # Update de tijd van de laatste knopdruk
        keuze = "PAPIER"
        # Start het motorsignaal
        motor_pin.on()
        #print("Startpuls wit begin")
        time.sleep(0.05)
        motor_pin.off()
        #print("Startpuls wit eind")
        print_text("JOUW KEUZE IS PAPIER")
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        TEKST = "PRINTER IS " + computer_keuze
        print_text(TEKST)
        time.sleep(1.5)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        time.sleep(2)
        motor_pin.on()
        time.sleep(0.05)
        motor_pin.off()
        SPEL(keuze)

        # Print de tekst 'PAPIER'
        #print_text("PAPIER")
        
    # Controleer of de paperfeed-knop is ingedrukt
    #if paperfeed_button.value() == 1:
    #    motor_pin.on()
        #print("Paperfeed actief")
    else:
        motor_pin.off()
