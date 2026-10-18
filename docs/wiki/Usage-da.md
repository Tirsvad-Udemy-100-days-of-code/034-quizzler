🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

# Brug

## Kør

Med `.venv` aktivt:

```bash
python -m quizzler
```

Du skal have internetforbindelse for at hente ti sand/falsk-spørgsmål.

## Sådan spiller du

Læs spørgsmålet og tryk på det grønne flueben (Sand) eller det røde kryds (Falsk). Spørgsmålsfeltet bliver grønt ved rigtigt svar og rødt ved forkert svar, point øverst til højre stiger, og det næste spørgsmål kommer efter ét sekund. Efter det sidste spørgsmål er knapperne slået fra, og slutpointene vises.

![Question](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/question.png)
![Right answer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/right-answer.png)
![Wrong answer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/034-quizzler/raw/branch/main/docs/images/wrong-answer.png)

## Når noget går galt

Kan spørgsmålstjenesten ikke nås, vises et vindue med en kort besked, og programmet slutter med afslutningskode 1. Tjek din internetforbindelse og prøv igen.
