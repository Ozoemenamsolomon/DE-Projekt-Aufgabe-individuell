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

---

## **Agenda**

1.  **Theoretische Grundlagen**

    - Die Herausforderung traditioneller ETL
    - Die LLM-gestützte Lösung
    - Die Bedeutung des Kontexts
    - Ein neues Paradigma: Dynamische Transformationen

2.  **Projekteinführung & Workflow**
    - Projektübersicht & Ziele
    - Der 4-Schritte-Workflow
    - Code-Architektur & Demonstration
    - Fazit & Ausblick

---

<!-- _class: default -->

# **Teil 1: Theoretische Grundlagen**

---

## **Die Herausforderung traditioneller ETL**

ETL (Extract, Transform, Load) ist ein grundlegender Prozess im Data Engineering, birgt jedoch erhebliche Herausforderungen:

- **Hoher manueller Aufwand**: Das Schreiben und Pflegen von Transformationslogik ist zeitaufwändig und erfordert Fachkenntnisse.
- **Dokumentation ist ein Engpass**: Dokumentation wird oft vernachlässigt, ist veraltet oder inkonsistent, was Pipelines schwer verständlich und wartbar macht.
- **Langsame Entwicklungszyklen**: Die Kombination aus manueller Codierung und mangelhafter Dokumentation führt zu langen Iterationszeiten und hohem Wartungsaufwand.

![Diagramm einer komplexen, verworrenen ETL-Pipeline, die manuelle Arbeit und frustrierte Gesichter darstellt.](etl_challenge.png)

---

## **Die Lösung: LLM-gestützte Automatisierung**

LLMs sind hervorragend darin, natürliche Sprache zu verstehen und Code zu generieren, was zur Lösung dieser Probleme genutzt werden kann.

- **Automatisierte Codegenerierung**
  Ein LLM kann eine Benutzeranfrage in einfacher Sprache (z.B. "filtere alle Bioabfälle über 1000 kg") direkt in ausführbare Transformationslogik (z.B. Python/Pandas-Code) übersetzen.

- **Automatisierte Dokumentationsgenerierung**
  Gleichzeitig kann das LLM klare, konsistente und perfekt synchronisierte Dokumentation für den generierten Code erstellen.

---

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

---

## **Der Schlüssel zum Erfolg: Kontext bereitstellen**

Ein LLM ist kein Magier. Für korrekten und relevanten Code benötigt es hochwertigen **Kontext**. Das Prinzip lautet: "Garbage in, garbage out."

**Was ist "Kontext" in diesem Projekt?**

- **Daten-Schema (`Agent.md`)**: Eine detaillierte Beschreibung der `merged_data.csv` mit Spaltennamen, Datentypen und Beispielen.
- **Klare Anweisungen**: Regeln für das LLM, wie es die Ausgabe formatieren soll (z. B. Funktionsname `apply_transform`).
- **Die Benutzeranfrage (`user_prompt.txt`)**: Das spezifische, in natürlicher Sprache formulierte Ziel.

Diese Komponenten werden in einem **"Master-Prompt"** (`prompt_template.txt`) gebündelt.

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

---

## **Ein neues Paradigma: Dynamische Transformationen**

Dies führt zu einem neuen, flexibleren ETL-Paradigma.

- **Statische ETL (Extrahieren & Laden)**
  Die grundlegenden Teile der Pipeline – das Lesen von Quelldateien und das Schreiben in ein Ziel – bleiben statisch und robust.

- **Dynamischer "Transformieren"-Schritt**
  Die Transformationslogik wird zu einer "steckbaren", dynamischen Komponente, die bei Bedarf von einem LLM generiert wird.

Dies kombiniert die **Zuverlässigkeit** traditioneller ETL mit der **Flexibilität** von LLMs.

<!-- ![Konzeptionelles Diagramm, das die ETL-Pipeline mit statischen "Extract"- und "Load"-Blöcken zeigt, dazwischen ein dynamischer, durch ein LLM angetriebener "Transform"-Block.](dynamic_transform.png) -->

---

<!-- _class: default -->

# **Teil 2: Projekteinführung**

---

## **Projektübersicht: Ein LLM-gestütztes ETL-Framework**

Dieses Projekt implementiert das Paradigma der "Dynamischen Transformation".

**Ziel**: Eine funktionale ETL-Pipeline zu erstellen, bei der die Kern-Transformationslogik dynamisch von einem LLM basierend auf einer einfachen Benutzeranfrage generiert wird.

**Technologie**: Python, mit starkem Fokus auf die `pandas`-Bibliothek zur Datenmanipulation.

