SCHTASKS /parameter [argomenti]

Descrizione:
    Consente all'amministratore di creare, eliminare, ricercare,
    modificare, eseguire e terminare le operazioni pianificate
    su un sistema locale o remoto.

Elenco parametri:
    /Create         Crea una nuova attività pianificata.

    /Delete         Elimina le attività pianificate.

    /Query          Visualizza tutte le attività pianificate.

    /Change         Modifica le proprietà dell'attività pianificata.

    /Run            Esegue l'attività pianificata su richiesta.

    /End            Interrompe l'attività pianificata attualmente
                    in esecuzione.

    /ShowSid        Visualizza l'ID di sicurezza (SID) corrispondente a un nome di attività pianificata.

    /?              Visualizza questo messaggio della Guida.

Examples:
    SCHTASKS
    SCHTASKS /?
    SCHTASKS /Run /?
    SCHTASKS /End /?
    SCHTASKS /Create /?
    SCHTASKS /Delete /?
    SCHTASKS /Query  /?
    SCHTASKS /Change /?
    SCHTASKS /ShowSid /?
	
	
	C:\Users\Stefano>schtasks /create /?

SCHTASKS /Create [/S sistema [/U nomeutente [/P [password]]]]
    [/RU nomeutente [/RP password]] /SC pianificazione
[/MO modificatore] [/D giorno]
    [/M mesi] [/I tempoinattività] /TN nomeoperazione
/TR programma [/ST orainizio]
    [/RI intervallo] [ {/ET orafine | /DU durata} [/K] [/XML filexml] [/V1]]
    [/SD datainizio] [/ED datafine] [/IT | /NP] [/Z] [/F] [/HRESULT] [/?]

Descrizione:
    Consente all'amministratore di creare attività pianificate
    su sistemi locali o remoti.

Elenco parametri:
    /S   system        Specifica il sistema remoto a cui connettersi.
                       Se omesso, il parametro sistema assume come valore
                       il sistema locale.
    /U   nomeutente    Specifica il contesto utente in cui eseguire
                       schtasks.exe.

    /P   [password]    Specifica la password per il contesto utente
                       indicato. Se omesso, la password viene
                       richiesta.

    /RU  nomeutente    Specifica l'account utente (contesto utente)
                       usato per eseguire l'attività. Per l'account
                       di sistema, i valori validi sono "", "NT AUTHORITY\SYSTEM"
                       o "SYSTEM".
                       Per le attività v2, sono disponibili anche
                       "NT AUTHORITY\LOCALSERVICE" e
                       "NT AUTHORITY\NETWORKSERVICE" oltre ai
                       SID noti per tutti e tre.

    /RP  [password]    Specifica la password per l'utente indicato nella
                       casella "Esegui come".
                       Per fare in modo che la password venga richiesta
                       all'utente, il valore deve essere "*" o nullo.
                       La password viene ignorata per l'account di sistema.
                       Deve essere combinata con l'opzione /RU o /XML.

