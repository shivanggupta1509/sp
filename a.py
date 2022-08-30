import requests, string, random, argparse, sys

def getRandomString(length): #Letters and numbers
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def getRandomText(length): #Chars only
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))


def generate():
    nick = input('[username]-')
    passw = ('shivanggupta')
    email = nick+"@dripplay.tk"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, nick+":"+r.json()["username"]+":"+email+":"+passw)
        else:
            #Details available in r.json()["errors"]
            #print(r.json()["errors"])
            return (False, "Could not create the account, some errors occurred")
    else:
        return (False, "Could not load the page. Response code: "+ str(r.status_code))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="how many accounts to generate, default is 1", type=lambda x: (int(x) > 0) and int(x) or sys.exit("Invalid number: minimum amount is 1"))
    parser.add_argument("-o", "--output", help="output file, default prints to the console")
    args = parser.parse_args()

    N = args.number if args.number else 1
    file = open(args.output, "a") if args.output else sys.stdout
                             
    print("

        .d8888b.                    888    d8b  .d888                                    
d88P  Y88b                   888    Y8P d88P"                                     
Y88b.                        888        888                                       
 "Y888b.   88888b.   .d88b.  888888 888 888888 888  888                           
    "Y88b. 888 "88b d88""88b 888    888 888    888  888                           
      "888 888  888 888  888 888    888 888    888  888                           
Y88b  d88P 888 d88P Y88..88P Y88b.  888 888    Y88b 888                           
 "Y8888P"  88888P"   "Y88P"   "Y888 888 888     "Y88888                           
           888                                      888                           
           888                                 Y8b d88P                           
           888                                  "Y88P"                            
       d8888                                            888                       
      d88888                                            888                       
     d88P888                                            888                       
    d88P 888  .d8888b .d8888b .d88b.  888  888 88888b.  888888                    
   d88P  888 d88P"   d88P"   d88""88b 888  888 888 "88b 888                       
  d88P   888 888     888     888  888 888  888 888  888 888                       
 d8888888888 Y88b.   Y88b.   Y88..88P Y88b 888 888  888 Y88b.                     
d88P     888  "Y8888P "Y8888P "Y88P"   "Y88888 888  888  "Y888                    
                                                                                  
                                                                                  
                                                                                  
 .d8888b.                                             888                         
d88P  Y88b                                            888                         
888    888                                            888                         
888         .d88b.  88888b.   .d88b.  888d888 8888b.  888888 .d88b.  888d888      
888  88888 d8P  Y8b 888 "88b d8P  Y8b 888P"      "88b 888   d88""88b 888P"        
888    888 88888888 888  888 88888888 888    .d888888 888   888  888 888          
Y88b  d88P Y8b.     888  888 Y8b.     888    888  888 Y88b. Y88..88P 888          
 "Y8888P88  "Y8888  888  888  "Y8888  888    "Y888888  "Y888 "Y88P"  888          
                                                                                  
                                                                                  
       By -                          oooo          .o                                                 
         `888        o888                                                 
 .oooo.o  888 .oo.    888  oooo    ooo oooo    ooo ooo. .oo.    .oooooooo 
d88(  "8  888P"Y88b   888   `88.  .8'   `88b..8P'  `888P"Y88b  888' `88b  
`"Y88b.   888   888   888    `88..8'      Y888'     888   888  888   888  
o.  )88b  888   888   888     `888'     .o8"'88b    888   888  `88bod8P'  
8""888P' o888o o888o o888o     `8'     o88'   888o o888o o888o `8oooooo.  
                                                               d"     YD  
                                                               "Y88888P'  
                                                                                 
                    
Generating accounts in the following format:", file=sys.stdout)
    print("NICKNAME:USERNAME:EMAIL:PASSWORD\n", file=sys.stdout)
    for i in range(N):
        result = generate()
        if result[0]:
            print(result[1], file=file)
            if file is not sys.stdout:
                print(result[1], file=sys.stdout)
        else:
            print(str(i+1)+"/"+str(N)+": "+result[1], file=sys.stdout)

    if file is not sys.stdout: file.close()
