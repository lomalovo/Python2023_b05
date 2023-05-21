def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    answer: str = ""
    letters:list[str] = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for letter in message:
        if letter == " ":
            answer += " "
        elif letter == ",":
            answer += ","
        elif letter == ".":
            answer += "."
        elif letter == "-":
            answer += "-"
        elif letter == "'":
            answer += "'"
        else:
            ind: int = letters.index(letter)
            if ind < 26:
                answer += letters[(ind + n) % 26]
            else:
                answer += letters[26 + (ind - 26 + n) % 26]
    return answer