# converting mpeg4 files into frames
#https://www.opcito.com/blogs/extracting-text-from-images-with-tesseract-ocr-opencv-and-python 
#https://medium.com/analytics-vidhya/targeted-ocr-on-documents-with-opencv-and-pytesseract-edc10b5ecb62

import cv2
import time
import os
import numpy
import pytesseract
import datetime as dt
import pandas as pd

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


subscription_key = os.getenv('subscription_key')
endpoint= os.getenv('endpoint')



FRAMES_PER_SECOND=-1
TRANSITION_FRAMES=3 # When dates transition check three frames before and after. 
DATA_LIST = []

def extractString(subsetImage, output_loc, count, imageFileName, imageType, imageWrite = False, displayImage=False):
    numberDetected = 0
    # gray_image = cv2.cvtColor(subsetImage, cv2.COLOR_BGR2GRAY)

    # # threshold_img = gray_image

    # # gray_image =cv2.GaussianBlur(gray_image, (3,3), 0)

    # # ret, threshold_img = cv2.threshold(gray_image,127,255,cv2.THRESH_TOZERO)

    # # threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)[1]


    # count_white = numpy.sum(threshold_img > 0)
    # count_black = numpy.sum(threshold_img == 0)
    # if count_black > count_white:
    #     threshold_img = 255 - threshold_img

    # threshold_img = cv2.copyMakeBorder(threshold_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 255, 255))

    # # threshold_img=cv2.Canny(threshold_img,100,200) 

    # if (displayImage):

    #     # display image
    #     cv2.imshow('threshold image', threshold_img)
    #     #Maintain output window until user presses a key

    #     cv2.waitKey(0)

    #     #Destroying present windows on screen

    #     cv2.destroyAllWindows()

    # if (imageWrite):
    #     fileNameMinusExtension = imageFileName.partition('.')[0] # drop the .mpg extension
    #     cv2.imwrite(output_loc + fileNameMinusExtension + " " + imageType + "%#06d.jpg" % (count+1), threshold_img)
    
    # # pytesseract.pytesseract.tesseract_cmd = r'/home/azureuser/MpegProcessorWithObjectDetetion/MpegProcessor/.venv/bin/pytesseract'
    # # sudo apt install tesseract-ocr, for the following to work
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    # # print("1  " + pytesseract.image_to_string(threshold_img))
    # # print("2  " + pytesseract.image_to_string(threshold_img, lang='eng', config=r'--psm 6 -c tessedit_char_whitelist=0123456789/'))
    # # print("3  " + pytesseract.image_to_string(threshold_img, lang='eng', config=r'--psm 12 -c tessedit_char_whitelist=0123456789/'))
    # # print("4  " + pytesseract.image_to_string(threshold_img, config=r'--psm 12 -c tessedit_char_whitelist=0123456789/'))
    # # print("5  " + pytesseract.image_to_string(threshold_img, config=r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/'))
    # # print("6  " + pytesseract.image_to_string(threshold_img, config=r'--psm 10 -c tessedit_char_whitelist=0123456789/'))
    # # print("7" + pytesseract.image_to_string(threshold_img, config=r'--psm 1 --oem 3  -c tessedit_char_whitelist=0123456789/'))
    # numberDetected = pytesseract.image_to_string(threshold_img, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    # # print("Number detected = " + numberDetected)
    return numberDetected

def extractDateStringFromFrame(frame, output_loc, imageFileName):
    # # import pytesseract
    # # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    # # print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))

    # # # get dimensions of image
    # # dimensions = frame.shape
    
    # # # height, width, number of channels in image
    # # height = frame.shape[0]
    # # width = frame.shape[1]
    # # channels = frame.shape[2]
    
    # # print('Image Dimension    : ',dimensions)
    # # print('Image Height       : ',height) 
    # # print('Image Width        : ',width)
    # # print('Number of Channels : ',channels)


    # # subsetImage = frame[425:465, 110:340]
    # # Image height = 576 - (460-500), width = 720 (110:160, 170:225, 240:330)

    # subsetImage = frame[455:505, 110:330]   # minimum size has to be 50X50
    # # gray_image = cv2.cvtColor(subsetImage, cv2.COLOR_BGR2GRAY)
    # # threshold_img = cv2.copyMakeBorder(gray_image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=(255, 255, 255))

    # fileNameMinusExtension = imageFileName.partition('.')[0]
    # jpgFileName = fileNameMinusExtension + ".jpg"

    # outputfilename = os.path.join(output_loc, jpgFileName)
    # print("output file name =" + outputfilename)
    # cv2.imwrite(outputfilename, subsetImage)

    
    # # SubsetImageDate = frame[460:500, 110:160]
    # # SubsetImageMonth = frame[460:500, 170:225]
    # # subsetImageYear = frame[460:500, 240:330]

    # # recognize_printed_text_in_stream(outputfilename)
    # recognize_text(outputfilename)
    
    # # strDate = str.strip(extractString(SubsetImageDate, output_loc, count, imageFileName, "Date - ", imageWrite=True))
    # # strMonth = str.strip(extractString(SubsetImageMonth, output_loc, count, imageFileName, "Month - ", imageWrite=True))
    # # strYear = str.strip(extractString(subsetImageYear, output_loc, count, imageFileName, "Year - ", imageWrite=True))

    # # print (" count = " + str(count + 1) + ": Date = " + strDate +"/" + strMonth + "/" + strYear)
    return

