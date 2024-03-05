

<h1 align="center"> Github Tips / Tutorial and more</h1>
<div>
<td> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Logo_Universit%C3%A9_de_Lausanne.svg/2000px-Logo_Universit%C3%A9_de_Lausanne.svg.png" style="padding-right:10px;width:240px;float:left"/></td>
<h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2></td>
<hr style="clear:both">
<p style="font-size:0.85em; margin:2px; text-align:justify">
<br>
<br>
</div>

## Learning Goals
By the end of this tutorial, you will understand how setup the environment to allow you to use the best out of Github during the semester. 

## Table of contents for exercises: 
* [Exercise 1: Git Cloning main steps: (5 minutes)](#)
* [Exercise 2: Cloning the course repository: (10 minutes) ](#)
* [Exercise 3: Creating a new PRIVATE repository for assignment 1 and run it on Google Cloud Shell: (15 minutes)](#)
* [Exercise 4: Additional Tips ](#)

## Requirements before beginning this tutorial:
- [x] Github installed on your computer: 
----------
- **Mac**
- ```bash
    git --version
- If you need to [update](https://phoenixnap.com/kb/how-to-update-git) your version of Github:
- ```bash
    brew update
    brew install git
    brew upgrade git
    git --version
- If you encounter [errors](https://stackoverflow.com/questions/75509911/fatal-couldnt-find-remote-ref-refs-heads-master):
- ```bash
    brew tap --repair
    brew cleanup
    brew update-reset
    brew update
    brew install git
    brew upgrade git
    git --version
- Keep up to date with the latest versions of Github: using this [link](https://enterprise.github.com/releases) or this [link](https://git-scm.com/)

- **Windows**
- ```bash
    git --version
- If you need to update:
- ```bash
    git update 
    git update-git-for-windows
------------
**What is Git ? Why do we use it ? How does it work ?** You can have a look at this [blog post](https://towardsdatascience.com/learn-basic-git-commands-for-your-data-science-works-2a75396d530d) that explains more in depth how git and github works! 

------------------

## Exercise 1: Git Cloning main steps: (5 minutes)
- **Step 1: Creating a Github repository** In this step we are going to clone a Github repository, this can be public or private. You can click the + sign, **New repository**. Then you can simply type the repository name: i.e: **my_first_repository**. Keep your code private and add a readme file. 
- **Step 2: Cloning a Github repository** In this step, we are going to clone the repository into your local computer. 
- Go to your local terminal and type: 
- ```bash
    git clone <repository_url> (In our case: https://github.com/GITHUB_USERNAME/my_first_repository.git or go to your profile - code - HTTPS)
- ```bash
    cd my_first_repository
- You can open this in your code editor i.e: in visual studio code and modify a file:
- ```bash
    code .
- Or you can do this directly in the terminal
- ```bash
    touch new_file.py (mac) or New-Item -ItemType file new_file.py (windows)
- Add the file to the commit: 
- ```bash
    git add . 
- Add a commit message: 
- ```bash
    git commit -m "First Commit"
- Push the modification onto your private repository
- ```bash
    git push
- You should now see the file called **new_file.py** on your private repository ! 

------------
## Exercise 2: Cloning the course repository: (10 minutes)

This allows you to have access to the course repository, pull the changes. Each week, new content of the course will be added to the course github repository, therefore, you can clone that repository on your private account and pull the new folders / files each week. This allows you to directly modify the folder and use it in your private repository **More importantly:** This avoids you to have to download all the files / folder at each new lab. The steps are as follows: 

- **Step 1:** Create a **PRIVATE** repository named **big_scale_analytics_2024** (exactly). It has to be empty (no README, no license)
- **Step 2:** Clone the private repository you have created on your local computer
- ```bash 
    git clone https://github.com/GITHUB_USERNAME/big_scale_analytics_2024
- The warning message: **warning: You appear to have cloned an empty repository** is **normal**
- **Step 3:** Add the course repository to yours - allowing to fetch changes from the course repository but also push your changes on your private repo. 
- **git remote add:** associates the remote alias "course" with the specified repository URL, allowing you to refer to this remote by the name "course" in Git commands.
- **git pull course main:** fetches changes from the remote named "course" and merges the changes from its "main" branch into your current local branch.
- **git push course main:** pushes the local changes to the remote named "course" in its "main" branch; prior commits should be committed before pushing.
- ```bash
    cd big_scale_analytics_2024
    git remote add course <public_course_repo_url> (in our case git remote add course https://github.com/michalis0/Cloud-and-Advanced-Analytics )
    git pull course main (here your pulling the entire github of the course)
    git push origin main (here your pushing the entire github of the course on your private repository)
- Now you have the entire course on your private repository, and on this you can:
    - **1. Pull the last changes on the course repository** (i.e before each lab / course we will update the repository). Therefore you can just:
    - ```bash
        git pull course main
    - This will show you the new files added: i.e:  labs/2-BigQuery/Readme.md | 2 +-
    - You then need to push those new files on your private repository:
    - ```bash
      git push

    - **2. Modify directly the files and push them on your private repository:**
    - For example, you can modify the app.py of the streamlit app of assignment 1: change the title from:
    - ```
      st.title("Movies from the TMDB Dataset") to st.title("Movies of the Dataset !")
    - git add .
    - git commit -m "modify readme"
    - git push

- **Everytime you go in class please pull to get the last labs - and commit everytime you change the files!** 

**Note:** 
- **git status:** displays the current state of your local repository, showing modified files, untracked files, and the branch you are on, helping you understand the status of your workspace.
- **Files to not modify** please do not modify the **Readme.md** files, only python files / python Notebooks should be modified. If readme.md files are changed and updated on our side, this could lead to **conflicts without the git files** 

**Other commands:**
- ```bash
    git remote -v
    **open the url:** git open https://github.com/username/repository (mac) or git start https://github.com/username/repository (windows)

------ 

## Exercise 3: Creating a new PRIVATE repository for assignment 1 and run it on Google Cloud Shell: (15 minutes)

**What are the advantages of using cloud shell for your assignment ?** 
- You don't need to install packages locally on your computer
- Cloud shell already provides pre-installed packages / python libraries

**You will find below the steps to:**
- 1. Create a new **private** repository on Github
- 2. Clone that repository in the Google Cloud Shell
- 3. Open it in the Editor of Google Cloud Shell (which is an instance of Visual Studio Code)
- 4. Create a virtual environment (necessary to install your packages)
- 5. Run the streamlit app on Google Cloud Shell
- 6. Deploy the App on Cloud Run

**It is recommended to follow these steps as this will help you with assignment 1**

------------------

**1. Create a new private repository on Github:**
- **1.1** You will need to go to your Github Account - https://github.com/GITHUB-USERNAME, then select the + icon and click on **Create new repository**. You need to add a **repository name** (i.e: Assignment-1) and a **description**. Then select **private** and **Add a README file**, then select **Create repository**. Your private repository has just been created!

**2. Clone that repository in the Google Cloud Shell**
- **2.1** You need to access your Google Cloud account - you can follow this [link](https://console.cloud.google.com/), select your project and activate the Cloud Shell (CF lab 1). The cloud shell is basically a terminal on which you can clone repositories which creates a copy in your Google Cloud account (similar as if you did this on your local computer).
- **2.2** Once activated, you can clone the repository you just created. You can start by copying the link:
  ```bash
  git clone https://github.com/Github_username/repository-name.git (this link can also by copied directly on your repository - by clicking code - HTTPS and copy the link)
- **2.3** Then you can paste it into the Cloud Shell. You will need to add your **Username** (github-username) and the **Github Personal access token** (CF lab 1). 
- **2.4** You should now be able to see your repository name in your existing folders on Google Cloud Shell, this can be accessed by typing: **ls** (Linux command to list files in your directory, in our case, in the cloud directory) in the terminal. You can then access that folder by typing **cd** (Linux command to change the directory - **C**hange **D**irectory). If you repository name is **Assignment-1**, the command:
- ```bash
  cd Assignment-1
- Allows you to navigate to that folder

**3. Open the project into the virtual code editor:**
- Now that you have cloned your repository, you can open it into the Editor, which is equivalent to opening Visual Studio Code on your local computer.
- To do so, click on **Open Editor**. Select the hamburger icon and select **file**, **open folder**, you should be able to find a path. This is the path of your **cloud shell**, you can imagine it being your personal laptop. So you should see **/home/username/**, then to access the cloned repository, type in the path, the name of the repository you just created, which in our case is Assignment-1, so this would be: **/home/username/Assignment-1**, select it and click **OK**. You should now see your project opened in the Editor, i.e: just a readme file !

**4. Creating a streamlit app and pushing this on your private repository:**
- You now have access to your project and you can add some code and download libraries, without worrying about downloading them on your local computer !
- Open the **terminal in the Editor** - select the hamburger icon - **View** - **Terminal**
- Once this is open, if it is not selected, click on the plus sign and select **bash** (which is essentially a command-line interface allowing to execute commands, i.e install libraries).
- We are now going to create a virtual environment, where you will have all your packages / libraries installed in one specific place. Having a virtual environment allows you to have all the depencies related to your project in one specific place, so that you can keep updated packages related to your project, allowing a stable application. If you want more information concerning virtual environment, please refer to the [documentation](https://docs.python.org/3/library/venv.html).
- To do so, you can install the packages related to the virtual enviroments and created your first virtual enviroment using:
- ```bash
  pip install virtualenv
  python3.9 -m venv ./envs/assignment-env (here we are using the python interpreter version 3.9)
- **!Important!** it is good practice to put this virtual enviroment in a **.gitignore** file, which essentially ignores this folder when pushed on your repository. We do this to avoid having unnecessary packages on our Github (and potential conflicts). 
- To add a .gitignore file, go to your editor, select **new File** and create a **.gititnore file** and add **/envs** inside. Once this added, the /envs folder should be light gray, meaning that it will be ignored once you push. Let's try and see.
- Go to your terminal - cloud shell terminal - for this you should be careful to be in the correct directory - you can find this by doing ls or cd, as mentionned before, push the new files. To do so:
- ```
  git status (Displays repository status - here you should see Untracked files: .gitignore, the file we just added)
  git add . (add all changes)
  git status (You can now see the new file added)
  git commit -m "your commit message" (commits the change with a message)
  git push (uploads the changes to your repository)

- There is also an option to commit and add directly:
- ```bash
  git commit -am "your commit message"

- Go to you private repository and see the changes ! You should be able to see your .gitignore added to your repository

**5. Adding Streamlit and running a small streamlit app**
- Now that your environment is set-up, we can run a streamlit app
- First create a file called **app.py** and copy / paste the code below in it:
- ```
  import streamlit as st
  st.title('Streamlit app for assignment 1!')
- Now run:
- ```
  streamlit run app.py
- You should get this error: **bash: streamlit: command not found**, why ? Because streamlit is not installed in your project nor in your virtual enviromnent.
- You can go back to the **Editor Terminal** and activate your enviroment, this can be done with:
- ```
  source envs/assignment-env/bin/activate (activates your enviroment, there allowing you to use / download libraries)
- Now you should be able to see in the terminal: (assignment-env) email@cloudshell ...
- You can now install streamlit:
- ```
  pip install streamlit
- Now you can enter: **streamlit run app.py** - you should see a Network URL (address where Streamlit app is hosted - locally) and an External URL (Access the streamlit app from different devices than the hosted device running streamlit).
- As you can see, again, the website takes time to load. This is because we are running the app from Google Cloud Shell, and unlike running the streamlit app locally, Google Cloud Shell needs specific requirements to run that website. Therefore, to run it, you can paste this command (**NOTE** if you want to run streamlit on your local computer, streamlit run app.py is enough to run the website)
- ```
  streamlit run app.py --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false
- **Then select the Web Preview Icon** (at the right of Use the Legacy editor) and select **change port** and change the port to 8501 and you should be able to see the app !
- You can now commit and push the changes (by going back to the cloud shell terminal) - the new file app.py should be visible on your private repository !


**6. Deploy the App on Cloud Run**
- This is a recall of cloud run, please refer to Lab 1 if you have any doubts or questions
- You need to add a requirements.txt file and add streamlit inside it
- You also need a dockerfile, you can copy the same code given in lab 1 for the Dockerfile.
- Don't forget to push on your private repo !
- Build the docker:
- ```bash
    docker build -t eu.gcr.io/PROJECT_ID/my_streamlit_app:latest .
-  ```bash
    docker push eu.gcr.io/PROJECT_ID/my_streamlit_app:latest
- Go to the container registery and deploy the app (CF lab 1).
  
- **Done ! You just published you app**

## Exercise 4: Additional Tips (Google Colab):

You can import python Notebooks directly from Github onto your Google Colab, **without downloading it directly on your local computer**. To do so, you can follow those steps:
1. Say we want to open this [file](https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/2-BigQuery/notebooks/BigQuery_exercises.ipynb) on Google Colab
2. You can simply go to Google Colab - Select **Open Notebook** - **GitHub** - and paste the URL - in our case: https://github.com/michalis0/Cloud-and-Advanced-Analytics/blob/main/labs/2-BigQuery/notebooks/BigQuery_exercises.ipynb and select the file: labs/2-BigQuery/notebooks/BigQuery_exercises.ipynb.
3. **Done:** You just opened the python Notebook, you can also push your changes onto your private repository: **File** - **Keep a copy on Github**

