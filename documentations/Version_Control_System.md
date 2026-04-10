# Version Control System Basics Documentation

A comprehensive beginner-friendly guide to understanding the fundamentals of Version Control System.

---

## Version Control System (VCS)
Software that records changes to files or projects over time, allowing individuals or teams to track, compare, and revert to previous versions. 

It acts as a project history manager, enabling multiple collaborators to work on the same codebase simultaneously without overwriting each other's work.

---

## Components of Version Control Systems
Version Control Systems work using a few core concepts that help teams manage code changes and collaborate efficiently.

* **1. Repository:** A Central location that stores all project files along with their complete change history and metadata like author and commit message.

* **2. Revision:** A specific saved version of a file or project, identified using a unique ID such as a hash or number.

* **3. Branch:** A separate copy of the codebase used to develop features or fix bugs without affecting the main code.

* **4. Merging:** The process of combining changes from one branch into another, which may sometimes require resolving conflicts.

* **5. Commit:** A snapshot of changes made to the codebase at a specific time, used to track and manage project history.

---

## Local Version Control Systems (Local VCS)
A Local Version Control System LVCS stores all project versions on a single computer and is mainly used by one user without remote collaboration.

**Characteristics:**
- No internet or server dependency
- Useful for individual projects
- Limited to single-user environments.

---

## Centralized Version Control Systems

In a Central Version Control System, all the files and their version history are stored in a single central server. Developers connect to this server to access or modify files.

* **Update/Checkout:** A developer retrieves the latest version of the files from the central server.
* **Make Changes:** The developer works on the files.
* **Commit:** The developer saves (commits) the changes directly back to the central server, making them immediately available to everyone else.

* **Pros**
   - Enables collaboration among multiple developers through a central repository.
   - Provides visibility into project activities and changes.
   -  Allows fine-grained access control for administrators.

* **Cons**
   - Has a single point of failure because everything depends on the central repository.
   - If the server goes down, developers cannot collaborate or commit changes.

---

## Distributed Version Control Systems

A Distributed Version Control System allows each developer to have a local repository along with a working copy of the project. Changes made in the local repository are not automatically visible to others.

* **Commit:** Saves changes to the local repository, visible only to the developer.

* **Push:** Uploads committed changes to the central/shared repository so others can access them.

* **Pull:** Downloads changes from the central repository to the local repository.

---

## Git
Git records what changed, when it changed, who changed it, and even where it happened.
Git is a powerful tool that constantly keeps track of every change you make to your files. Now, what kind of files are we talking about? Almost any kind, not just code. It could be anything like an image, a text file, codes using languages like Python, JavaScript, PHP, videos, images, etc. and manages each change, like:
* Which line was edited?
* When it was done?
* By whom?

---

## 3 Stages of Git

* **Working Directory:** Where we currently see and edit our files.
* **Staging Area(Index):** A "prep zone" where we pick and choose which changes to include in our next commit.
* **Local Repository:** Where Git permanently saves the snapshots (commits) on our computer.

---

## Important Key Points of Git

* Git saves and tracks multiple versions of the same file.
* Git is also known as a Version Control System.
* Linus Torvalds created git.
* We can use Git to keep track of changes and maintain different versions of almost any file or code safely stored.
* GitHub is now owned by Microsoft and is maintained with great care and attention, especially in the programming community.

---

## Difference between Git and GitHub:

* **Git** is a tool that runs locally on our computer system. It tracks all the changes to your file and manages all your files and code, and keeps everything organized.

* **GitHub** acts as that central online server where your team’s entire project lives, making it easy for everyone to see, edit and share updates in one single place without any confusion.

* **GitHub** is mainly divided into two major parts: Local (refers to our own computer) and Remote (lives in the cloud, it’s where we push or upload our local work).

* `Local to Remote` → Store code to Remote
* `Remote to Local` → Pull code to Local

* In a **local computer**, the folder where we are working on a project is called the **working directory**. This is where all the actions happen like writing code, creating new files and modifying existing code. When our project looks good and is working properly, save the changes. Then, move to the next step, **Stage**.

* **Stage meaning** → Alright, my changes are ready – They can move to the next step. Staging is the 2nd step in our **Local Git’s Workflow**. Thinking of the staging area as a middle ground where all the files are saved and sits between the working directory and the local repository. 

