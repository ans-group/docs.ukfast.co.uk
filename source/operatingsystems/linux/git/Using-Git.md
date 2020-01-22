# Using Git

##SETUP

Firstly, you will need to have installed git on your local machine.

Set your name and email address using the following commands, commits are associated by these credentials:

```bash
git config --global user.name "Support"
git config --global user.email support@ukfast.co.uk
```
### CLONING REPO'S


To start using a public repository, you can clone a repo to your local machine using either https or ssh. To get the full path navigate to the repo in github or gitlab.

```bash
git clone https://github.com/path/to/repo
```


```bash
git clone ssh://user-name@github.com/path/to/repo.git
```

### Git ADD, COMMIT AND PUSH 


Once you have made a change to the source code in your repos directory, use the git add command 

```bash
git add .           # add's all changed files
git add filename    # add's only specified file
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


### CHECK YOUR CHANGES 

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

### BRANCHES


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

Use git diff to show us the changes:

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

### PULLING 

Use git pull to fetch and incorporate changes from the remote repository into your current branch.

```bash
git pull
```

Although git is very good at combining multiple changes, running a git pull can sometimes result in merge conflicts depending on how far behind your branch is :

```bash
Auto-merging example2.txt
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

If you open the offending file in a text editor, you’ll find an indication of the bits that are different, something like this:

```bash
<<<<<<< HEAD
hello world
=======
Hello World!
>>>>>>> 031389f2cd2acde08e32f0beb084b2f7c3257fff
```

Edit the bits from <<<<<<< to >>>>>>>, to make the file just as you want it.

Then the usual add, commit, push:

```bash
git add -A (add all files/changes to files)
git commit -m "Fix merge conflicts"
git push
```
