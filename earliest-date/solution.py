def main():
    n = int(input())
    dates = []
    for _ in range(n):
        s = str(input())
        dates.append(s)
    dates.sort()

    print(dates[0])

if __name__ == '__main__':
    main()