* **Local Repository:** Once we are confident about our work, we commit it. Committing means permanently storing and saving those changes to our local repository. Locking up about the recorded version of our project’s history.

---

## Repository

A Repository is a place where all the versions of your files and their complete change history are stored.

* **1. Version Control (Code) Repositories:** Used by developers to store project files and their complete revision history.
   - **Local Repository:** Stored on an individual's computer for personal work.
   - **Remote Repository:** Hosted on a server like GitHub to allow team collaboration.

* **2. Data Repositories:** Centralized locations for database, ofter used in business intelligence or scientific research for reporting and analysis.

* **3. Software Package Repositories:** Host compiled libraries and dependencies that other programs can download and use (e.g., npm for JavaScript or PyPI for Python).

In software architecture, a Repository is also a design pattern. It acts as an abstraction layer between an application's business logic and its data storage (like a database).
* **Meditation:** It treats the database like an in-memory collection of objects.
* **Decoupling:** By using an interface, developers can swap the underlying data source (e.g., moving from SQL to NoSQL) without changing the main application code.

---

## .gitignore

**What is .gitignore?**
- It is used to ignore files that should not be tracked by Git.
- It prevents committing unnecessary files like dependencies, logs, etc. or sensitive data like API Keys/passwords to source control.

**Example:** node_modules/, .env, .log files

* **Location of .gitignore:** Placed at the root of the repository, through subdirectories can have their own.

---

## git push
- Sending local changes to the remote
- This makes our work accessible to other team members and services as a cloud backup.
```bash
git push origin <branch-name>
```

* **Push All Branches**
Sends all our local branches to the remote at once.
```bash
git push --all
```

* **Push Tags**
Uploads any release tags like v1.0 that aren't sent during a normal push.
```bash
git push --tags
```

* **Force Push**
Overwrites the remote history with our local repository. Use this with extreme caution as it can delete teammate's work.
```bash
git push --force
```

---

## git fetch

- Bringing remote changes into your local repository, but not automatically merging them yet.
- This makes it a "safe" command because it lets you see what others have done before we decide to integrate it.

```bash
git fetch origin
```

**Why use git fetch?**
* **Safety:** Unlike `git pull`, which immediately tries to merge changes and can cause merge conflicts, `git fetch` only updates our remote tracking branches (e.g., origin/main)
* **Previewing:** We can inspect the new commits using `git log` or compare them to our current work using `git diff` before merging.
* **Stay Updated:** It informs us if our local branch is "ahead" or "behind" the remote version.

* **Useful Variants:**
* Fetch All Remotes
```bash
git fetch -all
```

* Fetch a specific branch
```bash
git fetch origin <branch-name>
```

* Clean Up
```bash
git fetch --prune
```

---

## git merge

- git merge is the command used to combine two or more development histories - typically different branches - into a single branch. 
- It is the primary tool for integrating work, such as a completed feature branch, back into the main codebase.

**Core Merging Process**
* Switch to the target branch
```bash
git checkout main
```

* Pull latest updates
```bash
git pull origin main
```

* Execute the merge
```bash
git merge feature-branch
```

**Common Merge Types**
* *Fast-Forward Merge:* Occurs if the target branch has no new commits since we branched off. Git simply moves the pointer forward to the latest commit of the source branch.

* *Three-way (Recursive) Merge:* Occurs when both branches have diverged with their own new commits. Git creates a new merge commit to tie the histories together.

* *Squash Merge:* Combines all commits from the source branch into a single commit on the target branch, keeping the history cleaner.
```bash
git merge --squash <branch-name>
```

**Merge Conflicts**

Conflicts happens when
* same file
* same codes 
* Modified differently in two or more branches

**Handling Conflicts**

If the same lines in a file were changed in both branches, Git will pause the merge and report a merge conflict.

* *Identify:* Run `git status` to see unmerged files.
* *Resolve:* Open the files and manually choose between the changes marked by conflict markers (<<<<<<< HEAD, =======, >>>>>>>).
* *Complete:* After fixing, stage the changes with `git add <file>` and run `git commit` to finish.
* *Abort:* If the conflict is too messy, use `git merge --abort` to return to the pre-merge state.

