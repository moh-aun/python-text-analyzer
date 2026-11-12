
def analyze_text():
    print("=== Simple Text Analyzer ===")

    text = input("Enter some text: ").strip()

    if not text:
        print("Please enter some text.")
        return

    words = text.split()
    sentences = text.count(".") + text.count("!") + text.count("?")

    print("\n--- Analysis Results ---")
    print("Characters:", len(text))
    print("Words:", len(words))
    print("Sentences:", sentences)
    print("Unique words:", len(set(word.lower().strip(".,!?") for word in words)))

    print("\nMost common words:")
    word_counts = {}

    for word in words:
        clean_word = word.lower().strip(".,!?")
        if clean_word:
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

    for word, count in sorted(
        word_counts.items(), key=lambda item: item[1], reverse=True
    )[:5]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    analyze_text()
