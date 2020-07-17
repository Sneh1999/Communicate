import cv2
import imutils
import numpy as np

# background 
background = None


class Detection: 
    # To detect gestures
    def detect_gestures(image,weight):
        global background
        if background is None: 
            background = image.copy().astype("float")
        
        # compute weighted average ,accumulate it and update the background
        cv2.accumulateWeighted(image, background, weight)

    # Detect hand segment
    def detect_hand_segment(image,threshold=25):
        global background
        # find the absolute difference between background anc current frame
        diff = cv2.absdiff(background.astype("uint8"),image)
        # threshold the diff image so that we get the foreground
        threshold = cv2.threshold(diff,threshold,255,cv2.THRESH_BINARY)[1]
        # get the contours in the threshold image
        (cnts, _) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # return None, if no countours detected
        if len(cnts) == 0:
            return
        else:
            # based on countour area , get the maximum countour in which is th ehand
            segmented = max(cnts,key=cv2.contourArea)
            return (threshold,segmented)
