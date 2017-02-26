# Making changes to your branch
Now that we've create a new branch, it's time to make our changes. In this lesson, we'll be adding your name and GitHub username to the collaborators.md file.

To follow along as intended, you should be working on your cloned fork, in the *collab_add* branch. You should also have a text editor picked out that you will use to make your changes.

*sidenote*: if you're familiar with vi, you can make changes directly from your git shell

## A brief intro to markdown
Before we start editing the collaborators.md file, let's take a second to talk about markdown (.md files that is).

What is markdown?
- Markdown is what's called a "markup language". It's designed to provide a simple syntax for formatting text that can then easily be converted (using a markdown tool) into HTML. 
- Markdown files use the extension **md**.
- You may have noticed that all of these lessons are written in markdown.
- If you'd like to see what raw markdown looks like, try clicking the *Raw* button at the top-right hand corner of this text pane.

The collaborators.md file - the one we'll be editing - contains a markdown table, so let's talk about those real quick. Here's what a raw table looks like in markdown:

```
| Header1 | Header2 |
|---------|---------|
| value1  | value2  |
| value3  | value4  |
```

The table uses pipe and dash characters. The first row is where we define our table headers. The second row (the one with all the dashes) is the standard format for telling markdown converters to treat the top row as a header. Each of the following rows contains the values corresponding to the columns they fall in.

Here's what our sample table looks like when rendered by GitHub:

| Header1 | Header2 |
|---------|---------|
| value1  | value2  |
| value3  | value4  |

## Add your information to the collaborators.md file
Ok, now that we have an understanding of markdown, we're ready to update the collaborators.md file.

1. Open the file in your favorite text editor. If you've been following along, it should be located at *~/git_clones/git_drills/pyaug/collaborators.md*

    *rant*: Microsoft word is not a text editor...don't use it

2. Add your name and GitHub username to the appropriate columns. When you're done, it should look something like this. Please don't remove any existing entries, just add yours to the bottom.

    ```
    # pyaug contributors

    | Name                      | GitHub Username            |
    |---------------------------|----------------------------|
    | Cory Taylor               | ctaylor08                  |
    |                           |                            |
    |                           |                            |
    ```

3. Save your changes
