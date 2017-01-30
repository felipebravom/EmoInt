# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# evaluate.py
# Author: felipebravom
# Descrition: checks format and calculates Pearsons correlation WASSA-2017 Shared Task on Emotion Intensity (EmoInt)
# usage: python evaluate.py <number-of-pairs> <file-predictions-1> <file-gold-1> ..... <file-predictions-n> <file-gold-n>
# requires: numpy

import numpy
import sys
import scipy.stats
import math


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
                raise ValueError('Format problem.')
        
        
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
                    raise ValueError('Invalid tweet id.')
            else:
                raise ValueError('Format problem.')
            
            
        gold_scores=[]  
        pred_scores=[]
         
            
        for id in data_dic:
            if(len(data_dic[id])==2):
                gold_scores.append(data_dic[id][0])
                pred_scores.append(data_dic[id][1])
            else:
                raise ValueError('Repeated id in test data.')
                
      
        # return zero correlation if predictions are constant
        if numpy.std(pred_scores)==0 or numpy.std(gold_scores)==0:
            return (0,0)
        

        pears_corr=scipy.stats.pearsonr(pred_scores,gold_scores)[0]                                    
        spear_corr=scipy.stats.spearmanr(pred_scores,gold_scores)[0]                                
                                    
      
        return (pears_corr,spear_corr)
        
       
                                    
                          
        
    else:
        raise ValueError('Predictions and gold data have different number of lines.')

def main(argv):
    try:
        num_pairs=int(argv[0])
    except ValueError:
        raise ValueError('First parameter must be an integer.')
    
    
    if len(argv)!=num_pairs*2+1:
        raise ValueError('Invalid number of parameters.')

    pear_results=[]
    spear_results=[]
        
        
    for i in range(0,num_pairs*2,2):
        pred=argv[i+1]
        gold=argv[i+2]       
        result=evaluate(pred,gold)
        print "Pearsons correlation between "+pred+" and "+gold+":\t"+str(result[0])        
        pear_results.append(result[0])
        
        
        print "Spearman correlation between "+pred+" and "+gold+":\t"+str(result[1])        
        spear_results.append(result[1])
        
        
    avg_pear=numpy.mean(pear_results)
    avg_spear=numpy.mean(spear_results)
    
    print
    
    print "Average Pearsons correlation:\t"+str(avg_pear)
    print "Average Spearman correlation:\t"+str(avg_spear)
        
if __name__ == "__main__":
    main(sys.argv[1:])

 
    
     