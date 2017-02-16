# Tydzień pierwszy - praca domowa

## Dokończ kalkulator

W pliku index.html znajduje się zaczęty lecz nieskończony kalkulator.

Zadanie polega na:

* Sciągnieciu pliku index.html lokalnie na swój komputer
* Uruchomieniu serwera plików staycznych przy pomocy komendy `python3.6 -m http.server 8000` lub `python -m http.server 8000` (oczywiście po wcześniejszym zainstalowaniu pythona) i pracy nad plikiem index.html korzystając z adresu `http://127.0.0.1:8000` lub `http://localhost:8000` lub `http://0.0.0.0:8000` (przynajmniej jeden powinien działać)
* Dokończ kalkulator w taki sposób aby po kliknięciu w dane działanie pod nagłówkiem **wynik** pojawił się prawidłowy wynik działania na które wskazuje dany button

## Markdown converter
HTML nie jest najwygodniejszym sposobem na formatowanie plików tekstowych. Wśród wielu ludzi popularne są tak zwane silniki formatowania tekstu które w łatwy sposób można później zamienić (skonwertować) na dokument HTML. Dość popularnym silnikiem jest silnik [Markdown](https://en.wikipedia.org/wiki/Markdown). Zadanie polega na skorzystaniu z biblioteki [Showdown](https://github.com/showdownjs/showdown) (podobnie jak korzysta się z jQuery) oraz tagu `textarea` aby zamienić tekst w formacie markdown na HTML i wstawieniu tak wygenerowanego html z powrotem do dokumentu. Można skorzystać z pliku `index.html` jako szablonu.

## Instalacja i uruchomienie django
* Zainstalować wersję nr 3.5.3 [Python](https://www.python.org/downloads/)
* Korzystając z programu `pip` który pownien być dołączony do pakietu Python zainstalować [Django](https://www.djangoproject.com/)
* Zweryfikować że django zostało poprawnie zainstalowane poprzez odpalenie uruchomienie serwera i sprawdzenie go w lokalnej przeglądarce [Zacznij tu](https://docs.djangoproject.com/en/1.10/intro/install/)

## Instalacja GIT

### Windows
Pobrać i zainstalować [sourcetree](https://www.sourcetreeapp.com/)
### Ubuntu linux
Zainstalować git z konsoli przy pomocy poleceń
```
$ sudo apt update
$ sudo apt install git
```
