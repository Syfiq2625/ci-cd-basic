def is_palindrome(text: str) -> bool:
    """Mengecek apakah sebuah teks adalah palindrom (dibaca sama dari depan/belakang)."""
    # Hilangkan spasi dan ubah ke huruf kecil
    cleaned = "".join(text.split()).lower()
    return cleaned == cleaned[::-1]


def reverse_string(text: str) -> str:
    """Membalik urutan karakter dalam teks."""
    return text[::-1]

# Memicu CI 