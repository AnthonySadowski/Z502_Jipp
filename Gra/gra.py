# ====== KONFIGURACJA ======
ADRES_API = "TWOJ_ADRES_API"   
KANAL = 67                     
LICZBA_RUND = 5                

radio.set_group(KANAL)

# ====== POMOCNICZE ======
def czekaj_na_puszczenie():
    # czekamy, az gracz pusci przycisk (zeby klikniecie nie liczilo sie podwojnie)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(20)

def graj_runde():
    # Losowe oczekiwanie, potem CEL - trzeba szybko nacisnac A lub B
    basic.show_icon(IconNames.ASLEEP)
    basic.pause(Math.random_range(1500, 4000))
    basic.show_icon(IconNames.TARGET)
    start = input.running_time()
    while True:
        if input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            czas = input.running_time() - start
            punkty = 500 - czas // 2       # max 500 pkt za runde
            if punkty < 1:
                punkty = 1
            basic.show_icon(IconNames.HAPPY)
            czekaj_na_puszczenie()
            return punkty
        if input.running_time() - start > 1500:
            basic.show_icon(IconNames.SAD)  # za wolno - 0 punktow
            czekaj_na_puszczenie()
            return 0

# ====== GRA (start przyciskiem A) ======
def on_button_a():
    id_gry = Math.random_range(1, 1000)    # losowe ID od 1 do 1000
    wynik = 0
    basic.show_string("START!")
    for i in range(LICZBA_RUND):
        basic.clear_screen()
        basic.pause(800)
        wynik = wynik + graj_runde()
        basic.show_number(wynik)           # wynik czesciowy
    # ---- KONIEC GRY: WYSYLKA NA KANAL 67 ----
    basic.show_string("Koniec")
    wiadomosc = ("id:" + convert_to_text(id_gry) +
                 ";wynik:" + convert_to_text(wynik) +
                 ";adresAPI:" + ADRES_API)
    radio.send_string(wiadomosc)
    basic.show_icon(IconNames.YES)
    basic.pause(1000)
    basic.show_string("Wyslano")
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_a)
