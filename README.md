Opis projektu
1. Gra i komunikacja między micro:bitami

Gra na refleks dla dwóch micro:bitów. Co rundę na ekranie pierwszego micro:bita pojawia się cel — gracz jak najszybciej wciska przycisk A lub B; im szybsza reakcja, tym więcej punktów. Po 5 rundach wynik jest wysyłany przez radio (kanał 67) do drugiego micro:bita.
2. Przepływ danych

Drugi micro:bit odbiera wynik radiem i przekazuje go przez USB do bramki na komputerze — skrypt-python, który wysyła dane żądaniem HTTP POST do API. API zapisuje wynik w bazie Supabase. Wyniki prezentuje aplikacja WWW we Flasku na VPS, pobierająca dane z tej samej bazy.
3. Stack (Linux VPS)

    OS: Ubuntu Server LTS, dostęp przez SSH, firewall ufw,
    Aplikacja: Python 3 + Flask, serwer Gunicorn (WSGI),
    Proxy: Nginx (reverse proxy, HTTPS przez Certbot/Let's Encrypt),
    Baza: PostgreSQL w Supabase (dostęp przez supabase-py),
    Utrzymanie: usługa systemd z auto-startem, opcjonalnie Docker.
