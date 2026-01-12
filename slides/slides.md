---
marp: true
lang: de
title: LLMs zur Automatisierung von ETL-Pipelines und Dokumentation
author: Solomon Obinna Ozoemenam
style: |
  section {
    font-size: 1.7em;
  }
transition: slide
footer: Data Engineering Projektaufgabe |   12. Januar 2026
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.svg')
class:
  - lead
---

# **LLMs zur Automatisierung von ETL-Pipelines und Dokumentation**

**Projektaufgabe: Data Engineering**
_12. Januar 2026_

<!--
Guten Tag zusammen. Mein Name ist [Ihr Name] und heute präsentiere ich mein Projekt zum Thema "LLMs zur Automatisierung von ETL-Pipelines und Dokumentation".
-->

---

## **Agenda**

- **Zentrale Ergebnisse**

- **Theoretische Grundlagen**

  - Grundlagen: Was sind ETL & LLMs?
  - Die Herausforderung traditioneller ETL
  - Die LLM-gestützte Lösung & die Bedeutung des Kontexts
  - Ein neues Paradigma: Dynamische Transformationen

- **Projekteinführung & Workflow**
  - Projektübersicht & Ziele
  - Der 4-Schritte-Workflow
  - Code-Architektur & Demonstration
  - Fazit, Limitationen & Ausblick

<!--
Hier ist ein Überblick über das, was wir heute besprechen werden. Wir beginnen mit der Motivation und den theoretischen Grundlagen, die die Basis für dieses Projekt bilden. Danach werde ich das Projekt selbst vorstellen, einschließlich seines Workflows und einer Demonstration, bevor wir mit einem Fazit und der Diskussion von Limitationen abschließen.
-->

---

## **Zentrale Ergebnisse**

- **Problem**: Traditionelle ETL-Prozesse sind langsam, manuell und schlecht dokumentiert.<sup><a href="#ref-1">[1]</a></sup>
- **Lösung**: Dieses Projekt nutzt ein LLM, um aus einer einfachen Textanforderung automatisch sowohl den **Python-Code** für die Datentransformation als auch die zugehörige **Dokumentation** zu generieren.<sup><a href="#ref-2">[2]</a></sup>
- **Ergebnis**: Ein agiles, "selbst-dokumentierendes" ETL-Framework, das den Entwicklungsaufwand erheblich reduziert und Fachexperten direkt einbindet.<sup><a href="#ref-3">[3]</a></sup>

```mermaid
graph LR
    A[Anforderung] --> B((LLM));
    B --> C[Code + Doku];
    C --> D[Automatisiertes<br>Ergebnis];
```

<!--
Bevor wir ins Detail gehen, hier die Kernaussage meines Projekts:
Das Hauptproblem traditioneller Datenprozesse ist, dass sie langsam und schlecht dokumentiert sind.
Meine Lösung ist ein Framework, das ein großes Sprachmodell nutzt, um aus einer einfachen Textanfrage automatisch sowohl den Code als auch die Dokumentation zu generieren.
Das Ergebnis ist eine extrem agile, sich selbst dokumentierende Pipeline, die den manuellen Aufwand drastisch senkt und Fachexperten befähigt, direkt mit den Daten zu arbeiten.
-->

---

<!-- _class: default -->

# **Teil 1: Theoretische Grundlagen**

---

## **Grundlagen: Was sind ETL & LLMs?**

- **ETL (Extract, Transform, Load)**:

  - **Extract**: Daten aus Quellen extrahieren.
  - **Transform**: Daten bereinigen, anreichern, umwandeln.
  - **Load**: Daten in ein Zielsystem (z.B. Data Warehouse) laden.
  - _Traditionell ein starrer, manueller Prozess._<sup><a href="#ref-4">[4]</a></sup>

- **LLM (Large Language Model)**:
  - Ein KI-Modell, das trainiert wurde, menschliche Sprache zu verstehen und zu generieren.
  - Kann Aufgaben wie Übersetzung, Zusammenfassung und **Code-Generierung** ausführen.<sup><a href="#ref-5">[5]</a></sup>

