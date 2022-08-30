# converting mpeg4 files into frames
#https://www.opcito.com/blogs/extracting-text-from-images-with-tesseract-ocr-opencv-and-python 
#https://medium.com/analytics-vidhya/targeted-ocr-on-documents-with-opencv-and-pytesseract-edc10b5ecb62

import cv2
import time
import os


def extractDateStringFromFrame(frame):
    # import pytesseract
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    # print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))

    # get dimensions of image
    dimensions = frame.shape
    
    # height, width, number of channels in image
    height = frame.shape[0]
    width = frame.shape[1]
    channels = frame.shape[2]
    
    print('Image Dimension    : ',dimensions)
    print('Image Height       : ',height)
    print('Image Width        : ',width)
    print('Number of Channels : ',channels)


    subsetImage = frame[425:465, 110:340]

    #cv2.imshow('Image', subsetImage)
    #cv2.waitKey(0) 

    gray_image = cv2.cvtColor(subsetImage, cv2.COLOR_BGR2GRAY)

    # threshold_img = gray_image

    gray_image =cv2.GaussianBlur(gray_image, (3,3), 0)

    ret, threshold_img = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)

    # threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # display image

    cv2.imshow('threshold image', threshold_img)
    # Maintain output window until user presses a key

    cv2.waitKey(0)

    # Destroying present windows on screen

    cv2.destroyAllWindows()


    import pytesseract
    # pytesseract.pytesseract.tesseract_cmd = r'/home/azureuser/MpegProcessorWithObjectDetetion/MpegProcessor/.venv/bin/pytesseract'
    # sudo apt install tesseract-ocr, for the following to work
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    print(pytesseract.image_to_string(threshold_img))
    print(pytesseract.image_to_string(threshold_img, lang='eng', config=r'--psm 6 -c tessedit_char_whitelist=0123456789./'))
    print(pytesseract.image_to_string(threshold_img, lang='eng', config=r'--psm 12 -c tessedit_char_whitelist=0123456789./'))
    print(pytesseract.image_to_string(threshold_img, config=r'--psm 12 -c tessedit_char_whitelist=0123456789./'))
    print(pytesseract.image_to_string(threshold_img, config=r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789./'))
    print(pytesseract.image_to_string(threshold_img, config=r'--psm 10 -c tessedit_char_whitelist=0123456789./'))
    print(pytesseract.image_to_string(threshold_img, config=r'--psm 1 --oem 3  -c tessedit_char_whitelist=0123456789./'))

    return







def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        # extract Date from the Frame 
        extractDateStringFromFrame(frame)
        # cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1) or ( count > 2 )):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":

    input_loc = './Data/2022-08-23 14-03-48.mp4'
    output_loc = '/Data/Output/'
    video_to_frames(input_loc, output_loc)