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
import sys
    
    
    

def split_dataset(file_name,out_name):
    """
    Splits a dataset into training and testing datasets using a split parameter
    """
    f=open(file_name, "rb")
    lines=f.readlines()
    f.close()
   
    
         
    out=open(out_name,"w")    
   
    
    for line in lines:
        parts=line.split("\t")
        trans_line = '\t'.join([parts[0],parts[1],parts[2],str(1-float(parts[3].strip()))+'\n'])
        out.write(trans_line)

           
        
        
  
    
    
    out.close()
    
   

    
    
    
    
def main(argv):  
     split_dataset(argv[0],argv[1])


if __name__ == '__main__':
    main(sys.argv[1:])

    