import cv2 as cv
#Class used for initialising a webcam object and capturing video feed.
class Webcam:
    def __init__(self, device=0):
        self.device = device
    
    #capture function
    def capture(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            #capture each frame
            ret, frame = cap.read()

            
            if not ret:
                print("Can't receive frame. Exiting...")
                break

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            #display resulting frame
            cv.imshow('frame',gray)
            #set q as quit key
            if cv.waitKey(1) == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows()