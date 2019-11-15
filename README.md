# Git Started

## Story

What does Git mean? It stands for "global information tracker": when you're in a
good mood, and it actually works for you. Angels sing, and a light suddenly
fills the room. Or "goddamn idiotic truckload of sh*t": when it breaks.

This was actually a quote from Linus Torvalds, the creator of Linux and
the Git version control system. Torvalds also said that since he is an
egotistical bastard, he named this another child of his after himself, too:
the word 'git' is a British slang for 'an unpleasant or contemptible
person'. Well, Git has a reputation of being obscure and hard to use.

We hope you'll find it not _that_ hard; it is just a tool created by
developers for developers: it has a really bad UX, but at the end of the
day it is the Swiss Army knife of source code management. The best strategy
is to use it a lot, and we recommend you to read a good book about it later on.

All the projects in Codecool are handled under Git, and this project
covers the necessary basics of Git usage.

## What are you going to learn?

- clone a remote repository from GitHub,
- add and modify files,
- create commits,
- handle excluded files,
- and push the result back to the remote server.

**This is what you need to do with every project in the future.**

## Tasks


1. Follow this link to create your project repository: https://classroom.github.com/a/eYB2Fw7c

    - The repository is created under `https://github.com/CodecoolGlobal` with the name `git-started-<username>`.

2. Clone the repository under a `projects` folder on your computer (which can be anywhere in your user's home space)!

    - The repository is cloned into `projects/git-started-<username>`.

3. Add a `.gitignore` file that skips the `temp` folder and all the files with `tmp` extension! Commit this new file! Remember writing meaningful and well formed commit messages!

    - File `.gitignore` is added with the second commit (the first is the original "Initial commit").
    - Git filters for `temp` and the `tmp` extension.
    - The commit message is meaningful.
    - The commit message has coherent form and style (e.g. "Fix broken link on contact page").
    - There is no typo in the commit message.

4. Create a folder named `data` and a file `lorem.txt` in it. Add the first sentence of "Lorem Ipsum" into the file, then commit.

    - New file `data/lorem.txt` gets added to the repo with the third commit.
    - The content is as expected, the first sentence of "Lorem Ipsum".
    - The commit message is meaningful.
    - The commit message has coherent form and style (e.g. "Fix broken link on contact page").
    - There is no typo in the commit message.

5. Add a folder named `temp` and copy `lorem.txt` in it. If you've written the `.gitignore` file properly, it will not get committed later.

    - There is a `lorem.txt` file in the `temp` folder in the working directory.

6. Add the next 3 sentences of "Lorem Ipsum", each one in separate lines, to `data/lorem.txt`, and commit!

    - The 4th commit adds 3 lines to `data/lorem.txt`.
    - The file contains the first four sentences of "Lorem Ipsum".
    - The commit message is meaningful.
    - The commit message has coherent form and style (e.g. "Fix broken link on contact page").
    - There is no typo in the commit message.

7. Rename `data/lorem.txt` to `data/lorem_ipsum.txt`, and commit!

    - The 5th commit replaces `data/lorem.txt` with `data/lorem_ipsum.txt`.
    - The commit message is meaningful.
    - The commit message has coherent form and style (e.g. "Fix broken link on contact page").
    - There is no typo in the commit message.

8. Push all the above changes to GitHub!

    - All the 5 commits are on GitHub.

9. [OPTIONAL] Check your commit history on GitHub. Create a `git-history.txt` file that includes the commit hash of each commit. Add the new file, commit, and push.

    - A new file named `git-history.txt` is added to the repository.
    - This file contains the 5 earlier commit hashes.


## General requirements


 - You need to have Git installed (check `git --version` on your system), otherwise visit [this page](https://git-scm.com/downloads).

## Background materials

- :exclamation: https://learn.code.cool/codecool-graph/#/../pages/git/git-basics
- :lollipop: Git's [original introduction](https://github.com/git/git/blob/e83c5163316f89bfbde7d9ab23ca2e25604af290/README) by Linus Torvalds
- :exclamation: [Git home page](https://git-scm.com/)
- :exclamation: About [nice commit messages](https://chris.beams.io/posts/git-commit/)
- :open_book: A comprehensive and free [Git book](https://git-scm.com/book/en/v2)
- :lollipop: [.gitignore generator](http://gitignore.io/)
- :lollipop: [Lorem Ipsum generator](https://loremipsum.io/)