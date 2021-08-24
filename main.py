import time
import pyfiglet
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyperclip

driver = webdriver.Chrome('./driver/chromedriver')
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600)
waitTime = 0.5
msgBoxClassName = '_13NKt'
plugin = 0


def plugin_menu():
    global plugin
    print('''1. Add serial number.
2. Add Time Stamp
3. Add Microsecond Stamp
Enter your choice : ''', end='')
    plugin = int(input())
    if plugin not in [1, 2, 3]:
        print("Invalid Input. Please try again")
        plugin_menu()
    else:
        print("Plugin change Successful.")


def exit_menu():
    print('''1. Again
2. Back
3. Exit
Enter your choice : ''', end="")
    choice = input()
    if choice == "1":
        return
    if choice == "2":
        menu()
    elif choice == "3":
        credits()
        driver.quit()
    else:
        print("Invalid input.\nPlease try again")
        exit_menu()
    exit()


def left_triangle():
    while True:
        print("Enter the message : ", end="")
        msg = input()
        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]

        for i in range(len(msg)):
            msg_box.send_keys(msg[:i+1] + Keys.ENTER)
            time.sleep(waitTime)

        exit_menu()


def right_triangle():
    while True:
        print("Enter the message : ", end="")
        msg = input()
        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]

        for i in range(len(msg) + 1):
            msg_box.send_keys(msg[len(msg)-i-1:] + Keys.ENTER)
            time.sleep(waitTime)

        exit_menu()


def repeater():
    while True:
        print("Enter the number of times you want the message to be repeated (-1 for infinity) : ", end = "")
        counter = int(input())
        print("Enter the message : ", end="")
        msg = input()
        print('Do you want to add a dynamic add-on to your text(y/n) : ', end='')
        addon = input().lower()

        if addon == 'y':
            plugin_menu()

        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]
        if counter != -1:
            constant_time = time.time()
            for i in range(counter):
                ad = ''
                if plugin == 1:
                    ad = str(i+1) + " : "
                elif plugin == 2:
                    ad = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) + " : "
                elif plugin == 3:
                    ad = str(round(time.time()-constant_time, 3)) + " : "

                msg_box.send_keys(ad + msg + Keys.ENTER)
                time.sleep(waitTime)

        else:
            print("Exit the program to stop the process.")
            i = 1
            constant_time = time.time()
            while True:
                ad = ''
                if plugin == 1:
                    ad = str(i) + " : "
                elif plugin == 2:
                    ad = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()) + " : "
                elif plugin == 3:
                    ad = str(round(time.time()-constant_time, 3)) + " : "

                msg_box.send_keys(ad + msg + Keys.ENTER)
                time.sleep(waitTime)
                i += 1

        exit_menu()


def per_character():
    while True:
        print("Enter the message (Blank spaces will be replaced by '_') : ", end="")
        msg = input()
        msg = msg.replace(' ', '_')
        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]
        for i in msg:
            msg_box.send_keys(i + Keys.ENTER)
            time.sleep(waitTime)

        exit_menu()


