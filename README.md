# Broker 360 – Biuro Nieruchomości

Profesjonalna strona internetowa biura nieruchomości Broker 360, przygotowana w technologii Django.

Projekt umożliwia prezentowanie ofert nieruchomości, zarządzanie nimi za pomocą panelu administracyjnego oraz odbieranie wiadomości przesyłanych przez formularz kontaktowy.

## Najważniejsze funkcje

- strona główna biura nieruchomości,
- prezentacja aktualnych ofert,
- osobna strona szczegółowa każdej nieruchomości,
- czytelne adresy ofert tworzone na podstawie ich nazw,
- galeria zdjęć nieruchomości,
- możliwość ustawienia zdjęcia głównego,
- panel administratora do zarządzania ofertami,
- statusy ofert: aktywna, rezerwacja, sprzedana i wynajęta,
- formularz kontaktowy,
- zapis wiadomości w bazie danych,
- wymóg podania adresu e-mail lub numeru telefonu,
- potwierdzenie zapoznania się z polityką prywatności,
- strona polityki prywatności,
- responsywny wygląd dostosowany do komputerów i telefonów.

## Technologie

- Python 3.11
- Django 5.2
- SQLite
- HTML5
- CSS3
- Pillow
- Git
- GitHub

## Struktura projektu

Projekt składa się z dwóch głównych aplikacji Django:

### `properties`

Aplikacja odpowiada za:

- oferty nieruchomości,
- zdjęcia ofert,
- stronę główną,
- szczegóły poszczególnych ofert,
- panel zarządzania nieruchomościami.

### `contact`

Aplikacja odpowiada za:

- formularz kontaktowy,
- zapisywanie wiadomości,
- stronę podziękowania,
- politykę prywatności.

## Uruchomienie projektu lokalnie

### 1. Pobierz repozytorium

```bash
git clone https://github.com/Wierzchowiecki/broker360.git
cd broker360