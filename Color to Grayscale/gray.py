# Load opencv module
import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.
# The default resolutions
# are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object. The output is
# stored in 'output.avi' file.

out = cv2.VideoWriter('output.avi',
                      cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                      10, (frame_width,frame_height))

ret, prev_frame = cap.read()

while(True):
    ret, frame = cap.read()

    if ret:
        red = frame[:,:, 0]
        green = frame[:,:, 1]
        blue = frame[:,:, 2]
        gray = 0.21 * red + 0.72 * green + 0.07 * blue
        gray_image = frame
        for i in range(3):
            gray_image[:,:,i] = gray
        # Write the frame into the file 'output.avi'

        frame_diff = cv2.absdiff(gray_image, prev_frame)

        out.write(gray_image)
        print(gray_image.dtype)
        print(frame.shape)
        print(gray_image.shape)

        # Display the resulting frame
        cv2.imshow('Frame_diff', frame_diff)
        prev_frame = gray_image.copy()
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done,
# release the video capture and write objects
cap.release()
out.release()

# Closes all the frames
cv2.destroyAllWindows()

