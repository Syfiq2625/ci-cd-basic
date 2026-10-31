from analyzer import (
    count_characters,
    count_words,
    count_lines,
    most_common_word
)


def main():
    print("=== TEXT ANALYZER ===")

    text = input("Masukkan teks: ")

    characters = count_characters(text)
    words = count_words(text)
    lines = count_lines(text)
    common_word = most_common_word(text)

    print("\n=== ANALYSIS RESULT ===")
    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Lines: {lines}")
    print(f"Most common word: {common_word}")


if __name__ == "__main__":
    main()