<!--
Kurz zu den Grundlagen: ETL ist der klassische Prozess, um Daten von A nach B zu bekommen, wobei der Transformationsschritt oft sehr aufwändig ist. LLMs sind KI-Modelle, die Text verstehen und erzeugen können. In unserem Fall nutzen wir sie als eine Art "programmierenden Assistenten".
-->

---

## **Motivation: Warum ist dieses Thema relevant?**

- **"Demokratisierung" der Daten**: Fachanwender ohne tiefe Programmierkenntnisse können komplexe Analysen selbst anstoßen.<sup><a href="#ref-6">[6]</a></sup>
- **Agilität & Geschwindigkeit**: Deutlich schnellere Iterationszyklen im Vergleich zu traditionellen, ticket-basierten Entwicklungsprozessen.<sup><a href="#ref-7">[7]</a></sup>
- **"Lebende" Dokumentation**: Die automatisch generierte Dokumentation dient als Wissensdatenbank, verhindert Wissenssilos und ist immer aktuell.<sup><a href="#ref-8">[8]</a></sup>

```mermaid
graph TD
    A[Fachanwender] -- Natürliche Sprache --> B((Automatisierte<br>Datenplattform<br>/ LLM));
    C[Entwickler] -- Definiert Regeln &<br>Daten-Schemata --> B;
    B -- Generierter Code &<br>Doku --> D[Daten-Transformation];
    D --> E[Analyse &<br>Erkenntnisse];
    E --> A;
```

<!--
Warum ist dieses Thema gerade jetzt so relevant? Es gibt drei Haupttreiber.
Erstens die "Demokratisierung" der Daten. Durch die Übersetzung von natürlicher Sprache zu Code können Fachanwender, die die Daten am besten kennen, selbst komplexe Transformationen anstoßen, ohne auf Entwicklerressourcen warten zu müssen.
Zweitens führt dies zu einer enormen Steigerung der Agilität. Statt wochenlanger Zyklen für die Umsetzung können neue Anforderungen in Stunden oder Minuten realisiert werden.
Und drittens schaffen wir eine "lebende" Dokumentation. Da Code und Doku zusammen generiert werden, gehört das Problem veralteter Dokumentationen der Vergangenheit an.
-->

---

## **Die Herausforderung traditioneller ETL**

- Hoher manueller Aufwand
- Veraltete oder fehlende Dokumentation
- Langsame Entwicklungszyklen & hohe Wartungskosten<sup><a href="#ref-9">[9]</a></sup>

---

```mermaid
graph TD
    subgraph "Manuelle Prozesse"
        A[Anforderung] --> B{Entwickler<br>schreibt Code};
        B --> C[Code-Review];
        C --> D[Manuelle<br>Dokumentation];
        D --> E[Deployment];
    end
    B -.-> A;
    D -.-> B;
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#f9f,stroke:#333,stroke-width:2px
```

<!--
Beginnen wir mit dem Kernproblem. ETL ist ein fundamentaler Prozess, aber traditionell mit erheblichen Herausforderungen verbunden.
Der manuelle Aufwand für das Schreiben und Anpassen von Transformationslogik ist enorm.
Ein noch größeres Problem ist oft die Dokumentation. Sie wird häufig vernachlässigt, ist veraltet oder inkonsistent.
Diese Faktoren führen unweigerlich zu langsamen Entwicklungszyklen und hohen Wartungskosten.
-->

---

## **Die Lösung: LLM, Kontext & Prompt**

- **LLM als "Übersetzer"**: Wandelt Anforderung in Code & Doku um.<sup><a href="#ref-10">[10]</a></sup>
- **Kontext vs. Prompt**: Eine wichtige Unterscheidung.<sup><a href="#ref-11">[11]</a></sup>
  - **Kontext**: Die statische "DNA" des Projekts. Eine einmalige Einrichtung, die Daten-Schemata, Regeln und Ausgabeformate definiert (`Agent.md`).
  - **User Prompt**: Die dynamische Benutzeranfrage. Ändert sich mit jeder neuen Anforderung (`user_prompt.txt`).

---

```mermaid
graph TD
    graph TD
    A["Kontext<br>(Agent.md)"]
    B["User Prompt<br>(user_prompt.txt)"]

    A --> E
    B --> E{LLM}

    E --> F[Generierter Code &<br>Dokumentation]
```

