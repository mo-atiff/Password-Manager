import random
import string
import json
import os
import winsound

import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 180)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

jsdict = {'Name': None,
          'Passwords': [{None : None}],
          'Identity': None,
          'Securityquest': {None : None}}

print('1 : TO ADD OR CREATE NEW PASSWORD FILES')
print('2 : TO VIEW PASSWORD FILES IN READ-ONLY-MODE')
print('3 : CUSTOMIZED PASSWORD SAVING')

cho = int(input('ENTER YOUR CHOICE : '))
engine.say(f'You Entered Choice{cho}')
# engine.say('Hii')
engine.runAndWait()

if cho == 1:

    def Pass_gen():
        max_length = 10

        print('-'*65, 'Password-Generator', '-'*64)
        sign = input('Type "Yes" To Generate Strong Password For You : ')
        sign = sign.lower()

        letters = string.ascii_letters
        nums = string.digits
        nums = list(nums)
        spc_char = '!@#$%^&*()-+_'
        spc_char = list(spc_char)

        c = 65
        capalpha = []
        for i in letters:
            if ord(i) == c:
                capalpha.append(i)
                c += 1

        d = 97
        smallalpha = []
        for i in letters:
            if ord(i) == d:
                smallalpha.append(i)
                d += 1
            if ord(i) == 65:
                pass

        if sign == 'yes':
            combo = capalpha+smallalpha+nums+spc_char

            caps = random.choice(capalpha)
            small = random.choice(smallalpha)
            num = random.choice(nums)
            spc = random.choice(spc_char)

            password = caps+small+num+spc

            for i in range(max_length-4):
                comborandom = random.choice(combo)
                password += comborandom

            password = list(password)
            random.shuffle(password)
            strong = ''
            strong = strong.join(password)

            Password = strong
            print('Your Password :', Password)
            engine.say('Your Password Boss')
            engine.runAndWait()

            yesorno = input('Save Your Password So That You Dont Have To Remember It (Type "yes" To Save It) : ')
            yesorno = yesorno.lower()
            if yesorno == 'yes':
                name = input('What Name Do You Wanna Give To Your File (just write file name with no extensions) : ')
                name = f'{name}.json'
                # with open(name, 'w') as jsfile:
                if name in os.listdir():
                    print('\nFile Name Already Exists : ')
                    verify = input('\nEnter Your User-Name Of File : ')
                    with open(name, 'r') as d:
                        l = json.load(d)
                        if verify == l['Name']:
                            engine.say('Access granted')
                            engine.runAndWait()
                            add = input('\nDo You Want to Add a New Password To Your Existing File??? (type "yes" if u) : ')
                            add = add.lower()
                            if add == 'yes':
                                with open(name, 'r+') as exists:
                                    R = json.load(exists)
                                    web = input('Enter The Website Domain For Which You Wanna Save This Password : ')
                                    R['Passwords'].append({web: Password})

                                    with open(name, 'r+') as done:
                                        json.dump(R, done)
                                        print('Password Added Sucessfully...')
                                        engine.say('Password Added Sucessfully...')

                                        exit()

                        elif verify != l['Name']:
                            print("Sorry Your User-Name Doesn't Match")
                            engine.say("Sorry User-Name Doesn't Match")
                            engine.runAndWait()
                            n = input('\nLet us Try By Another Way.. (Enter Your Identity) : ')
                            engine.say("Ok soo let us try by another way")
                            engine.runAndWait()
                            if n == l['Identity']:
                                add = input(
                                    '\nDo You Want to Add a New Password To Your Existing File??? (type "yes" if u) : ')
                                add = add.lower()
                                if add == 'yes':
                                    with open(name, 'r+') as exists:
                                        R = json.load(exists)
                                        web = input('Enter The Website Domain For Which You Wanna Save This Password : ')
                                        R['Passwords'].append({web: Password})

                                        with open(name, 'r+') as done:
                                            json.dump(R, done)
                                            print('Password Added Sucessfully...')
                                            engine.runAndWait()
                                            exit()

                            elif n != l["Identity"]:
                                print('Dear User As You Have Forgotten Your User-Name and Identity You Cannot Have Access to Your Existing File \nYou Have To Create a New One')
                                exit()



                k = json.dumps(jsdict, indent=2)
                with open(name, 'w') as File:
                    File.write(k)
                web = input('Enter The Website Domain For Which You Wanna Save This Password : ')
                your_name = input('Enter Your Name(to access your file) : ')
                iden = input('Enter Your Identity(This is useful to access your file...Try not to forget it) : ')
                print('\nInCase if you forget it...Worry not...We will set Security questions')
                print('\n1 : IN WHICH CITY WERE YOU BORN IN\n2 : YOUR PET(animal) NAME\n3 : WHICH SCHOOL DID U STUDY IN\n4 : THE THING YOU LOVE THE MOST')
                choice = int(input('\nEnter Your Choice : '))
                if choice == 1:
                    # print()
                    c11 = 'IN WHICH CITY WERE YOU BORN IN'
                    c1 = input('\nIN WHICH CITY WERE YOU BORN IN : ')
                    with open(name, 'r+') as file:
                        data = json.load(file)
                        data['Securityquest'] = {c11 : c1}
                        data['Name'] = your_name
                        data['Identity'] = iden
                        data['Passwords'].append({web : Password})

                        with open(name, 'r+') as f:
                            json.dump(data, f)

                elif choice == 2:
                    # print()
                    c22 = 'YOUR PET(animal) NAME'
                    c2 = input('\nYOUR PET(animal) NAME : ')
                    with open(name, 'r+') as fil2:
                        data2 = json.load(fil2)
                        data2['Securityquest'] = {c22 : c2}
                        data2['Name'] = your_name
                        data2['Identity'] = iden
                        data2['Passwords'].append({web : Password})

                        with open(name, 'r+') as f2:
                            json.dump(data2, f2)

                elif choice == 3:
                    # print()
                    c33 = 'WHICH SCHOOL DID U STUDY IN'
                    c3 = input('\nWHICH SCHOOL DID U STUDY IN : ')
                    with open(name, 'r+') as fil3:
                        data3 = json.load(fil3)
                        data3['Securityquest'] = {c33 : c3}
                        data3['Name'] = your_name
                        data3['Identity'] = iden
                        data3['Passwords'].append({web : Password})

                        with open(name, 'r+') as f3:
                            json.dump(data3, f3)

                elif choice == 4:
                    # print()
                    c44 = 'THE THING YOU LOVE THE MOST'
                    c4 = input('\nTHE THING YOU LOVE THE MOST : ')
                    with open(name, 'r+') as fil4:
                        data4 = json.load(fil4)
                        print(data4)
                        data4['Securityquest'] = {c44 : c4}
                        data4['Name'] = your_name
                        data4['Identity'] = iden
                        data4['Passwords'].append({web : Password})

                        with open(name, 'r+') as f4:
                            json.dump(data4, f4)

                print('\n\nCongratulations Your Password is in Safe Hands :)')
                engine.say('Congratulations Your Password is in Safe Hands')
                engine.runAndWait()

            else:
                print('Thank You For Using us Glad That We Are Helpful To You :)')
                engine.say('Thank You For Using us Glad That We Are Helpful To You')
                engine.runAndWait()



        else:
            print('Sorry Program Terminated You Should Have Typed "yes" Instead You Typed Something else')
            engine.say('Sorry Program Terminated You Should Have Typed "yes" Instead You Typed Something else')
            engine.runAndWait()

        # engine.runAndWait()

    Pass_gen()

