def rotate(slovo: str):
    slovo = slovo.strip()
    return slovo[::-1] == slovo

if __name__ == "__main__":
    inp = input('Введите слово: ')
    print(rotate(inp))

