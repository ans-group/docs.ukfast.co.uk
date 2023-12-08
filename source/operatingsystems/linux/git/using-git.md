# Using Git

### Setup

Firstly, you will need to have installed `git` on your local machine.

Set your name and email address using the following commands, commits are associated by these credentials:

```bash
git config --global user.name "Support"
git config --global user.email support@ukfast.co.uk
```

### Cloning a repo

To start using a public repository, you can clone a repo to your local machine using either `HTTPS` or `SSH`. To get the full path navigate to the repo in GitHub or GitLab.

```bash
git clone https://github.com/path/to/repo
```

```bash
git clone ssh://user-name@github.com/path/to/repo.git
```

### Git add, commit and push

Once you have made a change to the source code in your repos directory, use the `git add` command

```bash
git add .           # adds all changed files
git add filename    # adds only specified file
git add *           # wildcard, used for *.txt
```

Commit changes as often as possible and provide useful commit messages for the community

```bash
git commit -m "Updated README.md"
```

When you are ready to publish your new code, push it to the remote repo specifying the remote branch:

```bash
 git push origin master
```

### Check your changes

It's very important to know what you are committing and make sure what you think you are pushing is what you will push to the remote branch :

Git status checks working tree status - that is which files can be committed

```bash
git status
```

```bash
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#       new file:   .gitignore
#       new file:   example2.txt
#
```

Git diff does a comparison of the files in your repo since the last commit, and shows the differences

```bash
git diff
```

```bash
diff --git a/example2.txt b/example2.txt
index e69de29..3b18e51 100644
--- a/example2.txt
+++ b/example2.txt
@@ -0,0 +1 @@
+hello world
```

### Branches

Ideally you would never be pushing to the master branch directly and instead branching off from the master committing and pushing your changes then merging back to the master branch.

 Check existing branches

```bash
git branch -a
```

Create a new branch and switch to it

```bash
git branch newbranch
git checkout newbranch
```

You can then push the new branch to the repo instead of to the master branch 

```bash
git push origin newbranch
```

First switch back to the master branch

```bash
git checkout master
```

Use `git diff` to show us the changes:

```bash
git diff master newbranch
```

Once we're happy we can merge the changes and push the changes

```bash
git merge newbranch
```

```bash
git push origin master
```

### Pulling

Use `git pull` to fetch and incorporate changes from the remote repository into your current branch.

```bash
git pull
```

Although Git is very good at combining multiple changes, running a `git pull` can sometimes result in merge conflicts depending on how far behind your branch is:

```bash
Auto-merging example2.txt
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

If you open the offending file in a text editor, you'll find an indication of the bits that are different, something like this:

```bash
<<<<<<< HEAD
hello world
=======
Hello World!
>>>>>>> 031389f2cd2acde08e32f0beb084b2f7c3257fff
```

Edit the bits from `<<<<<<<` to `>>>>>>>,` to make the file just as you want it.

Then the usual `add`, `commit`, `push`:

```bash
git add -A (add all files/changes to files)
git commit -m "Fix merge conflicts"
git push
```

### Forking

When you don't have permission to push to a repository directly, you will likely want to Fork the repository and start a new pull request to apply your suggested changes. Typically this would need to be approved before being merged into the original branch.

First look at the currently configured remote repositories

```bash
git remote -v
origin  https://github.com/path/to/repo.git (fetch)
origin  https://github.com/path/to/repo.git (push)
```

Now we will specify a new remote repository, we will call it `upstream`

```bash
git remote add upstream https://github.com/path/to/origional/repo.git
```

Have a look at the now configured remote repositories

```bash
git remote -v
origin  https://github.com/path/to/repo.git (fetch)
origin  https://github.com/path/to/repo.git (push)
upstream  https://github.com/path/to/origional/repo.git (fetch)
upstream  https://github.com/path/to/origional/repo.git (push)
```

Now we will fetch respective commits from the `upstream/master`

```bash
git fetch upstream
> remote: Counting objects: 75, done.
> remote: Compressing objects: 100% (53/53), done.
> remote: Total 62 (delta 27), reused 44 (delta 9)
> Unpacking objects: 100% (62/62), done.
> From https://github.com/path/to/origional/repo.git
>  * [new branch]      master     -> upstream/master
```

On your local `master` branch

```bash
git checkout master
```

Merge the commits from the `upstream/master`, this will leave all local changes untouched.

```bash
git merge upstream/master
Merge made by the 'recursive' strategy.
 path/to/changed/file.md | 148 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 path/to/another/changed/file.md  |   1 +
 2 files changed, 149 insertions(+)
 create mode 100644 path/to/changed/file.md
```

Remember to push your changes to your remote `origin`

```bash
git push origin
```

```eval_rst
  .. title::  Using Git
  .. meta::
     :title:  Using Git | ANS Documentation
     :description: An advanced guide on basic git commands
     :keywords: ukfast, linux, install, centos, cloud, server, virtual, git, eCommerce, branch, fork, merge, gitlab, devops, github
```
