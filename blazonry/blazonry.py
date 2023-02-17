class Blazonry(object):
    def __init__(self):
        self.ordinary = {
            'Pale':'sa trakom po sredini vertikalno',
            'Fess':'sa trakom po sredini horizontalno',
            'Bend':'sa trakom po levoj dijagonali',
            'Saltire':'sa dvema trakama ukrstene u X',
            'Chevron':'sa dvema trakama ukrstene tako da obrazuju sledeci oblik: ^',
            'Pall':'sa trima trakama ukrstene u Y'
            }
        self.charges = {
            'wolf':'vuk',
            'pellet':'sacma',
            'fetterlock':'katanac',
            'dagger':'bodez',
            'fleurs de lis':'ljiljan(a)',
            'mullet':'zvezda',
            'crescents': 'polumesec(a)',
            'maple leaf': 'javorov list',
            'sword':'mac',
            'rose':'ruza',
            'snowflake':'pahuljica',
            'cup':'putir',
            'wolfs':'vuka(ova)',
            'pellets':'sacme',
            'fetterlocks':'katanca',
            'daggers':'bodeza',
            'mullets':'zvezde',
            'maple leafs': 'javorova lista',
            'swords':'maca',
            'roses':'ruze',
            'snowflakes':'pahuljice',
            'cups':'putira'
        }
        self.position = {
            'base': ' u donjem delu stita',
            'dexterbase':' dole levo',
            'middlebase':' dole u sredini',
            'sinisterbase':' dole desno',
            'honourpoint':' u gornjem delu sredista stita',
            'fesspoint':' u centru stita',
            'navelpoint':' u donjem delu sredista stita',
            'dexter side':' na levoj strani',
            'sinister side':' na desnoj strana',
            'Pale':' po sredini vertikalno',
            'Fess':' po sredini horizontalno',
            'Bend':' po levoj dijagonali',
            'Saltire':' po dijagonalama',
            'Chevron':' rasporedjene u  ^',
            'Pall':' rasporedjene u Y'
        }

        self.colors = {
                        "Azure":"plave",
                        "Vert":"zelene",
                        "Gules":"crvene",
                        "Sable":"crne",
                        "Purpure":"ljubicaste",
                        "Ermine":"bele pozadine sa crnim sarama",
                        "Vair":"bele pozadine sa plavim zvonima",
                        "Or":"zlatne",
                        "Argent":"srebrne"
                    }
        self.party = {
            'Per Pale': 'podeljen na dva dela po vertikali',
            'Per Fess': 'podeljen na dva dela po horizontali',
            'Per Bend': 'podeljen na dva dela po levoj dijagonali',
            'Per Saltire':'podeljen na cetiri dela po dijagonalama',
            'Per Chevron':'podeljen na dva dela tako da linije podele obrazuju ^',
            'Per Pall':'podeljen na tri dela tako da linije podele obrazuju Y',
            'Bary': 'na horizontalne pruge',
            'Paly': 'na vertikalne pruge',
            'Bendy': 'na dijagonalne pruge',
            'Lozengy':'na romboide',
            'Gyronny':'na kvadratice'
        }

        self.numbers = {
            'one': '1',
            'two':'2',
            'three':'3',
            'four':'4',
            'five':'5',
            'six':'6',
            'seven':'7',
            'eight':'8',
            'nine':'9',
            'ten':'10',
        }
        
   

    def interpret(self, model, output_path=''):
        rbr = 1
        result_for_file = ""
        turtle_field_color, turtle_party, turtle_chief,turtle_bordure, turtle_ordinary, turtle_ordinary_color = None, None, None, None, None, None
        for field in model.fields:

            if field.__class__.__name__ == "SimpleField":
                try:
                    field_color = self.colors[field.color]
                    turtle_field_color = field.color
                except:
                    result = "pogresna boja stita"
                    turtle_field_color = None
                    # print("pogresna boja stita")
                    break   
                
                if field.color != "Ermine" and field.color != "Vair":
                    print(str(rbr) + ". Stit " , field_color + " boje")
                    result_for_file += str(rbr) + ". Stit " + field_color + " boje" +"\n"
                else:
                    print(str(rbr) + ". Stit " , field_color)
                    result_for_file += str(rbr) + ". Stit " + field_color +"\n"
                rbr +=1
            else:
                try:
                    result = "Stit "
                    if len(field.color) !=0:
                        colors = analyze_colors(self,field.color)
                        result += colors + "boje"
                        turtle_field_color = field.color
                    if field.party is not None:
                        field_party = self.party[field.party]
                        result += " "+field_party
                        turtle_party = field.party
                    if field.charges.__class__.__name__ == "ChargesThereIsOrdinary":
                        ordinary = self.ordinary[field.charges.ordinary.ordinary]
                        ordinary_color = self.colors[field.charges.ordinary.color]
                        turtle_ordinary = field.charges.ordinary.ordinary
                        turtle_ordinary_color = field.charges.ordinary.color
                        result += ", " + ordinary + " - " + ordinary_color + " boje"
                        if field.charges.chargesOnTheFiled is not None:
                            charges_on_the_field = self.charges[field.charges.chargesOnTheFiled.charge]
                            charges_num, charges_color, _ = analyze_charges(self, field.charges.chargesOnTheFiled)
                            result += ", koja se nalazi izmedju " + charges_num  + charges_on_the_field + charges_color
                    
                        if field.charges.chargesOnTheOrdinary is not None:
                            charges_on_the_ordinary = self.charges[field.charges.chargesOnTheOrdinary.charge]
                            ordinary_ch_num, ordinary_ch_color, _ = analyze_charges(self, field.charges.chargesOnTheOrdinary)
                            result += ". Na traci(trakama) se nalazi(e) " + ordinary_ch_num +charges_on_the_ordinary + ordinary_ch_color
                    
                    elif field.charges.__class__.__name__ == "ChargesNoOrdinary":
                        result += " na kom se nalazi(e) "
                        for idx, charge in enumerate(field.charges.charge):
                            charges_on_the_field = self.charges[charge.charge]
                            charges_num, charges_color, charge_position = analyze_charges(self,charge)
                            if charges_num == "":
                                charges_num = " 1 "

                            if len(field.charges.charge) == 1:
                                result +=charges_num  + charges_on_the_field + charges_color + charge_position
                            else:    
                                if idx == (len(field.charges.charge)-1):
                                    result += " i "+ charges_num  + charges_on_the_field + charges_color + charge_position 
                                else:
                                    result +=charges_num  + charges_on_the_field + charges_color + charge_position + ", "
                     
                    if field.chief is not None:
                        chief_color =self.colors[field.chief.color]
                        result += ". Preko gornje ivice stita nalazi se traka " + chief_color + " boje"
                        turtle_chief = field.chief.color
                        if len(field.chief.charge) != 0: #samo ako ima naboja na chief-u
                            result += " na kojoj se nalazi(e) "

                            for idx, charge in enumerate(field.chief.charge):
                                charges_on_the_chief = self.charges[charge.charge]
                                chief_charges_num, chief_charges_color, chief_charge_position = analyze_charges(self,charge)

                                if idx == (len(field.chief.charge)-1):
                                    result += " i "+ chief_charges_num  + charges_on_the_chief + chief_charges_color + chief_charge_position 
                                else:
                                    result +=chief_charges_num  + charges_on_the_chief + chief_charges_color + chief_charge_position + ", "
                    
                    if field.bordure is not None:
                        bordure_color =self.colors[field.bordure.color]
                        turtle_bordure = field.bordure.color
                        for idx, charge in enumerate(field.bordure.charges):
                            suma_pozicija = add(self, charge.numbers)
                            if len(charge.numbers) == 0 or int(self.numbers[charge.number]) == suma_pozicija:
                                result += ". Stit je uokviren trakom " + bordure_color + " boje"
                                charges_on_the_bordure = self.charges[charge.charge]
                                bordure_charges_num, bordure_charges_color, bordure_charges_position = analyze_bordure_charges(self,charge)
                                
                                if len(field.bordure.charges) == 1:
                                    result +=  " na kojoj se nalazi(e) "+ str(bordure_charges_num)  + charges_on_the_bordure + bordure_charges_color + bordure_charges_position

                                else:                                    
                                    if idx == (len(field.bordure.charges)-1):
                                        result += " i "+ str(bordure_charges_num)  + charges_on_the_bordure + bordure_charges_color + bordure_charges_position
                                    else:
                                        result +=str(bordure_charges_num)  + charges_on_the_bordure + bordure_charges_color +bordure_charges_position + ", "
                            else:
                                result = "" #result.replace(result,"")
                                result += f"Neispravan blazon! Naveli ste  {str(self.numbers[charge.number])} {str(self.charges[charge.charge])}, a rasporedjujete {str(suma_pozicija)}: '{charge.number} {charge.charge} {' '.join(charge.color)} {', '.join(charge.numbers)}'"                              
                    if field.cadency is not None:
                        cadency_colors = field.cadency.color
                        cadency_number = "1"
                        cadency_charge = self.charges[field.cadency.charge]

                        if field.cadency.number is not None:
                            cadency_number = self.numbers[field.cadency.number]
                        if len(cadency_colors) > int(cadency_number):
                            result = ""
                            result += f"Neispravan blazon! Naveli ste {str(len(cadency_colors))} boje(a), a samo {str(int(cadency_number))} naboj(a): '{field.cadency.charge} {', '.join(cadency_colors)}' "                              
                        else:
                            if len(cadency_colors) == 1:
                                cadency_color =self.colors[cadency_colors[0]]
                                result += f" Preko osnovne kompozicije je postavljen {cadency_number} {cadency_charge} {cadency_color} boje." 
                            else:
                                result += f" Preko osnovne kompozicije je postavljeno {cadency_number} {cadency_charge} " 
                                cadency_color = analyze_colors(self,cadency_colors)     
                                result += cadency_color + "boje."                                   

                except Exception as e:
                    print("greska")
                    print(str(e))

                print("" + str(rbr) +".",result)
                result_for_file += str(rbr) +". " + result + "\n"
                rbr +=1
        if output_path != '':
            save_in_file(output_path,result_for_file)
        return turtle_field_color, turtle_party, turtle_chief,turtle_bordure, turtle_ordinary, turtle_ordinary_color
        




