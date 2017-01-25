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
# felipebravom
# Running example: python evaluate.py data/wekapredictions.csvfixed data/anger-ratings-0to1.test.gold.tsv

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
      
        
        pred_scores=[]
        gold_scores=[]
        
        for line in pred_lines:
            parts=line.split('\t')
            if len(parts)==4:     
                  pred_scores.append(float(line.split('\t')[3]))
            else:
                raise ValueError('Format problem.')
            
            
        for line in gold_lines:
            parts=line.split('\t')
            if len(parts)==4:   
                gold_scores.append(float(line.split('\t')[3]))
            else:
                raise ValueError('Format problem.')
            
        
        pears_corr=numpy.corrcoef(pred_scores, gold_scores)[0, 1]
        print "Pearsons correlation\t"+str(pears_corr)+"\n"
        
    else:
        raise ValueError('Predictions and gold data have different number of lines')

def main(argv):
    pred=argv[0]
    gold=argv[1]
    evaluate(pred,gold)  
        
if __name__ == "__main__":
    main(sys.argv[1:])

 
    
     