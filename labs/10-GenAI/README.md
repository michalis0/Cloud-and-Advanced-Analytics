<h1 align="center"> LAB 10 - GENAI</h1>
<div>
    <br/>
    <img src="https://www.unil.ch/modules/refonte-assets/images/unil-logo.svg" style="padding-right:10px;width:180px;float:left"/>
    <br/><br/><br/>
    <h2 style="white-space: nowrap">Cloud and Advanced Analytics </h2>
    <hr style="clear:both">
    <p style="font-size:0.85em; margin:2px; text-align:justify">
    <br/>
</div>

## Learning Goals
In this lab, you will use Vertex AI and the Gemini API to design more reliable prompts for large language models.

By the end of the lab, you should be able to:

- call a Gemini model from a Jupyter notebook;
- write structured prompts with a clear persona, an explicit task, constraints, input data, and an expected output format;
- separate instructions from the data provided to the model in order to reduce ambiguity;
- compare zero-shot and few-shot prompting;
- request structured outputs, such as JSON;
- reduce unsupported answers by asking the model to rely only on the provided evidence.

## Introduction

This lab focuses on practical prompt engineering with Gemini on Vertex AI. The goal is to give you a few professional habits that you can reuse in analytics, automation, and text-processing tasks.

The lab uses a small set of essential prompt engineering practices:

- role prompting with personas;
- reusable prompt templates;
- few-shot examples;
- structured outputs;
- evidence-based answers.

## Lab Walkthrough

In the lab, you will first learn the essentials of effective AI prompting, covering setup requirements, the creation of helper functions, and fundamental prompting principles such as using delimiters and structured outputs. The section on Iterative Prompt Development teaches refining prompts to enhance clarity and relevance, dealing with common issues like text length and focus. 

In the **Summarizing** section, techniques for creating concise summaries with specific constraints, such as word limits or thematic focuses, are explored, along with the differences between extracting and summarizing content. 

The **Inferring** section delves into sentiment analysis and extracting nuanced information from texts, such as identifying emotions and important details like product names. Transforming text covers practical applications like translation, tone adjustments, format changes, and improving text quality through grammar checks. 

In the **Expanding** section, students will learn to craft detailed, context-aware automated responses by incorporating details from customer interactions. The lab concludes by summarizing key learnings and urging students to apply these techniques to new challenges, emphasizing the importance of ethical considerations in real-world AI applications. This structured approach equips students with the skills to effectively interact with AI tools, enhancing their problem-solving capabilities.


### Pre-Lab Setup 

* Enable vertex AI APIs

**Creation of Notebook:**

* **1.1** Go to the [Google Cloud Console](https://console.cloud.google.com).
* **1.2** In the search bar, enter **Vertex AI (Agent Platform)**. You will arrive on the Vertex AI dashboard.
* **1.3** In the left navigation pane, under **Notebooks**, choose **Workbench**, where you will need to **enable all recommended APIs**.
* **1.4** Click **Instances**, then click **Create New**, then click **Advanced** and set up the new instance as follows:
  * **Region**: us-central1 (lowa)
  * **Zone**: us-central1-a
  * (In *us-central1 (Iowa)*, (It is possible to attach an NVIDIA T4 GPU, but for this lab, we will not use it)
  * Under **Machine type**, select **E2**, then click **Create**.
* **1.5** Once the instance has been created, **wait for it to provision**. This usually takes about 1–2 minutes. Then, select **Open JupyterLab**. This will open a **JupyterLab** instance.
### Exercise

* Download the notebook from GitHub and upload it to Vertex AI to be able to run it! Choose *Python 3 (ipykernel)* to run the GenAI_lab.ipynb notebook.

**IMPORTANT**:
* Please delete all instances that you create in Vertex AI so that you can save Google credits!




