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

import math


def create_arff(file_name):
    """
    Creates an arff dataset
    """
    
    

    header='@relation '+file_name+'\n\n@attribute content string\n@attribute score numeric \n\n@data\n'
    out=open(file_name+'.arff',"w")
    out.write(header)

       
    f=open(file_name, "rb")
    lines=f.readlines()
    for line in lines:
        parts=line.split("\t")
        if len(parts)==2:
     
            message=parts[0]
            label=parts[1].strip()
            line='\"'+message+'\",'+label+'\n'
            out.write(line)
    

    f.close()  
    out.close()  
    
    
    

def split_dataset(file_name,split):
    """
    Splits a dataset into training and testing datasets using a split parameter
    """
    f=open(file_name, "rb")
    lines=f.readlines()
    
    cut_off=int(math.ceil(len(lines)*split))
    
    train=open(file_name+'.train',"w")
    for line in lines[1:cut_off]:
        train.write(line)
    train.close()
    
    test=open(file_name+'.test',"w")
    for line in lines[cut_off+1:len(lines)]:
        test.write(line)
    test.close()
    
    
    
    


if __name__ == '__main__':
    file_name="data/anger-ratings-0to1.txt" 
    split_dataset(file_name,0.5)
    create_arff(file_name)
    create_arff(file_name+'.train')
    create_arff(file_name+'.test')
    
    