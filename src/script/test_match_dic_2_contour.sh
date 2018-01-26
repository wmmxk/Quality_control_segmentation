#!/bin/bash
dataDir=$(dirname $(dirname $PWD))/final_data
contourPath=$dataDir/contourfiles
dicPath=$dataDir/dicoms
outputDir=$(dirname $dataDir)/out_data/tmp

source activate py3

#loop through the lines in link.csv file except the firston
# three arguments are constructed 
sed 1d $dataDir/link.csv | while IFS=',' read dicID contourID
do
	 currentContourPath=$contourPath/$contourID
   for contourFile in `ls $currentContourPath/i-contours/ |head -n 10`
   do
		  dicFolder=$dicPath/$dicID 
      contourFilePath=$currentContourPath/i-contours/$contourFile
			outFile=$outputDir/${dicID}_${contourFile:3:-19}
			python ../../src/libs/match_dic_2_contour.py  $dicFolder $contourFilePath  $outFile 
	  done
done
