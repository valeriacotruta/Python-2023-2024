# STATES-OF-THE-WORLD
## CLIENT

### DESCRIERE
        Aplicatia Client este o parte a intregii aplicatii software create care faciliteaza interactiunea, in mod direct, cu utilizatorul, pentru a-i oferi un suport vizual de accesare a functionalitatilor implementate in cadrul aplicatiei STATES-OF-THE-WORLD.    
        Clientul acceseaza informatia din baza de date, prin intermediul API-ului, folosind biblioteca Requests.
    **Requests** permite trimiterea cererilor HTTP/1.1 intr-un mod elegant si extrem de simplu. 
    Pentru a trimite o cerere catre API-ul aplicatiei, am definit URL-ul API-ului drept http://127.0.0.1:8080/.
    La rularea clientului, se cere tastarea unei rute pentru a primi informatii despre anumite state sau pentru a insera informatiile colectate de crawler in baza de date.

### RUTE
    **METODE GET**
    - top-10-tari-populatie
    - top-10-tari-densitate
    - top-10-tari-suprafata
    - toate-tarile?fus-orar={time_zone} (time_zone - un fus orar, precum _UTC−08:00_, _UTC+09:00_ sau _UTC±00:00_)
    - toate-tarile?vecin={neighbour} (neighbour - o tara vecina)
    - toate-tarile?limba={language} (language - o limba)
    - toate-tarile?regim-politic={political_regime} (political_regime - un regim politic)
    **METODA POST**
    - insert-all-data 