def save_in_file(path, result):
    with open(path, 'w+') as f:
        f.write(result)
    print(f"\n---You can also find result in {path}---")

def analyze_colors(self, colors: list):
    result = ""        
    for idx, color in enumerate(colors):
        if idx != (len(colors)-1) or len(colors) == 1:
            result += self.colors[color] + " "
        else: #ako je poslednja boja u nizu dodaj "i" ispred
            result += "i "+self.colors[color] + " "
    return result

def analyze_charges(self,charge):
    chargesNum = ''
    chargesColor = ''
    chargesPosition = ''
    if charge.number is not None:
        chargesNum = self.numbers[charge.number] + " "
    if len(charge.color) != 0:
        chargesColor = " "+analyze_colors(self, charge.color) + "boje"
    if charge.position is not None:
        chargesPosition = self.position[charge.position.value]
    
    return chargesNum, chargesColor, chargesPosition

def analyze_bordure_charges(self,charge):
    chargesNum = ''
    chargesColor = ''
    chargesPosition = ''
    if charge.number is not None:
        chargesNum = self.numbers[charge.number] + " "
    if len(charge.color) != 0:
        chargesColor = " "+analyze_colors(self, charge.color) + "boje"

    if charge.numbers is not None:
        if 2 <= len(charge.numbers):
            chargesPosition += ": "  + self.numbers[charge.numbers[0]] + " na vrhu, " + self.numbers[charge.numbers[1]] + " u sredini"
        if len(charge.numbers) == 3:
            chargesPosition += ", " + self.numbers[charge.numbers[2]] + " u osnovi stita. "
        else:
            chargesPosition += ". "
    
    return chargesNum, chargesColor, chargesPosition


def add(self,list_str):
    amount = 0
    for num in list_str:
        num = self.numbers[num]
        amount += int(num)

    return amount

