---
marp: true
lang: de
title: LLMs zur Automatisierung von ETL-Pipelines und Dokumentation
author: Solomon Obinna Ozoemenam
date: 12. Januar 2026
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

- **Theoretische Grundlagen**
    - Die Herausforderung traditioneller ETL
    - Die LLM-gestützte Lösung
    - Die Bedeutung des Kontexts
    - Ein neues Paradigma: Dynamische Transformationen

- **Projekteinführung & Workflow**
    - Projektübersicht & Ziele
    - Der 4-Schritte-Workflow
    - Code-Architektur & Demonstration
    - Fazit & Ausblick

<!--
Hier ist ein Überblick über das, was wir heute besprechen werden. Wir beginnen mit den theoretischen Grundlagen, die die Motivation für dieses Projekt bilden. Danach werde ich das Projekt selbst vorstellen, einschließlich seines Workflows, der Architektur und einer kurzen Demonstration.
-->

---

<!-- _class: default -->

# **Teil 1: Theoretische Grundlagen**

---

## **Die Herausforderung traditioneller ETL**

- Hoher manueller Aufwand
- Veraltete oder fehlende Dokumentation
- Langsame Entwicklungszyklen & hohe Wartungskosten

![Diagramm einer komplexen, verworrenen ETL-Pipeline, die manuelle Arbeit und frustrierte Gesichter darstellt.](etl_challenge.png)

<!--
Beginnen wir mit dem Kernproblem. ETL – Extract, Transform, Load – ist ein fundamentaler Prozess im Data Engineering. Traditionell ist dieser Prozess jedoch mit erheblichen Herausforderungen verbunden.

Der manuelle Aufwand für das Schreiben und Anpassen von Transformationslogik ist enorm und erfordert spezialisierte Entwickler.

Ein noch größeres Problem ist oft die Dokumentation. Sie wird häufig vernachlässigt, ist veraltet oder inkonsistent, was es extrem schwierig macht, bestehende Pipelines zu verstehen und zu warten.

Diese Faktoren führen unweigerlich zu langsamen Entwicklungszyklen und hohen Wartungskosten.
-->

---

## **Die Lösung: LLM-gestützte Automatisierung**

- **Automatisierte Codegenerierung**: Übersetzt natürliche Sprache in ausführbaren Python/Pandas-Code.
- **Automatisierte Dokumentationsgenerierung**: Erstellt gleichzeitig klare und konsistente Dokumentation.

```mermaid
graph TD
    subgraph "Input"
        A[Master-Prompt<br>(Schema + Regeln + Benutzeranfrage)]
    end

    A --> B(LLM - Large Language Model)

    subgraph "Output"
        C["apply_transform() Funktion<br>(Python-Code)"]
        D["TRANSFORM_DOCUMENTATION<br>(Markdown)"]
    end

    B --> C
    B --> D
```

<!--
Hier kommen Large Language Models ins Spiel. LLMs sind hervorragend darin, natürliche Sprache zu verstehen und Code zu generieren. Diese Fähigkeit können wir nutzen, um die größten Schwachstellen im ETL-Prozess zu adressieren.

Erstens, durch automatisierte Codegenerierung. Ein LLM kann eine Benutzeranfrage in einfacher Sprache, wie "filtere alle Bioabfälle über 1000 kg", direkt in lauffähigen Code übersetzen.

Zweitens, und das ist entscheidend, kann das LLM gleichzeitig eine klare und perfekt synchronisierte Dokumentation für genau diesen Code erstellen. Das Problem der veralteten Doku wird damit im Kern gelöst.

Wie dieses Diagramm zeigt, nimmt das LLM einen aufbereiteten "Master-Prompt" entgegen und erzeugt daraus sowohl den Code als auch die Dokumentation.
-->

---

## **Der Schlüssel zum Erfolg: Kontext bereitstellen**

- Ein LLM benötigt hochwertigen Kontext: **"Garbage in, garbage out."**
- **Kontext** = Daten-Schema + Anweisungen + Benutzeranfrage
- Alle Komponenten werden in einem **"Master-Prompt"** gebündelt.

