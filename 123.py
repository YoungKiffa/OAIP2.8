def main():
    # 1 zadanie
    word = input().split()
    print(*list(map(lambda x: x.rjust(len(max(word, key=len)), "*"), word)), sep="\n")


if __name__ == "__main__":
    main()
