1. First go to the the directory you made changes
2. Run CMD: git branch
this will show the current branch you are in and this should be 'master'
3. Run CMD: git pull
this will pull the latest queries and code from the master to your local directory
4.Once the code is up to date in your local directory, to make any changes to the branch we need to create a new branch and we should not do any direct changes to the master
5. Run CMD: git checkout -b new_branch this will create new branch
6. do the necessary changes and save.
7. Run CMD: git add --all which adds all changes to the current branch
8. Run CMD: git commit -m 'comments for the changes' to commit the changes
9. Run CMD: git push origin new_branch
10. no go to the gitlab.castlighthealth.com site and raise a request for code merge.
once the above merge request is accepted, merge the code in gitlab.
11. Run CMD: git checkout master to goto the master
12. now do the git pull to load all changes to your location.
you can do the changes you want then save it.
13. How to pull only one branch changes CMD:   git pull origin WHSE5439_OCT7
