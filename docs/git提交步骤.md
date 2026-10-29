# Git 提交步骤指南

> 适用本机环境：`D:\study` → GitHub 仓库 `pcc_work`
> 更新日期：2026-10-29

---

## 0. 先记住三件事

1. **提交 = 三个动作**：`add`（挑文件）→ `commit`（存快照）→ `push`（送云端）
2. **`add` 和 `commit` 不需要网络**，只有 `push` 需要
3. **`commit` 只到本地**，GitHub 上看不到；必须再 `push`

---

## 1. 你的仓库信息

| 项目 | 值 |
| --- | --- |
| 仓库路径 | `D:\study` |
| 远程地址 | `https://github.com/3178927761-jpg/pcc_work.git` |
| 主分支 | `main` |
| 提交身份 | `3178927761-jpg <3178927761-jpg@users.noreply.github.com>` |
| 凭证方式 | Git Credential Manager（已记住，无需重复输入密码） |

---

## 2. 日常提交（90% 的情况用这套）

```bash
cd /d D:\study

# ① 看现状：哪些文件改了
git status

# ② 把改动加入暂存区
git add .                    # 全部改动
git add ch15_xxx.py          # 或只提交指定文件

# ③ 存快照
git commit -m "feat: 完成第 15 章 15-1 立方数折线图"

# ④ 推到 GitHub
git push
```

**每一步成功的反馈长什么样：**

| 步骤 | 正常输出 |
| --- | --- |
| `git status` | 列出 `modified:` / `Untracked files:`；若干净则显示 `nothing to commit, working tree clean` |
| `git add .` 后再 `git status` | 文件从红色变为绿色，出现在 `Changes to be committed:` 下 |
| `git commit` | `[main 7de06ee] feat: ...` 加一行 `1 file changed, 20 insertions(+)` |
| `git push` | `911ec24..7de06ee  main -> main` |

---

## 3. 提交信息怎么写

**格式：`<类型>: <做了什么>`**

| 类型 | 用于 |
| --- | --- |
| `feat` | 新增功能或练习 |
| `fix` | 修复 bug |
| `docs` | 文档改动 |
| `refactor` | 重构（不改变功能） |
| `chore` | 杂项（配置、依赖、清理） |

**好的写法：**

```text
feat: 完成第 15 章 15-1 立方数折线图
fix: 修正 ch07_while.py 的无限循环
docs: 更新 README 学习进度
```

**坏的写法：** `修改`、`更新`、`1`、`asdf`

**判断标准：三个月后的你，只看这一行能不能想起改了什么。**

---

## 4. 提交前自检（30 秒）

```bash
git status          # ① 有没有不该提交的文件混进来？
git diff            # ② 具体改了哪几行？
git diff --cached   # ③ 暂存区里到底是什么内容？
```

**永远不要提交：**

| 内容 | 原因 |
| --- | --- |
| `.venv/` | 几千个第三方库文件，仓库会瞬间臃肿 |
| `__pycache__/` | Python 自动生成的字节码，可随时重建 |
| `.idea/` | IDE 个人配置，只对你这台机器有意义 |
| 密码 / Token / 密钥 | 一旦推到公开仓库，几秒钟内就会被爬虫抓走 |

以上已写在 `.gitignore` 里。**新增文件后务必 `git status` 扫一眼**，确认没有意外进入。

---

## 5. 常见情况处理

| 情况 | 命令 |
| --- | --- |
| 漏了文件，想补进上一次提交 | `git add 漏掉的文件` → `git commit --amend --no-edit` |
| 提交说明写错了 | `git commit --amend -m "新说明"` |
| 撤销上次提交但保留改动 | `git reset --soft HEAD~1` |
| 丢弃某文件的未提交改动 | `git restore 文件名` |
| 已提交的文件想移出版本控制（保留本地） | `git rm --cached 文件名`，并加进 `.gitignore` |
| 改到一半要临时切去做别的 | `git stash` → 回来后 `git stash pop` |
| `push` 被拒绝（远程有本地没有的提交） | `git pull --rebase` → 再 `git push` |
| 查看提交历史 | `git log --oneline --graph --all` |

