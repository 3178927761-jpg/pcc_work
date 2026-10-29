def digital_root(n):
    while n >= 10:
        total = 0
        while n > 0:
            total = 0
            total += n % 10
            n //= 10
        n = total
    return n


def main():
    for n in [9875, 38, 5]:
        print(n, "->", digital_root(n))


if __name__ == "__main__":
    main()
