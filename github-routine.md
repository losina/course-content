***DISCLAIMER***: This text is largely copied from NMA's [The zen of reviewing tutorials for Neuromatch Academy (NMA)](https://github.com/NeuromatchAcademy/course-content/blob/main/tutorials/reviewing-tutorials.md) written by NMA waxing team (esp. Patrick Mineault, Michael Waskom, Marco Brigham, and Madineh Sarvestani).

## Workflow for incorporation into the Github repostory

Most of the notebook preparation is coordinated on Google Drive by making copies and sharing/tracking links. But after review and waxing, notebooks should be incorporated into the [CIS-522 Github Repository](https://github.com/CIS-522/course-content). Github is the canonical source for the version of the tutorials that students will actually see, so it is important to get this process right.

The process involves both automated and manual quality control. Here is a guide to the basic steps you should follow. If you are new to the process, it is best to communicate on Slack about what you are doing (#waxers).

While it's helpful to have multiple people handle the work of merging the tutorials, if you're not familiar/confident with Github, feel free to hand the job off (just coordinate on Slack).

1. Create a new feature branch off of main in the `CIS-522/course-content` repository.
  - In the github UI, this can be accomplished from the `Branch` dropdown menu.
  - Include `WxTy` in the name. (Replace `x` and `y` to match the week and tutorial number).
  - It is best to branch off main at the time you're ready to push your tutorials, ~so that the CI will run the latest version of the notebook processing workflow~.
  - ~For the CI workflow to run properly,~ the PR must be made from a feature branch on the main repository, not a fork.
2. ~Notebooks are required to have a sequential execution history on a fresh kernel. This will be automatically checked as part of CI. Before you push, execute the entire notebook (`Runtime -> Restart and run all` in the Colab menu) and make sure it completes without any errors. Then save the notebook~.
3. Push the notebook from Colab to Github:
  - Final steps in Colab before commit:
    1. `Runtime` -> `Restart runtime`
    2. (only necessary for instructor version)`Runtime` -> `Run all` and make sure the notebook runs fully without any error
    3. `Runtime` -> `Factory reset runtime`
    4. `Edit` -> `Clear all outputs`
  - `File -> Save a copy in Github` in the Colab menu
  - Select the course repository: (`NeuromatchAcademy/course-content`)
  - Select your feature branch: (e.g. `WxDy`)
  - Write out the complete file path, using the standardized template:
    - `tutorials/W{x}_{Topic}/Wx_Tutorial{i}.ipynb`
    - Replace `{x}`, `{Topic}` and `{i}`
    - ~See the [tutorials directory](https://github.com/NeuromatchAcademy/course-content/tree/main/tutorials) for a list of names to use for `{Topic}`~
    - An example filename will look like this: `tutorials/W1_AlphaZero/W1_Tutorial1.ipynb`
    - Don't copy the filename from a rich text display (e.g. the Github UI), because mixing unicode and ASCII can produce duplicate files. Copying the path from the URL bar works.
  - Make sure that "Include a link to Colaboratory" remains checked.
  - **Important**: Double-check that the file path is correct before pushing. Fixing incorrect names is a substantial pain, because multiple derivative files will be created using the name you push.
4. Repeat Step 3 with the other tutorials for that day.
5. On Github, open a Pull Request from your feature branch onto `main`.
6. ~Opening the PR will trigger the notebook CI workflow. This will (1) run QC checks on the notebooks and (2) create student versions and derivative static files (solution images and scripts).
  - If the checks fail, click through to the Github Action log and try to figure out what's wrong (or ask for help on Slack).
  - Fix the problem on Colab, then repeat step 3 for that notebook. This will trigger a re-run of the CI workflow.~
7. All PRs must be approved by someone else with commit rights to the repository before they can be merged. You can select reviewers in the upper-right-hand corner of the Pull Request UI. The week content creators and waxers are good reviewers.
8. ~Do visual checks of the processed and derivative files to make sure the student versions look correct.~
  - ~The embedded "Open in Colab badge" is modified as part of the CI workflow to point towards the main branch, so you will need to manually change the URL to point towards the feature branch if you want to open on Colab.~
  - ~The links to the solution images and scripts will also reference `main` so those won't be populated yet.~
9. If everything looks good, the reviewer should approve the PR and then do a squash-merge onto main.
10. Delete the feature branch after the merge is complete.