```mermaid
graph TD
    subgraph "Kontext-Komponenten"
        A[Daten-Schema<br>(Agent.md)]
        B[Benutzeranfrage<br>(user_prompt.txt)]
        C[Anweisungen & Regeln]
    end

    A --> D{Master-Prompt}
    B --> D
    C --> D

    D --> E((LLM))

    E --> F[Generierter Code &<br>Dokumentation]
```

<!--
Ein LLM ist jedoch kein Magier. Um korrekten und relevanten Code zu generieren, benötigt es exzellenten Kontext. Hier gilt das Prinzip: "Garbage in, garbage out."

In diesem Projekt besteht der Kontext aus drei Hauptkomponenten:
Erstens, das Daten-Schema, hinterlegt in der Datei `Agent.md`. Es beschreibt detailliert die Spalten, Datentypen und Inhalte unserer Zieldaten.
Zweitens, klare Anweisungen und Regeln, wie das LLM seine Ausgabe formatieren soll – zum Beispiel, dass die Funktion `apply_transform` heißen muss.
Und drittens, natürlich die spezifische Benutzeranfrage aus der `user_prompt.txt`.

Wie das Diagramm zeigt, werden all diese Teile zu einem "Master-Prompt" zusammengefügt, der dem LLM die bestmögliche Grundlage für seine Arbeit gibt.
-->

---

## **Ein neues Paradigma: Dynamische Transformationen**

- **Statische ETL (Extrahieren & Laden)**: Robuste, unveränderliche Basis.
- **Dynamischer "Transformieren"-Schritt**: Flexible, bei Bedarf vom LLM generierte Logik.
- Kombiniert **Zuverlässigkeit** mit **Flexibilität**.

![Konzeptionelles Diagramm, das die ETL-Pipeline mit statischen "Extract"- und "Load"-Blöcken zeigt, dazwischen ein dynamischer, durch ein LLM angetriebener "Transform"-Block.](dynamic_transform.png)

<!--
Dies führt uns zu einem neuen, flexibleren ETL-Paradigma.
Wir behalten die statischen, robusten Teile der Pipeline – also das Extrahieren der Rohdaten und das Laden der Zieldaten – bei. Diese bilden eine stabile Basis.
Der entscheidende Unterschied ist der "Transformieren"-Schritt. Dieser wird zu einer dynamischen, austauschbaren Komponente, deren Logik bei Bedarf von einem LLM generiert wird.
Dieser Ansatz kombiniert die Zuverlässigkeit einer traditionellen Architektur mit der unglaublichen Flexibilität, die LLMs bieten.
-->

---

<!-- _class: default -->

# **Teil 2: Projekteinführung**

---

## **Projektübersicht: Ein LLM-gestütztes ETL-Framework**

- **Ziel**: Eine ETL-Pipeline mit dynamisch generierter Transformationslogik.
- **Technologie**: Python & pandas.

![Architekturübersicht des Projekts, die den Fluss von der Benutzereingabe über das LLM zur Code-Generierung und Integration in die ETL-Pipeline visualisiert.](project_architecture.png)

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

![Flussdiagramm mit vier nummerierten Schritten, die den Workflow von der Benutzereingabe über die LLM-Codegenerierung bis zur Pipeline-Ausführung darstellen.](workflow_steps.png)

<!--
Der daraus resultierende Workflow ist einfach und benutzerzentriert, wie man hier in vier Schritten sieht.

Zuerst schreibt der Benutzer seine Anforderung in natürlicher Sprache in die `user_prompt.txt`-Datei.

Zweitens generiert er mit einem LLM und einer vorbereiteten Vorlage den Code.

Drittens fügt er den generierten Code in die `dynamic_transforms.py`-Datei ein.

Und schließlich führt er das Hauptskript aus, das die gesamte Pipeline von Anfang bis Ende orchestriert.
-->

---

## **Code-Architektur**

```
.
├── etl/
│   ├── extract.py        # Statische Logik
│   └── load.py           # Statische Logik
├── transforms/
│   └── dynamic_transforms.py # DYNAMISCHE LOGIK
├── data/
│   ├── merged_data.csv       # Die saubere Quelle für Transformationen.
│   └── transformed_output.csv# Die endgültigen, transformierten Daten.
├── main_pipeline.py      # Orchestrator
├── Agent.md              # Kontext: Datenschema
├── prompt_template.txt   # Kontext: Vorlage
└── user_prompt.txt       # Kontext: Benutzeranfrage
```

