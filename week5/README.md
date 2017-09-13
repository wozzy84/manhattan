# Tydzień Piąty - Plan na sesję

## Blok pierwszy - Javascript
Kontynuacja nauki Javascript - sterowanie przepływem programu

### Pętle


* [x] wyjaśnienie oraz zastosowanie pętli `while`
* [x] objaśnienie oraz zastosowania pętli `do`
* [x] objaśnienie oraz zastosowanie pętli `for`
* [x] wcześniejsze zakańczanie wykonywania pętli przy użyciu słowa kluczowego `break`

### Sterowanie warunkowe

* [x] objaśnienie i wykorzystanie konstrukcji `switch`

### Funkcje

* [x] definiowanie funkcji
* [x] parametry oraz zakres funkcji (czyli zmienne globalne vs zmienne lokalne)
* [x] zagnieżdżanie zakresów funkcji (czyli o możliwości dostępu do zmiennych w funkcjach zagnieżdżonych)
* [x] funkcje jako wartości (czyli o możliwości przekazaniu funkcji jako parametr do innych funkcji)

## Praca domowa

1. `triangle` - napisz funkcję która wyświetli w konsoli trójkąt o określonej wysokości podanej jako parametr

np. wywołanie funkcji `triangle(4)` wyświetli w konsoli taki trójkąt
```
#
##
###
####
```
2. `reversedTriangle` - napisz funkcję działającą analogicznie do funkcji `triangle` z tą różnicą, że wyświetlony w konsoli zostanie odwrócony trójkąt

np. `reversedTriangle(3)` zwróci:
```
###
##
#
```

3. `centeredTriangle`

`centeredTriangle(4)` wyświetli w konsoli:
```
   #
  ###
 #####
#######
```

4. `reverseNumber` - napisz funkcję która zwróci liczbę napisaną w odwrotnej kolejności np: `reverseNumber(332244)` zwróci `442233`

5. `fizzBuzz` - napisz funkcję która przyjmuję liczbę `n` jako parametr i wyświetla w konsoli wszystkie liczby w kolejności od 1 do `n` jednakże z pewnymi wyjątkami:
- jeżeli liczba która ma być wyświetlona jest podzielna przez 3 - wtedy zamiast tej liczby ma się wyświetlić `Fizz`
- jeżeli liczba jest podzielna przez 5 - wtedy zamiast liczby wyświetlamy `Buzz`
- jeżeli liczba jest jednocześnie podzielna przez 3 oraz pięć wtedy wyświetlamy `FizzBuzz`

np. `fizzBuzz(16)` wyświetli w konsoli:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

6. `gcd` - Napisz funkcję która znajduje największy wspólny dzielnik dwóch liczb np: `gcd(6, 15)` zwróci `3`
