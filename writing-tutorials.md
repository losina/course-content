# Writing tutorials for CIS-522

Thank you for writing a tutorial for CIS-522! Unlike most university classes, these notebooks will contain not just just assignemnts but the bulk of instruction. They're the centerpiece of the course! It's important that these notebooks stick to a consistent pedagogical style, so please follow these instructions carefully.


## Environment

Tutorials are written in Python and Pytorch in a Google Colab environment.

We also have the parameters of a basic environment in *environment.yml* in case students would prefer to work on their home machines (if available) or if problems with Colab arise.
## Tutorial structure

There will be 2 tutorial notebooks per week. These tutorials are mixes of exercises, explanatory text, and pre-written code. Each of these should be designed to take 2 and 1/2 hours to complete, maximum. Keep in mind that this includes time for thinking and discussion with podmates.

Each of these tutorials will contain 10-15 embedded Youtube videos recorded by the course instructors. These are short (1-5 minutes each). Each of these videos starts and ends a "learning chunk" of the tutorial. It's your job to design the tutorial so that it has good chunks!


## Creation timeline

As a tutorial writer, you are the *first* of many people who will help create these notebooks. It's important to start early. To make sure everyone down the line has time, we've set up a rather rigid timeline. You can see this timeline in graphical form in the [Content Tracker](https://docs.google.com/spreadsheets/d/1wwSyALbDyRRnkkzBk7jPQy26lhGKadvpxqkJnDHVaUQ/edit?usp=sharing) Sheet.

Course weeks will begin on Thursdays. Here's what will happen in the two months before each week, and whose role that is.
-  **(>6 Thursdays prior) Whitepaper due.** *[course instructors]* The whitepaper states the teaching goals of that week and contains a rough outline of the notebook. 
-  **(5 Thursdays prior) Working notebooks due.** *[tutorial writers]* This is most of the hard work! The **working notebook** is a first draft of the tutorial. It will *implement* all of the code that students will be expected to write, and it should work! It should indicate which parts of the code will be student exercises. It should also indicate where videos will later be embedded. Where there will later be explanatory text, these notebooks will have placeholders.
-  **(4 Thursdays prior) Working notebooks waxed.** *[waxing team]* During this week, the waxing team will polish your notebooks. They will be edited to have a consistent style, content, and difficulty with the rest of the course, if needed.
-  **(3 Thursdays prior) Didactic (final) notebooks due.** *[tutorial writers]* After getting the waxed notebooks back, it's time to actually write all the student exercises and fill out missing explanatory text. These will contain `solution` cells containing the working code; we have automatic scripts to separate these out and create student notebooks.
-  **(2 Thursdays prior) Final notebooks waxed.** *[waxing team]* Videos will be included at this point, and the notebooks will be finished.
-  **(1 Thursday prior) Notebooks reviews due.** *[TAs]* Other TAs will take the courses ahead of time, and submit any bugs or criticism.
-  **(Thursday run day) All bugs fixed.** *[waxing team / tutorial writers]* Reviews are incorporated in the final week.

As these deadlines pass, please update the [Content Tracker](https://docs.google.com/spreadsheets/d/1wwSyALbDyRRnkkzBk7jPQy26lhGKadvpxqkJnDHVaUQ/edit?usp=sharing) with links to the Colabs. Works-in-progress Colabs will eventually be uploaded the the course Github.



## Structure of tutorials

Markdown headings (`#`, `##`, `###`, etc.) can be used to automatically create headings for tutorials, objectives, and exercises, respectively. Use `---` in markdown to separate different exercises/sections.

Since we will be following the general Neuromatch Academy format, it may be helpful to look at some [NMA tutorials](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials).

When each tutorial is complete, it should:
1. Import all necessary libraries, in a separate code cell at the top of the tutorial. Don't hide this cell or give it an `@title` since this squashes the code cell.
2. For other setup cells (figure settings, helper functions, data loading):
    - Write `# @title Figure Settings` (or other relevant title) at the top of each cell.
    - Hide the cell: Left-click `...`>`Form`>`Hide code` (special colab trickery).
    - Include the following settings for figures:
      ```# @title Figure Settings  
      %matplotlib inline 
      fig_w, fig_h = (8, 6)
      plt.rcParams.update({'figure.figsize': (fig_w, fig_h)})
      %config InlineBackend.figure_format = 'retina'

   - check the notebook [`Installing Python libraries.ipynb`](https://github.com/NeuromatchAcademy/course-content/blob/master/tutorials/utils/Installing%20Python%20libraries.ipynb) on how to install additional libraries or your custom library
2. Describe the tutorial objectives using 2-3 sentences + bullet points
3. Start with a soft landing exercise to make students feel confident and relaxed.
4. Split core tutorial content into additional exercises. Each exercise should have:
   - A markdown heading (i.e., `#### Excercise: <descriptive name>`) at the appropriate level to fit into the notebook outline.
   - A short description of what we want the student to do in this exercise
   - All equations necessary to implement the computation req. in the exercise (incl. links to external papers/websites for further reading)
   - A detailed bullet point list of the itemized actions we want the students to perform to complete the exercise
   - Code skeleton, including all the plotting function req. for completing the exercise. Add `...` to indicate where students should fill in parts of the code. Comment out lines of code that aren't valid Python or that won't run until the exercise is complete.
   - When the exercise would involve writing a function, provide a stub with all the parameters defined (including complete [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
   ocstrings). The stub function should raise a `NotImplementedError` to indicate that it is part of an exercise. Add a message to the error so that this is explicit. Otherwise students may get confused about why the code won't run.
   - (optional) Include hints in the code skeleton to highlight where the students should complete the code and what Python functions they could use to complete it (e.g.: '# Hint: use the function `np.exp()` to exponentiate' )
   - (optional) A sample output of what the correct output of the exercise should look like. To prevent students from focussing on reproducing exactly the plots/sample outputs rather than understanding the core concepts, we provide them with the plotting functions and use the XKCD style for the expected sample outputs.
5. Solutions for each excercise in the tutorial. 
   - The solution should be written in a separate cell. The first line of the solution cell should begin with a comment that starts `# to_remove`. This comment will signal that the cell should be removed from the student version of the tutorial.
    - Make sure that later content doesn't depend on variables defined in these solution cells or on the output of the completed functions. Where necessary, you can "comment-out" such references and make it clear that the student should uncomment them once the exercise is complete. But it is better for the exercises to be self-contained.
6. Tutorial notebooks should be able to execute from top-to-bottom without error, including after the solution cells are removed. This allows us to automatically enforce a minimum standard of correctness.
7. Each tutorial stands on its own. Like a memorable story, set the context in the introduction, take the student forward through the exercises, and anchor learned points in the conclusion section.

Have a look at a reference NMA tutorial to see what a tutorial looks like in the end: [Bayes Day tutorial 1](https://colab.research.google.com/github/NeuromatchAcademy/course-content/blob/master/tutorials/W2D1_BayesianStatistics/W2D1_Tutorial1.ipynb)

NMA materials also offer a collection of self-contained [Tutorial demos](https://github.com/NeuromatchAcademy/course-content/tree/master/tutorials/demo) illustrating invidual components.