**Abort Merge**

* Restore branch to pre-merge states
```bash
git merge --abort
```

| Command                           | Purpose                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------- |
| `git merge --no-ff <branch>`      | Forces a merge commit even if a fast-forward is possible (preserves history). |
| `git merge --no-commit <branch>`  | Merges changes but stops before creating the final commit for review.         |
| `git merge --continue`            | Resumes a merge after manual conflict resolution.                             |
| `git log --graph --oneline --all` | Visualizes your branch history and merges.                                    |

---

## git pull

* `git pull` is a command used to update the local version of a repository with changes from remote repository such as GitHub. 
* It ensures the local environment is synchronized with the latest work from our team.
* **Fetching + merging** - so, your working directory immediately reflects the remote changes.
* **git pull** = **git fetch** + **git merge**
   - *git fetch* - It downloads the latest commits, files, and branches from the remote repository into local "remote-tracking" branches. (e.g., origin/main)
   - *git merge* - It immediately integrates those downloaded changes into current active local branch.

**Common Variations**
* Pull updated for the current branch from its tracked remote counterpart.
```bash
git pull
```

* Specially pull changes from a named branch (like main or develop) on the origin remote.
```bash
git pull origin <branch_name>
```

* Instead of merge, it "replays" local commits on top of the newly fetched remote changes. These results in a cleaner, linear history without "merge commits".
```bash
git pull rebase
```

**Why use it?**
* *Stay Updated:* Running it regularly prevents you from working on outdated code.
* *Avoid Conflicts:* Pulling before you start new work—and especially before you git push—helps you identify and resolve merge conflicts early.
* *Collaboration:* It is the primary way to receive contributions made by others.

**Difference from Git fetch**
- While `git pull` automatically merge changes, `git fetch` only downloads them.
- Developers often prefer using `git fetch`, first to review changes before safely deciding to merge them manually.

---

# git remote

- A `git remote` is a reference or "bookmark" to a version of our project hosted elsewhere, typically on a server like GitHub. 
- While our local repository is our private workspace, remotes allows us to collaborate with others by syncing changes between different versions of the same project.

```bash
git remote
```

| **Command**                     | **What it does**                                                               |
| ------------------------------- | ------------------------------------------------------------------------------ |
| `git remote -v`                 | Shows all linked remotes along with their fetch and push URLs.                 |
| `git remote add <name> <url>`   | Adds (connects) a new remote repository to your local repo.                    |
| `git remote show <name>`        | Displays detailed information about a specific remote, including its branches. |
| `git remote rename <old> <new>` | Renames an existing remote.                                                    |
| `git remote remove <name>`      | Removes (unlinks) a remote from your local repository.                         |

**Why use remotes?**
* *Collaboration:* Multiple people can work on the same codebase simultaneously.
* *Backup:* If our local machine fails, our work is safely stored on the remote server.
* *Deployment:* Web servers can pull code from a remote to go live with new updates.

---

## git stash
`git stash` is a command used to temporarily save uncommitted changes in our working directory so we can switch to a different task without committing incomplete work.

**Why use it?**
* *Context Switching:* If we are mid feature and need to fix an urgent bug on another branch, we can stash our current work, switch branches, and fix the bug without losing progress.

* *Cleaner Pulls:* Stash our local changes before running `git pull` to avoid merge conflicts with incoming code.

* *Experimental Code:* Use it as a safety net to save a version of our code before trying something risky.

**Key Commands**
* Saves all tracked, modified files and stages to a nre stash entry.
```bash
git stash
```

OR 

```bash
git stash push
```

* Display all stashes we have saved, ordered by index
```bash
git stash list
```

* Reapplies the changes from the stash to our current branch but keeps the stash in the list
```bash
git stash apply
```

* Reapplies the changes and removes the stash from the list
```bash
git stash pop
```

* Permanently deletes a specific stash from the list
```bash
git stash drop stash@{n}
```

* Deletes all stashed changes in the repositories
```bash
git stash clear
```

**Important Options**
**1. Stash Untracked Files:**
```bash
git stash -u
```

**2. Stash with a message:**
```bash
git stash push-m "message"
```

