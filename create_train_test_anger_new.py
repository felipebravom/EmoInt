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

# create_train_test.py
# felipebravom

import math
import random
import operator

    
def map_ids(train,dev,test,anger_new):
    train_map={}
    dev_map={}
    test_map={}


    max_id=1    
    
    with open(train, "rb") as f:
        lines=f.readlines()
        for line in lines:
            train_map[line.split("\t")[1]]=line
            t_id=int(line.split("\t")[0])
            max_id = t_id if t_id > max_id else max_id                 
                      
        f.close()
        
    
    with open(dev, "rb") as f:
        lines=f.readlines()
        for line in lines:
            dev_map[line.split("\t")[1]]=line            
            t_id=int(line.split("\t")[0])
            max_id = t_id if t_id > max_id else max_id
        f.close()
    
    with open(test, "rb") as f:
        lines=f.readlines()
        for line in lines:
            test_map[line.split("\t")[1]]=line            
            t_id=int(line.split("\t")[0])
            max_id = t_id if t_id > max_id else max_id
                     
        f.close()
        
        
        
    train_file=open('anger-ratings-0to1.train.txt',"w")
    dev_target_file=open('anger-ratings-0to1.dev.target.txt',"w")
    dev_gold_file=open('anger-ratings-0to1.dev.gold.txt',"w")
    test_target_file=open('anger-ratings-0to1.test.target.txt',"w")
    test_gold_file=open('anger-ratings-0to1.test.gold.txt',"w")
    
#    id=start_id
#    
#    for line in train_dict:
#        parts=line[0].split('\t')
#        train_file.write(str(id)+'\t'+parts[0]+'\t'+emotion+'\t'+parts[1])
#        id+=1
#    train_file.close()
        
    other_count=0

        
    with open(anger_new, "rb") as f:
        train_lines=[]
        dev_target_lines=[]
        dev_gold_lines=[]
        test_target_lines=[]
        test_gold_lines=[]
        
        
        lines=f.readlines()
        for line in lines:
            parts=line.split("\t")
            
            if train_map.has_key(parts[0]):
                old_train_line=train_map[parts[0]]
                old_id=old_train_line.split("\t")[0]
                train_lines.append((old_id,('\t'.join([old_id,parts[0],'anger',parts[1]]))))     
                
               # print "TRAIN"
            elif dev_map.has_key(parts[0]):
                old_dev_line=dev_map[parts[0]]
                old_id=old_dev_line.split("\t")[0]
                
                dev_gold_lines.append((old_id,('\t'.join([old_id,parts[0],'anger',parts[1]]))))  
                dev_target_lines.append((old_id,('\t'.join([old_id,parts[0],'anger','NONE\n']))))  
                
                
#                dev_gold_file.write('\t'.join([old_id,parts[0],'anger',parts[1]]))  
#                dev_target_file.write('\t'.join([old_id,parts[0],'anger','NONE']))
                
                
                #print "DEV"
            elif test_map.has_key(parts[0]):
                old_test_line=test_map[parts[0]]
                old_id=old_test_line.split("\t")[0]
                
                test_gold_lines.append((old_id,('\t'.join([old_id,parts[0],'anger',parts[1]]))))  
                test_target_lines.append((old_id,('\t'.join([old_id,parts[0],'anger','NONE\n'])))) 
                
#                test_gold_file.write('\t'.join([old_id,parts[0],'anger',parts[1]]))  
#                test_target_file.write('\t'.join([old_id,parts[0],'anger','NONE']))
                
                
                #print "TEST"
            else:
                other_count+=1
                print "other"
                print line
        f.close()
        
        train_lines=sorted(train_lines, key=lambda x: x[0])
        dev_target_lines=sorted(dev_target_lines, key=lambda x: x[0])
        dev_gold_lines=sorted(dev_gold_lines, key=lambda x: x[0])
        test_target_lines=sorted(test_target_lines, key=lambda x: x[0])
        test_gold_lines=sorted(test_gold_lines, key=lambda x: x[0])
        

        print len(test_target_lines),test_target_lines


        for line in train_lines:
            train_file.write(line[1])        
            
            
        
        for line in dev_target_lines:
            dev_target_file.write(line[1])                          
            
        for line in dev_gold_lines:
            dev_gold_file.write(line[1])
            
            
        for line in test_target_lines:
            test_target_file.write(line[1])
            
            
        for line in test_gold_lines:
            test_gold_file.write(line[1])
    

    
    train_file.close()
    dev_target_file.close()
    dev_gold_file.close()
    test_target_file.close()
    test_gold_file.close()
    

def split_dataset(file_name,split,emotion,start_id):
    """
    Splits a dataset into training and testing datasets using a split parameter
    """
    f=open(file_name, "rb")
    lines=f.readlines()
    f.close()
    
    # Group tweets starting with the same tokens in lists 
    prefix_keys={}
    for line in lines:
        parts=line.split("\t")
        text=parts[0]
        tokens=text.split(" ")
        prefix=tokens[0:int(math.ceil(len(tokens)*0.5))]
        prefix_hash=hash(str(prefix))  
        
        if prefix_hash in prefix_keys:
            prefix_keys[prefix_hash].append(line)
        else:
            prefix_keys[prefix_hash]=[line]
            
    
   

    # creates dicts with scores as keys    
    train_dict={}
    test_instances=[]

    
      
    # initliazes the random object
    random.seed(a=1)
    # separtes random and testing using reservoir sampling
    for key in prefix_keys:
        r=random.random()
        if r<=split:
            for line in prefix_keys[key]:
                train_dict[line]=float(line.split('\t')[1])
        else:
            for line in prefix_keys[key]:
                test_instances.append(line)
            
            
    #sort by score
    train_dict = sorted(train_dict.items(), key=operator.itemgetter(1),reverse=True)
            
            
    train_file=open(emotion+'-ratings-0to1.train.tsv',"w")
    
 
    id=start_id
    
    for line in train_dict:
        parts=line[0].split('\t')
        train_file.write(str(id)+'\t'+parts[0]+'\t'+emotion+'\t'+parts[1])
        id+=1
    train_file.close()
    

    test_file_gold=open(emotion+'-ratings-0to1.test.gold.tsv',"w")   
    
    test_file_target=open(emotion+'-ratings-0to1.test.target.tsv',"w")    
        
    for line in test_instances:
        parts=line.split('\t')
        test_file_gold.write(str(id)+'\t'+parts[0]+'\t'+emotion+'\t'+parts[1])
        test_file_target.write(str(id)+'\t'+parts[0]+'\t'+emotion+'\tNONE\n')
        id+=1
    
    
    test_file_gold.close()
    
    
    
    


if __name__ == '__main__':
    file_name="data/sadness-ratings-0to1-clean.txt" 
    old_train="data/final_data/anger-ratings-0to1.train.txt"
    old_dev="data/final_data/anger-ratings-0to1.dev.gold.txt"
    old_test="data/final_data/anger-ratings-0to1.test.gold.txt"
    
    anger_new="data/anger-ratings-0to1-v2.txt"
    
    
    map_ids(old_train,old_dev,old_test, anger_new)
    #split_dataset(file_name,0.53,'sadness',40000)

    