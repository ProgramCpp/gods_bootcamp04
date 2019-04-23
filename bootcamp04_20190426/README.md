# Course Plan Break Down

* S1 = 60 minutes each before lunch
* S2 = 75’ before lunch
* S3, S4 = 90 minutes each after lunch

## Day 1 - (Syafri, Anthony)
### S1 - Intro to DS GOJEK (Syafri)
* Who we are 
* What we believe
* Data Science use cases at GOJEK? 
* How to spot DS opportunities? 

### S2 - Enter Data Science - Light Theory (Syafri)
* AI - Big Data - Machine Learning 
* How all these three are related? 
* Machine Learning: 
	* What are different ML model classes
* Data Science Flow
* The three DS core. (Biz, Math, Coding)
* DS Problem formulation (northstar metrics to solve: BCR)
* ML 101 (Linear regression): (use Jupyter notebook for demo)
	* Parameter estimations: 
		* Loss minimization (intuitively)
		* Bias-Variance trade-offs 
	* Model Evaluation: 
		* Briefly about model evaluation

### S3 - Pandas + EDA (Anthony)
* Intro to Case Studies  15’
* Intro to Pandas (notebook)  45’ 
	* Definitions
	* Basic functions
	* Merging dataframes
* Intro to Data Visualization (notebook) 45’
	* Introducing matplotlib and seaborn with some basic charts
	* A bit more not so simple charts (with interaction, sankey flow, etc)

### S4 - Exercises (Anthony)
* Pandas Exercises
* Viz Exercises


## Day 2 - (Alam, Mitbal, Gibran)
*use collabs
### S1 - Regression (linear) (Alam) - 60’
	Keywords : Problem Definition, Correlation, IID, Practice
	Gradient Descent
### S2 - Classification (logistic, Tree based) (Iqbal) 60’
	Keywords : Problem Definition, Information Theory, Entropy, Type of Classification, Problem, Practice (add
### S3 - Ensemble, Feature Engineering, Feature selection (Gibran) 90’
* 40 mins - Feature Engineering & Feature Selection
* 50 mins - Ensemble learning (bagging & boosting) - hands on
	
	Keywords : Averaging model, OneHot, Bootstrap, Bagging, Boosting
	
### S4 - Evaluation & Exercise (Alam, Iqbal, Gibran) 90’
	Keywords : Cost Function, Bias-Variance-Trade Off, Cross Validation, F1 Score, Recall, (other metrics)
* Regression: using new dataset with non-poly linear reg + plot
* Classification: using new imbalanced dataset, discuss other classification metrics, also using medium dataset (F1 score, recall, etc)
* Ensemble: boosting (adaboost) hands-on, using medium dataset(bias-variance tradeoff)

## Day 3 - (Mannu, Darius)

### S1 - Unsupervised Learning
* 10 mins - Theory
* 50 mins - Guided K-Means algorithm creation (hands-on exercise)

### S2 - Unsupervised Learning 
* 60 mins - Application to K-Means on an image (hands-on exercise)
* 10 mins - Other unsupervised learning algorithms theory
* 5 mins - Homework explanation (wine data)

### S3 - “Neural Network 101” and “Advanced topics”
* 10 mins - Why an what for NN.
* 10 mins - What are computation graphs and derivations over computation graphs
* 30 mins: Hands on : Implement logistic regression in NN style.
* 10 mins: NN representation
* 5 mins: Activation functions
* 20 mins: Gradient descent and Backpropagation

### S4 - “Advanced topics continue” and “Practical approach”:
* 10 mins: continue Gradient descent and Backpropagation
* 10 mins: Initialization of weights
* 30 mins: Hands on: Implement shallow NN using python and numpy
* 10 mins: Explain homework, building blocks of DNN, forward and back prop for DNN
* 5 mins: Softmax regression
* 30 mins: Hands on: Softmax regression using Keras

## Day 4 (Dipta)
* S1 - Intro to the Kaggle problem, participants make group, start
* S2 - Kaggle-ing
* S4 - Presentation from the top 5 of the teams


# DS Bootcamp Environment Setup

For some module, you are required to install this environment.
For the rest, we will use Google Colab

#### Installing pyenv for python

For Mac:
```
brew install pyenv
```

For Ubuntu, you need to clone the repo.
```
cd
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Then, modify your environment variables.
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/<.bash_profile/.zshrc>
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/<.bash_profile/.zshrc>
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/<.bash_profile/.zshrc>
```
Note for *Ubuntu*, modify your `~/.bashrc` instead of `~/.bash_profile`.

Lastly, restart your shell so the path changes take effect.
```
exec "$SHELL"
```
* Refer to [pyenv](https://github.com/pyenv/pyenv#installation) for more details

#### Setting up the environment

Install dependencies:
(you have to be connected to Gojek Integration VPN in order to install dependencies from http://artifactory-gojek.golabs.io)

```
make env
```