def character_art():
    f = "1943____*|*3-d*|*3x5*|*4x4_offr*|*5lineoblique*|*5x7*|*5x8*|*64f1____*|*6x10*|*6x9*|*a_zooloo*|*acrobatic" \
        "*|*advenger*|*alligator*|*alligator2*|*alphabet*|*aquaplan*|*arrows*|*asc_____*|*ascii___*|*assalt_m" \
        "*|*asslt__m*|*atc_____*|*atc_gran*|*avatar*|*b_m__200*|*banner*|*banner3*|*banner3-D*|*banner4*|*barbwire" \
        "*|*basic*|*battle_s*|*battlesh*|*baz__bil*|*beer_pub*|*bell*|*big*|*bigchief*|*binary*|*block*|*brite" \
        "*|*briteb*|*britebi*|*britei*|*broadway*|*bubble*|*bubble__*|*bubble_b*|*bulbhead*|*c1______*|*c2______" \
        "*|*c_ascii_*|*c_consen*|*calgphy2*|*caligraphy*|*catwalk*|*caus_in_*|*char1___*|*char2___*|*char3___" \
        "*|*char4___*|*charact1*|*charact2*|*charact3*|*charact4*|*charact5*|*charact6*|*characte*|*charset_*|*chartr" \
        "*|*chartri*|*chunky*|*clb6x10*|*clb8x10*|*clb8x8*|*cli8x8*|*clr4x6*|*clr5x10*|*clr5x6*|*clr5x8*|*clr6x10" \
        "*|*clr6x6*|*clr6x8*|*clr7x10*|*clr7x8*|*clr8x10*|*clr8x8*|*coil_cop*|*coinstak*|*colossal*|*com_sen_" \
        "*|*computer*|*contessa*|*contrast*|*convoy__*|*cosmic*|*cosmike*|*cour*|*courb*|*courbi*|*couri*|*crawford" \
        "*|*cricket*|*cursive*|*cyberlarge*|*cybermedium*|*cybersmall*|*d_dragon*|*dcs_bfmo*|*decimal*|*deep_str" \
        "*|*defleppard*|*demo_1__*|*demo_2__*|*demo_m__*|*devilish*|*diamond*|*digital*|*doh*|*doom*|*dotmatrix" \
        "*|*double*|*drpepper*|*druid___*|*dwhistled*|*e__fist_*|*ebbs_1__*|*ebbs_2__*|*eca_____*|*eftichess" \
        "*|*eftifont*|*eftipiti*|*eftirobot*|*eftitalic*|*eftiwall*|*eftiwater*|*epic*|*etcrvs__*|*f15_____" \
        "*|*faces_of*|*fair_mea*|*fairligh*|*fantasy_*|*fbr12___*|*fbr1____*|*fbr2____*|*fbr_stri*|*fbr_tilt*|*fender" \
        "*|*finalass*|*fireing_*|*flyn_sh*|*fourtops*|*fp1_____*|*fp2_____*|*fraktur*|*funky_dr*|*future_1*|*future_2" \
        "*|*future_3*|*future_4*|*future_5*|*future_6*|*future_7*|*future_8*|*fuzzy*|*gauntlet*|*ghost_bo*|*goofy" \
        "*|*gothic*|*gothic__*|*graceful*|*gradient*|*graffiti*|*grand_pr*|*greek*|*green_be*|*hades___*|*heavy_me" \
        "*|*helv*|*helvb*|*helvbi*|*helvi*|*heroboti*|*hex*|*high_noo*|*hills___*|*hollywood*|*home_pak*|*house_of" \
        "*|*hypa_bal*|*hyper___*|*inc_raw_*|*invita*|*isometric1*|*isometric2*|*isometric3*|*isometric4*|*italic" \
        "*|*italics_*|*ivrit*|*jazmine*|*jerusalem*|*joust___*|*katakana*|*kban*|*kgames_i*|*kik_star*|*krak_out" \
        "*|*larry3d*|*lazy_jon*|*lcd*|*lean*|*letter_w*|*letters*|*letterw3*|*lexible_*|*linux*|*lockergnome" \
        "*|*mad_nurs*|*madrid*|*magic_ma*|*marquee*|*master_o*|*maxfour*|*mayhem_d*|*mcg_____*|*mig_ally*|*mike" \
        "*|*mini*|*mirror*|*mnemonic*|*modern__*|*morse*|*moscow*|*mshebrew210*|*nancyj*|*nancyj-fancy*|*nancyj" \
        "-underlined*|*new_asci*|*nfi1____*|*nipples*|*notie_ca*|*npn_____*|*ntgreek*|*nvscript*|*o8*|*octal" \
        "*|*odel_lak*|*ogre*|*ok_beer_*|*os2*|*outrun__*|*p_s_h_m_*|*p_skateb*|*pacos_pe*|*panther_*|*pawn_ins*|*pawp" \
        "*|*peaks*|*pebbles*|*pepper*|*phonix__*|*platoon2*|*platoon_*|*pod_____*|*poison*|*puffy*|*pyramid*|*r2" \
        "-d2___*|*rad_____*|*rad_phan*|*radical_*|*rainbow_*|*rally_s2*|*rally_sp*|*rampage_*|*rastan__*|*raw_recu" \
        "*|*rci_____*|*rectangles*|*relief*|*relief2*|*rev*|*ripper!_*|*road_rai*|*rockbox_*|*rok_____*|*roman" \
        "*|*roman___*|*rot13*|*rounded*|*rowancap*|*rozzo*|*runic*|*runyc*|*sans*|*sansb*|*sansbi*|*sansi*|*sblood" \
        "*|*sbook*|*sbookb*|*sbookbi*|*sbooki*|*script*|*script__*|*serifcap*|*shadow*|*shimrod*|*short*|*skate_ro" \
        "*|*skateord*|*skateroc*|*sketch_s*|*slant*|*slide*|*slscript*|*sm______*|*small*|*smisome1*|*smkeyboard" \
        "*|*smscript*|*smshadow*|*smslant*|*smtengwar*|*space_op*|*spc_demo*|*speed*|*stacey*|*stampatello*|*standard" \
        "*|*star_war*|*starwars*|*stealth_*|*stellar*|*stencil1*|*stencil2*|*stop*|*straight*|*street_s*|*subteran" \
        "*|*super_te*|*t__of_ap*|*tanja*|*tav1____*|*taxi____*|*tec1____*|*tec_7000*|*tecrvs__*|*tengwar*|*term" \
        "*|*thick*|*thin*|*threepoint*|*ti_pan__*|*ticks*|*ticksslant*|*tiles*|*times*|*timesofl*|*tinker-toy" \
        "*|*tomahawk*|*tombstone*|*top_duck*|*trashman*|*trek*|*triad_st*|*ts1_____*|*tsalagi*|*tsm_____*|*tsn_base" \
        "*|*tty*|*ttyb*|*tubular*|*twin_cob*|*twopoint*|*type_set*|*ucf_fan_*|*ugalympi*|*unarmed_*|*univers" \
        "*|*usa_____*|*usa_pq__*|*usaflag*|*utopia*|*utopiab*|*utopiabi*|*utopiai*|*vortron_*|*war_of_w*|*wavy" \
        "*|*weird*|*whimsy*|*xbrite*|*xbriteb*|*xbritebi*|*xbritei*|*xchartr*|*xchartri*|*xcour*|*xcourb*|*xcourbi" \
        "*|*xcouri*|*xhelv*|*xhelvb*|*xhelvbi*|*xhelvi*|*xsans*|*xsansb*|*xsansbi*|*xsansi*|*xsbook*|*xsbookb" \
        "*|*xsbookbi*|*xsbooki*|*xtimes*|*xtty*|*xttyb*|*yie-ar__*|*yie_ar_k*|*z-pilot_*|*zig_zag_*|*zone7___ "
    fonts = f.split('*|*')
    chosen_font = 'calgphy2'
    while True:
        word = []
        print("Enter the message (Blank spaces will be replaced by '.') : ", end="")
        msg = input()

        # creating default print
        for i in msg:
            character = pyfiglet.figlet_format(i, font = chosen_font)
            character = character.split('\n')
            # character[0] = character[0]+' .'
            # for j in range(len(character)):
            #     character[j] = '. ' + character[j]
            character[0]='```'+character[0]
            character[-1] = character[-1]+'```'
            word.append(character)

        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]

        # menu
        while True:
            print('''
            1. Change Font
            2. Demo
            3. Continue
            4. Back
            5. Exit
            Enter your choice : 
            ''', end="")
            choice = int(input())

            if choice == 3:
                break
            if choice == 4:
                return
            if choice == 5:
                credits()
                driver.quit()
                exit()

            elif choice == 1:
                while True:
                    print("Enter font name (or 'help' to get list of fonts) : ", end='')
                    chosen_font = input().lower()

                    if chosen_font == 'help':
                        for i in range(0, len(fonts)-len(fonts) % 5, 5):
                            for j in range(5):
                                print(str(i+j+1).rjust(4) + '. ' + fonts[i+j].ljust(14), end = "")
                            print()
                        print("\nEnter the number of the font you want to use : ", end='')
                        font_number = int(input())
                        while font_number < 1 or font_number > len(fonts):
                            print("\nIncorrect Input. Please try again.\nEnter the number of the font you want to use "
                                  ": ", end='')
                            font_number = int(input())
                        chosen_font = fonts[font_number-1]

                    if chosen_font in fonts:
                        break
                    print("Incorrect font name. Try again.")

                # print for given font
                word = []
                for i in msg:
                    character = pyfiglet.figlet_format(i, font = chosen_font)
                    character = character.split('\n')
                    # character[0] = character[0]+' .'
                    # for j in range(len(character)):
                    #     character[j] = '. ' + character[j]
                    character[0]='```'+character[0]
                    character[-1] = character[-1]+'```'
                    word.append(character)
                    
                print("This will be sent :")
                for character in word:
                    for line in character:
                        print(line)

            elif choice == 2:
                print("This will be sent :")
                for character in word:
                    for line in character:
                        print(line)

        for character in word:
            pyperclip.copy('\n'.join(character))
            msg_box.send_keys(Keys.CONTROL, 'v')
            time.sleep(waitTime/2)
            msg_box.send_keys(Keys.ENTER)
            msg_box.send_keys(Keys.ENTER)
            time.sleep(waitTime/2)

        exit_menu()


