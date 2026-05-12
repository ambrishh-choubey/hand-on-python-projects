print("welcome to the game who gonnna be a millionare")


questions=[["whon is virat kohli","wwe" ,"cricketer","footballer","dancer" ,2],
           ["what is the capital of france","rome","paris","berlin", "italy", 2],
           ["which planet is known as red planet","MERCURY","Venus","EARTH","MARS",4],
           ["what is the largest mammal ?","elephant","BLUE WHALE","TIGER","LION",2],
            ["WHO WROTE ROMEO AND JULLETE","CHARLES DICKENS","WILLIAM SHAKESPEARE","JANE AUSTIN","HOMER",2],
            ["what is the square root of 64","6","8","10","12",2] ,
            ["which counttry is known as land of rising sun ","china","japan","north korea","india",2],
            ["who painted mona lisa?","vincent van gogh","pablo picasssoo","leonardo da vicii","claiude monet",2],
            ["who is the fastest land animal?","cheetah","lion","elephant","horse"],
            ["who killed ravanaa?","ram","laxman","sitaa","vibhishan",1],
            ["whose family cat does belongs to ? ","tiger","lion","rhino","croco",1]

         ]
prizes = [1000,2000,5000,10000,20000,80000,320000,640000,1280000,2560000,5000000]
i=0
for question in questions:
    
    
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

# check whether the ans is correct or not
    a =int(input("enter your answer.1 for a/,2 for b/,3 forc /, and 4 for d\n"))
    if(question[5]==a):
        print("correct answer")
    else:
        print(f"incorrect answer,the correct answer was {question[5]}.\nBETTER LUCK NEXT TIME ")
        break
    # sum +=prizes[i]
    print(f"you won {prizes[i]}")
    i+=1
