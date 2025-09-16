# CTF-Repo-Base

A CTF Challenge Automated Build Repository Powered by GitHub Actions

这是一个经过 `LilCTF 2025` 实际使用验证的一种优秀 CTF 赛事题目自动化管理方案，在实际使用过程中，请根据自身需要灵活调整。

## 赛事运维指南

在使用本模板仓库前，请进行以下操作：

1. 启动仓库的 GitHub Action 功能
2. 准备好你的 Docker Registry(如 阿里云 ACR)，并在仓库 Settings - Secrets 添加变量: `ACR_REGISTRY` `ACR_USERNAME` `ACR_PASSWORD` `ACR_NAMESPACE`
3. (推荐) 配置 Branch Protecting Rule，防止出题人对 main 分支的误更改。（需要 GitHub 订阅）

然后请根据自身需要修改出题人指南及各模板文件。

## 出题人指南

**每一道题使用一个完全独立的分支**，总是基于主分支、但不需要向主分支发起 Pull Request。合并建议由赛事运维适时进行，出题人无需关心。**每次在编辑前记得检查一下分支有没有切对**。

新建一道题目时，建议 checkout 到 snapshot，然后使用以下命令创建你的题目分支：

```bash
git branch 你的分支名
git switch 你的分支名
```

然后你就可以在这个分支里上传你的题目了，但请注意以下要求：

**你应该在 `.github/workflows` 文件夹放一个用于在 push 时自动构建 Docker 镜像的配置文件，建议复制 `!challenge-example.yml` 去改**。在你的分支第一次 push 前，务必把所有带 `CHANGE_ME` 字样的地方改掉。

不要忘记 push，将最新的修改同步到远程仓库。

**每次你在本地开始工作前，建议先 `git pull`，确保你的分支是最新的。**

### 要求

- 分支名为方向和题目简称，只包含小写字母、数字、中划线，例如 `misc-check-in`。
- 不要在根目录放任何文件（你正在读的这一份 README.md 除外）。建一个与分支同名的文件夹，所有的文件（包括 `.gitignore` 之类，如果你需要的话）都放在这个文件夹里。
- 除非得到允许，否则不要从任何其他分支 merge 到你的分支。允许 rebase, squash, cherry-pick，但一般情况下每个分支完全独立，不需要做任何合并操作。
- 不要在仓库里存放大于 10MB 的文件，确有必要请提前获得允许。
- Docker 容器注入 flag 的环境变量需要与现有题目保持一致（兼容 `A1CTF_FLAG`、`GZCTF_FLAG`、`FLAG`）

### 建议

以下内容把 snapshot 中已有题目的复制去改一下。

- 使用 <https://github.com/GZCTF/challenge-base> 作为基础镜像，用于简化启动过程的编写，并在不同题目间共用镜像层。（已经出好的用其他基础镜像的题目可以不改。）
- 在题目文件夹中放一个 `README.md`，写明部署信息和其他需要说明的内容。
- 编译产生的二进制文件除非很有必要，否则不要放在仓库里。用 `.gitignore` 忽略掉它们。
- 推荐在 workflow 中作为 artifact 上传：由构建镜像产生的发给选手的附件，例如编译的二进制文件以及 libc 之类的文件，以便附件与远程环境完全相同。
- 不需要换国内源（因为是用 GitHub 的 Action runner 来 build 的）

### 拉镜像

- <https://github.com/settings/tokens/new> 给自己的 GitHub 账号创建一个 Personal Access Token，权限选择 `read:packages`，保存好 token。
- `docker login ghcr.io -u <你的 GitHub 账号> -p <你的 token>`，登录到 GitHub 的 Docker registry。
- `docker pull ghcr.io/xxxx/xxxctf-2025-internal/xxx:latest`
- 自己在本地测的时候，`docker run -d -e '环境变量名=FLAG{this_is_a_test_flag}' -p 宿主机端口:容器内端口 ghcr.io/xxxx/xxxctf-2025-internal/容器名`