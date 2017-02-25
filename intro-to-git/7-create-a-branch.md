# Create a feature branch
When you start a project, it will, by default, contain one "branch" called "master". You're master branch should always contain the most up-to-date, vetted, and supported code. It should house the software in a state that is suitable for customers.

With that said, you don't want to actively be developing using the master branch. So, the solution is to create new branches from which you can safetly update your source code. 

So, what is a branch anyway?

Think of it as yet another copy of your code. Git provides all the functionality to keep track of the changes you make, so that when it's ready, you can easily integrate your updates back into the master branch.

For this practice project, we will be making to types of branches:
- "Feature" branches
    - We'll make these when we want to add brand new functionality to our code base
- "Issue" branches
    - These branches will be used to address specific issues submitted to the project

For this lesson, we'll be adding a very important feature: You!!!

We'll show you how to create a feature branch from your clone of the project. Then, you'll update the collaborators.md file by adding your name and GitHub username to the markdow table.

To follow along, you will need to have cloned your fork of the project to your working computer, and have the git shell open. Let's get started!

## Create the "collab_add" feature branch
1. Step one is to make sure that your git shell's current working directory is in the right place. If you followed along with the [Clone a repo](6-clone-a-repo.md) lesson, everything should be saved at **~/git_clones/git_drills/**. From your git shell, run the following command to move into that directory:

    ```bash
    $ cd ~/git_clones/git_drills
    ```
2. Next, we'll create our branch and switch to it using the following commands:

    ```bash
    $ git branch collab_add
    $ git checkout collab_add
    ```

    The ```git branch``` command created a new branch and the ```git checkout``` command told git that it is where we want to work.