**3. Stash Specific Files:**
```bash
git stash push path/to/file
```

---

# git diff

- The `git diff` command is a powerful tool used to compare changes between different states of a repository, such as the working directory, staging area, commits, and branches.
- It outputs the exact lines that have been added, removed, or modified.

**Core Commands**
* Displays changes in our working directory that have not yer been staged
```bash
git diff
```

* Shows changes that are staged and ready for the next commit but not yet saved in history
```bash
git diff --staged
```

* Show all local changes - both staged and unstaged - compared to our last commit
```bash
git diff HEAD
```

* Compares differences between two specific commits using their hashes
```bash
git diff <commit1><commit2>
```

**Understand the Output**

* Git uses a "unified diff" format to display changes: 
  - **File Headers:** Indicates which files are being compared (e.g., a/file.txt and b/file.txt).
  - Hunk Header (@@ -1,3 +1,5 @@):** Summarizes where changes occur. The numbers indicate the starting line and the number of lines shown for the original (-) and modified (+) versions.

**Prefixes:**
- *- (Red):* Lines removed from the first version.
- *+ (Green):* Lines added to the second version.
- *(Space):* Context lines that remain unchanged

**Useful Options**

* **--stat:** Provides a summary of changes, including a list of modified files and the number of insertions/deletions for each.
* **--word-diff:** Highlights changes at the word level rather than the entire line, making it easier to spot small edits.
* **--name-only:** Lists only the names of files that have changed.
* **git difftool:** Opens an external graphical diff tool (like VS Code, Beyond Compare, or Vimdiff) to view changes side-by-side.

---

## git reset

- `git reset` is a powerful command used to undo changes by moving our current branch to a specific commit. 
- It essentially lets travel back in time to a previous state of project.

**Three main modes**
| Mode      | What it does?                        | Best for                          |
|-----------|--------------------------------------|-----------------------------------|
| `--soft`  | Keeps changes staged                 | Squashing commits                 |
| `--mixed` | Unstages changes (default)           | Re-selecting changes              |
| `--hard`  | Deletes all local changes            | Resetting to clean state          |

---

## git branch

- In Git, a `branch` is essentially a lightweight, moveable pointer to a specific commit in project's history.
- It allows us to diverge from the main line of development to work on new features, bug fixes or experiments without affecting the stable main code.

**Why use Branches?**
* **Isolation:** Changes made on one branch do not affect others until you choose to merge them.
* **Parallel Development:** Multiple team members can work on different tasks simultaneously without interfering with each other's work.
* **Safe Experimentation:** You can test new ideas in a separate branch and simply delete it if they don't work out.

**Essential Git Branching Commands**
* Create a new branch
```bash
git branch <name>
```

* Switch to a branch
```bash
git switch <name>
```

* Create and Switch in one step
```bash
git switch -c <name>
```

* List all branches
```bash
git branch
```

* Merge a branch into current
```bash
git merge <name>
```

* Delete a merged branch
```bash
git branch -d <name>
```

* Delete an unmerged branch
```bash
git branch -D <name>
```

---

## git help

git help is your built-in documentation system inside Git. It helps you understand commands, options, and usage without leaving the terminal.

```bash
git help
```

It shows a list of:
- Common Git commands (clone, commit, push, etc.)
- Available subcommands
- General guidance on how to use Git

**Types of Help Outputs**
| Command              | Output Type  | Use Case             |
| -------------------- | ------------ | -------------------- |
| `git help`           | Command list | Explore Git commands |
| `git help <command>` | Full manual  | Deep understanding   |
| `git <command> -h`   | Short help   | Quick reference      |

---

## git revert

- git revert is used to undo a commit safely without deleting history
- Creates a new commit that undoes the previous commit
- Safe for shared branches
- Does not rewrite history

**What git revert does?**
```bash
git revert <commit_id>
```

- It creates a new commit that reverses the changes of a previous commit
- Your history stays intact (nothing is deleted)

**Difference between revert vs reset**

| Feature        | `git revert`        | `git reset`           |
| -------------- | ------------------- | --------------------- |
| History        | Preserved           | Rewritten             |
| Safe for team  | Yes                 | No (can break others) |
| Creates commit | Yes                 | No                    |
| Use case       | Undo changes safely | Fix local mistakes    |

