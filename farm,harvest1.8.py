import os
import requests
import bs4
def ea():
    ex = input ( "?you want exit:" )
    if ex == "yes":
        exit ()
    else:
        l ()
def a():
    print("(|farm<>harvest|)")
    print("""||||||||||||\n|____1.8___|""")
    print("a = get all\np=ping")
    s=input(":")
    if s=="a":
        ur()
    elif s=="p":
        url = input ( "url:" )
        if url == "exit":
            ea()
        elif url == "back":
            a ()
        else:
            os.system(f"ping {url} -t")
            a()
    else:
        a()

def ur():
    urt=input("url:")
    if urt == "exit":
        ea()
    elif urt =="back":
        a()
    elif urt == "help":
        print("back = back\nexit = exit\nurl = scan")
        ur()
    else:
        u=requests.get(f"{urt}")
        print(f"{u}\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")
        print(f"{u.content}\n\n\n\n\n\n\n\n\n")
        print(                            " 0                         0\n-___________________________-")
        print(f"[{u.cookies}]\n\n\n\n\n-____________________________________________________________________________________________________________________________________________________________________________-")
        html=u.text
        html1=bs4.BeautifulSoup(html,"html.parser")
        print(f"{html1}\n\n\n\n\n\n\n\n\n\n\n\n\n")
        html75 = html1.findAll ("html", attrs={"": ""} )
        print("html text:")
        for html75 in html75:
            print(f"{html75.text}\n\n")
        scrip=html1.findAll("script",attrs={"": ""})
        print("script text:")
        for scrip in scrip:
            print ( f"{scrip.text}\n\n" )
        a = input ( "Do you want to search for something specific? yes or no:" )
        if a == "نعم" or a=="yes" or a=="يب":
            rt = input ( "Type:" )
            nm=input("Parameter:")
            h =input(f"{nm}:")
            html56 = html1.find ( f"{rt}", attrs={f"{nm}": f"{h}"})
            print(html56)
            html46 = html1.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
            r=input("text or no:")
            if r=="text":
                print(f"{html46}\n\n\n")
                for html46 in html46:
                    print(html46.text)
                print(len(html46))
                sr = bs4.BeautifulSoup ( html, "lxml" )
                se = input ( "num:" )
                sea = int (se)
                html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print("\n")
                print ( html47[sea].text )
                print(":farm harvest:")
                ur()
            elif r == 'no':
                print(f"{html46}\n\n\n")
                for html46 in html46:
                    print (html46)
                print(len(html46))
                sr = bs4.BeautifulSoup ( html, "lxml" )
                se = input ( "num:" )
                sea = int(se)
                html47 = sr.findAll ( f"{rt}", attrs={f"{nm}": f"{h}"} )
                print (html47[sea])
                print(":farm harvest:")
                ur()
            else:
                a()
        else:
            a ()
def g():
    try:
        ur()
    except requests.exceptions.MissingSchema:
        print ( "false" )
        print("(https://)")
        g()
    except requests.exceptions.ConnectionError:
        print("false")
        g()
    except ValueError:
        g()
    except IndexError:
        print("false")
        l()
    except TypeError:
        g()
    except UnboundLocalError:
        l()
    except KeyboardInterrupt:
        ex = input ( "?you want exit:" )
        if ex == "yes":
            exit ()
        else:
            l ()
    except SyntaxError:
        l()
def l():
    try:
        a()
    except requests.exceptions.MissingSchema:
        print ( "false" )
        print("(https://)")
        g()
    except requests.exceptions.ConnectionError:
        print("false")
        g()
    except IndexError:
        g()
    except ValueError:
        g()
    except TypeError:
        g()
    except UnboundLocalError:
        l()
    except KeyboardInterrupt:
        ex = input ( "?you want exit:" )
        if ex == "yes":
            exit ()
        else:
            l()
    except SyntaxError:
        l()

l()
