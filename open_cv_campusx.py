import numpy as np
import cv2
#Read an Image
img = cv2.imread("C:/Users/Nikhil Sharma/Pictures/Screenshots/Screenshot 2023-09-23 193915.png")
#cv2.imshow("window",img)
#cv2.waitKey(0)
#Convert to grayscale
grey_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#print(grey_image.shape)
#cv2.imshow("window",grey_image)
#cv2.waitKey(0)
#Image Resizing
img_resize = cv2.resize(img,(3002,3000))
#Flipping images
img_flip = cv2.flip(img,0)
#Cropping an image
img_crop = img[0:300,0:300]
#saving an image
cv2.imwrite("nishant_first_saved.jpg",img_crop)
#Drawing shapes and texts on images
image_zero = np.zeros((500,500,3))
#Drawing Rectangle
cv2.rectangle(image_zero,pt1 = (100,100),pt2 = (300,300),color = (255,0,0),thickness = -1) #use -1 for filling the rectangle
#DRawing Circle
cv2.circle(image_zero,center=(400,400),radius = 60,thickness=2,color = (0,23,0))
#Drawing line
cv2.line(image_zero,pt1 = (12,42),pt2 = (320,300),thickness = 2,color= (12,34,43))
#Adding text
cv2.putText(image_zero,org = (300,300),fontScale=20,color = (0,234,233),text = "Hello",fontFace=cv2.FONT_ITALIC)
#Working with open cv events
# Draw circles on images
'''def draw(event,x,y,flags,params):
    if event==0:
        print("hovering")
    if event ==1:
        cv2.circle(img_events,center=(x,y),radius = 15,color = (0,0,255),thickness =-1)
    if event==4:
        print("mouse released")
cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
img_events = np.zeros((512,512,3))
while True:
    cv2.imshow("window",img_events)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break
cv2.destroyAllWindows()'''
#Draw a rectangle when you drag the mouse
'''img_event = np.zeros((5120,5120,3))
flag= False
ix = -1
iy = -1
def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        flag = True
        ix = x
        iy =y
    elif event==0:
        if flag==True:
            cv2.rectangle(img_event,pt1= (ix,iy) ,pt2 = (x,y),color = (0,0,255) ,thickness = 1)
    elif event==4:
        flag=False
        cv2.rectangle(img_event, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 0), thickness=1)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",draw)
while True:
    cv2.imshow("window",img_event)
    if cv2.waitKey(1) & 0xFF==ord("x"):
        break
cv2.destroyAllWindows()'''
#Building a cropping tool
'''flag= False
ix =-1
iy=-1
def crop(event,x,y,flags,parmas):
    global flag,ix,iy
    if event==1:
        flag =True
        ix =x
        iy= 1
    elif event==4:
        flag= False
        cv2.rectangle(img,pt1 = (ix,iy),pt2 = (x,y),color = (0,0,134),thickness=2)
        cropped_img = img[iy:y,ix:x]
        cv2.imshow("new_win",cropped_img)
        cv2.waitKey(0)

cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF==ord("a"):
        break
cv2.destroyAllWindows()'''
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output11.avi', fourcc, 20.0, (640,  480))

while True:
    ret,frame = cap.read()
    out.write(frame)
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
    cv2.imshow("webcam",img_gray)
    if cv2.waitKey(1) & 0xFF==ord("x"):
        break
out.release()
cv2.destroyAllWindows()