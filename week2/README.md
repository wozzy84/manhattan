# Tydzień Drugi - Plan na sesję

W drugim tygodniu podzielmy sesję na 3 bloki:

## Blok pierwszy - podstawy Narzędzia Kontroli Wersji
Celem będzie zapoznanie się z podstawowymi funkcjami narzędzia kontroli wersji GIT, założenie sobie konta na Github oraz upewnienie się, że wszyscy wiedzą jak `wypychać` swoje zmiany na Github.

Plan wygląda następująco:
* [x] Wstęp i omówienie
* [x] Inicializowanie lokalnego repozytorium
* [x] Śledzenie zmian w repozytorium
* [x] Dodawanie zmian do repozytorium
* [x] Commitowanie zmian w repozytorium
* [x] Konfiguracja zdalnego repozytorium
* [x] Pchanie zmian do zdalnego repozytorium

## Blok drugi - Javascript
Kontynuacja a raczej troszeczkę porządniejszy wstęp do tego jakże cudownego języka skryptowego

* [x] Omówienie jakim językiem jest javascript
* [x] Przegląd gramatyki języka javascript
* [x] Typy danych w Javascript
* [x] Instrukcje
* [x] Wyrażenia
* [x] Lista słów zarezerwowanych
* [ ] Literały
* [ ] Funkcje

## Blok trzeci - Style
W tym bloku skupimy się na upiększeniu naszego kalkulatora oraz postaramy się dodać do niego kilka użytecznych funkcji

* [ ] Dodawanie plików CSS do plików HTML
* [ ] Definiowanie styli osadzonych bezpośrednio w pliku HTML
* [ ] Importowanie zewnętrznych bibliotek styli do pliku HTML
* [ ] Dodawanie plików javascript do plików HTML
* [ ] Kilka użytecznych funkcji (może sami zdecydujemy co dodamy i przegadamy jak to zrobić)

# Praca domowa

## GIT i Github
* Sklonować moje reposytorium
* Ogarnąć przełączanie branch-y w git
* Zmienić branch na `css` i otworzyć index.html (otworzyć w przeglądarce za pomocą serwera)
* Przejrzeć nagłówek pod kątem tego w jaki sposób dołącza się style do plików CSS
* Zwróć uwagę, że korzystam z tzw frameworka CSS [foundation](http://foundation.zurb.com/) - przejrzyj dokumentację. Wiele nazw klas z których korzystam w dokumencie HTML zostało zdefiniowanych w tymże frameworku.
* Zwróć uwagę na to, że skrypt javascript jest ładowany z pliku [/js/app.js](https://github.com/RadekMolenda/manhattan/blob/css/week2/js/app.js) a nie osadzony w bezpośrednio w dokumencie html. Ten plik będziecie musieli decydować później.
* Zwróć uwagę na to, że style zdefiniowane przeze mnie zostały dołączone do dokumentu w postaci pliku [/css/app.css](https://github.com/RadekMolenda/manhattan/blob/css/week2/css/app.css). Jak myślisz za co odpowiadają tamte zdefiniowane style?

## Kalkulator
Przejrzyj plik `/js/app.js`. Zwróć uwagę na to jak została wykorzystana funkcja [eval](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval). Zwróć również uwagę na to, że nie należy nadużywać funkcji `eval`, praktycznie nie należy wcale z niej korzystać bo to [samo zło](http://stackoverflow.com/questions/197769/when-is-javascripts-eval-not-evil). Jednak jej użycie znacznie upraszcza program - słowem na początek może być.

Zauważ również, że jeden np. `$(".numbers button")` pozwala na wybranie wszystkich buttonów z pudełka o nazwie klasy "numbers". Oraz zdefiniowanie akcji na każdym z osobna z tych buttonów. `$(this)` w tym przypadku odwołuje się do buttonu w który kliknęliśmy.

* Zadanie pierwsze polega na dodaniu obsługi funkcji `x^y` - x do potęgi y, która nie działa
* Zadanie drugie polega na dodaniu obsługi funkcji `%` - reszta z dzielenia, która nie działa
* Zadanie trzecie polega na dodaniu obsługi wpisywania liczb z poziomu klawiatury przy pomocy javascript w taki sposób żeby nie trzeba było klikać w input żeby móc dodać kolejne cyfry do liczby. Zresztą `normalne` wpisywanie do tego pola input i tak nie działa
* Zadanie czwarte polega na dodaniu obsługi `+,-,*,%,/` z poziomu klawiatury w taki sposób żeby wykonwyana była taka sama akcja co przez kliknięcie w odpowiedni button
* Zadanie piąte polega na wypchnięciu zmian do swojego repo i zawiadomienie mnie o tym przez podesłanie linka
