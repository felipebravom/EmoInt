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

# tweets_to_arff.py
# Author: felipebravom
# Descrition: checks format and calculates Pearsons correlation WASSA-2017 Shared Task on Emotion Intensity (EmoInt)
# usage: python evaluate.py <file-predictions> <file-gold>
# requires: numpy

import numpy
import sys


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
                
      
        
        cov=numpy.cov(pred_scores, gold_scores)[0, 1]
        sd_pred=numpy.std(pred_scores)
        
        #Replace zero standard deviation values
        sd_pred= sd_pred if sd_pred != 0 else 1
        
        sd_gold=numpy.std(gold_scores)
        sd_gold= sd_gold if sd_gold != 0 else 1

        pears_corr=cov/(sd_pred*sd_gold)
        
        print "Pearsons correlation\t"+str(pears_corr)+"\n"
                                    
                          
        
    else:
        raise ValueError('Predictions and gold data have different number of lines.')

def main(argv):
    pred=argv[0]
    gold=argv[1]
    evaluate(pred,gold)  
        
if __name__ == "__main__":
    main(sys.argv[1:])

 
    
     