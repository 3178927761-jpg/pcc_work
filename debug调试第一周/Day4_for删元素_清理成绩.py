def remove_failed(scores):
    for score in scores:
        if score < 60:
            scores.remove(score)
    return scores


def main():
    scores = [55, 45, 80, 50, 90]
    print("清理后：", remove_failed(scores))


if __name__ == "__main__":
    main()
