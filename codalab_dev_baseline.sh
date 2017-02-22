

mkdir submission-dev

#### anger  ########

python tweets_to_arff.py data/anger-ratings-0to1.train.txt data/anger-ratings-0to1.train.arff

python tweets_to_arff.py data/anger-ratings-0to1.dev.target.txt data/anger-ratings-0to1.dev.target.arff



java -Xmx20G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/anger-ratings-0to1.train.arff -T data/anger-ratings-0to1.dev.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file submission-dev/anger-pred.txt" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToSparseFeatureVector -M 2 -I 3 -R -Q 3 -A -D 3 -E 5 -L -O -F -G 2 -I 2\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $WEKA_HOME/packages/AffectiveTweets/resources/w2v.twitter.edinburgh10M.400d.csv.gz -S 0 -K 20 -L -O\"  -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000

python fix_weka_output.py submission-dev/anger-pred.txt submission-dev/anger-pred.txt

#### fear  ########

python tweets_to_arff.py data/fear-ratings-0to1.train.txt data/fear-ratings-0to1.train.arff

python tweets_to_arff.py data/fear-ratings-0to1.dev.target.txt data/fear-ratings-0to1.dev.target.arff


java -Xmx20G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/fear-ratings-0to1.train.arff -T data/fear-ratings-0to1.dev.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file submission-dev/fear-pred.txt" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToSparseFeatureVector -M 2 -I 3 -R -Q 3 -A -D 3 -E 5 -L -O -F -G 2 -I 2\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $WEKA_HOME/packages/AffectiveTweets/resources/w2v.twitter.edinburgh10M.400d.csv.gz -S 0 -K 20 -L -O\"  -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000

python fix_weka_output.py submission-dev/fear-pred.txt submission-dev/fear-pred.txt


#### joy  ########

python tweets_to_arff.py data/joy-ratings-0to1.train.txt data/joy-ratings-0to1.train.arff

python tweets_to_arff.py data/joy-ratings-0to1.dev.target.txt data/joy-ratings-0to1.dev.target.arff


java -Xmx20G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/joy-ratings-0to1.train.arff -T data/joy-ratings-0to1.dev.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file submission-dev/joy-pred.txt" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToSparseFeatureVector -M 2 -I 3 -R -Q 3 -A -D 3 -E 5 -L -O -F -G 2 -I 2\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $WEKA_HOME/packages/AffectiveTweets/resources/w2v.twitter.edinburgh10M.400d.csv.gz -S 0 -K 20 -L -O\"  -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000

python fix_weka_output.py submission-dev/joy-pred.txt submission-dev/joy-pred.txt

#### sadness  ########

python tweets_to_arff.py data/sadness-ratings-0to1.train.txt data/sadness-ratings-0to1.train.arff

python tweets_to_arff.py data/sadness-ratings-0to1.dev.target.txt data/sadness-ratings-0to1.dev.target.arff


java -Xmx20G -cp $HOME/weka-3-8-1/weka.jar weka.Run weka.classifiers.meta.FilteredClassifier -t data/sadness-ratings-0to1.train.arff -T data/sadness-ratings-0to1.dev.target.arff -classifications "weka.classifiers.evaluation.output.prediction.CSV -use-tab -p first-last -file submission-dev/sadness-pred.txt" -F "weka.filters.MultiFilter -F \"weka.filters.unsupervised.attribute.TweetToSparseFeatureVector -M 2 -I 3 -R -Q 3 -A -D 3 -E 5 -L -O -F -G 2 -I 2\" -F \"weka.filters.unsupervised.attribute.TweetToLexiconFeatureVector -I 2 -A -D -F -H -J -L -N -P -Q -R -T -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToSentiStrengthFeatureVector -I 2 -U -O\" -F \"weka.filters.unsupervised.attribute.TweetToEmbeddingsFeatureVector -I 2 -B $WEKA_HOME/packages/AffectiveTweets/resources/w2v.twitter.edinburgh10M.400d.csv.gz -S 0 -K 20 -L -O\"  -F \"weka.filters.unsupervised.attribute.Reorder -R 5-last,4\"" -W weka.classifiers.functions.LibLINEAR -- -S 12 -C 1.0 -E 0.001 -B 1.0 -L 0.1 -I 1000

python fix_weka_output.py submission-dev/sadness-pred.txt submission-dev/sadness-pred.txt


## Create submission-dev file


cd submission-dev && zip ../submission-dev.zip * && cd .. && rm -r submission-dev
