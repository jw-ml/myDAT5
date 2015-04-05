#Using machines to separate HAM from SPAM
####DAT5 Project Proposal
Question. Can we predict whether an email is spam based on the text of that email?

I would like to apply machine learning and data science techniques to separate spam from ham. Additionaly, through this project, I hope to learn how to extract information from text-based data, how to convert text into a useful feature set for purposes of mahcine learning, and to make predictions about whether an email is spam or ham without hard-coding specific rules.

Data:
  * This project will use a [subset of the Enron email corpus and some know spam email](http://www.aueb.gr/users/ion/data/enron-spam/)
  * Specifically, this project will use the email in its raw form

(Initial) project workplan:
  * Extract and process data using the Natural Language Toolkit [(nltk)](http://www.nltk.org/) for python
  * Use scikit-learn to apply different machine learning techniques to the data, such as Naive Bayes, Support Vector Machines, K-nearest neighbors, etc.
  * Revisit data extraction stage to see how incorporating additional text processing techniques affect prediction ability. Such feature may include filtering out stop words, stemming words back to a root word, and applying weights to words based on frequency (or something)
  * Revisit analysis by further refining feature set and by applying dimesion reduction techniques.
