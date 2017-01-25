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

# fix_weka_output.py
# felipebravom
# Running example: python fix_weka_output.py data/wekapredictions.csv data/wekapredictionsfixed.csv
import sys

def fix_output(input_file,output_file):
    """
    Fixes the output of a Weka classifier
    """
    f=open(input_file, "rb")
    lines=f.readlines()
    f.close()
    
    out=open(output_file,"w") 
    for line in lines[1:len(lines)]:
        parts=line.split("\t")
        if len(parts)==7:
            out.write(parts[4]+'\t'+parts[5][1:len(parts[5])-1]+'\t'+parts[6].strip()+'\t'+parts[2]+'\n')
    out.close()
            
    
   
    
def main(argv):
    input_file=argv[0]
    output_file=argv[1]
    fix_output(input_file,output_file)
   
        
if __name__ == "__main__":
    main(sys.argv[1:])
