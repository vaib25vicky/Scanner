# Scanner
Simple Document Scanner made with python and openCV

## How it works?
1) Take original image and resize it.
2) Perform Gaussian Blur to smooth the image.
3) Apply Canny Edge Detection technique.
4) Apply Contour Detection to detect largest contour/boundary.
5) Apply Perspective Transform and Adaptive Thresholding.

## Usage:

 ```
 python scan.py --image <path-to-your-file>
 
 ````
 
 ## Credits 
 My sincere thanks to the article and the author here : https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/.
 He article really ease the process and is well explained.

