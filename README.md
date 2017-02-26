# EmoInt
Scripts for for the  [WASSA-2017](http://optima.jrc.it/wassa2017/) Shared Task on Emotion Intensity [(EmoInt)](http://saifmohammad.com/WebPages/EmotionIntensity-SharedTask.html).  


## 1. Evaluation Script
The evaluation script [evaluate.py](evaluate.py) calculates the following four measures between the gold standard scores and the given predictions. 
 1. Pearson_0_1: corresponds to the [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) caclualted between all the predicions and the gold instances.
 2. Spearman_0_1: corresponds to the [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient) caclualted between all the predicions and the gold instances.
 3. Pearson_05_1: corresponds to the Pearson correlation between predictions and gold instances where the gold score is greater than or equal to 0.5. 
 4. Separman_05_1: corresponds to the Spearman correlation between predictions and gold instances where the gold score is greater than or equal to 0.5. 
 
The script can receive multiple pairs of prediction and gold standard files. In case of receiving more than one pair, it will compute the average Pearson and Spearman correlation. Note that the average Pearson_0_1 obtained for the four emotions (anger, fear, joy and sadness) is the bottom-line competition metric and that remainder metrics are only given as a reference.


### 1.1. Prerequisites
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [numpy](http://www.numpy.org/)
* [SciPy](http://www.scipy.org/)

### 1.2. Usage


 ```bash
python evaluate.py <number-of-pairs> <file-prediction-1> <file-gold-1> ..... <file-prediction-n> <file-gold-n>
```

Example:

 ```bash
python evaluate.py 4 anger-pred.txt anger-gold.txt fear-pred.txt fear-gold.txt joy-pred.txt joy-gold.txt sadness-pred.txt sadness-gold.txt
```

### 1.3. Format
Each input file must have the following format: id[tab]tweet[tab]emotion[tab]score. The script will complain in case of receiving a file with wrong format. 

If you want to use the script purely a format checker, evaluate your predictions against themselves:

 ```bash
python evaluate.py 1 anger-pred.txt anger-pred.txt
```

## 2. Weka Baseline System
We have implemented a [WEKA](http://www.cs.waikato.ac.nz/~ml/weka/) package called [AffectiveTweets](https://github.com/felipebravom/AffectiveTweets) to be used as a baseline system. The package allows calculating multiple features from a tweet. Installation instructions are given in the project's [webpage](https://github.com/felipebravom/AffectiveTweets#installation). Make sure to install the LibLinear and RankCorrelation packages before running the baselines.  

We have also implemented the [tweets_to_arff.py](tweets_to_arff.py) script for converting the task data into [arff](http://weka.wikispaces.com/ARFF) format, and the [fix_weka_output.py](fix_weka_output.py) script for converting weka predictions into the official submission format.   


### 2.1. Example

1. Convert training and target data for the anger emotion into arff format:

 ```bash
python tweets_to_arff.py data/anger-ratings-0to1.train.txt data/anger-ratings-0to1.train.arff
python tweets_to_arff.py data/anger-ratings-0to1.test.target.txt data/anger-ratings-0to1.test.target.arff
```
 If testing data hasn't been provided yet, you can split the training file into training and testing sub-samples. 

2. Train an SVM regression (from LibLinear) on the training data using lexicons, SentiStrength, and word embeddings as features, classify the target tweets, and output the predictions:

 ```bash
java -Xmx4G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/anger-ratings-0to1.train.arff -T data/anger-ratings-0to1.test.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file data/anger-predictions.csv" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $HOME/wekafiles/packages/AffectiveTweets/resources/w2v.twitter.edinburgh.100d.csv.gz -S 0 -K 15 -L -O\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000 
```

 Make sure that the LibLinear Weka package has been properly installed. 

3. Convert the predictions into the task format:

 ```bash
python fix_weka_output.py data/anger-pred.txt data/anger-pred.txt
 ```
 
4. Evaluate the predictions: 
 
 ```bash
python evaluate.py 1 data/anger-pred.txt data/anger-ratings-0to1.test.gold.txt
 ```
 
### 2.2. Another example
  Next, we show another example using all the features supported by the baseline system: word n-grams, character n-grams, Brown word clusters, POS tags, lexicons, SentiStrengh, and word embeddings.  In this case we are using word embeddings trained from a large corpus of tweets that can be downloaded [here](https://github.com/felipebravom/AffectiveTweets/releases/download/1.0.0/w2v.twitter.edinburgh10M.400d.csv.gz). Replace the step 2 from the previous example by the following command:
 
  ```bash
java -Xmx8G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/anger-ratings-0to1.train.arff -T data/anger-ratings-0to1.test.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file data/anger-predictions.csv" -F "weka.filters.MultiFilter -F  \"weka.filters.unsupervised.attribute.TweetToSparseFeatureVector -M 2 -I 3 -R -Q 3 -A -D 3 -E 5 -L -O -F -G 2 -I 2\" -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $HOME/wekafiles/packages/AffectiveTweets/resources/w2v.twitter.edinburgh10M.400d.csv.gz -S 0 -K 15 -L -O\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000 
```
 
 
### 2.3 Cross-validation
There is also possible to obtain cross-validated performance results using Weka. 
 * In the following example, we train an SVM regression using lexicon features and we omit the testing file (-T) for obtaining cross-validated results: 

  ```bash
java -Xmx4G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/anger-ratings-0to1.train.arff  -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000 
```

## 3. CodaLab
A valid submission file for Codalab is a zip compressed file containing the following files:

1. anger-pred.txt
2. fear-pred.txt
3. joy-pred.txt
4. sadness-pred.txt

Each of these files must follow the official submission [format](#13-format). An example of submission file for the development data can be downloaded [here](submission-dev.zip). The predictions were obtained using the Weka baseline system with the configuration used in the example from Section [2.2](#22-another-example). 
A reference bash code for building this submission file from scratch is provided [here](codalab_dev_baseline.sh).

