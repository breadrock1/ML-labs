# Machine Learning Labs

![GitHub](https://badgen.net/badge/icon/github?icon=github&label)
![version](https://img.shields.io/badge/version-1.0-blue)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)

Machine Learning. This is set of laboratory tasks of Machine Learning.

## Contents

- [What is ML](#whatis)
- [Labs](#labs)
	* [Lab 1 - Method of nearest neighbors](#lab_1)
	* [Lab 2 - Pipelines and backup](#lab_2)
	* [Lab 3 - Linearias and Regressions](#lab_3)
	* [Lab 4 - Trees](#lab_4)
	* [Lab 5 - Neural networks](#lab_5)
	* [Lab 6 - NLP](#lab_6)


## <a name="whatis"/> What is Machine Learning?

Machine learning (ML) is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence. Machine learning algorithms build a model based on sample data, known as training data, in order to make predictions or decisions without being explicitly programmed to do so. Machine learning algorithms are used in a wide variety of applications, such as in medicine, email filtering, speech recognition, and computer vision, where it is difficult or unfeasible to develop conventional algorithms to perform the needed tasks.

A subset of machine learning is closely related to computational statistics, which focuses on making predictions using computers; but not all machine learning is statistical learning. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a related field of study, focusing on exploratory data analysis through unsupervised learning. Some implementations of machine learning use data and neural networks in a way that mimics the working of a biological brain. In its application across business problems, machine learning is also referred to as predictive analytics.

Lits and useful links:
  
- [Introduction to ML](https://habr.com/ru/post/448892/)
- [ML project-walkthrough by @WillKoehrsen](https://github.com/WillKoehrsen/machine-learning-project-walkthrough)
- [Used dataset of Heart Disease UCI](https://www.kaggle.com/ronitf/heart-disease-uci)


## <a name="labs"/> Labs

### <a name="lab_1"/> Laboratory № 1 - KNN

To manipulate your data set by analogy with those considered: data preprocessing, predictions using the method of nearest neighbors.	

### <a name="lab_2"/> Laboratory № 2 - Pipeline and backup

Select and justify a quality metric. Try several machine learning methods from sklearn, see which method is best suited in the context of the selected metric (so far without selecting hyper parameters). Optimize KNN according to metric. Wrap all previous actions with data (conversion, normalization, etc. - from the first and second labs) in Pipeline and save the resulting model in pickle.

### <a name="lab_3"/> Laboratory № 3 - Linearias and Regressions 

Train logistic regression on your data, select the parameters. Compare the results of applying L1 and L2 regularizations. View the weights of signs, explain the obtained values. Perform feature selection using L1 regularization, select the optimal C, explain the result.

### <a name="lab_4"/> Laboratory № 4 - Trees

Verify the instability of a single tree on its data. Select the most important traits by random forest, compare the result with the selection of traits by a linear method with L1 -regulation. Compare the performance of a random forest without cross-validation with cross-validation. Compare the quality of work and the training time (% time at the beginning of the cell) of the forest with gradient boosting over decision trees, choosing the optimal parameters for each. It will be especially good if you train gradient boosting on a video card.

### <a name="lab_5"/> Laboratory № 5 - Neural networks

Collect a set of photos of your team members. Train the neuron so that she will classify the new photos of the participants well.

### <a name="lab_6"/> Laboratory № 6 - NLP

Classify Russian texts into several categories. It is best if the body of the texts is really large. To pre-process texts: normalization, lemmatization, etc. Compare embeddings. Try several classification methods.


