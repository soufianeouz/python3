import sys

if __name__ == "__main__":
    count = len(sys.argv)
    scores = []

    if count == 1:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        for arg in range(1,count):
            try:
                value = int(sys.argv[arg])
                scores.append(value)
            except ValueError:
                print("Invalid score:", sys.argv[arg])
        if scores:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        else:
            print("No valid scores to calculate stats.")
            