def recognize_text(outputfilename):
    """RecognizeTextUsingRecognizeAPI.
    This will recognize text of the given image using the recognizeText API.
    The file name of the image is provided. 
    """
    line_text = ""
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    with open(outputfilename, "rb") as image_stream:
        job = client.recognize_text_in_stream(
            image=image_stream,
            mode="Printed",
            raw=True
        )
    operation_id = job.headers['Operation-Location'].split('/')[-1]

    image_analysis = client.get_text_operation_result(operation_id)
    while image_analysis.status in ['NotStarted', 'Running']:
        time.sleep(1)
        image_analysis = client.get_text_operation_result(
            operation_id=operation_id)

    #print("Job completion is: {}\n".format(image_analysis.status))

    #print("Recognized:\n")
    lines = image_analysis.recognition_result.lines
    # print(lines[0].words[0].text)  # "make"
    
    for line in lines:
        line_text = " ".join([word.text for word in line.words])
    # print("Date extracted = " + line_text)
    return line_text

def appendToGlobalList(     frameNumber , 
                            extractedDate,
                            formattedDate):
 
    global DATA_LIST
    global FRAMES_PER_SECOND


    elapsedSeconds, remainingFrames = divmod(frameNumber, FRAMES_PER_SECOND)
    m,s = divmod(elapsedSeconds, 60)
    h, m = divmod(m, 60)


    hour = "%#02d" % (h)
    minutes = "%#02d" % (m)
    seconds = "%#02d" % (elapsedSeconds)
    framesRem = "%#02d" % (remainingFrames)

    thisdict =	{
            "Frame Number" : frameNumber,
            "DateTime Extracted" : extractedDate ,
            "Formatted Date": formattedDate.strftime("%d %b %Y"),
            "Elpsed Time From Origin" : hour + ":" + minutes + ":" + seconds + ":" +framesRem
    }

    print (thisdict)

    DATA_LIST.append(thisdict)

    return 

def isStringDate(stringDate, frameNumber):
    bRv = False
    fmt ="%d/%m/%Y"
    # print("checking if its a string = " + stringDate)
    parsedDateTime = None
    try:
        parsedDateTime = dt.datetime.strptime(stringDate, fmt)
        appendToGlobalList(frameNumber=frameNumber, extractedDate=stringDate, formattedDate=parsedDateTime)
        bRv = True
    except ValueError as err:
        pass

    return bRv, parsedDateTime

def createSubImageAndSave(frame, output_loc, imageFileName, frameNumber ):
    subsetImage = frame[455:505, 110:330]   # minimum size has to be 50X50
    fileNameMinusExtension = imageFileName.partition('.')[0] # get the file name minus the extension
    jpgFileName = fileNameMinusExtension + ".jpg"

    outputfilename = os.path.join(output_loc, jpgFileName)
    # print("output file name =" + outputfilename)
    cv2.imwrite(outputfilename, subsetImage)
    returnedDate = recognize_text(outputfilename)
    brv = False
    parsedDateTime = None
    if (    isinstance(returnedDate, str) 
            and len(returnedDate) > 0):
        returnedDate = returnedDate.strip()
        returnedDate = returnedDate.replace('.', '/')
        returnedDate = returnedDate.replace(' ', '')
        brv, parsedDateTime = isStringDate(returnedDate, frameNumber)
    return brv, parsedDateTime

def findChangeOverFrameNumber(  cap, 
                                output_loc, 
                                imageFileName,
                                frameCount, 
                                numberOfFrameIncrementsPerIteration,
                                currentCapturedTime):

    changeOverFrameNumber = frameCount


    startPosition = int(frameCount) - int(numberOfFrameIncrementsPerIteration)
    startPosition = 0 if startPosition < 0 else startPosition

    maxIndex  = int(frameCount) + int(numberOfFrameIncrementsPerIteration)
    step = int(FRAMES_PER_SECOND)

    if (numberOfFrameIncrementsPerIteration < FRAMES_PER_SECOND ):
        step = 1


    bExitLoop = False


    for x in range (startPosition, maxIndex, step): 
        print ("x = {0}".format(str(x)))
        cap.set(cv2.CAP_PROP_POS_FRAMES, x)
        ret, frame = cap.read() # for the first time, we set that to the first instance. Next one will vary
        if not ret:
            continue
        brv, parsedDateTime = createSubImageAndSave(frame, output_loc, imageFileName, frameNumber=x)
        if (brv):
            if (parsedDateTime != currentCapturedTime):
                if (step == 1): # we are already single stepping
                    changeOverFrameNumber = x
                    print("Found the change-over frame = {0}, date found = {1}".format(str(changeOverFrameNumber), str(parsedDateTime)))
                    break
                else:
                    startIndex = 0 if (x-step < 0) else (x-step)
                    for y in range (startIndex, x): # 
                        print ("y = {0}".format(str(y)))
                        cap.set(cv2.CAP_PROP_POS_FRAMES, y)
                        ret, frame = cap.read() # for the first time, we set that to the first instance. Next one will vary
                        if not ret:
                            continue
                        brv, parsedDateTime = createSubImageAndSave(frame, output_loc, imageFileName, frameNumber=y)
                        if (brv):
                            if (parsedDateTime != currentCapturedTime ):
                                changeOverFrameNumber = y
                                print("Found the change-over frame = {0}, date found = {1}".format(str(changeOverFrameNumber), str(parsedDateTime)))
                                bExitLoop = True
                                break
                            else:
                                pass
                        else:
                            pass
                    if (bExitLoop): # for the external loop
                        break
            else:
                pass
        else:
            print("Date time returned error within the for loop. Continuing!!!")

    return changeOverFrameNumber