<!-- ![Architekturübersicht des Projekts, die den Fluss von der Benutzereingabe über das LLM zur Code-Generierung und Integration in die ETL-Pipeline visualisiert.](project_architecture.png) -->

---

## **Der 4-Schritte-Workflow**

Der Workflow ist einfach und benutzerzentriert gestaltet.

1.  **Prompt schreiben**
    Der Benutzer beschreibt die gewünschte Datentransformation in einer einfachen Textdatei: `user_prompt.txt`.

2.  **Code generieren mit einem LLM**
    Der Benutzer kopiert eine Master-Prompt-Vorlage (die das Datenschema und die Benutzeranfrage enthält) und sendet sie an ein LLM.

---

3.  **Transformationsskript aktualisieren**
    Der Benutzer fügt die vom LLM generierte Python-Funktion und Dokumentation in eine spezielle Python-Datei ein: `transforms/dynamic_transforms.py`.

4.  **Pipeline ausführen**
    Der Benutzer führt das Hauptskript (`python main_pipeline.py`) aus, das den gesamten ETL-Prozess orchestriert.

![Flussdiagramm mit vier nummerierten Schritten, die den Workflow von der Benutzereingabe über die LLM-Codegenerierung bis zur Pipeline-Ausführung darstellen.](workflow_steps.png)

---

## **Code-Architektur**

Das Projekt ist modular aufgebaut und trennt statische Logik von den dynamischen, vom LLM generierten Teilen.

```
.
├── etl/
│   ├── extract.py            # Statisch: Führt Rohdaten zu einer CSV-Datei zusammen.
│   └── load.py               # Statisch: Speichert die endgültigen Ausgabedaten.
├── transforms/
│   └── dynamic_transforms.py # << DYNAMISCH: Hier kommt der vom LLM generierte Code hin.
├── data/
│   ├── merged_data.csv       # Die saubere Quelle für Transformationen.
│   └── transformed_output.csv# Die endgültigen, transformierten Daten.
├── main_pipeline.py          # Haupt-Orchestrierungs-Skript.
├── Agent.md                  # Das dem LLM bereitgestellte Datenschema.
├── prompt_template.txt       # Die Master-Prompt-Vorlage für das LLM.
└── user_prompt.txt           # << Die natürlichsprachliche Anfrage des Benutzers.
```

<!-- ![Screenshot einer IDE, die die Projektdateistruktur mit den Ordnern "etl", "transforms" und den Hauptdateien anzeigt.](project_folder_structure.png) -->

---

## **Konzeptionelle Demonstration**

Gehen wir ein Beispiel durch.

**1. Der Benutzer-Prompt (`user_prompt.txt`)**

```
Filtern Sie den Datensatz so, dass nur Datensätze enthalten sind,
bei denen `WASTE_TYPE_TXT` 'Bioabfall FFM' ist und das Nettogewicht (`NET_WEIGHT`) größer als 1000 KG ist.
```

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

---

**3. Das Ergebnis**
Die Ausführung von `main_pipeline.py` wendet diese Logik an und speichert die gefilterten Daten in `transformed_output.csv`.

![Dreiteilige Ansicht, die eine Benutzereingabe, den vom LLM generierten Python-Code und einen Ausschnitt der resultierenden transformierten Daten zeigt.](demo_sequence.png)

---

## **Fazit & Ausblick**

Dieses Projekt demonstriert erfolgreich ein Framework zur Integration von LLMs in einen ETL-Workflow, das sowohl Code- als auch Dokumentationsgenerierung automatisiert.

### **Wesentliche Vorteile**:

- Reduziert den manuellen Aufwand und die Entwicklungszeit erheblich.
- Ermöglicht nicht-technischen Benutzern die Durchführung komplexer Datentransformationen.
- Stellt sicher, dass die Dokumentation immer mit der Transformationslogik synchronisiert ist.

---

### **Ausblick**:

- **Vollständige Automatisierung**: Direkter LLM-API-Aufruf in das Pipeline-Skript integrieren.
- **UI-Integration**: Eine einfache Benutzeroberfläche (z.B. mit Streamlit) für eine benutzerfreundlichere Erfahrung entwickeln.
- **Breitere Unterstützung**: Unterstützung weiterer Datenquellen, Ziele und Transformationsbibliotheken.

![Abstrakte Darstellung einer KI, die Datenflüsse automatisiert, Symbol für Effizienz und Innovation.](conclusion_future.png)

---

<!-- _class: lead -->

# **Vielen Dank!**

## Fragen?

<!-- ![Ein Dankeschön-Grafik mit einem Fragezeichen, das zum Stellen von Fragen einlädt.](thank_you_qa.png) -->
