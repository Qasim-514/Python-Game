import random

import pandas as pd


SUSPECTS = pd.DataFrame(
    [
        {"Suspect": "Ada Finch", "Motive": "debt", "Alibi": "the greenhouse", "Keepsake": "a silver button", "Witness": "the night guard"},
        {"Suspect": "Bram Holloway", "Motive": "revenge", "Alibi": "the clock tower", "Keepsake": "a red glove", "Witness": "the pianist"},
        {"Suspect": "Cleo Marlow", "Motive": "ambition", "Alibi": "the library", "Keepsake": "a brass key", "Witness": "the chef"},
        {"Suspect": "Dorian Pike", "Motive": "debt", "Alibi": "the clock tower", "Keepsake": "a blue ribbon", "Witness": "the pianist"},
        {"Suspect": "Esme Vale", "Motive": "jealousy", "Alibi": "the greenhouse", "Keepsake": "a red glove", "Witness": "the chef"},
        {"Suspect": "Felix Wren", "Motive": "ambition", "Alibi": "the observatory", "Keepsake": "a silver button", "Witness": "the night guard"},
        {"Suspect": "Greta Moss", "Motive": "revenge", "Alibi": "the library", "Keepsake": "a blue ribbon", "Witness": "the chef"},
        {"Suspect": "Hugo Bell", "Motive": "jealousy", "Alibi": "the observatory", "Keepsake": "a brass key", "Witness": "the pianist"},
    ]
)
CLUE_COLUMNS = ["Motive", "Alibi", "Keepsake", "Witness"]


def show_candidates(candidates: pd.DataFrame) -> None:
    names = candidates["Suspect"].tolist()
    print("Still in the frame: " + (", ".join(names) if names else "nobody"))


def play_case() -> tuple[str, int, int]:
    culprit = SUSPECTS.sample(1).iloc[0]
    remaining = SUSPECTS.copy()
    clue_columns = random.sample(CLUE_COLUMNS, len(CLUE_COLUMNS))
    clues_used = 0
    guesses_left = 2

    print("\nCASE FILE 01: THE MISSING MOONSTONE")
    print("At midnight, the Moonstone vanished from Bellweather Museum during a brief blackout.")
    print("The doors were locked, so the thief must be one of the eight guests still inside.")
    print("Your case notes track each guest's motive, alibi, keepsake, and witness.")
    print("Each clue reveals one detail shared by the thief and filters the suspect list.")
    print("Use clues carefully: you have only two accusations before the trail goes cold.")
    print("Commands: clue, suspects, guess <name>, quit")
    print("Example: guess Ada Finch")
    show_candidates(remaining)

    while guesses_left:
        command = input("\nDetective > ").strip()
        action, _, detail = command.partition(" ")
        action = action.lower()

        if action == "quit":
            return "quit", clues_used, guesses_left
        if action == "suspects":
            show_candidates(remaining)
            continue
        if action == "clue":
            if not clue_columns:
                print("No clues remain. Make your accusation.")
                continue
            column = clue_columns.pop(0)
            value = culprit[column]
            remaining = remaining[remaining[column] == value]
            clues_used += 1
            print(f"CLUE: The {column.lower()} clue points to {value}.")
            show_candidates(remaining)
            continue
        if action == "guess":
            guess = detail.strip().casefold()
            if not guess:
                print("Try: guess Ada Finch")
                continue
            if guess == culprit["Suspect"].casefold():
                print(f"Case closed. {culprit['Suspect']} took the Moonstone.")
                return culprit["Suspect"], clues_used, guesses_left
            guesses_left -= 1
            print(f"That accusation doesn't hold. Guesses left: {guesses_left}.")
            continue
        print("I didn't understand that. Use clue, suspects, guess <name>, or quit.")

    print(f"The thief was {culprit['Suspect']}. The Moonstone is still missing.")
    return culprit["Suspect"], clues_used, guesses_left


def main() -> None:
    print("=" * 42)
    print("       THE PANDAS DETECTIVE AGENCY")
    print("=" * 42)
    print("A quiet city, a stolen heirloom, and a trail of small details.")
    print("Solve each case by comparing evidence and narrowing the suspect list.")
    case_log = pd.DataFrame(columns=["Case", "Clues", "Guesses left", "Solved"])
    case_number = 1

    while True:
        culprit, clues_used, guesses_left = play_case()
        if culprit == "quit":
            break

        solved = guesses_left > 0
        case_log.loc[len(case_log)] = [case_number, clues_used, guesses_left, solved]
        case_number += 1
        print("\nCASE REPORT")
        print(case_log.to_string(index=False))
        print(f"Cases solved: {int(case_log['Solved'].sum())}/{len(case_log)}")

        if input("\nOpen another case? [y/N] ").strip().lower() != "y":
            break

    print("\nThe agency is closed. Keep your notes; the city will need you again.")


if __name__ == "__main__":
    main()