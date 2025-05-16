from features import add  # Weitere Module (subtract, multiply...) später ergänzen


def main():
    print("Willkommen zum Mini-Taschenrechner!")
    print("Beispielrechnungen:")

    print(f"2 + 3 = {add.calculate(2, 3)}")
    # Weitere Beispiele folgen, sobald Gruppen ihre Module einfügen


if __name__ == "__main__":
    main()