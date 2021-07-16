import cv2
  
  #face classifiers
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')  
  # grab webcam
webcam = cv2.VideoCapture(0)
while True:
    successful_frame_read,frame = webcam.read()
    if not successful_frame_read:
      break
    
    #change into grayscale
    frame_grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
    #detect faces
    faces = face_detector.detectMultiScale(frame_grayscale,scaleFactor=1.7,minNeighbors=4)
    
    # print(faces)
    for (x,y,w,h) in faces:
    #   #draw a rectangle around face
      cv2.rectangle(frame,(x,y),(x+w,y+h),(100,200,50),4)
      # the_face = (x,y,w,h)
      the_face = frame[y:y+h,x:x+w]
      face_grayscale = cv2.cvtColor(the_face,cv2.COLOR_BGR2GRAY)

      smiles = smile_detector.detectMultiScale(face_grayscale,scaleFactor=1.7,minNeighbors=40)
      # for(x1,y1,w1,h1) in smiles:

      #   # draw rectangle around the smile
      #   cv2.rectangle(the_face,(x1,y1),(x1+w1,y1+h1),(150,50,200),2)
      if len(smiles)>0:
        cv2.putText(frame,'Smiling',(x,y+h+40),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(255,255,255))  
    # run smile detactor within those faces
    
    cv2.imshow('Default',frame)
    cv2.waitKey(1)