elif cho == 2:
    name = input('\nEnter The Name Of Your File (With no Extensions): ')
    name = f'{name}.json'
    if name in os.listdir():
        print('\nFile Found : ')
        with open(name, 'r') as file:
            data = json.load(file)
            fil = input('Enter User-Name : ')
            iden = input('Enter Your Identity : ')
            if (fil == data['Name']) and (iden == data['Identity']):
                show = json.dumps(data, indent=2)
                print()
                print('-'*65, 'Your-File', '-'*64)
                print()
                print(show)
                winsound.Beep(1100, 200)
                print('ACCESS GRANTED')
                engine.say('Access granted')
                engine.runAndWait()

    else:
        print('\nFile Not Found...Dear User You First Need To Create The File')
        engine.say('file not foubd')
        engine.runAndWait()


elif cho == 3:
    Cpass = input('Enter Your Password : ')
    Cweb = input('Enter The Website Domain For Which You Wanna Save This Password : ')
    print('\nIam Saving This Password')
    file = input('\nEnter A File Name To Save(without extensions) : ')
    file = f'{file}.json'

    if file in os.listdir():
        print('File Found Already Exists')
        name = input('Enter User-Name Of Your File : ')
        with open(file, 'r+') as fille:
            data = json.load(fille)
            if name == data['Name']:
                winsound.Beep(1100, 200)
                print('ACCESS GRANTED')
                engine.say('Access granted')
                engine.runAndWait()
                data['Passwords'].append({Cweb : Cpass})

                with open(file, 'r+') as fil:
                    json.dump(data, fil)
                    print('File Updated')
                    engine.say('File updated successfully')
                    engine.runAndWait()

