import cv2
import time
import pyttsx3
import cvzone
from cvzone.HandTrackingModule import HandDetector

from gtts import gTTS
import os
import pygame



sinhala_text = "වජිර තොගෙ ප්‍රෝග්‍රැම් එක හරි. වැඩ කරන්න කලින් දැනගනින් වැඩ කරන හැටි. මුලින්ම එස් අකුර ඔබපන් කීබෝඩ් එකේ ඊට පස්සෙ තොගෙ කැමති ඇගිල්ලක් මට පෙන්නපන් මම ඊට පස්සෙ උබට ඇගිල්ලෙ නම සුද්ද සින්හලෙන් කියන්නම්"
tts = gTTS(text=sinhala_text, lang='si')
audio_path = 'sinhala_output.mp3'
tts.save(audio_path)

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(audio_path)

pygame.mixer.music.play()


while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


pygame.mixer.quit()
os.remove(audio_path)




cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer =0
start = False
stateResult = False


while True:

    success, img = cap.read()

    hands,img = detector.findHands(img)

    
    if start:
        if stateResult is False:

            timer = time.time() - initialTime
            if timer>3:
                stateResult = True
                timer =0

                if hands:
                    
                    playerMove = None
                    hand = hands[0]
                    finger = detector.fingersUp(hand)
                    print(finger)
                    if finger == [0,0,0,0,0]:
                        playerMove = 0
                    if finger ==[1,0,0,0,0]:
                        playerMove = 1
                    if finger ==[0,1,0,0,0]:
                        playerMove = 2
                    if finger ==[0,0,1,0,0]:
                        playerMove = 3
                    if finger ==[0,0,0,1,0]:
                        playerMove = 4
                    if finger ==[0,0,0,0,1]:
                        playerMove = 5
                    if finger ==[1,1,0,0,0] or finger ==[0,1,1,0,0] or finger ==[0,0,1,1,0] or finger ==[0,0,0,1,1] or finger ==[1,0,0,0,1] or finger ==[1,0,0,1,0] or finger ==[0,1,0,0,1] or finger ==[0,1,0,1,0] or finger ==[0,0,1,0,1] or finger ==[0,0,1,1,0] or finger ==[1,0,1,0,0] or finger ==[1,1,0,0,0]:
                        playerMove = 6
                    
                    if playerMove == 0:
                        ss = "එක ඇගිල්ලක් විතරක් පෙන්නපන් පකෝ"
                        sayFinger(ss)
                        
                    if playerMove == 1:
                        ss ="මහපට ඇගිල්ල"
                        sayFinger(ss)
                    if playerMove == 2:
                        ss = "දබරගිල්ල" 
                        sayFinger(ss)
                    if playerMove == 3:
                        ss = "මැදගිල්ල"
                        sayFinger(ss)
                    if playerMove == 4:
                        ss = "වෙදගිල්ල"
                        sayFinger(ss)
                    if playerMove == 5:
                        ss ="සුලගිල්ල"
                        sayFinger(ss)
                    if playerMove == 6:
                        ss = "එක ඇගිල්ලක් විතරක් පෙන්නපන් පකෝ"
                        sayFinger(ss)

        

    cv2.imshow("Image", img)
    key =cv2.waitKey(1)

    if key == ord('s'):
        start = True
        initialTime = time.time()
        stateResult = False

    def sayFinger(ss):
        tts = gTTS(text=ss, lang='si')
        audio_path = 'sinhala_output.mp3'
        tts.save(audio_path)
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()
        os.remove(audio_path)
