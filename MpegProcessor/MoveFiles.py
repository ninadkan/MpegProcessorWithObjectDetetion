#Move files between two numbers 
import argparse
import os
import time


def countNumberOfFilesInEachFolder(sourceFolder):
    for root, dirs, files in os.walk(sourceFolder):
        print ("Number of files in {0} folder = {1}".format(root, str(len(files)) ) )
    return


def moveFiles(  sourceFolder,
                destinationFolder,
                imageLabel,
                partialInputFileName,
                partialInputFileNameExtension,
                startFileNumber,
                endFileNumber,
                deleteFile = False):
    '''
    This python function moves a collection of files to a specified destination folder \r\n
    The destination folder, if one level does not exist is created \r
    sourceFolder = Location from where the files need to be copied, end with a '/', \n
    destinationFolder = Destination location; end with a '/' \n
    imageLabel = Destination folder name that will signify the image label \n
    partialInputFileName = start name of the file \n
    partialInputFileNameExtension = extension of the file name that is to be copied \v
    startFileNumber = start file number \n
    endFileNumber = end file number. This number is not executed \n
    deleteFile = set to true to remove the file, else it moves the file
    Function returns the number of files successfully moved \n
    '''

    try:
        os.mkdir(destinationFolder + str(imageLabel))
    except OSError:
        pass

    newDestinationFolderName = destinationFolder + str(imageLabel) + '/'
    print ("New destination folder = " + newDestinationFolderName)

    for count in range(startFileNumber, endFileNumber):
        countNumber = "%#06d" % (count)
        sourceFileName = sourceFolder + partialInputFileName + countNumber + partialInputFileNameExtension
        if (deleteFile):
            os.remove(sourceFileName)
        else:
            destinationFileName = newDestinationFolderName + partialInputFileName + countNumber + partialInputFileNameExtension
            os.rename(sourceFileName, destinationFileName)
    return (endFileNumber - startFileNumber)


if __name__ == "__main__":
    # # # parser = argparse.ArgumentParser(
    # # #     description=__doc__,
    # # #     formatter_class=argparse.RawTextHelpFormatter,
    # # #     usage='use "%(prog)s --help" for more information'
    # # # )

    # # # parser = argparse.ArgumentParser(description=__doc__,
    # # #                 formatter_class=argparse.RawDescriptionHelpFormatter)
    # # # parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
    # # # subparsers = parser.add_subparsers(dest="command")
    # # # process_parser = subparsers.add_parser("moveFiles", help=moveFiles.__doc__)

    # # # process_parser.add_argument("sourceFolder", nargs='?',  help="Source Folder")
    # # # process_parser.add_argument("destinationFolder", nargs='?', help="Destination Folder")
    # # # process_parser.add_argument("imageLabel", nargs='?', help="Image  Label")
    # # # process_parser.add_argument("partialInputFileName", nargs='?', help="Partial Input File Name")
    # # # process_parser.add_argument("partialInputFileNameExtension", nargs='?', default='.jpg', help="Partial Input File Name")
    # # # process_parser.add_argument("startFileNumber", nargs='?', default=000000, help="Start File Numner")
    # # # process_parser.add_argument("endFileNumber", nargs='?',default=000000, help="End File Number")
    
    # # # args = parser.parse_args()
    # # # if args.command == "moveFiles":

    # # #     # Log the time
    # # #     time_start = time.time()

    # # #     numberOfFilesMoved = moveFiles( sourceFolder = args.sourceFolder,
    # # #                                     destinationFolder = args.destinationFolder,
    # # #                                     imageLabel = args.imageLabel,
    # # #                                     partialInputFileName = args.partialInputFileName,
    # # #                                     partialInputFileNameExtension = args.partialInputFileNameExtension,
    # # #                                     startFileNumber = args.startFileNumber,
    # # #                                     endFileNumber = args.endFileNumber)

    # # #     print ("")


    # # # #usage python3 MoveFile.py "./Data/Output/Cassette1/0/" "./labelledImages/" 8 "2022-08-22 20-04-13 Date - " ".jpg" 0 210   

    # # #     # Log the time
    time_start = time.time()


    # itemList = []
    # # itemList.append (tuple([1,1904,11, False, "Date"]))
    # # itemList.append (tuple([1904,3049,25, False, "Date"]))
    # # itemList.append (tuple([3049,3917,2, False, "Date"]))
    # # itemList.append (tuple([3917,6000,8, False, "Date"]))
    # # itemList.append (tuple([6000,9802,8, True, "Date"]))
    # # itemList.append (tuple([9802,14000,11, False, "Date"]))
    # # itemList.append (tuple([14000,17224,11, True, "Date"]))
    # # itemList.append (tuple([17224,22000,12, False, "Date"]))
    # # itemList.append (tuple([22000,31758,12, True, "Date"]))
    # # itemList.append (tuple([31758,34864,14, False, "Date"]))
    # # itemList.append (tuple([34864,34973,8, False, "Date"]))
    # # itemList.append (tuple([34973,39000,17, False, "Date"]))
    # # itemList.append (tuple([39000,43005,17, True, "Date"]))
    # # itemList.append (tuple([43005,48829,19, False, "Date"]))
    # # itemList.append (tuple([48829,53816,20, False, "Date"]))
 
    # # itemList.append (tuple([1, 3049,9 , False, "Month"]))
    # # itemList.append (tuple([3049,3917 ,10 , False, "Month"]))
    # # itemList.append (tuple([3917, 6000, 11, False, "Month"]))
    # # itemList.append (tuple([6000,50000 ,11 , True, "Month"]))
    # # itemList.append (tuple([50000,53816 , 11, True, "Month"]))
 
    # # itemList.append (tuple([1, 4000,2004 ,False , "Year"]))
    # # itemList.append (tuple([4000,40000 , 2004,True , "Year"]))
    # # itemList.append (tuple([40000,44000 , 2004,False , "Year"]))
    # # itemList.append (tuple([44000,53816 ,2004 ,True , "Year"]))
    
    # for i, item in enumerate(itemList):
 
    #     startFileNumber=item[0]
    #     endFileNumber = item[1]
    #     imageLabel= item[2]
    #     deleteFile = item[3]


    #     numberOfFilesMoved = moveFiles(     sourceFolder=  "./Data/Output/Cassette1/8/" ,# "./Data/Output/" , # "./Data/Output/Cassette1/0/",
    #                                         destinationFolder= "./labelledImages/",
    #                                         imageLabel= imageLabel,
    #                                         partialInputFileName= "2022-08-22 21-05-52 " + item[4] + " - " ,
    #                                         partialInputFileNameExtension=".jpg" ,
    #                                         startFileNumber=startFileNumber ,
    #                                         endFileNumber = endFileNumber,
    #                                         deleteFile = deleteFile)

 
    #     print(" Total files moved = {0} , start File Numner = {1}, End file number = {2}".\
    #                                 format(str(numberOfFilesMoved), str(startFileNumber), str(endFileNumber)))  
    # 
     
    time_end = time.time()
    elapsedTime = time_end-time_start
    print("Elapsed time = " + time.strftime("%H:%M:%S", time.gmtime(elapsedTime))) 


    countNumberOfFilesInEachFolder("./labelledImages/")