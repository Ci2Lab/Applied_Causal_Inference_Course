# Applied Causal Inference Course

![img](lectures/img/causality_intro_image.png)

This course offers a comprehensive overview of applied causal inference, focusing on developing a deep understanding of how to analyze and model cause-and-effect relationships in various domains.

The course begins with an introduction to the foundations of causal inference, including core concepts like correlation, association, and the limitations of traditional statistical methods. It then progresses to more advanced topics, such as interventions, counterfactuals, and graphical causal models like Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs). Practical examples, real-world case studies, and hands-on activities are used throughout the course to solidify learning.

By the end of the course, students will be able to build, interpret, and analyze causal models to address a wide range of scientific and real-world problems using modern data science techniques.

This is an ongoing course, so keep track of updates and feel free to share your feedback.

Thanks,  
[Reza Arghandeh](https://www.hvl.no/en/employee/?user=Reza.Arghandeh)


---

### Learning Objectives:

- Develop an understanding of how to use causal inference to move beyond correlation and address cause-and-effect relationships in data.
- Learn to model causal structures using Directed Acyclic Graphs (DAGs) and apply them to real-world scenarios.
- Understand the transition from observational data to making causal claims through interventions and counterfactual analysis.
- Gain practical experience in using Structural Causal Models (SCMs) to formalize the data generation process and investigate causal effects.
- Explore data-driven causal discovery methods and learn how to discover causal relationships from observational data using modern algorithms.

---

# Lectures

|   | **Chapter**                    | **Description**            | 
|---|---------------------------------|---------------------------|
|   | 1 - [Introduction to Causality](./lectures/CH-1-Introduction-to-Causality.ipynb) | Overview of causality, correlation vs. causation, and the role of observational data in making causal claims. | 
|   | 2 - [Ladder of Causality](./lectures/CH-2-Ladder-of-Causality.ipynb) | Introduction to Judea Pearl’s Ladder of Causality: from associations to interventions and counterfactuals. [Activity](./lectures/CH-2-Activity-Bias.ipynb) | 
|   | 3 - [Graphical Causal Models](./lectures/CH-3-Graphical-Causal-Models.ipynb) | Learning how to represent and analyze causal relationships using Directed Acyclic Graphs (DAGs) and their role in identifying independence and dependence relationships. |
|   | 4 - [Structural Causal Models](./lectures/CH-4-Structural-Causal-Models.ipynb) | Introduction to Structural Causal Models (SCMs), including how they capture the data generation process and formalize causal relationships. |
|   | 5 - [Causal Model Discovery from Data](./lectures/CH-5-Causal-Model-Discovery.ipynb) | Practical approaches to discovering causal models from observational data, including an overview of constraint-based and score-based methods. |

---

## Suggested Python Libraries 

- [DoWhy](https://py-why.github.io/dowhy/index.html): A Python library that provides several tools for causal inference, modeling causal assumptions, and validating them. It is user-friendly and widely used for causal inference tasks, including treatment effect estimation and counterfactual analysis.
  
- [pgmpy](https://pgmpy.org): Python library for Probabilistic Graphical Models, supporting structure learning, parameter estimation, inference, and causal discovery. It's a more advanced library for those interested in Bayesian networks and probabilistic models.

- [bnlearn](https://erdogant.github.io/bnlearn/pages/html/index.html): A library for learning the graphical structure of Bayesian networks in Python. It builds on pgmpy but with a simpler and more user-friendly interface, making it a good starting point for Bayesian network tasks.

- [gCastle](https://github.com/huawei-noah/trustworthyAI/tree/master/gcastle): A powerful library for causal structure learning that supports a variety of algorithms, including constraint-based and score-based methods for discovering causal graphs from observational data.

- [EconML](https://github.com/microsoft/EconML): Developed by Microsoft, this library is designed for estimating heterogeneous treatment effects using machine learning techniques. It combines econometrics and machine learning, offering advanced models like Double Machine Learning (DML) and Targeted Regularized Learning (TRL).

- [CausalNex](https://causalnex.readthedocs.io/en/latest/): A library focusing on causal structure learning, particularly for Bayesian networks. It offers an intuitive API for building and visualizing causal graphs and provides support for interventions and counterfactual queries.


---

## Suggested Books

All of these books are open access.

- **[The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net)** by Nick Huntington-Klein (2023) - A beginner-friendly, open-access book on causality.
- **[Causal Inference, The Mixtape](https://mixtape.scunning.com)** by Scott Cunningham (2023) - A well-written introduction to causal inference.
- **[The Elements of Causal Inference](https://mitpress.mit.edu/books/elements-causal-inference)** by Jonas Peters et al. (2017) - A technical book on causal inference in the context of machine learning.
- **[Applied Causal Inference Powered by ML and AI](https://www.causalml-book.org)** by Victor Chernozhukov et al. (2024) - A comprehensive technical book merging causal inference with modern ML/AI techniques.
- **[Introduction to Causal Inference](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf)** by Brady Neal (2020) - A structured, open-access textbook explaining the fundamentals of causal inference.
- **[Causal Inference: What If?](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/04/hernanrobins_WhatIf_26apr24.pdf)** by Miguel Hernan and Jamie Robins (2024) - A comprehensive textbook on causal inference with an academic focus.

---

## Acknowledgments

This course was developed with partial support from the RCN-INTPART DTRF Project.  
https://www.bigdata.vestforsk.no/ongoing/intpart-dtrf