/XML
    /SC   pianificazione   Specifica la frequenza della pianificazione.
                           Tipi di pianificazione validi: MINUTE,HOURLY, DAILY,
                           WEEKLY, MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE,
                           ONEVENT.

    /MO   modificatore   Definisce ulteriormente il tipo di
                         controllo sulla frequenza della
                         pianificazione. I valori validi sono elencati
                         nella sezione "Modificatori" seguente.
    /D    giorni       Specifica i giorni della settimana in cui eseguire
                       l'attività.
                       Valori validi: MON, TUE, WED, THU, FRI, SAT, SUN e per
                       le pianificazioni mensili 1 - 31 (giorni del mese).
                       Il carattere jolly "*" specifica tutti i giorni.
    /M    mesi         Specifica i mesi dell'anno. Il valore predefinito è il
                       primo giorno del mese. Valori validi: JAN, FEB, MAR,
                       APR, MAY, JUN, JUL, AUG, SEP, OCT,NOV, DEC.
                       Il carattere jolly "*" specifica tutti i mesi.

    /I    tempoinattività  Specifica l'intervallo di tempo di inattività
                           da attendere prima di eseguire un'attività
                           ONIDLE pianificata.
                           Intervallo valido: 1 - 999 minuti.

    /TN   nomeattività  Specifica la stringa nel formato percorso\nome
                       che identifica in modo univoco l'attività pianificata.

    /TR   esecuzioneattività  Specifica il percorso e il nome file del programma da eseguire
                              all'orario pianificato.
                              Esempio: C:\windows\system32\calc.exe

    /ST   orainizio    Specifica l'ora di inizio dell'esecuzione dell'attività.
                       Il formato è HH:mm (24 ore), ad esempio 14:30 corrisponde
                       a 2:30 PM. Il valore predefinito è l'ora corrente se non
                       è specificato /ST. L'opzione è necessaria con /SC ONCE.
    /RI   intervallo   Specifica l'intervallo di ripetizione in minuti. Non è
                       applicabile ai tipi di pianificazioni: MINUTE, HOURLY,
                       ONSTART, ONLOGON, ONIDLE, ONEVENT.
                       Intervallo valido: 1 - 599940 minuti.

                       Se è specificato /ET o /DU, il valore predefinito è
                       10 minuti

    /ET   orafine      Specifica l'ora di fine dell'esecuzione
                       dell'attività. Il formato è HH.mm
                       (24 ore), ad esempio 14:50 corrisponde a 2:50 PM.
                       Non applicabile ai tipi di pianificazioni: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT.

    /DU   durata       Specifica la durata di esecuzione dell'attività. Il
                       formato è HH:mm. Questa opzione non è applicabile con /ET e
                       con /ET e per i tipi di pianificazione: ONSTART,
                       ONLOGON, ONIDLE, ONEVENT.
                       Per le attività /V1, se è specificato /RI,
                       il valore predefinito è 1 ora.

    /K                   Termina l'attività all'ora di fine o al raggiungimento della durata.

                       Non applicabile ai tipi di pianificazioni: ONSTART,
                                   È necessario
                                   specificare /ET o /DU.

    /SD   datainizio   Specifica la prima data in cui l'attività verrà eseguita.
                       Il formato è dd/mm/yyyy. Il valore predefinito è la data
                       corrente. Non applicabile ai tipi di pianificazione:
                       ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /ED   datafine     Specifica l'ultima data in cui l'attività deve essere
                       eseguita. Il formato è dd/mm/yyyy. Non applicabile ai tipi
                       di pianificazione: ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT.

    /EC   NomeCanale   Specifica il canale di eventi per i trigger OnEvent.

    /IT                Consente di eseguire l'attività in modo interattivo
                       solo se l'utente /RU è connesso nel momento in cui il
                       processo viene eseguito.
                       Questa attività viene eseguita solo se l'utente è
                       connesso.

    /NP                Nessuna password memorizzata. L'attività viene eseguita
                       in modalità non interattiva con l'account dell'utente
                       specificato. Sono disponibili solo risorse locali.

    /Z                 Contrassegna l'attività per l'eliminazione dopo l'ultima
                       esecuzione.

    /XML  filexml      Crea un'attività dal codice XML dell'attività specificato
                       in un file.
                       Può essere combinata con le opzioni /RU e /RP, oppure
                       solo con  /RP, quando l'XML contiene già l'entità.

    /V1                Crea un'attività visibile alle piattaforme precedenti a.
                       Vista. Non compatibile con /XML.

    /F                 Impone la creazione dell'attività e annulla gli avvisi se
                       l'attività specificata esiste già.

    /RL   livello      Imposta il livello di esecuzione per il processo.
                       I valori validi sono LIMITED e HIGHEST.
                       Il valore predefinito è LIMITED.

    /DELAY ritardo     Specifica il tempo di attesa per il ritardo dell'esecuzione dell'attività
                       dopo l'attivazione del trigger. Il formato è mmmm:ss.
                       L'opzione è valida solo per i tipi di pianificazione
                       ONSTART, ONLOGON, ONEVENT.

    /HRESULT             Per facilitare la diagnostica, il codice di uscita del processo
                         sarà nel formato HRESULT.

    /?                 Visualizza questo messaggio della Guida.

