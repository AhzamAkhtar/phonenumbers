def get_info():
    import phonenumbers
    from test import number
    from phonenumbers import geocoder
    countrycode="+91"
    lnumber="7827549899"
    number=countrycode+lnumber
    ch_nmber = phonenumbers.parse(number, "CH")
    print(number, "Is from ", geocoder.description_for_number(ch_nmber, "en"))
    from phonenumbers import carrier
    service_number = phonenumbers.parse(number, "RO")
    print("And Carieer name is",carrier.name_for_number(service_number, "en"))
def text_to_handwritting():
    import pywhatkit as kit
    import cv2 as cv
    kit.text_to_handwriting("Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum et Malorum (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.",save_to="handwriting.png")
    img=cv.imread("handwriting.png")
    cv.imshow("Display",img)
    cv.waitKey(0)
    cv.destroyAllWindows()
text_to_handwritting()

