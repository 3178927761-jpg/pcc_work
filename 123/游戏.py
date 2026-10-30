"""
康威生命游戏 · 终端版
规则只有三条：
  1. 活细胞周围有 2 或 3 个活邻居 → 继续活
  2. 活细胞邻居 <2（孤独）或 >3（拥挤）→ 死亡
  3. 死细胞周围正好 3 个活邻居 → 复活

用法：
  python life.py            随机开局
  python life.py glider     滑翔机（会斜着一直走）
  python life.py pulsar     脉冲星（周期振荡）
  python life.py rpentomino R五连块（演化 1000+ 代才稳定）
"""

import os
import random
import sys
import time

W, H = 44, 22                 # 棋盘宽、高
ALIVE, DEAD = "#", "."


def blank(w=W, h=H):
    """造一个全空的棋盘（二维列表）"""
    return [[DEAD] * w for _ in range(h)]


def place(board, pattern, top, left):
    """把图案贴到棋盘的指定位置，O 表示活细胞"""
    for dy, row in enumerate(pattern):
        for dx, ch in enumerate(row):
            if ch == "O":
                y, x = top + dy, left + dx
                if 0 <= y < len(board) and 0 <= x < len(board[0]):
                    board[y][x] = ALIVE


def neighbors(board, y, x):
    """数一数 (y,x) 周围 8 格有几个活细胞。边界环绕，避免图案一撞墙就死光"""
    h, w = len(board), len(board[0])
    n = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy or dx:                                  # 跳过自己
                if board[(y + dy) % h][(x + dx) % w] == ALIVE:
                    n += 1
    return n


def step(board):
    """推演一代：按照三条规则生成新棋盘"""
    h, w = len(board), len(board[0])
    new = blank(w, h)
    for y in range(h):
        for x in range(w):
            n = neighbors(board, y, x)
            if board[y][x] == ALIVE:
                new[y][x] = ALIVE if n in (2, 3) else DEAD   # 规则 1、2
            else:
                new[y][x] = ALIVE if n == 3 else DEAD        # 规则 3
    return new


def frame(board, gen, peak):
    """把棋盘渲染成一段文字"""
    w = len(board[0])
    lines = ["+" + "-" * w + "+"]
    for row in board:
        lines.append("|" + "".join(row) + "|")
    lines.append("+" + "-" * w + "+")
    alive = sum(r.count(ALIVE) for r in board)
    lines.append(f"  第 {gen} 代   存活 {alive:4d}   最高 {peak:4d}   （Ctrl+C 退出）")
    return "\n".join(lines), alive


# ---------- 几个经典图案 ----------
PATTERNS = {
    "glider": ["O..",
               ".O.",
               "OOO"],
    "blinker": ["OOO"],
    "block": ["OO",
              "OO"],
    "rpentomino": [".OO",
                   "OO.",
                   ".O."],
    "pulsar": ["..OOO...OOO..",
               ".............",
               "O....O.O....O",
               "O....O.O....O",
               "O....O.O....O",
               "..OOO...OOO..",
               ".............",
               "..OOO...OOO..",
               "O....O.O....O",
               "O....O.O....O",
               "O....O.O....O",
               ".............",
               "..OOO...OOO.."],
}


def use_ansi():
    """判断当前环境能不能用光标控制实现原地动画"""
    if os.environ.get("PYCHARM_HOSTED"):     # PyCharm 的 Run 控制台不认 ANSI
        return False
    if os.name == "nt":
        os.system("")                        # 让 Windows 控制台支持 ANSI
    return sys.stdout.isatty()


def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "random"
    board = blank()

    if name == "random":
        for y in range(H):
            for x in range(W):
                board[y][x] = ALIVE if random.random() < 0.25 else DEAD
    elif name in PATTERNS:
        p = PATTERNS[name]
        place(board, p, (H - len(p)) // 2, (W - len(p[0])) // 2)
    else:
        print(f"未知图案：{name}")
        print("可选：random " + " ".join(PATTERNS))
        return

    ansi = use_ansi()
    if ansi:
        sys.stdout.write("\033[2J")          # 清屏

    gen, peak = 0, 0
    try:
        while True:
            text, alive = frame(board, gen, peak)
            peak = max(peak, alive)
            if ansi:
                sys.stdout.write("\033[H" + text + "\n")   # 光标回左上角重绘
            else:
                sys.stdout.write("\n" + text + "\n")       # 不支持就往下滚
            sys.stdout.flush()

            if alive == 0:
                print("\n所有细胞都死了，游戏结束。")
                break
            gen += 1
            time.sleep(0.15)
            board = step(board)
    except KeyboardInterrupt:
        print(f"\n\n已停止：共演化 {gen} 代，本局最多同时存活 {peak} 个细胞。")


if __name__ == "__main__":
    main()