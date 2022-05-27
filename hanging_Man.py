#import os
from google.colab import output
word=input('Choose the secret word :): ')
word=word.lower()
#os.system('cls') 
output.clear()
State1='________________\n|\n|\n|\n|\n|__\n'
State2='________________\n|       O      \n|\n|\n|\n|__\n'
State3='________________\n|       O      \n|       |\n|\n|\n|__\n'
State4='________________\n|       O      \n|      /|\n|\n|\n|__\n'
State5='________________\n|       O      \n|      /|\ \n|\n|\n|__\n'
State6='________________\n|       O      \n|      /|\ \n|       /      \n|\n|__\n'
State7='________________\n|       O      \n|      /|\ \n|       /\      \n|\n|__\n'

drawings=[State1,State2,State3,State4,State5,State6,State7]

#Ask player one the word
spaces=''
conts=0;
#spaces of the letter
for letters in word:
  if letters != ' ':
    spaces=spaces+'_ '
  else: 
    spaces=spaces+'  '
    conts=conts+1
print('Guess the word:')

#Initial Scenary
error=0
#scenary(error)
print(drawings[error])
numlet=len(set(word))-1
print(spaces)
ac=0
allet=[]

#Ask player two a letter
while numlet != ac:
  letter=input('Choose a letter:')[0]
  letter=letter.lower()
  if letter in word and letter not in allet:
    ac=ac+1;
    allet.append(letter)
    pos=[]
    while letter in word:
      pos.append(word.find(letter))
      spaces1=list(spaces)
      spaces1[word.find(letter)*2]=letter
      spaces="".join(spaces1)
      word=word.replace(word[word.find(letter)],'.',1)
      
  else:
    error=error+1;
    if error>=6:
      output.clear()
      print(drawings[error])
      print('srry u Lost')
      break
  output.clear()
  print(drawings[error])
  print(spaces)
if ac==numlet:
  print('Congrats, U Won')