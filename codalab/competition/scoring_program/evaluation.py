#!/usr/bin/env python
import sys
import os.path
import scipy.stats
import numpy


def evaluate(pred,gold):
    
    f=open(pred, "rb")
    pred_lines=f.readlines()
    f.close()
    
    f=open(gold, "rb")
    gold_lines=f.readlines()
    f.close()
    

    if(len(pred_lines)==len(gold_lines)):       
        # align tweets ids with gold scores and predictions
        data_dic={}
        
        for line in gold_lines:
            parts=line.split('\t')
            if len(parts)==4:   
                data_dic[int(parts[0])]=[float(line.split('\t')[3])]
            else:
                sys.exit('Format problem.')
        
        
        for line in pred_lines:
            parts=line.split('\t')
            if len(parts)==4:  
                if int(parts[0]) in data_dic:
                    try:
                        data_dic[int(parts[0])].append(float(line.split('\t')[3]))
                    except ValueError:
                        # Invalid predictions are replaced by a default value
                        data_dic[int(parts[0])].append(0.5)
                else:
                    sys.exit('Invalid tweet id.')
            else:
                sys.exit('Format problem.')
            
        
        # lists storing gold and prediction scores
        gold_scores=[]  
        pred_scores=[]
         
        
        # lists storing gold and prediction scores where gold score >= 0.5
        gold_scores_range_05_1=[]
        pred_scores_range_05_1=[]
            
        for id in data_dic:
            if(len(data_dic[id])==2):
                gold_scores.append(data_dic[id][0])
                pred_scores.append(data_dic[id][1])
                
                if(data_dic[id][0]>=0.5):
                    gold_scores_range_05_1.append(data_dic[id][0])
                    pred_scores_range_05_1.append(data_dic[id][1])
                
            else:
                sys.exit('Repeated id in test data.')
                
      
        # return zero correlation if predictions are constant
        if numpy.std(pred_scores)==0 or numpy.std(gold_scores)==0:
            return (0,0,0,0)
        

        pears_corr=scipy.stats.pearsonr(pred_scores,gold_scores)[0]                                    
        spear_corr=scipy.stats.spearmanr(pred_scores,gold_scores)[0]                                
                                    
        
        pears_corr_range_05_1=scipy.stats.pearsonr(pred_scores_range_05_1,gold_scores_range_05_1)[0]                                    
        spear_corr_range_05_1=scipy.stats.spearmanr(pred_scores_range_05_1,gold_scores_range_05_1)[0]           
        
      
        return (pears_corr,spear_corr,pears_corr_range_05_1,spear_corr_range_05_1)
       
                                    
                          
        
    else:
        sys.exit('Predictions and gold data have different number of lines.')
        
        


def main(argv):
    #https://github.com/Tivix/competition-examples/blob/master/compute_pi/program/evaluate.py
    # as per the metadata file, input and output directories are the arguments

    [input_dir, output_dir] = argv
    
    # unzipped submission data is always in the 'res' subdirectory
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    
    
    anger_truth_path = os.path.join(input_dir, 'ref', 'anger-gold.txt')
    fear_truth_path = os.path.join(input_dir, 'ref', 'fear-gold.txt')
    joy_truth_path = os.path.join(input_dir, 'ref', 'joy-gold.txt')
    sadness_truth_path = os.path.join(input_dir, 'ref', 'sadness-gold.txt')
    
    
    anger_submission_path = os.path.join(input_dir, 'res', 'anger-pred.txt')
    if not os.path.exists(anger_submission_path):
        sys.exit('Could not find submission file {0}'.format(anger_submission_path))

    fear_submission_path = os.path.join(input_dir, 'res', 'fear-pred.txt')
    if not os.path.exists(fear_submission_path):
        sys.exit('Could not find submission file {0}'.format(fear_submission_path))
        
        
    joy_submission_path = os.path.join(input_dir, 'res', 'joy-pred.txt')
    if not os.path.exists(joy_submission_path):
        sys.exit('Could not find submission file {0}'.format(joy_submission_path))    
        
        
    sadness_submission_path = os.path.join(input_dir, 'res', 'sadness-pred.txt')
    if not os.path.exists(sadness_submission_path):
        sys.exit('Could not find submission file {0}'.format(sadness_submission_path))      
    

    
    
    anger_scores=evaluate(anger_submission_path, anger_truth_path)
    fear_scores=evaluate(fear_submission_path, fear_truth_path)    
    joy_scores=evaluate(joy_submission_path, joy_truth_path)
    sadness_scores=evaluate(sadness_submission_path, sadness_truth_path)
    
    
    avg_pearson=numpy.mean([anger_scores[0],fear_scores[0],joy_scores[0],sadness_scores[0]])
    avg_spearman=numpy.mean([anger_scores[1],fear_scores[1],joy_scores[1],sadness_scores[1]])
    
    avg_pearson_range_05_1=numpy.mean([anger_scores[2],fear_scores[2],joy_scores[2],sadness_scores[2]])
    avg_spearman_range_05_1=numpy.mean([anger_scores[3],fear_scores[3],joy_scores[3],sadness_scores[3]])
    
    # the scores for the leaderboard must be in a file named "scores.txt"
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    
    output_file=open(os.path.join(output_dir, 'scores.txt'),"w")

 
    output_file.write("avg_pearson:{0}\n".format(avg_pearson)) 
    output_file.write("avg_spearman:{0}\n".format(avg_spearman))
    

    output_file.write("anger_pearson:{0}\n".format(anger_scores[0])) 
    output_file.write("anger_spearman:{0}\n".format(anger_scores[1]))
    

    output_file.write("fear_pearson:{0}\n".format(fear_scores[0])) 
    output_file.write("fear_spearman:{0}\n".format(fear_scores[1]))
    
    output_file.write("joy_pearson:{0}\n".format(joy_scores[0])) 
    output_file.write("joy_spearman:{0}\n".format(joy_scores[1]))
    
    output_file.write("sadness_pearson:{0}\n".format(sadness_scores[0])) 
    output_file.write("sadness_spearman:{0}\n".format(sadness_scores[1]))
    
    
    
    output_file.write("avg_pearson_range_05_1:{0}\n".format(avg_pearson_range_05_1)) 
    output_file.write("avg_spearman_range_05_1:{0}\n".format(avg_spearman_range_05_1))
    

    output_file.write("anger_pearson_range_05_1:{0}\n".format(anger_scores[2])) 
    output_file.write("anger_spearman_range_05_1:{0}\n".format(anger_scores[3]))
    

    output_file.write("fear_pearson_range_05_1:{0}\n".format(fear_scores[2])) 
    output_file.write("fear_spearman_range_05_1:{0}\n".format(fear_scores[3]))
    
    output_file.write("joy_pearson_range_05_1:{0}\n".format(joy_scores[2])) 
    output_file.write("joy_spearman_range_05_1:{0}\n".format(joy_scores[3]))
    
    output_file.write("sadness_pearson_range_05_1:{0}\n".format(sadness_scores[2])) 
    output_file.write("sadness_spearman_range_05_1:{0}\n".format(sadness_scores[3]))
    
    
    
    
    output_file.close()
    
 
    
    
if __name__ == "__main__":
    main(sys.argv[1:])    
    
    