def menu():
    global waitTime
    functions = [left_triangle, right_triangle, per_character, repeater, character_art]
    while True:
        print('''
        1. T           2. g           3. T           4. Testing
           Te             ng             e              Testing
           Tes            ing            s              Testing
           Test           ting           t              Testing
           Testi          sting          i              Testing
           Testin         esting         n              Testing
           Testing        Testing        g              Testing
        
        5. Words in Ascii Art(buggy)
        6. Change Waiting time
        7. Exit
        
        Enter your choice : ''', end='')
        choice = int(input())
        if choice in range(1, 6):
            functions[choice-1]()
        elif choice == 6:
            print("Current waiting time = " + str(waitTime))
            print("Enter new waiting time (0.5 - 60) : ", end='')
            new_time = float(input())
            if new_time < 0.5 or new_time > 60.0:
                print("Invalid input. Waiting time didn't change.")
            else:
                waitTime = new_time
                print("Waiting time successfully changed.")
        elif choice == 7:
            driver.quit()
            exit()
        else:
            print("Invalid input.\nPlease try again")
def testing():
    global msgBoxClassName
    try:
        msg_box = driver.find_elements_by_class_name(msgBoxClassName)[-1]
        msg_box.send_keys('.' + Keys.ENTER)
        print("Check if the recepient has recieved a '.' as a message. If not enter N: ", end="")
        result = input()
        if result=='N' or result=='n' or result=='no':
            raise RuntimeError
    except:
        print('Unable to send Test message.\nChech for class name of inout field using inspect and update the field.\nCurrent class name:', msgBoxClassName)
        msgBoxClassName = input("Enter new class name: ")
        if msgBoxClassName=='EXIT':
            return
        testing()

def main():
    print("Login to WhatsApp Web using your mobile and go to the chat you want to send your message to.")
    input("Press Enter to continue...")
    
    testing()
    menu()


main()
