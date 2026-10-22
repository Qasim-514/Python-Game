# Python-Game
A public Python game project

## The Pandas Detective Agency

Solve **The Missing Moonstone**, a short terminal mystery. After the Moonstone disappears from Bellweather Museum during a blackout, you investigate eight guests who were still inside. Request clues about each suspect's motive, alibi, keepsake, or witness, then use the evidence to narrow the field and identify the thief.

The game uses pandas DataFrames to store the suspect profiles, filter the remaining candidates as clues arrive, and display a report of your solved cases.

## Getting Started

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Start the game:

```bash
python data_detective.py
```

## Commands

- `clue` reveals a detail and narrows the suspect list.
- `suspects` shows who is still under suspicion.
- `guess <name>` makes an accusation, for example `guess Ada Finch`.
- `quit` closes the current case.

You have two accusations per case. Solve the mystery while using as few clues as you can.
