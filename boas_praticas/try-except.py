try:
    with open("file.txt") as f:
        print(f)
except FileNotFoundError:
    print("O arquivo file.txt não existe")