# Make Your First PR on GitHub

For people who are new to GitHub and want to make their first PR.</br>
No need to get scared and confused !! Thir repo is just for your practise.</br>
You may make mistake while creating a PR to this repo, but that is totally fine. This is exactly the reason why this repository is created.</br>
So you can TRY, FAIL, LEARN and then IMPROVE. :)

You don't need to know any programming skill to make PR or contribute to this repository either, just follow the steps below and try to make a PR today!

### What can you do to contribute to this repo?

This repo is just for practise purpose, hence you can just add a folder in this repository. Name the folder as your GitHub username and inside that folder, you can add anything you like. Some suggestions will be that you can add any code, or project in any programming language you like, or you can simply add a readme file in that repo and write why you started with Open-source.</br>
Check out the issue created for this purpose [here](https://github.com/swati-gwc/MakeYourFirst_PR/issues/1).</br>
NOTE: THE FOLDER YOU WILL ADD MUST NOT BE EMPTY!

### Steps to make a PR

> - Do not edit/delete someone else's code in this repository. You can only insert new files/folder in this repository.
> - Give a meaningful name to whatever file or folder you are adding, for e.g., if you have written a C++ code on bubble sort, then bubble_sort.cpp is one example of valid name.

Following are the steps to guide you:

* Step 1: Fork the repo and Go to your Git terminal and  clone it on your machine.
* Step 2: Add a upstream link to main branch in your cloned repo
    ```
    git remote add upstream https://github.com/swati-gwc/MakeYourFirst_PR.git
    ```
* Step 3: Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
    ```
    git pull upstream main https://github.com/swati-gwc/MakeYourFirst_PR.git
    ```
* Step 4: Create your feature branch (This is a necessary step, so don't skip it. Also, name the branch as your own name/username)
    ```
    git checkout -b <feature-name>
    ```
* Step 5: Commit all the changes (Write commit message as "My first PR")
    ```
    git commit -m "Write a meaningfull but small commit message"
    ```
* Step 6: Push the changes for review
    ```
    git push origin <branch-name>
    ```
* Step 7: Create a PR on Github. (Don't just hit the create a pull request button, you must write a PR message to clarify why are you contributing. You can write, "Contribution to issue #1" . )


The above rules may seem hard to follow. But every beginner feels the same and most importantly when you will start to make PR's to real projects, in future, you have to adhere to Contributing rules they have set. Otherwise, your PR will not get merged and your efforts will go waste. So make it a practise right from start.

