## HUBERT NIEWIEROWICZ
## GRA SHANNON SWITCHING


## Cel projektu:

Celem projektu było stworzenie programu umożliwiającego rozgrywanie partii w grę „Shannon switching” w wariancie Gale między człowiekiem a graczem komputerowym o dwóch rodzajach. Pierwszym z nich miał być gracz losowo wybierający legalny ruch, a drugi – wybierający najlepszy ruch na podstawie kilku głównych kryteriów. Celem było także zaimplementowanie samej gry i interfejsu użytkownika w okienku.


## Opis projektu:

Program realizuje wystawione cele, czyli przede wszystkim umożliwia rozgrywanie gry „Shannon switching” w okienku. Oprócz tego, program jest wyposażony w prosty lecz użyteczny interfejs użytkownika, ciekawą grafikę, okienko z instrukcją, a także zabezpiecza się przed błędnymi ruchami użytkownika w grze.

Możliwe są 3 rodzaje rozgrywania gry:
* Multiplayer – gra w dwie osoby, gracze grają przeciwko siebie wykonując ruchy jeden po drugim.
* Single player EASY – gra dla jednej osoby z graczem komuperowym, wybierającym w każdej turze losowy legalny ruch.
* Single player HARD – gra dla jednej osoby z graczem komuperowym, wybierającym w każdej turze najlepszy ruch na podstawie kilku głównych kryteriów.

Niektóre z ustawień można łatwo zmienić według podanej później instrukcji. Nie zważając na to, jakie kolory tak naprawdę są wyświetlane na ekranie, w kodzie jeden gracz nosi nazwę „red”, a drugi – „blue”. Chodzi tu tylko o odróżnienie dwóch graczy.


## Opis klas:

* Button() – klasa umożliwiająca implementację przycisku. Metoda draw() służy do narysowania przycisku i sprawdzenia, czy został on wciśnięty. Jest ona wywoływana w każdej iteracji podstawowej pętli gry. Przycisk podczas wciśnięcia zmienia kolor, lecz przede wszystkim aktywuje lub łączy linie według wejść użytkownika.
* UI_Button(Button) – klasa przycisku do interfejsu użytkownika. Metoda draw_ui() ma funkcjonalność podobną do wcześniej opisanej metody draw(), lecz różni się tym, że słuzy do określenia rodzaju gry, a także do tego, aby określić, kiedy użytkownik chce zobaczyć instrukcję gry.
* Player() – klasa określająca obu graczy. Przechowuje przyciski i graf linii należący do każdego z graczy. Posiada metodę append_graph(), która po każdym ruchu dodaje do grafu nowo dodaną linię.
* Game() – klasa przechowująca parametry gry, takie jak: kolejka, instrukcje do rozpoczęcia lub zakończenia gry czy też dane o tym, jaki przycisk został aktywowany, a jaki połączony.


## Instrukcja uruchomienia:

```
git clone https://gitlab-stud.elka.pw.edu.pl/hniewier/pipr-projekt-shannon-connect
cd pipr-projekt-shannon-connect
pip install pygame
python game.py
```

Do konfiguracji udostępnionych jest kilka parametrów gry: ilość klatek na sekundę i zbiór kolorów używanych w grze. Program używa dwóch zbiorów kolorów, w których znajdują się po dwa kolory: podstawowy i dopełniający. W przypadku chęci zmiany kolorów zalecane jest, aby pierwszy zbiór miał odcienie białego/szarego, a zbiór drugi – odcienie czerwonego/bordowego (najlepiej będzie to pasowało do ogólnego wyglądu gry). Aby dokonać konfiguracji danych parametrów należy podczas uruchomienia podać odpowiednie flagi.

Zmiana ilości klatek na sekundę:
```
--fps {nowa ilość klatek na sekundę}
```

Zmiana koloru podstawowego pierwszego zbioru:
```
--color1p {nowy kolor}
```

Zmiana koloru podstawowego drugiego zbioru:
```
--color2p {nowy kolor}
```

Zmiana koloru dopełniającego pierwszego zbioru:
```
--color1s {nowy kolor}
```

Zmiana koloru dopełniającego drugiego zbioru:
```
--color2s {nowy kolor}
```

Przykład uruchomienia gry ze zmienionymi parametrami:
```
python game.py –fps 50 –color1p ivory
```


## Część refleksyjna:

Cały projekt był dla mnie bardzo ciekawym i kształcącym wyzwaniem. Od razu postawiłem sobie cel, że produktem końcowym ma być gra z pełnym interfejsem i ciekawą grafiką w okienku. Mimo tego, że najpierw przypadkiem zacząłem implementować niezgodną z poleceniem wersję gry, pomogło mi to w głębszym zrozumieniu działania tego typu programu. Mogę przyznać, że jestem szczęśliwy z efektu końcowego, z tego, ile pracy włożyłem w projekt, a w końcu i z ilości nowej wiedzy, jaką zdobyłem tworząc samemu od zera całą grę. Przy większym projekcie raczej zawsze da się coś zrobić inaczej i lepiej, lecz po naprawdę wielu zmianach struktury kodu jestem z niego teraz zadowolony. W końcu chciałbym usłyszeć od prowadzącego uwagi dotyczące kodu, gdyż czuję także, że mógłbym niektóre aspekty programu poprawić.

## Diagram architektury projektu znajduje się w katalogu „docs” pod nazwą „diagram.pdf”.
