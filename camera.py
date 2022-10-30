import cv2

vid = cv2.VideoCapture(0)

while True:

    ret, frame = vid.read()
    cv2.imshow('Orencio Camera', frame)
    cv2.resize()

    if cv2.waitKey(4) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()