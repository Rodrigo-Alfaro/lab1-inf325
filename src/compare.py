def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def compare_files(file1, file2, file3):
    content1 = read_file(file1)
    content2 = read_file(file2)
    content3 = read_file(file3)

    if content1 == content2 == content3:
        print("All three files have the SAME content.")
    else:
        print("The files have DIFFERENT content.")
        if content1 != content2:
            print(f"{file1} and {file2} differ.")
        if content1 != content3:
            print(f"{file1} and {file3} differ.")
        if content2 != content3:
            print(f"{file2} and {file3} differ.")

if __name__ == "__main__":
    compare_files("nodo1.txt", "nodo2.txt", "nodo3.txt")