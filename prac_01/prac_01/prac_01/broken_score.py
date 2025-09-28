"""
Classify a score: Invalid / Bad / Passable / Excellent.
"""
def classify(score: float) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"

def main():
    score = float(input("Score: "))
    print(classify(score))

if __name__ == "__main__":
    main()
