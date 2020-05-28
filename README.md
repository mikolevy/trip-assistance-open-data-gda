## Jak zacząć?

1. Zainstaluj zależności:
 - Jeśli używasz PyCharma możesz po prostu otworzyć projekt i kliknąć na "Install requirements from Pipfile.lock" 
 na wiadomości, która pokaże się po otwarciu dowolnego pliku
 - Inną opcją jest odpalenie z konsoli `pipenv install` w katalogu projektu
 
2. Pobierz dane o przystankach i rozkładach jazdy z Otwartego Gdańska:
 - URL do pliku z przystankami znajdziesz wchodząc na 'Lista Przystanków' na stronie https://ckan.multimediagdansk.pl/dataset/tristar
 - Rozkłady możesz pobrać ręcznie linia po linii ze strony Otwartego Gdańska albo użyć pomocnicznego skryptu `download_schedules_helper.py` 
  W tym celu pobierz plik z informacjami o linkach do rozkładów jazdy (URL do niego znajdziesz na podstronie "Rozkład Jazdy" Otwartego Gdańska).
  Nazwij plik `stoptimes.json` i umieść go w głównym katalogu projektu a następnie uruchom skrypt `download_schedules_helper.py`

3. Utwórz strukturę katalogów jak w `data_loaders.py`:
 - `bus_data/bus_stops.json` 
 - `bus_data/schedules/<DATA>/<NUMER-LINII>.json` -> jeżeli korzystasz ze skrytpu pomocniczego do pobrania rozkładów to wystarczy skopiować pliki z rozkładami w odpowiednie miejsce   

4. Uruchom `trip_assistance.py`

## How to start?

1. Install dependencies:
 - If you are using PyCharm you can just open the project, open file and click "Install requirements from Pipfile.lock" on the prompt message
 - Other option is to use terminal: run `pipenv install` in project directory
 
2. Pull bus stops and schedules data from Open Gdańsk:
 - Bus stops url you can find going to 'Lista Przystanków' on https://ckan.multimediagdansk.pl/dataset/tristar
 - To pull schedules you can get them manually bus line by bus line from Open Gdańsk or use `download_schedules_helper.py` script.
 First download file with info about links to schedules (URL to this file you will find on page "Rozkład Jazdy" on Open Gdańsk).
 Call file `stoptimes.json` and put it in project's root directory. Run script `download_schedules_helper.py`
 
3. Create directory structures as in `data_loaders.py`:
 - `bus_data/bus_stops.json` 
 - `bus_data/schedules/<DATA>/<LINE-NUMBER>.json` -> if you are using helper script to download schedules you will need only copy pate downloaded files   
   
4. Run `trip_assistance.py` script

