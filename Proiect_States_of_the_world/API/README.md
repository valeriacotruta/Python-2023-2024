# STATES-OF-THE-WORLD
## API

### DESCRIERE
        API-ul furnizeaza un set de reguli prin care acesta expune diverse functionalitati, date sau operatiuni pe care aplicatia Client le poate primi.
    Functionalitatile oferite sunt:
    - un crawler pentru a colecta informatii despre tarile lumii de pe Wikipedia;
    - inserarea sau preluarea informatiilor in/din baza de date utilizata dupa extragerea informatiilor de catre crawler;
    - expunerea mai multor rute accesibile aplicatiei Client prin metoda HTTP GET sau POST pentru operarea cu datele extrase de catre crawler. 
        Pentru implementarea crawler-ului, am utilizat biblioteca BeautifulSoup.
    **BeautifulSoup** facilitează extragerea informațiilor din paginile web, construind un arbore de analiză pentru paginile date cu ajutorul tag-urilor HTML. 
        Pentru crearea API-ului, am utilizat **Flask** - un framework ce faciliteaza dezvoltarea aplicatiilor web in cadrul limbajului Python. 
    Acesta permite definirea rutelor si asocierea lor cu diferite functionalitati sau metode pentru gestionarea cererilor de la aplicatia Client intr-un mod minimalist.
        Clientul acceseaza informatia din baza de date, prin intermediul API-ului, folosind biblioteca Requests.
    **Requests** permite trimiterea cererilor HTTP/1.1 intr-un mod elegant si extrem de simplu. 

### RUTE
    **METODE GET**
    - http://127.0.0.1:8080/top-10-tari-populatie
    - http://127.0.0.1:8080/top-10-tari-densitate
    - http://127.0.0.1:8080/top-10-tari-suprafata
    - http://127.0.0.1:8080/toate-tarile?fus-orar={time_zone} (time_zone - un fus orar, precum _UTC−08:00_, _UTC+09:00_ sau _UTC±00:00_)
    - http://127.0.0.1:8080/toate-tarile?vecin={neighbour} (neighbour - o tara vecina)
    - http://127.0.0.1:8080/toate-tarile?limba={language} (language - o limba)
    - http://127.0.0.1:8080/toate-tarile?regim-politic={political_regime} (political_regime - un regim politic)
    **METODA POST**
    - http://127.0.0.1:8080/insert-all-data 

### BAZA DE DATE
    Am utilizat MySQL, deoarece :
    - este un sistem de gestionare a bazelor de date relationale;
    - este gratis si open-source;
    - este fiabil pentru aplicatii mari, cat si pentru aplicatii mici. 
    
#### Informatii despre baza de date:
    host='localhost',
    database='states_of_the_world',
    user='root',
    password='valeriacotruta'
    
    Pentru crearea tabelelor din baza de date, consultati fisierul _Proiect_States_of_the_world/API/scripts/models/tables_created.sql_.
        
### PAGINILE WEB UTILIZATE PENTRU COLECTAREA INFORMATIILOR DESPRE TARILE LUMII
     - https://en.wikipedia.org/wiki/List_of_national_capitals_by_population : extragerea statelor si capitalele aferente lor
     - https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population : extragerea numarului populatiei
     - https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density : extragerea densitatii populatiei
     - https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area : extragerea suprafetei statelor
     - https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_number_of_land_borders : extragerea vecinatatii
     - https://en.wikipedia.org/wiki/List_of_official_languages_by_country_and_territory : extragerea limbilor oficiale
     - https://en.wikipedia.org/wiki/List_of_time_zones_by_country : extragerea fusurilor orare
     - https://en.m.wikipedia.org/wiki/List_of_countries_by_system_of_government : extragerea regimelor politice

### BIBLIOGRAFIE
    - https://gdt050579.github.io/python-course-fii/administrative.html
    - https://pynative.com/python-mysql-database-connection/ 
    - https://www.w3schools.com/python/default.asp
    - https://www.w3schools.com/sql/default.asp
    - https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html
    - https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch 
    - https://www.geeksforgeeks.org/private-methods-in-python/
    - https://www.w3schools.com/python/python_regex.asp
    - https://www.moesif.com/blog/technical/api-development/Building-RESTful-API-with-Flask/
    - https://anderfernandez.com/en/blog/how-to-create-api-python/
    - https://rajansahu713.medium.com/hands-on-guide-to-restful-api-using-flask-python-16270f866ffe
    - https://www.programiz.com/python-programming/docstrings
    - https://www.digitalocean.com/community/tutorials/python-str-repr-functions
    - https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
