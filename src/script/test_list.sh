#!/bin/bash
dataDir=$(dirname $(dirname $PWD))/final_data
contourPath=$dataDir/contourfiles
dicPath=$dataDir/dicoms
outputDir=$(dirname $dataDir)/out_data/tmp

sed 1d $dataDir/link.csv | while IFS=',' read dicID contourID
do
	 currentContourPath=$contourPath/$contourID
   for contourFile in `ls $currentContourPath/i-contours/ |head -n 1`
   do
		  dicFolder=$dicPath/$dicID 
      contourFilePath=$currentContourPath/$contourFile
			outFile=$outputDir/${dicID}_${contourFile:3:-19}.jpg
			echo $dicFolder $contourFilePath  $outFile 
	  done
done