Modificatori: valori validi per il parametro /MO per tipo di pianificazione:
    MINUTE:  1 - 1439 minuti.
    HOURLY:  1 - 23 ore.
    DAILY:   1 - 365 giorni.
    WEEKLY:  1 - 52 settimane.
    ONCE:    Nessun modificatore.
    ONSTART: Nessun modificatore.
    ONLOGON: Nessun modificatore.
    ONIDLE:  Nessun modificatore.
    MONTHLY: 1 - 12, o
             FIRST, SECOND, THIRD, FOURTH, LAST, LASTDAY.

    ONEVENT:  stringa di query di eventi XPath.
Esempi:
    ==> Crea un'attività pianificata "doc" sul computer remoto "ABC"
        che esegue notepad.exe ogni ora per l'utente "nomeutente".

        SCHTASKS /Create /S ABC /U utente /P password /RU nomeutente
                 /RP password /SC HOURLY /TN doc /TR notepad

    ==> Crea un'attività pianificata "accountant" sul computer remoto
                "ABC" per eseguire calc.exe ogni cinque minuti dall'ora
        di inizio all'ora di fine specificate
        tra l'ora di avvio e l'ora di fine.

        SCHTASKS /Create /S ABC /U dominio\utente /P password /SC MINUTE
                 /MO 5 /TN accountant /TR calc.exe /ST 12:00 /ET 14:00
                 /SD 06/06/2006 /ED 06/06/2006 /RU nomeutente /RP password

    ==> Crea un'attività pianificata "oragioco" per eseguire
        freecell la prima domenica di ogni mese.

        SCHTASKS /Create /SC MONTHLY /MO first /D SUN /TN oragioco
                 /TR c:\windows\system32\freecell

    ==> Crea un'attività pianificata "rapporto" sul computer remoto "ABC"
        per eseguire notepad.exe ogni settimana.

        SCHTASKS /Create /S ABC /U utente /P password /RU nomeutente
                 /RP password /SC WEEKLY /TN rapporto /TR notepad.exe

    ==> Crea un'attività pianificata "logtracker"sul computer remoto "ABC"
        per eseguire notepad.exe ogni cinque minuti a partire dall'ora di avvio
        specificata senza ora di fine. Verrà chiesto di immettere la password
        /RP.

        SCHTASKS /Create /S ABC /U dominio\utente /P password /SC MINUTE
                 /MO 5 /TN logtracker
                 /TR c:\windows\system32\notepad.exe /ST 18:30
                 /RU nomeutente /RP

    ==> Crea un'attività pianificata "gioco" per eseguire
        ogni giorno freecell.exe alle 12:00, terminando automaticamente
        il processo alle 14:00

        SCHTASKS /Create /SC DAILY /TN gioco /TR c:\freecell /ST 12:00
                 /ET 14:00 /K
    ==> Crea un'attività pianificata "EventLog" che esegua wevtvwr.msc
        ogni volta che l'evento 101 viene pubblicato nel canale di sistema

        SCHTASKS /Create /TN EventLog /TR wevtvwr.msc /SC ONEVENT
                 /EC System /MO *[System/EventID=101]
    ==> Per includere spazi nei percorsi di file utilizzare due coppie di virgolette,
        una per CMD.EXE e una per SchTasks.exe. Le virgolette esterne per CMD
        devono essere doppie. Le virgolette interne possono essere singole o
        doppie con escape:
        SCHTASKS /Create
           /tr "'c:\programmi\internet explorer\iexplorer.exe'
           \"c:\log data\today.xml\"" ...

C:\Users\Stefano>