![Screenshot einer IDE, die die Projektdateistruktur mit den Ordnern "etl", "transforms" und den Hauptdateien anzeigt.](project_folder_structure.png)

<!--
Die Code-Architektur spiegelt diese Trennung von statischer und dynamischer Logik wider.

Der `etl`-Ordner enthält die statischen Skripte zum Extrahieren und Laden der Daten.
Im `transforms`-Ordner befindet sich die `dynamic_transforms.py`, die als Platzhalter für den LLM-generierten Code dient.
Die `main_pipeline.py` ist der Orchestrator, der alles zusammenfügt.
Die übrigen Textdateien bilden das Prompting-Framework, das dem LLM den notwendigen Kontext liefert.
-->

---

## **Konzeptionelle Demonstration**

**1. Der Benutzer-Prompt (`user_prompt.txt`)**
```
Filtern Sie Datensätze, bei denen `WASTE_TYPE_TXT` 'Bioabfall FFM'
ist und `NET_WEIGHT` größer als 1000 KG ist.
```

<!--
Hier sehen wir es in Aktion. Der Benutzer schreibt eine klare Anforderung in die `user_prompt.txt`-Datei.
-->

---

**2. Der vom LLM generierte Code (`dynamic_transforms.py`)**
```python
def apply_transform(df: pd.DataFrame) -> pd.DataFrame:
    waste_type_filter = df['WASTE_TYPE_TXT'] == 'Bioabfall FFM'
    weight_filter = df['NET_WEIGHT'] > 1000
    transformed_df = df[waste_type_filter & weight_filter].copy()
    return transformed_df

TRANSFORM_DOCUMENTATION = """
## Bioabfall- und Gewichtsfilter

Diese Transformation filtert Datensätze, um nur solche einzuschließen,
bei denen `WASTE_TYPE_TXT` 'Bioabfall FFM' ist
und `NET_WEIGHT` größer als 1000 KG ist.
"""
```

<!--
Das LLM generiert daraufhin die passende `apply_transform`-Funktion sowie die zugehörige Dokumentation.
-->

---

**3. Das Ergebnis**
Die `main_pipeline.py` wendet diese Logik an und speichert die gefilterten Daten in `transformed_output.csv`.

![Dreiteilige Ansicht, die eine Benutzereingabe, den vom LLM generierten Python-Code und einen Ausschnitt der resultierenden transformierten Daten zeigt.](demo_sequence.png)

<!--
Wenn die Haupt-Pipeline ausgeführt wird, wird genau diese Logik angewendet. Das Ergebnis ist eine neue CSV-Datei, die nur noch die gefilterten Daten enthält.
-->

---

## **Fazit & Ausblick**

### **Wesentliche Vorteile**:
- Reduziert den manuellen Aufwand.
- Ermöglicht Fachanwendern komplexe Transformationen.
- Garantiert synchronisierte Dokumentation.

<!--
Zusammenfassend lässt sich sagen, dass dieses Projekt erfolgreich ein Framework zur Integration von LLMs in ETL-Workflows demonstriert. Die Vorteile liegen auf der Hand: weniger manueller Aufwand, die Befähigung von Fachexperten und immer aktuelle Dokumentation.
-->

---

### **Ausblick**:
- **Vollständige Automatisierung**: Direkter LLM-API-Aufruf integrieren.
- **UI-Integration**: Eine einfache Benutzeroberfläche (z.B. mit Streamlit) entwickeln.
- **Breitere Unterstützung**: Mehr Datenquellen, Ziele und Transformationsbibliotheken.

![Abstrakte Darstellung einer KI, die Datenflüsse automatisiert, Symbol für Effizienz und Innovation.](conclusion_future.png)

<!--
Die nächsten Schritte wären, den Prozess durch eine direkte API-Anbindung an ein LLM vollständig zu automatisieren und eventuell eine einfache Benutzeroberfläche zu entwickeln, um die Bedienung noch weiter zu vereinfachen.
-->

---

<!-- _class: lead -->

# **Vielen Dank!**

## Fragen?

<!-- ![Ein Dankeschön-Grafik mit einem Fragezeichen, das zum Stellen von Fragen einlädt.](thank_you_qa.png) -->