open Terminal and run following commands:

?????git clone git@github.com:user/repo.git

1.Initialize git in that folder (root Directory)

    git init

2.Add Git

    git add .

3.Link your TSf/Git to that Project - {url} replace with your git address

    git remote add origin {url}

4.Commit those Changes:

    git commit -m "initial commit"

5.Push - I pushed code as version1 you can use any name for your branch

    git push origin HEAD:Version1


Git Branching:


1.this will create new branch named(branch_name)

    git branch branch_name

2.this will open the new branch(branch_name)

    git checkout branch_name

3.this will do the work of both of the above statement

    git checkout -b branch_name

4.remove remote branch
    
    git push origin --delete <branchName>

5.Pull a certain branch from the remote server

    git pull origin other-branch

6.How do I get the current branch name in Git?

    git branch

    git rev-parse --abbrev-ref HEAD #To display only the name of the current branch you're on

7.Delete Local Branch
To delete the local branch, use one of the following:

    git branch -d <branch_name>
    git branch -D <branch_name>
    git branch -D <branch_name>
 


git status - показывает состояние вашего репозитория (рабочей копии) и где вы находитесь.
gitk - графическая утилита, которая показывает наш граф.
git log