def count_pairs(numbers, target):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                count += 1
                break
    return count


def main():
    numbers = [1, 2, 3, 4, 5, 5]
    target = 6
    print("数对个数：", count_pairs(numbers, target))


if __name__ == "__main__":
    main()
