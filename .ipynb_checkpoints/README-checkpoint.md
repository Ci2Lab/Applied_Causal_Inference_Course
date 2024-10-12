# Applied Causal Inference Course

![img](lectures/img/causality_intro_image.png)

This course offers a comprehensive overview of applied causal inference, focusing on developing a deep understanding of how to analyze and model cause-and-effect relationships in various domains.

The course begins with an introduction to the foundations of causal inference, including core concepts like correlation, association, and the limitations of traditional statistical methods. It then progresses to more advanced topics, such as interventions, counterfactuals, and graphical causal models like Directed Acyclic Graphs (DAGs) and Structural Causal Models (SCMs). Practical examples, real-world case studies, and hands-on activities are used throughout the course to solidify learning.

By the end of the course, students will be able to build, interpret, and analyze causal models to address a wide range of scientific and real-world problems using modern data science techniques.

This is an ongoing course, so keep track of updates and feel free to share your feedback.

Thanks,  
[Reza Arghandeh](https://www.hvl.no/en/employee/?user=Reza.Arghandeh)

---

### Course Goals:
- Build data literacy to critically engage with information and data in the modern world.
- Develop an understanding of bias in data, particularly in the context of causal discovery.
- Learn and apply the principles of causal modeling using DAGs and SCMs to infer cause-and-effect relationships.
- Gain practical experience in using causal inference techniques to analyze real-world data.

---

### Learning Objectives:
1. Translate scientific and practical questions into formal causal models.
2. Understand the theoretical properties and assumptions underlying causal models.
3. Apply causal models and methods to investigate questions across a variety of domains, from economics and healthcare to machine learning and AI.

---

# Lectures

|   | **Chapter**                    | **Discussion**            | 
|---|---------------------------------|---------------------------|
|   | 1 - [Introduction to Causality](./lectures/CH-1-Introduction-to-Causality.ipynb) | Overview of causality, correlation vs. causation, and the role of observational data in making causal claims. | 
|   | 2 - [Ladder of Causality](./lectures/CH-2-Ladder-of-Causality.ipynb) | Introduction to Judea Pearl’s Ladder of Causality: from associations to interventions and counterfactuals. [Activity](./lectures/CH-2-Activity-Bias.ipynb) | 
|   | 3 - [Graphical Causal Models](./lectures/CH-3-Graphical-Causal-Models.ipynb) | Learning how to represent and analyze causal relationships using Directed Acyclic Graphs (DAGs) and their role in identifying independence and dependence relationships. |
|   | 4 - [Structural Causal Models](./lectures/CH-4-Structural-Causal-Models.ipynb) | Introduction to Structural Causal Models (SCMs), including how they capture the data generation process and formalize causal relationships. |
|   | 5 - [Causal Model Discovery from Data](./lectures/CH-5-Causal-Model-Discovery.ipynb) | Practical approaches to discovering causal models from observational data, including an overview of constraint-based and score-based methods. |

---

## Suggested Python Libraries 

- [DoWhy](https://py-why.github.io/dowhy/index.html). A Python library that provides several tools for causal inference, modeling causal assumptions, and validating them.
- [pgmpy](https://pgmpy.org/). Python library for Bayesian Networks, supporting structure learning, parameter estimation, inference, and causal discovery.
- [bnlearn](https://erdogant.github.io/bnlearn/pages/html/index.html). Library for learning the graphical structure of Bayesian networks in Python, based on the pgmpy library but with simplified usage.
- [gCastle](https://github.com/huawei-noah/trustworthyAI/tree/master/gcastle). A library for causal structure learning, featuring data simulation, structure learning, and evaluation tools.

---

## Suggested Books

All these books are open-access!

- **The Effect: An Introduction to Research Design and Causality** by Nick Huntington-Klein (2023) - A beginner-friendly, open-access book on causality.
- **Causal Inference, The Mixtape** by Scott Cunningham (2023) - A well-written introduction to causal inference.
- **The Elements of Causal Inference** by Jonas Peters et al. (2017) - A technical book on causal inference in the context of machine learning.
- **Applied Causal Inference Powered by ML and AI** by Victor Chernozhukov et al. (2024) - A comprehensive technical book merging causal inference with modern ML/AI techniques.
- **Introduction to Causal Inference** by Brady Neal (2020) - A structured, open-access textbook explaining the fundamentals of causal inference.
- **Causal Inference: What If?** by Miguel Hernan and Jamie Robins (2024) - A comprehensive textbook on causal inference with an academic focus.

---

## Acknowledgments

This course was developed with partial support from the RCN-INTPART DTRF Project.  
https://www.bigdata.vestforsk.no/ongoing/intpart-dtrf
