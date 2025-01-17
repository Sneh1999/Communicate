from detect import Detection as detect
import cv2
import imutils

if __name__ == "__main__":

    # initialize weight for running average
    aWeight = 0.5

    #  get the refrence to webcam
    camera = cv2.VideoCapture(0)


    # Region of intrest coordinates
    top,right,bottom,left = 10,350,225,590


    # initialize num of frames
    num_frames = 0

    # keep logging, until intrerupted
    while(True):
        # get the current frame
        (grabbed,frame) = camera.read()

        # resize the frame 
        frame = imutils.resize(frame,width=700)

        # flip the frame so that it is not a mirror view
        frame = cv2.flip(frame,1)

        # clone the frame
        clone = frame.copy()

        # get the height and width of the frame
        (height,width) = frame.shape[:2]

        # get the ROI
        roi = frame[top:bottom,right:left]

        # convert the roi to grayscale and blur it
        gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # to get the background, keep looking till a threshold is reached
        # so that our running average model gets calibrated
        if num_frames < 30:
            detect.detect_gestures(gray,aWeight)
        
        else:
            # segment the hand section
            hand = detect.detect_hand_segment(gray)
            #  check whether hand region is segmented
            if hand is not None:
                #  if yes, unpack the threshold image and segmented region
                (threshold,segmented) = hand
                # draw the segmented region and display the frame
                cv2.drawContours(clone, [segmented + (right, top)], -1, (0, 0, 255))
                cv2.imshow("Thesholded", threshold)
        

        #  draw the segmented hand
        cv2.rectangle(clone,(left,top),(right,bottom),(0,255,0),2)


        #  increment the number of frames
        num_frames +=1
        #  display the frame with segmented hand
        cv2.imshow("Video Feed",clone)

        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF

        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            break

# free up memory
camera.release()
cv2.destroyAllWindows()






