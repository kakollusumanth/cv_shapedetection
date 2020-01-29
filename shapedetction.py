import cv2
import numpy as np
shapes=cv2.imread(r'C:\poly.jpg')
gray=cv2.imread(r'C:\poly.jpg',0)
_,trash=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(trash,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print(str(len(contours)))
for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    cv2.drawContours(shapes,[approx],0,(255,0,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    if len(approx)==3:
        cv2.putText(shapes,'Triangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),4)
    if len(approx)==4:
        cv2.putText(shapes,'rectangle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.51,(0,0,255),4)
    if len(approx)==5:
        cv2.putText(shapes,'pentagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.51,(0,0,255),4)
    if len(approx)==6:
        cv2.putText(shapes,'hexagon',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.51,(0,0,255),4)
    else:
        cv2.putText(shapes,'circle',(x,y),cv2.FONT_HERSHEY_COMPLEX,0.51,(0,0,255),4)
        
    #print(contour,approx)
    #print('abcdef')
    #print(cv2.arcLength(contour,True))
    
cv2.imshow('shapes',shapes)
cv2.waitKey(0)
cv2.destroyAllWindows()
