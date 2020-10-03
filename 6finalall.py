try:
  import datetime
  list_v=['track1','track2','track3']
  rating_v=[8,5,6]
  cklist=['true','true','true']
  counter=0
  cnt=-1
  noc=[10,19,15]
  pl=[5,6,7]
 #===================================================================
  def addVideo(name):

    temp=0
    flag = 0
    for i in range(len(list_v)):
        if (name == list_v[i]):
            flag = 1
            c=i
            break
    if(flag==0):
     list_v.append(name)
     print('following video title was added to the inventory                                                   |')
     cklist.append('true')
     rt=int(input('enter the rating of the following video:-                                                          |\n'))
     rating_v.append(rt)
     pr = int(input('enter the price of the following video(per day):-                                                  |\n'))
     pl.append(pr)
     nc = int(input('enter the number of copies of the video :-                                                         |\n'))
     noc.append(nc)
    else:
        print('a track with same name allready exists in our library                                                    |')
        print('amount of the copies was increased                                                                       |')
        temp=noc[c]+1
        noc[i]=temp
        cklist[c]='true'

 #==========================================================================
  def doCheckout(name):

    flag = 0
    for i in range(len(list_v)):
        if(name==list_v[i]):
            flag=1
            counter=i;
            break
    if(flag==1):
        if(cklist[counter]=='true' and noc[counter]>0):
         print('thanks for purchse the following music video :-')
         print(list_v[counter])
         noc[counter] = noc[counter] - 1
         nd = int(input('enter the number of days for which you want to rent the video :-'))
         prc=nd*pl[counter]
         print('price you have to pay for this video is :- ')
         print(prc)
         print('checkout date for the video is:-')
         print(datetime.date.today())
         print('return date for video is :-')
         e = datetime.date.today() + datetime.timedelta(days=nd)
         print(e)
         print('rating for the track you purchaed is  :- ')
         print(rating_v[counter])
         if(noc[counter]<1):
           cklist[counter] = 'false'

        else:
            print('not avilable :(')
            print('visit again ')
    else:
        print('the following music is not there in our library')
        print(name)

 #================================================================
  def receiveRating(name,rate):

    for i in range(len(list_v)):
     if(list_v[i]==name):
      print('the old rating was')
      print(rating_v[i])
      rating_v[i]=rate
      print('the new rating was successfully recorded')
      print(rating_v[i])
      break
    else:
        print('the video title you entered is not in inventory ')

 #===================================================================
  def doReturn(name):
    flag=0

    for i in range(len(list_v)):
        if (name == list_v[i]):
            flag = 1
            ct = i;
            break
    if (flag == 1):
        print('thanks for returning the video:- ')
        ct= list_v.index(name)
        cklist[ct]='true'
        temp1 = noc[ct] + 1
        noc[ct] = temp1
        print('how much will you rate this video(between 0-10):- ')
        rat=int(input("enter the rating for the video:- "))
        print('the old rating is')
        print(rating_v[ct])
        rating_v[ct] = rat
        print('the new rating was successfully recorded')
        print(rating_v[ct])
    else:
        print('the following music is not there in our library:- ')
        print(name)

 #====================================================================
  def listinventory():
    print('__________________________________________________________________________________________________________')
    print('|sr no.        |video name        |no. of copies left        |current rating       |rent(per day price)  |')
    print('__________________________________________________________________________________________________________')
    formated ='|{0}             |{1}            |       {2}                 |      {3}              |       {4}             {5}'
    for i in range(len(list_v)):
     z=i+1
     print(formated.format(z,list_v[i],noc[i],rating_v[i],pl[i],'|'))
    print('|________________________________________________________________________________________________________|')
 #=====================================================================
  def prg(m):
   n=1
   while(n!=0):
     print('------------------------------')
     print('|\t enter your choices        | \n'
          '|\t 1 for adding video        |\n'
          '|\t 2 for checkout the video  |\n'
          '|\t 3 rate a video            |\n'
          '|\t 4 return the video        |\n'
          '|\t 5 see inventory           |\n'
          '|\t 6 to exit                 |')
     print('------------------------------')
     choice=int(input('enter your choice\n'))
     if(choice==1):
      print('___________________________________________________________________________________________________________')
      title=input("enter the title of videos add to library :-                                                        |\n")
      addVideo(title)
      print('___________________________________________________________________________________________________________')
    #=====================================================================
     elif (choice == 2):
      print('___________________________________________________________________________________________________________')
      cktitle=input("enter the title of videos you want to check out :-                                                 |\n")
      doCheckout(cktitle)
      print('___________________________________________________________________________________________________________')
    #====================================================================
     elif (choice == 3):
      print('___________________________________________________________________________________________________________')
      rtitle=input("enter the title of video that you want to rate :-                                                   |\n")
      rateing=int(input("enter the rating for the video:-                                                               |\n"))
      receiveRating(rtitle,rateing)
      print('___________________________________________________________________________________________________________')
    #=======================================================================
     elif (choice == 4):
      print('___________________________________________________________________________________________________________')
      retitle=input("enter the title of video you want to retur to library :-                                           |\n")
      doReturn(retitle)
      print('___________________________________________________________________________________________________________')
    #===========================================================================
     elif (choice == 5):

      listinventory()

    #=============================================================================
     elif (choice == 6):
      print('___________________________________________________________________________________________________________')
      print( 'thanks for visiting')
      print('___________________________________________________________________________________________________________')
      n=0
     else:
        print('_________________________________________________________________________________________________________')
        print('oops you made a mistake')
        print('try again')
        print('_________________________________________________________________________________________________________')
  c='wellcome'
  print(c)
  prg(c)
except ValueError as e:
    print('you made an mistake ')
    print('you may have entered a character where a integer input was expected or vice-versa')
    re = 'restart'
    prg(re)