<!--
Die Lösung liegt darin, ein LLM als intelligenten Übersetzer einzusetzen. Aber ein LLM ist kein Magier. Die Qualität des Ergebnisses hängt direkt von der Qualität des Inputs ab. Hier gilt das Prinzip: "Garbage in, garbage out."

Der Schlüssel zum Erfolg ist die Kombination aus einem stabilen Kontext (der die "Spielregeln" festlegt) und einem flexiblen Prompt (der die "Aufgabe" beschreibt).
Nur mit diesem gebündelten Befehl kann das LLM präzise und nützliche Ergebnisse liefern.
-->

---

## **Ein neues Paradigma: Dynamische Transformationen**

- **Statische ETL (Extrahieren & Laden)**: Robuste, unveränderliche Basis.
  - _Derzeit begrenzt auf CSV-Dateien für Projektspezifikationen, um Komplexität zu reduzieren._
- **Dynamischer "Transformieren"-Schritt**: Flexible, bei Bedarf vom LLM generierte Logik.
- Kombiniert **Zuverlässigkeit** mit **Flexibilität**.<sup><a href="#ref-12">[12]</a></sup>

---

```mermaid
graph LR
    A[Datenquelle] --> B[Static Extract];
    subgraph "Dynamischer Teil"
        C(LLM generiert<br>Transformations-Code) --> D[Transform];
    end
    B --> D;
    D --> E[Static Load];
    E --> F[Ziel-Datenbank];
    style C fill:#ccf,stroke:#333
```

<!--
Dies führt uns zu einem neuen ETL-Paradigma.
Wir behalten die statischen, robusten Teile der Pipeline bei – das Extrahieren und Laden.

Warum sind diese statisch? Für dieses Projekt wurde mit spezifischen CSV-Dateien gearbeitet. Um die Lösung nicht unnötig zu verkomplizieren, wurden Extraktion und Laden auf diesen Anwendungsfall zugeschnitten.

Der entscheidende Unterschied ist der "Transformieren"-Schritt. Dieser wird zu einer dynamischen Komponente, deren Logik bei Bedarf vom LLM generiert wird. Dieser Ansatz kombiniert die Zuverlässigkeit einer traditionellen Architektur mit der unglaublichen Flexibilität, die LLMs bieten.
-->

---

<!-- _class: default -->

# **Teil 2: Projekteinführung**

---

## **Projektübersicht: Ein LLM-gestütztes ETL-Framework**

- **Ziel**: Eine ETL-Pipeline mit dynamisch generierter Transformationslogik.
- **Technologie**: Python & pandas.

---

```mermaid
graph TD
    A[Benutzer schreibt<br>user_prompt.txt] --> B{Master-Prompt<br>wird erstellt};
    C[Agent.md<br>(Schema + Prompt-Vorlage)] --> B;
    B --> E((LLM));
    E --> F[dynamic_transforms.py<br>wird aktualisiert];
    F --> G[main_pipeline.py<br>führt Transformation aus];
    H[merged_data.csv] --> G;
    G --> I[transformed_output.csv];
```

<!--
Kommen wir nun zur konkreten Umsetzung in meinem Projekt.
Das Ziel war es, ein Framework zu schaffen, das genau dieses Paradigma der dynamischen Transformation implementiert.
Die gesamte Umsetzung erfolgte in Python, wobei die `pandas`-Bibliothek das Herzstück der Datenmanipulation bildet.
-->

---

## **Der 4-Schritte-Workflow**

1.  **Prompt schreiben** (`user_prompt.txt`)
2.  **Code generieren** (mit LLM)
3.  **Skript aktualisieren** (`dynamic_transforms.py`)
4.  **Pipeline ausführen** (`main_pipeline.py`)

---

![Grafik, die den 4-Schritte-Workflow darstellt: Prompt schreiben, Code generieren, Skript aktualisieren, Pipeline ausführen.](4-step-process.png)

```mermaid
graph TD
    A["1. Prompt schreiben<br>(user_prompt.txt)"] --> B["2. Code generieren<br>(mit LLM)"];
    B --> C["3. Skript aktualisieren<br>(dynamic_transforms.py)"];
    C --> D["4. Pipeline ausführen<br>(main_pipeline.py)"];
```

<!--
Der daraus resultierende Workflow ist einfach und benutzerzentriert.

