# ADR-001: Architekturentscheidung

## Entscheidung
Die Plattform wird modular aufgebaut (Layer Architecture).

---

## Gründe

- bessere Wartbarkeit
- klare Trennung von Verantwortlichkeiten
- skalierbar für KI-Integration

---

## Alternativen

- Monolith (abgelehnt wegen schlechter Erweiterbarkeit)
- Microservices (zu komplex für Startphase)

---

## Ergebnis

Layer-Architektur als Basis für MVP und Skalierung