---

## git rm

Remove files from:
- Working Directory
- Staging Area

```bash
git rm file.txt
git commit -m "Remove file"
git push origin <branch_name>
```

--- 

## git mv

Moves or renames files and stages change automatically.

```bash
git mv old.txt new.txt
```

---

## git show

Shows the detailed information about:
- a commit
- a tag
- a file at specific commit

```bash
git show
```

---

## git checkout

- For switching branches

```bash
git checkout main
```

- For restoring files
- For checking out commits

```bash
git checkout ---file.txt
```

---

## Amend Commit

- Modifies the last commit

```bash
git commit --amend
```

---

## Key Terminologies in GitHub

---

### 1. Repository

* A **Repository** is a place where we can store our complete code, their changes and their history.
* Once we are confident about our work, we commit it.
   - Which means we permanently stored and saving codes and their changes to local repository.

---

### 2. Star

* Bookmarking a repository on GitHub
* Shows appreciation to our project
* Helps in saving and quickly find useful resources/repositories.

---

### 3. Issues 

* Used to track tasks
* Requesting features
* Used for reporting bugs
* Assigning tasks to contributors
* Managing workflows

---

### 4. Snapshot

* Git does not store files as changes
* Git stores a snapshot of the entire project as a commit
* **snapshot** points to a tree contains metadata (like author, message, time)

---

### 5. SHA

* Common hash (SHA-I hash) - 40-character hexadecimal string
* Each git object has a unique ID based on:
   - file contents
   - Parent commit
   - Identifies commit uniquely

---

### 6. HEAD

* Pointer to the current branch reference
* HEAD → main → latest commit
* Normal HEAD → Points to branch
* Detached HEAD → points to commit directly

* If we checkout to a specific commit 
```bash
git checkout <commit>
```
Now, HEAD points to that specific commit.

---

### 7. README.md

A README.md file is the main documentation file of a repository.

It usually contains: 
- Project Name
- Description
- Installation Steps
- Usage instructions
- Technologies used
- Author information

It helps anyone understand:
- What does the project do?
- How to run it?
- How to contribute?

---

### 8. git reset

Moves branch pointer

**1. Soft Reset**
- Moves Head
- Keeps changes unstaged
- Does not touch working directory

```bash
git reset --soft HEAD~1
```

**2. Mixed Reset**
- Keeps working directory
- Moves Head
- Unstaged changes

```bash
git reset HEAD~1
```

**3. Hard Reset**
- Deletes staged changes
- Moves HEAD
- Deletes working directory changes

```bash
git reset --hard HEAD~1
```

---

### 9. git cherry-pick

Applies a specific commit from one branch onto other branch.

```bash
git checkout feature-payment
```
- on branch feature-payment (switching)

```bash
git log
```
- commit 9f8e7d6(E)
- fix payment button alignment

```bash
git checkout main
git cherry-pick 9f8e7d6
```

---

### 10. Reflog

Shows all movements of HEAD, even deleted commits.

```bash
git reflog
```

---

### 11. git clean

Remove untracked files / Permanently delete files

```bash
git clean -f
```

---

### 12. Bisect

Binary search to find the commit that introduced a bug.

```bash
git bisect start
git bisect bad
```

---

### 13. Blame

Shows who changed each line.

```bash
git blame <file_name>
```

---

### 14. Tagging

Tag marks specific points:
- usually releases
- stores author, date, message

```bash
git tag v1.0
```

---

### 15. Hooks

- Scripts that runs automatically at certain git events
- Location - .git/hooks/

**1. Client-side Hooks**
* Runs on developers machine

**2. Server-side Hooks**
* Runs on remote server

**3. Pre-commit Hooks**
* Runs before commit is created
* Prevent commits if
   - code has error
   - Tests fails 

**4. Commit-msg Hooks**
Validates commit message
- Scripts checks message pattern
- If invalid message pattern - commit rejected

---

### 16. Rebase

* Move one branch commits on the top of another branches
* Rewrite history - yes
* Not safe for shared branches
* No merge commits

A---B---C (main)
    |
    D---E  (feature)


```bash
git checkout feature
git rebase main
```

(feature) -  A---B---C---D'---E'

---