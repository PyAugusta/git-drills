# Merge your branch back into master
Now that we've made changes to our collab_add branch, it's time to merge it all back into our master branch.

Because the changes we made have been very simple, this should go fairly smoothly. To follow along, you should be working on the clone of your fork of this project inside the git shell.

1. First, let's swich back to our master branch and ensure that it contains the most up-to-date version of the code.

    ```bash
    $ git checkout master
    $ git pull
    ```

    The ```git pull``` command will pull down and re-clone the branch we're on (master in this case). This may be unneccesary for us because we shouldn't have changed anything in the master branch, but it's still good practice.

2. Next, we'll merge the master and collab_add feature branch.

    ```bash
    $ git merge --squash collab_add
    ```

    At this point, git will automatically check for any conflicts. If any are found, a message will be given instructing you which files have the conflicts appear in. You will have the opportunity to then manually fix those changes. If the only thing that changed is the addition of your entry in the collaborators.md file, then the above command should just work.

3. Now, commit and push your newly merged master branch.

    ```bash
    git commit -m "merge of collab_add into master"
    git push -u origin master
    ```

4. Take a look at your new master branch

    - Visit your fork in the browser, and inspect the collaborators.md file to see your change

And there you have it. In the [next lesson](10-submit-pull-request.md), we'll submit a pull request to let the main project developers know that we're ready to implement your changes.
