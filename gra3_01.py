


print("co chcesz zrobic?\n 1) Dodać czas\n 2) Oblicz ile jednostek T zabić\n 3) Dodatkowa funkcja")
wybor= input()

if wybor == str('1'):
    def czas():
        import datetime
        from datetime import timedelta
        print(datetime.datetime.now())
        dni=input("ile dni: ")
        data_plus_dni= (datetime.datetime.now() + timedelta(days=int(dni)))


        godzin= int(input("ile godzin: "))
        minut = int(input('ile minut: '))
        sekund= godzin*60*60

        minut_do_sekund = int(godzin*60*60)+int(minut*60)

        print(minut_do_sekund)

        dni_plus_sekund = (data_plus_dni) + timedelta(seconds=int(minut_do_sekund))

        import datetime

        days_ES = ['niedziela', "poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota"]

        t = dni_plus_sekund
        print(t)
        f = t.strftime("{%w} %Y-%m-%d").format(*days_ES)
        print(f)
        print(input("zakoncz enter"))



    czas()
elif wybor == str('2'):
    ilepkt = int(input('Podaj ile tysiecy punktów musisz zabić: '))
    ilepkt = ilepkt * 1000
    print(ilepkt)
    print('1) atak manualny\n2) atak procentowy')
    atak=input()

    if atak == str('1'):
        print('atak manualny')

        def jednostki():


            t8 = input('ile jedna jednostka T8 daje pkt: ')
            wynikt8 = ilepkt/float(t8)
            print('potrzebujesz tylko T8: ' + str(wynikt8))
            liczbat8 = input('Liczba jednostek t8: ')
            mocRazyLiczbat8 = int(liczbat8)*float(t8)
            print('Moc {} jednostek t8 wynosi {}'.format(int(liczbat8), mocRazyLiczbat8 ))
            print('Do {} brakuje ci {} pkt.'.format(ilepkt, ilepkt-mocRazyLiczbat8))


            t9 = input('\nile jedna jednostka T9 daje pkt: ')
            wynikt9 = ilepkt/float(t9)
            print('potrzebujesz tylko T9: ' + str(wynikt9))
            wymaganet9=(ilepkt-mocRazyLiczbat8)/float(t9)
            print('Aby osiagnac {} pkt. potrzebujesz {} jednostek T9: '.format((ilepkt-mocRazyLiczbat8), wymaganet9))
            liczbat9 = input('Liczba jednostek t9: ')
            mocRazyLiczbat9 = int(liczbat9)*float(t9)
            zostalot9=(ilepkt-mocRazyLiczbat8)
            print('Moc {} jednostek t9 wynosi {}'.format(int(liczbat9), mocRazyLiczbat9 ))
            zostalo_monit_t9 = zostalot9 #/float(t9)
            potrzebujeszt9 = (zostalo_monit_t9 - mocRazyLiczbat9)/float(t9)
            print('Potrzebujesz dodatkowo jednostek T9: ' + str(potrzebujeszt9))


            t10 = input('\nile jedna jednostka T10 daje pkt: ')
            wynikt10 = ilepkt/float(t10)
            print('potrzebujesz tylko T10: ' + str(wynikt10))
            wymaganet10=(ilepkt-mocRazyLiczbat8-mocRazyLiczbat9)/float(t10)
            print('Aby osiagnac {} pkt. potrzebujesz {} jednostek T10: '.format((ilepkt-mocRazyLiczbat8-mocRazyLiczbat9), wymaganet10))
            liczbat10 = input('Liczba jednostek t10: ')
            mocRazyLiczbat10 = int(liczbat10) * float(t10)
            zostalot10 = (ilepkt - mocRazyLiczbat9)
            print('Moc {} jednostek t10 wynosi {}'.format(int(liczbat10), mocRazyLiczbat10))
            zostalo_monitt10 = zostalot10 #/ float(t10)
            potrzebujeszt10 = (zostalo_monitt10 - mocRazyLiczbat10 -mocRazyLiczbat8)/ float(t10)
            print('Potrzebujesz dodatkowo jednostek T10: ' + str(potrzebujeszt10))


            t11 = input('\nile jedna jednostka T11 daje pkt: ')
            wynikt11 = ilepkt/float(t11)
            print('potrzebujesz tylko T11: ' + str(wynikt11))
            wymaganet11=(ilepkt-mocRazyLiczbat8-mocRazyLiczbat9-mocRazyLiczbat10)/float(t11)
            print('Aby osiagnac {} pkt. potrzebujesz {} jednostek T11: '.format((ilepkt-mocRazyLiczbat8-mocRazyLiczbat9-mocRazyLiczbat10), wymaganet11))
            liczbat11 = input('Liczba jednostek t11: ')
            mocRazyLiczbat11 = int(liczbat11) * float(t11)
            zostalot11 = (ilepkt - mocRazyLiczbat10)
            print('Moc {} jednostek t11 wynosi {}'.format(int(liczbat11), mocRazyLiczbat11))
            zostalo_monitt11 = zostalot11 # / float(t11)
            potrzebujeszt11 = (zostalo_monitt11 - mocRazyLiczbat11 -mocRazyLiczbat8 -mocRazyLiczbat9)/ float(t11)
            print('Potrzebujesz dodatkowo jednostek T11: ' + str(potrzebujeszt11))
            input("wyjscie")

        jednostki()

    elif atak == str('2'):
        print('atak procetowy')
        def atakprocent():
            
            stoprocent =100
            t8procent = input('ile % t8: ')
            print(stoprocent-int(t8procent))
            t9procent = input('ile % t9: ')
            print(stoprocent-int(t8procent)-int(t9procent))
            t10procent = input('ile % t10: ')
            print(stoprocent-int(t8procent)-int(t9procent)-int(t10procent))
            t11procent = input('ile % t11: ')
            procent_razem = t8procent+t9procent+t10procent+t11procent
            if stoprocent != procent_razem:
                print('nie masz 100%')
                dalej = input('Kontynuowac t/n')

                while dalej == ('t'):
                    print('ok')





        atakprocent()
elif wybor == str('3'):
    input('wyjscie-><-')