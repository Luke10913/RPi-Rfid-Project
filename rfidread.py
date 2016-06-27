import MFRC522
import RPi.GPIO as GPIO
def uidread():
    MIFAREReader = MFRC522.MFRC522()
    reading = True
    while reading:
        # while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        if status == MIFAREReader.MI_OK:
            print("Card detected")

        (status,backData) = MIFAREReader.MFRC522_Anticoll()
        if status == MIFAREReader.MI_OK:
            uid=str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])
            #print ("Card Number: "+str(backData[0])+str(backData[1])+str(backData[2])+str(backData[3])+str(backData[4])
            MIFAREReader.AntennaOff()
            reading=False
            return uid
