
# https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/blob/master/samples/vision/computer_vision_samples.py
import os.path

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


subscription_key = os.getenv('subscription_key')
endpoint= os.getenv('endpoint')


# SUBSCRIPTION_KEY_ENV_NAME = "COMPUTERVISION_SUBSCRIPTION_KEY"
# COMPUTERVISION_LOCATION = os.environ.get(
#     "COMPUTERVISION_LOCATION", "westcentralus")

IMAGES_FOLDER = './labelledImagesFormatted/year/2001/'


# def image_analysis_in_stream():
#     """ImageAnalysisInStream.

#     This will analyze an image from a stream and return all available features.
#     """

#     client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
#     # client = ComputerVisionClient(
#     #     endpoint="https://" + COMPUTERVISION_LOCATION + ".api.cognitive.microsoft.com/",
#     #     credentials=CognitiveServicesCredentials(subscription_key)
#     # )

#     with open(os.path.join(IMAGES_FOLDER, "house.jpg"), "rb") as image_stream:
#         image_analysis = client.analyze_image_in_stream(
#             image=image_stream,
#             visual_features=[
#                 VisualFeatureTypes.image_type,  # Could use simple str "ImageType"
#                 VisualFeatureTypes.faces,      # Could use simple str "Faces"
#                 VisualFeatureTypes.categories,  # Could use simple str "Categories"
#                 VisualFeatureTypes.color,      # Could use simple str "Color"
#                 VisualFeatureTypes.tags,       # Could use simple str "Tags"
#                 VisualFeatureTypes.description  # Could use simple str "Description"
#             ]
#         )

#     print("This image can be described as: {}\n".format(
#         image_analysis.description.captions[0].text))

#     print("Tags associated with this image:\nTag\t\tConfidence")
#     for tag in image_analysis.tags:
#         print("{}\t\t{}".format(tag.name, tag.confidence))

#     print("\nThe primary colors of this image are: {}".format(
#         image_analysis.color.dominant_colors))


def recognize_text():
    """RecognizeTextUsingRecognizeAPI.

    This will recognize text of the given image using the recognizeText API.
    """
    import time
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    with open(os.path.join(IMAGES_FOLDER, "2022-08-22 20-26-04 Year - 030341.jpg"), "rb") as image_stream:
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

    print("Job completion is: {}\n".format(image_analysis.status))

    print("Recognized:\n")
    lines = image_analysis.recognition_result.lines
    print(lines[0].words[0].text)  # "make"
    return

def recognize_printed_text_in_stream():
    """RecognizedPrintedTextUsingOCR_API.

    This will do an OCR analysis of the given image.
    """
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    with open(os.path.join(IMAGES_FOLDER, "2022-08-22 20-26-04 Year - 030341.jpg"), "rb") as image_stream:
        image_analysis = client.recognize_printed_text_in_stream(
            image=image_stream,
            language="en"
        )

    lines = image_analysis.regions[0].lines
    print("Recognized:\n")
    for line in lines:
        line_text = " ".join([word.text for word in line.words])
        print(line_text)


if __name__ == "__main__":
    # import sys, os.path
    # sys.path.append(os.path.abspath(os.path.join(__file__, "..", "..", "..")))
    # from samples.tools import execute_samples
    # execute_samples(globals(), SUBSCRIPTION_KEY_ENV_NAME)
    # recognize_text()
    recognize_printed_text_in_stream()
