import cv2
import easyocr
import matplotlib.pyplot as plt
import os

# Read image
img_path = os.path.join('..', 'data', 'speed_limit.png')
img = cv2.imread(img_path)

# Initialize reader
# just use the easyocr.Reader() function to initialize the reader.
reader = easyocr.Reader(['en'], gpu=False) ## I do not have a GPU in my computer

# Detect text
result = reader.readtext(img)

## Print result
for r in result:
    bbox, text, prob = r # bbox is the bounding box of the text, text is the text detected, and prob is the probability of the detection.

    ## set the threshold for the probability of the detection
    if prob > 0.5:
        ## convert bbox float to int
        points = [(int(pt[0]), int(pt[1])) for pt in bbox]
        ## draw bounding box
        cv2.rectangle(img, points[0], points[2], (0, 0, 255), 2)
        
        ## put text
        ## cv2.putText(img, text, location, font, fontScale, color, thickness)
        cv2.putText(img, text, points[0], cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
    
    
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.show()
## show with cv2
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()