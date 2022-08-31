#Move files between two numbers 
import argparse
import os
import time


def moveFiles(  sourceFolder,
                destinationFolder,
                imageLabel,
                partialInputFileName,
                partialInputFileNameExtension,
                startFileNumber,
                endFileNumber):
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
        print ("Source File = " + sourceFileName)
        destinationFileName = newDestinationFolderName + partialInputFileName + countNumber + partialInputFileNameExtension
        print ("Destination File = " + destinationFileName)
        os.rename(sourceFileName, destinationFileName)
    return count


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #     description=__doc__,
    #     formatter_class=argparse.RawTextHelpFormatter,
    #     usage='use "%(prog)s --help" for more information'
    # )

    # parser = argparse.ArgumentParser(description=__doc__,
    #                 formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
    # subparsers = parser.add_subparsers(dest="command")
    # process_parser = subparsers.add_parser("moveFiles", help=moveFiles.__doc__)

    # process_parser.add_argument("sourceFolder", nargs='?',  help="Source Folder")
    # process_parser.add_argument("destinationFolder", nargs='?', help="Destination Folder")
    # process_parser.add_argument("imageLabel", nargs='?', help="Image  Label")
    # process_parser.add_argument("partialInputFileName", nargs='?', help="Partial Input File Name")
    # process_parser.add_argument("partialInputFileNameExtension", nargs='?', default='.jpg', help="Partial Input File Name")
    # process_parser.add_argument("startFileNumber", nargs='?', default=000000, help="Start File Numner")
    # process_parser.add_argument("endFileNumber", nargs='?',default=000000, help="End File Number")
    
    # args = parser.parse_args()
    # if args.command == "moveFiles":

    #     # Log the time
    #     time_start = time.time()

    #     numberOfFilesMoved = moveFiles( sourceFolder = args.sourceFolder,
    #                                     destinationFolder = args.destinationFolder,
    #                                     imageLabel = args.imageLabel,
    #                                     partialInputFileName = args.partialInputFileName,
    #                                     partialInputFileNameExtension = args.partialInputFileNameExtension,
    #                                     startFileNumber = args.startFileNumber,
    #                                     endFileNumber = args.endFileNumber)

    #     print ("")


    # #usage python3 MoveFile.py "./Data/Output/Cassette1/0/" "./labelledImages/" 8 "2022-08-22 20-04-13 Date - " ".jpg" 0 210   

    #     # Log the time
    time_start = time.time()
    numberOfFilesMoved = moveFiles(     sourceFolder="./Data/Output/Cassette1/0/",
                                        destinationFolder= "./labelledImages/",
                                        imageLabel= 8,
                                        partialInputFileName= "2022-08-22 20-04-13 Date - " ,
                                        partialInputFileNameExtension=".jpg" ,
                                        startFileNumber=1,
                                        endFileNumber =210)

    time_end = time.time()
    elapsedTime = time_end-time_start
    print("Elapsed time = " + time.strftime("%H:%M:%S", time.gmtime(elapsedTime))+ " Total files moved = {0}".format(str(numberOfFilesMoved)))   


    