Zuerst schreibt der Benutzer seine Anforderung in natürlicher Sprache.
Zweitens generiert er mit einem LLM den Code.
Drittens fügt er den generierten Code in die dafür vorgesehene Python-Datei ein.
Und schließlich führt er das Hauptskript aus, das die gesamte Pipeline orchestriert.
-->

---

## **Code-Architektur**

```
.
├── etl/                  # Statische Logik
│   ├── extract.py
│   └── load.py
├── transforms/
│   └── dynamic_transforms.py # DYNAMISCHE LOGIK
├── main_pipeline.py      # Orchestrator
├── Agent.md              # Kontext: Datenschema & Prompt-Vorlage
└── user_prompt.txt       # Kontext: Benutzeranfrage
```

<!--
Die Code-Architektur spiegelt diese Trennung von statischer und dynamischer Logik wider.
Der `etl`-Ordner enthält die statischen Skripte.
Im `transforms`-Ordner befindet sich die Datei für den LLM-generierten Code.
Die `main_pipeline.py` ist der Orchestrator, der alles zusammenfügt.
Die übrigen Textdateien bilden das Prompting-Framework, das dem LLM den notwendigen Kontext liefert.
-->

---

## **Demonstration: Von der Anfrage zum Ergebnis**

**1. Benutzer-Prompt:**

```txt
Filtern Sie auf 'Bioabfall FFM' mit Gewicht > 1000 KG.
```

**2. Generierter Code:**

```python
def apply_transform(df):
    # ... filter logic ...
    return df
```

**3. Generierte Dokumentation:**

```md
## Bioabfall-Filter

Filtert Datensätze für 'Bioabfall FFM' über 1000 KG.
```

<!--
Hier sehen wir den Prozess im Überblick.
Auf der linken Seite steht die einfache Benutzeranfrage.
In der Mitte sehen wir den vom LLM generierten Python-Code, der diese Anfrage umsetzt.
Und rechts die automatisch erstellte Dokumentation.
Wenn die Pipeline läuft, wird genau dieser Code ausgeführt, um das Endergebnis zu erzeugen.
-->

---

## **Fazit & Limitationen**

### **Wesentliche Vorteile**:

- Reduziert manuellen Aufwand
- Ermöglicht Fachanwendern komplexe Transformationen
- Garantiert synchronisierte Dokumentation

### **Limitationen & Risiken**:

- **Korrektheit**: Generierter Code erfordert Überprüfung ("Human-in-the-Loop").<sup><a href="#ref-13">[13]</a></sup>
- **Prompt Engineering**: Ergebnisqualität hängt stark von der Prompt-Qualität ab.<sup><a href="#ref-14">[14]</a></sup>
- **Sicherheit**: Vorsicht beim Senden sensibler Schemainformationen an externe LLM-APIs.<sup><a href="#ref-15">[15]</a></sup>

---

![Warnschild-Grafik mit Symbolen für Code-Bugs, Sicherheitsschlösser und inkonsistente Ergebnisse, um Risiken darzustellen.](limitations_risks.png)

<!--
Zusammenfassend lässt sich sagen, dass die Vorteile auf der Hand liegen: weniger Aufwand, mehr Power für Fachexperten und immer aktuelle Dokumentation.

Es ist jedoch wichtig, auch die Limitationen zu erwähnen. Der generierte Code ist nicht immer perfekt und muss überprüft werden. Die Qualität des Ergebnisses hängt stark von der Qualität des Prompts ab. Und bei der Nutzung externer LLMs müssen Sicherheitsaspekte, insbesondere bei sensiblen Daten-Schemata, berücksichtigt werden.
-->

---

## **Ausblick**

- **Vollständige Automatisierung**: Direkter LLM-API-Aufruf in das Pipeline-Skript integrieren.
- **Dynamisches E & L**: Den `Extract`- und `Load`-Schritt flexibler gestalten, um z.B. SQL-Datenbanken oder JSON-Dateien zu unterstützen.
- **UI-Integration**: Eine einfache Benutzeroberfläche (z.B. mit Streamlit) für eine benutzerfreundlichere Erfahrung entwickeln.

![Abstrakte Darstellung einer KI, die Datenflüsse automatisiert, Symbol für Effizienz und Innovation.](conclusion_future.png)

