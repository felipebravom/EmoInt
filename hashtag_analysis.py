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

# hashtag_analysis.py
# felipebravom


import sys
import math
    
    
    

def hashtag_analysis(input_file, output_file):
    """
    Splits a dataset into training and testing datasets using a split parameter
    """
    f=open(input_file, "rb")
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
            
            
    out=open(output_file,"w")
    out.write('original_tweet\tscore_or\thashtag-removed_tweets\tscore_nohash\n')
    for key in prefix_keys:
        if len(prefix_keys[key])>=2:
            tweets=prefix_keys[key]
            tweets.sort(lambda x,y: cmp(len(x), len(y)), reverse=True)
            line=str()
            for tweet in tweets:
                
                line += tweet[0:(len(tweet)-1)]+'\t'
            
            out.write(line[0:(len(line)-1)]+'\n')
            
    out.close()
            
    
   

    
    
    


def main(argv):
    input_file=argv[0]
    output_file=argv[1]
    hashtag_analysis(input_file,output_file)
   
        
if __name__ == "__main__":
    main(sys.argv[1:])    

    