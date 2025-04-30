<h1 align="center"> LAB 10 - GENAI</h1>
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
In this lab, you'll learn how to develop best practices when prompting large language model like GEMINI. 

## Introduction
Welcome to the tenth lab of Cloud and Advanced Analytics! In this week, we'll use Vertex AI tool to call GEMINI API

## Lab Walkthrough

In the lab, students will first learn the essentials of effective AI prompting, covering setup requirements, the creation of helper functions, and fundamental prompting principles such as using delimiters and structured outputs. The section on Iterative Prompt Development teaches refining prompts to enhance clarity and relevance, dealing with common issues like text length and focus. 

In the **Summarizing** section, techniques for creating concise summaries with specific constraints, such as word limits or thematic focuses, are explored, along with the differences between extracting and summarizing content. 

The **Inferring** section delves into sentiment analysis and extracting nuanced information from texts, such as identifying emotions and important details like product names. Transforming text covers practical applications like translation, tone adjustments, format changes, and improving text quality through grammar checks. 

In the **Expanding** section, students will learn to craft detailed, context-aware automated responses by incorporating details from customer interactions. The lab concludes by summarizing key learnings and urging students to apply these techniques to new challenges, emphasizing the importance of ethical considerations in real-world AI applications. This structured approach equips students with the skills to effectively interact with AI tools, enhancing their problem-solving capabilities.


### Pre-Lab Setup 

* Enable vertex AI APIs

**Creation of Notebook:**

* **1.1** Please go to your [Google Cloud Console](https://console.cloud.google.com)
* **1.2** In Search enter **Vertex AI**, then press return - you will arrive on the Dashboard of Vertex AI, where you will need to **Enable all recommended APIs**
* **1.3** In the left-navigation pane, under **Tools**, **Notebooks**, choose **Workbench**.
* **1.4** Click **Instances**. User-managed notebooks are deprecated since April 14, 2025.
* **1.5** You will need to create a new Notebook - click on **CREATE NEW** and click **Create** (you can also set the region to something **different** than *europe-west6 (Switzerland)*). If you, for example, choose *us-central1 (Iowa)*, you can even attach 1 NVIDIA T4 GPU!
* **1.6** Once the Instance is created, click on the instance, and **wait for it to provision** (about 1-2 minutes). Then, select **Open JupyterLab** - this will open an instance of **JupyterLab**.

### Exercise

* Download the notebook from GitHub and upload it to Vertex AI to be able to run it! Choose *Python 3 (ipykernel)* to run the GenAI_lab.ipynb notebook.
* This lab is not long at all. The goal is that you do exercises and play around with the GEMINI API! Good luck :D

**IMPORTANT**:
* Please delete all instances that you create in Vertex AI so that you can save Google credits!