<!--
Die nächsten Schritte wären, den Prozess vollständig zu automatisieren, die Pipeline durch dynamische Extract- und Load-Schritte für verschiedene Datenformate zu erweitern und eventuell eine einfache Benutzeroberfläche zu entwickeln, um die Bedienung noch weiter zu vereinfachen.
-->

---

<!-- _class: default -->

# Referenzen

<p id="ref-1"><b>[1]</b> <a href="https://scholar.google.com/scholar?q=traditional+ETL+challenges%2C+data+pipeline+maintenance%2C+technical+debt+data+warehousing">traditional ETL challenges, data pipeline maintenance, technical debt data warehousing</a></p>
<p id="ref-2"><b>[2]</b> <a href="https://scholar.google.com/scholar?q=LLM+for+code+generation%2C+natural+language+to+code%2C+automatic+documentation">LLM for code generation%2C natural language to code%2C automatic documentation</a></p>
<p id="ref-3"><b>[3]</b> <a href="https://scholar.google.com/scholar?q=data+democratization%2C+self-service+analytics%2C+agile+data+engineering">data democratization%2C self-service analytics%2C agile data engineering</a></p>
<p id="ref-4"><b>[4]</b> <a href="https://scholar.google.com/scholar?q=ETL+fundamentals%2C+data+warehousing%2C+Ralph+Kimball%2C+Bill+Inmon">ETL fundamentals%2C data warehousing%2C Ralph Kimball%2C Bill Inmon</a></p>
<p id="ref-5"><b>[5]</b> <a href="https://scholar.google.com/scholar?q=large+language+models+survey%2C+attention+is+all+you+need%2C+code+generation+LLM">large language models survey%2C attention is all you need%2C code generation LLM</a></p>
<p id="ref-6"><b>[6]</b> <a href="https://scholar.google.com/scholar?q=data+democratization%2C+self-service+analytics%2C+citizen+data+scientist">data democratization%2C self-service analytics%2C citizen data scientist</a></p>
<p id="ref-7"><b>[7]</b> <a href="https://scholar.google.com/scholar?q=agile+data+warehousing%2C+agile+ETL+development">agile data warehousing%2C agile ETL development</a></p>
<p id="ref-8"><b>[8]</b> <a href="https://scholar.google.com/scholar?q=living+documentation%2C+documentation+as+code">living documentation%2C documentation as code</a></p>
<p id="ref-9"><b>[9]</b> <a href="https://scholar.google.com/scholar?q=challenges+of+traditional+ETL%2C+ETL+technical+debt%2C+data+pipeline+maintenance+costs">challenges of traditional ETL%2C ETL technical debt%2C data pipeline maintenance costs</a></p>
<p id="ref-10"><b>[10]</b> <a href="https://scholar.google.com/scholar?q=program+synthesis+with+large+language+models%2C+natural+language+to+code">program synthesis with large language models%2C natural language to code</a></p>
<p id="ref-11"><b>[11]</b> <a href="https://scholar.google.com/scholar?q=prompt+engineering%2C+in-context+learning+large+language+models">prompt engineering%2C in-context+learning large language models</a></p>
<p id="ref-12"><b>[12]</b> <a href="https://scholar.google.com/scholar?q=hybrid+data+architecture%2C+dynamic+data+pipelines%2C+configurable+etl">hybrid data architecture%2C dynamic data pipelines%2C configurable etl</a></p>
<p id="ref-13"><b>[13]</b> <a href="https://scholar.google.com/scholar?q=correctness+of+LLM-generated+code%2C+human+in+the+loop+code+generation">correctness of LLM-generated code%2C human in the loop code generation</a></p>
<p id="ref-14"><b>[14]</b> <a href="https://scholar.google.com/scholar?q=prompt+engineering+survey%2C+impact+of+prompt+design+on+LLM+performance">prompt engineering survey%2C impact of prompt design on LLM performance</a></p>
<p id="ref-15"><b>[15]</b> <a href="https://scholar.google.com/scholar?q=security+and+privacy+of+large+language+models%2C+data+leakage+LLM+APIs">security and privacy of large language models%2C data leakage LLM APIs</a></p>

---

<!-- _class: lead -->

# **Vielen Dank!**

## Fragen?
