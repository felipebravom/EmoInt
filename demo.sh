


python tweets_to_arff.py data/anger-ratings-0to1.train.tsv data/anger-ratings-0to1.train.arff
python tweets_to_arff.py data/anger-ratings-0to1.test.target.tsv data/anger-ratings-0to1.test.target.arff

java -Xmx4G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/anger-ratings-0to1.train.arff -T data/anger-ratings-0to1.test.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file data/wekapredictions.csv" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $HOME/wekafiles/packages/AffectiveTweets/resources/w2v.twitter.edinburgh.100d.csv.gz -S 0 -K 15 -L -O\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000 

python fix_weka_output.py data/wekapredictions.csv data/wekapredictionsfixed.csv

python evaluate.py data/wekapredictionsfixed.csv data/anger-ratings-0to1.test.gold.tsv