def video_to_frames(input_loc, output_loc, imageFileName):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """

    global DATA_LIST
    global FRAMES_PER_SECOND

    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()

    DATA_LIST = []


    # Find OpenCV version

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')


    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_frame_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_frame_length)

    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
    if int(major_ver)  < 3 :
        FRAMES_PER_SECOND = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(FRAMES_PER_SECOND))
    else :
        FRAMES_PER_SECOND = cap.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(FRAMES_PER_SECOND))


    video_Time = float(cap.get(cv2.CAP_PROP_POS_MSEC))
    print ("Video Time : ", str(video_Time)) # this time is displayed in what number; This returns 0.0 
    actualVideo_Time = float(video_frame_length/FRAMES_PER_SECOND)

    print ("True Video Time in seconds : ", str(actualVideo_Time)) 

    number_of_msec_per_frame = float(1000/FRAMES_PER_SECOND)
    print ("Number of msec per frame : ", str(number_of_msec_per_frame))

    NumberOfSecondsIncrementPerSuccessfulIteration = 20 # increment X seconds per iteration. 
    numberOfFrameIncrementsPerIteration = FRAMES_PER_SECOND* NumberOfSecondsIncrementPerSuccessfulIteration

    frameCount = 0
    currentCapturedTime = dt.datetime.min #set it to (1,1,1,0,0)
    globalVideoTime = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read() # for the first time, we set that to the first instance. Next one will vary
        if not ret:
            continue
        # Write the results back to output location.
        # extract Date from the Frame 
        # cv2.imwrite(output_loc + "/%#05d.jpg" % (frameCount+1), frame)
        # frameCount = frameCount + 1
        # If there are no more frames left
        if (frameCount >= (video_frame_length)):
        #if (frameCount > (video_frame_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % frameCount)
            print ("It took %d seconds forconversion." % (time_end-time_start))

            dfOut = pd.DataFrame(DATA_LIST)
            fileNameMinusExtension = imageFileName.partition('.')[0]
            outputFolderPathFileName= output_loc + fileNameMinusExtension + ".csv"
            dfOut.to_csv(outputFolderPathFileName, index=False)
            break
        else:
            # now we set the Frames to grow by the number of seconds that we want to increment
            # ???
            currentVideoTime = cap.get(cv2.CAP_PROP_POS_MSEC)
            # print("Current Video Time =", str(currentVideoTime))
            brv, parsedDateTime = createSubImageAndSave(frame, output_loc, imageFileName, frameNumber=frameCount)

            if (brv):
                if (currentCapturedTime == dt.datetime.min ): # first time
                    currentCapturedTime = parsedDateTime
                else:   # we've found a date different from our existing date
                    if (currentCapturedTime == parsedDateTime): 
                        pass
                    else:
                        print("Date time change found!!! Need to find changeover point and start from there")
                        findChangeOverFrameNumber(  cap, output_loc, imageFileName,
                                                    frameCount, 
                                                    numberOfFrameIncrementsPerIteration,
                                                    currentCapturedTime)
                        currentCapturedTime = parsedDateTime
            else:
                print("Parsing Date time returned error")

            frameCount += numberOfFrameIncrementsPerIteration 

            if (frameCount > (video_frame_length-1)): # ensure that we are not getting out of bound
                frameCount = video_frame_length
                cap.set(cv2.CAP_PROP_POS_FRAMES, frameCount-1)
            else:
                cap.set(cv2.CAP_PROP_POS_FRAMES, frameCount)


if __name__=="__main__":
    #input_loc = './Data/2022-08-23 14-03-48.mp4'
    # input_loc = './Data/2022-08-23 14-32-54.mp4'
    inputFolder = '/home/azureuser/MpegProcessorWithObjectDetetion/MpegProcessor/Data/Cassette1/'

    # get list of Files

    from os import listdir
    from os.path import isfile, join
    fileNames = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))] # extract filename from a folder

    numberOfIterations = 1 # controls our execution to check that code is working, then set this to a very big number
    for i, imageFileName in enumerate(fileNames):
        if ((numberOfIterations > 0) and (i > numberOfIterations)):
            break; # come of of the loop
        filename = os.path.join(inputFolder, imageFileName)
        output_loc = './Data/Cassette1/Output/' + str(i) + '/'
        video_to_frames(filename, output_loc, imageFileName)