# Diff Creator

This application allows you to create diffs from two different sources of text files. This app was originally designed to compare human transcripts with AI generated transcripts so the folders for the text files are labeled as `truth`for the human transcripts and `text` for the AI generated transcripts.

## Setting Up the Application
* This application uses the [Diffchecker CLI](https://www.diffchecker.com/cli/) so be sure that you have that installed before using the application.

## Running the Application
* Add your baseline comparison files to the `truth` folder
* Add the files you want to compare to the `text` folder
* Clear any existing text from the `diffs.csv` file unless you want the new list of diffs to be added to a previous list
* Run the `script.py` file
  * This will sort and iterate over each file in the `truth` and `text` folders and create diffs for each set of files and saving the file name and a link to the diff in a CSV folder.

**Note:** Files in the `truth` and `text` folders will be sorted and compared in order so be sure each version of a file has the same name or naming convention. When the diffs are created results from the `truth` folder will be on the left side and results from the `text` folder will be on the right.

