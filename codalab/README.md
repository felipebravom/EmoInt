# Sample CodaLab competition for SemEval #

This is a sample competition bundle for CodaLab competitions (https://competitions.codalab.org/) designed as a starting point for SemEval task organizers.

## Understanding CodaLab competitions ##

These descriptions and tutorials on CodaLab are a good place to start:
- https://www.youtube.com/watch?v=mU1yEEMrMvY
- Competition Roadmap: https://github.com/codalab/codalab-competitions/wiki/User_Competition-Roadmap
- Quickstart: https://github.com/codalab/codalab-worksheets/wiki/Quickstart
- Running a Competition: https://github.com/codalab/codalab-competitions/wiki/User_Running-a-Competition

## Understanding this sample competition ##

This sample competition looks for submissions with the text "Hello World!". If it finds
it, it gives it a score of 1, otherwise a score of 0.

To understand how a CodaLab competition bundle is created, take a look at the Makefile.
In short, you need to create a ZIP file that includes all the YAML and HTML files in the competition directory, as well as the zipped-up scoring program and reference data.
To do this automatically, you can run:

    make competition.zip

That ZIP file can then be used to create a new competition at CodaLab: https://competitions.codalab.org/competitions/create.
(You will need to register and create an account first.)
You may want to upload this competition with minimum (or no) editing first, just to get a feel of how a competition bundle works.

Once the competition has uploaded successfully:

- Note the secure url the system provides below the task title.
  This is the competition url that can be shared with others while you are still setting up the competition.
- Explore the admin features at the top such as "Edit" and "Submissions".
  (Note that the edit button takes a few seconds to load the page.)
- Try uploading a submission.
  You can generate a sample submission at the command line by running ``make submission.zip``, which, as you can see in the Makefile, makes a ZIP file containing just the ``answer.txt`` file.
  Then in your CodaLab competition:

  - Click on "Participate". Click on "Submit / View Results".
  - Enter a suitable description for each submission in the text box provided.
  - Click on the "Submit" button to upload the file.
  - This should execute the evaluation script on the submission and store the results.
  - You can monitor the progress on the "Submit / View Results" page by clicking the "+" beside your submission and then clicking on "Refresh status".
  - Your submission should move from "Submitted" to "Running" to "Finished".
  - When it is "Finished", explore various files generated on running the evaluation script. For example, text sent to STDOUT will be available in "View scoring output log".
  - Click on "Results" to see the leaderboard.


### CodaLab errors ###

Unfortunately, CodaLab has some bugs currently (which may be fixed by the time you read this).
For example:

- some times the system says: can't open the evaluation script, permission denied
- some times the system says: OSError: [Errno 39] Directory not empty
- some times the system stalls with the status "Submitting" and never reaches "Finished".

We have informed the CodaLab developers of these bugs, and they are working on fixing them.
In the meantime, the suggested workaround for most problems is to re-upload the submission; usually it will be successful after a few tries.

## Customizing this sample competition ##

You will need to customize many things in this sample competition to make it appropriate for your SemEval shared task

### competition.yaml ###

This is the main meta-data for your task.

- Edit the title and description.
- Modify the leaderboard.

  - Change "correct" to the name of your evaluation metric (e.g., fscore, accuracy)
  - Change "numeric_format" for the required digits after the decimal point. For example, using 2 will show two digits after the decimal.
  - If you will have multiple evaluation metrics, add a similar block for each of them.
  - You will need to make sure that your scoring program outputs these same names.

- Add extra phases if needed. If you're not sure whether you need extra phases or not, start a discussion on semeval-task-organizers@googlegroups.com.

### Other competition files ###

The other competition files are all referenced by competition.yaml and are included in the bundle you upload.
If you change any of their names, be sure to also change their names in competition.yaml.

- Replace the logo file with the logo for your task.
- Add details to each of the webpages.

### The scoring program ###

- Replace the sample scoring program with your task's scoring program. Your scoring program will have to follow the standard CodaLab directory structure for the reference data, the system submission, and the output ``scores.txt`` file: https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
- If you change the name of the evaluation script, then change it in the ``metadata`` file as well.
  For example, if your script is in Perl and called ``score.pl``, then use ``command: perl $program/score.pl $input $output``.
- Be sure that your evaluation script gives clear error messages when it fails.
  For example, if there is a formatting error in someone's submission, your script should explain the problem and exit with an error status (e.g., ``sys.exit("some error message")`` in Python).
- Be sure that your evaluation script is writing the output in the right format; it should print lines of the format ``<metric name>:<score>`` in the  ``scores.txt`` file. For example:

        correct:1
        f-score:0.74

### The reference data ###

The ``dev_data`` and ``test_data`` directories contain the reference data on which systems will be evaluated in the Development and Testing phases, respectively.
In the sample, the reference data for each takes the form of a single file, ``truth.txt``.
You should replace ``truth.txt`` with whatever file(s) and format(s) your scoring program expects for the reference data.
Your development data should already be prepared; it's just part of the training data that you have already released.
If you do not yet have reference data prepared for your Testing phase, then for now you can configure the Testing phase to use the Development phase data: ``reference_data: dev_data.zip``.  (You *must* specify reference data for all phases, or else CodaLab will throw an error when you try to publish your competition.)  You can add the real Testing data via the CodaLab graphical interface later, but you must do so before the Testing phase starts.
