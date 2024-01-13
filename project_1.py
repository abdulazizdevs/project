def rock_paper_scissors():
  while True:
    text = "Qog`oz"
    text_1 = int(input("1= Tosh,2= Qaychi,3= Qog`oz. Birini tanlang: "))
    if text_1 == 1:
      print("Siz yutqazdingiz")
      print("O`yin tugadi")
      game_over_1 = input("Yana shu o`yinni o`ynaysizmi: ")
      if game_over_1 == "Ha":
        rock_paper_scissors()
      elif game_over_1 == "Yo`q":
        mainMenu()
      break
    elif text_1 == 2:
      print("Siz yutdingiz")
      reply = int(input("Yana shu o`yinni o`ynamoqchi bo`lsangiz `1`ni bosing unday bo`lmasa `0`ni bosing: "))
      if reply == 1:
        rock_paper_scissors()
      else:
        mainMenu()
      break
    elif text_1 == 3:
      print("Hali o`yin davom etmoqda")
      rock_paper_scissors()
def guess_the_number():
  counter = 0
  left_border = 1 
  right_border = 100
  centr = 50
  print("Son o`ylang")
  while counter < 7:
    print("O`ylagan sonningiz",centr,"ga tengmi")
    num = int(input("Katta bo`lsa 1 ni bosing, kichik bo`lsa 2 ni bosing, teng bo`lsa 3 ni bosing: "))
    counter += 1
    if num == 1:
      left_border = centr 
      centr = (left_border + right_border) // 2
    elif num == 2:
      right_border = centr
      centr = (right_border + left_border) // 2
    else:
      print("Siz ",counter,"- ta urunishda topdingiz ")
      game_over = int(input("Yana shu o`yinni o`ynamoqchi bo`lsangiz `1`ni bosing unday bo`lmasa `0`ni bosing: "))
      if game_over == 1:
        guess_the_number()
      else:
        mainMenu()
      break
def mainMenu():
  question = int(input("Qaysi o`yinni o`ynaymiz 1,2: "))
  if question == 1:
    rock_paper_scissors()
  else:
    guess_the_number()
mainMenu()