# from gtts import gTTS
# tts = gTTS('Your are safe')
# tts.save('safe.mp3')
# tts = gTTS('Please wear a mask')
# tts.save('not_safe.mp3')


import os
# os.system("start safe.mp3")
# os.system("start not_safe.mp3")



i=0
temp="0"

mask = 0
unmask = 0
result=[]
mask_said=0
unmask_said=0
while i<10:
    f = open("speech.txt", "r")
    if(f.read()=="1"):
        unmask=0
        mask+=1
        print(mask)
    if(f.read()=="0"):
        mask=0
        unmask+=1
        print(unmask)
    if(mask>1 and mask_said==0):
        mask_said=1
        unmask_said=0
        os.system("start safe.mp3")
    if (unmask >1 and unmask_said==0):
        unmask_said=1
        mask_said=0
        os.system("start not_safe.mp3")

    # if (f.read() == "1" and temp=="0"):
    #     os.system("start safe.mp3")
    # f.close()
    # f = open("speech.txt", "r")
    # if (f.read() == "0" and temp=="1"):
    #     os.system("start not_safe.mp3")
    # f.close()
    # f = open("speech.txt", "r")
    # temp=f.read()
    # print(temp)
    # print(f.read())
    f.close()





  #
  #
  # if(temp!=f.read() and f.read()!="" and temp!=""):
  #       f = open("speech.txt", "r")
  #       # print(f.read())
  #       # print(temp)
  #       f = open("speech.txt", "r")
  #       if (f.read()=="1"):
  #           os.system("start safe.mp3")
  #           print("YES")
  #       f = open("speech.txt", "r")
  #       if (f.read()=="0"):
  #           os.system("start not_safe.mp3")
  #           print("NO")
  #       f = open("speech.txt", "r")
  #       temp=f.read()
  #       print(temp)
