## Class 5 Homework: Bias-Variance Tradeoff

Read this excellent article, [Understanding the Bias-Variance Tradeoff](http://scott.fortmann-roe.com/docs/BiasVariance.html), and be prepared to **discuss it in class** on Monday.

**Note:** You can ignore sections 4.2 and 4.3.

Here are some questions to think about while you read:
* In the Party Registration example, what are the features? What is the response? Is this a regression or classification problem?
	* Answer: the features or 'wealth' and 'religiousness'; the response is 'voter party registration'
* Conceptually, how is KNN being applied to this problem to make a prediction?
	* It is essentially takes the "average" of the k nearest neighbors and assigns that value in the prediction.
	* Or, to use a voting analogy, the k nearest neighbors 'vote' for their type, and the majority assigns their type to the point in question
* How do the four visualizations in section 3 relate to one another? Change the value of K using the slider, and make sure you understand what changed in the visualizations (and why it changed).
	* As k increases, the number of points taken into account increases. This makes the model less sensitive to outliers thus decreasing the variance
* In figures 4 and 5, what do the lighter colors versus the darker colors mean? How is the darkness calculated?
	* The shade of the colors signals the outcome of the knn vote. For example, a dark shade of blue means the most or all of the neighbors are democrats, where as a light shade would mean that some republicans were also included in the vote (but democrats had more) - it is a probability measure
* What  does the black line in figure 5 represent? What predictions would an ideal machine learning model make, with respect to this line?
	* The black line represents the line that was used to create the data. It is the "true" decision boundary. An ideal machine learning model would assign all points above the line to republicans, and all point below the line to democrats.
* Choose a very small value of K, and click the button "Generate New Training Data" a number of times. Do you "see" low variance or high variance? Do you "see" low bias or high bias?
	* I see higher variance. The color map changes pretty dramatically with each model. As k inreases, the model seems to move away from teh boundary line, which suggests higher bias
* Repeat this with a very large value of K. Do you "see" low variance or high variance? Do you "see" low bias or high bias?
	*
* Try using other values of K. What value of K do you think is "best"? How do you define "best"?
	* 
* Why should we care about variance at all? Shouldn't we just minimize bias and ignore variance?
	* 
* Does a high value for K cause "overfitting" or "underfitting"?
	* A high value of K leads to underfitting. It makes very "safe" predictions and isn't very sensitive to changes in the underlying training data.