> ⚠️ `git reset --hard` 和 `git push --force` 会**丢数据**，新手阶段先别碰。

---

## 6. PyCharm 图形操作对照

| 命令行 | PyCharm 操作 |
| --- | --- |
| `git status` | 左侧 Project 树看文件颜色：**蓝**=改过、**红**=未跟踪、**绿**=新增 |
| `git diff` | 选中文件按 `Ctrl+D` |
| `git add` | Commit 面板里**勾选**文件 |
| `git commit -m` | `Ctrl+K` → 写说明 → 点 **Commit** |
| `git push` | `Ctrl+Shift+K` |
| `git log` | 底部 **Git** 标签 → Log |
| `git restore` | 右键文件 → Git → Rollback |

> ⚠️ **Commit 和 Push 是两个按钮。** 只点 Commit，GitHub 上不会有任何变化。

---

## 7. 分支与合并（进阶）

```bash
git switch -c practice/ch15      # ① 建并切到新分支
# 在新分支上改代码……
git add . && git commit -m "feat: 第 15 章练习"
git switch main                  # ② 切回主分支
git merge practice/ch15          # ③ 合并进来
git push                         # ④ 推送主分支
```

**分支的意义：在分支上折腾，主分支永远是能跑的版本。**

---

## 8. 网络问题应急（本机已知问题）

`github.com:443` 时通时断（DNS 解析被污染，会返回一堆无关 IP）。典型报错：

```text
fatal: unable to access '...': Failed to connect to github.com:443 after 21513 ms
```

### 办法一：重试（多数情况第 2~5 次能成功）

```powershell
for ($i = 1; $i -le 8; $i++) {
    git -C D:\study push
    if ($LASTEXITCODE -eq 0) { "推送成功"; break }
    "第 $i 次失败，等 10 秒重试……"
    Start-Sleep -Seconds 10
}
```

### 办法二：改用 SSH（推荐，配一次永久有效）

实测 `ssh.github.com:443` 稳定可用，而被掐的是 `github.com:443`。

**① 生成密钥**（一路回车，不设密码短语）：

```bash
ssh-keygen -t ed25519 -C "3178927761-jpg"
```

**② 写 `~/.ssh/config`：**

```text
Host github.com
  HostName ssh.github.com
  Port 443
  User git
```

**③ 添加公钥**：把 `~/.ssh/id_ed25519.pub` 的内容粘贴到
GitHub → Settings → SSH and GPG keys → New SSH key

**④ 验证：**

```bash
ssh -T git@github.com
# 期望输出：Hi 3178927761-jpg! You've successfully authenticated...
```

**⑤ 把仓库远程地址切换为 SSH：**

```bash
git -C D:\study remote set-url origin git@github.com:3178927761-jpg/pcc_work.git
```

---

## 9. 命令速查表

| 目的 | 命令 |
| --- | --- |
| 查看状态 | `git status` |
| 查看具体改动 | `git diff` |
| 暂存全部改动 | `git add .` |
| 提交 | `git commit -m "说明"` |
| 推送到 GitHub | `git push` |
| 从 GitHub 拉取 | `git pull` |
| 查看历史 | `git log --oneline --graph` |
| 撤销工作区改动 | `git restore 文件` |
| 取消暂存 | `git restore --staged 文件` |
| 撤销上次提交（保留改动） | `git reset --soft HEAD~1` |
| 临时保存改动 | `git stash` / `git stash pop` |
| 新建分支 | `git switch -c 分支名` |
| 切换分支 | `git switch 分支名` |
| 合并分支 | `git merge 分支名` |
| 查看远程地址 | `git remote -v` |

---

## 每天收工三件事

```bash
git add .
git commit -m "feat: 今天的说明"
git push
```
