## Counts Number of lines , Word & Characters

if __name__ == '__main__':
    with open("D:\\Learning Hub\\Programming\\Python Programs\\College\\file.txt", "r") as file:

        lines = file.readlines()
        numberOfLines = len(lines)
        numberOfWords = sum(len(line.split()) for line in lines)
        numberOfCharacters = sum(len(line) for line in lines)  # Counting characters including spaces and newlines

    print(f"Lines: {numberOfLines}")
    print(f"Words: {numberOfWords}")
    print(f"Characters: {numberOfCharacters}")
