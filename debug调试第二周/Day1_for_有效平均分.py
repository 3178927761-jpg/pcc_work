def average_valid(scores):
    total = 0
    count = 0
    for i in range(len(scores)):
        score = scores[i]
        if score is None:
            continue
        count += 1
        total += score
    return total / count


def main():
    all_present = [80, 90, 70, 100]
    with_absent = [80, None, 90, 70]

    print("全部出席：", average_valid(all_present))
    print("有人缺考：", average_valid(with_absent))


if __name__ == "__main__":
    main()
