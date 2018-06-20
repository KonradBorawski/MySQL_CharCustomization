import pymysql.cursors
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.adapters.listadapter import ListAdapter 
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ListProperty, StringProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.config import Config 
kivy.config.Config.set('graphics','resizable', False)
from kivy.core.window import Window
Window.size = (1156, 1347/2)

dbconfig = {'host':'127.0.0.1',
            'user':'Kormi',
            'password':'haslo',
            'database': 'projektDB',}
conn = pymysql.connect(**dbconfig)
cursor = conn.cursor()
conn.commit()

Builder.load_file('screenone.kv')
Builder.load_file('screentwo.kv')
Builder.load_file('popups.kv')

def is_int(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False

def whichTable(content):
    if(content is 'Helm'):
        return 'helm'
    elif(content is 'Naramienniki'):
        return 'shoulders'
    elif(content is 'Zbroja'):
        return 'chestplate'
    elif(content is 'Rekawiczki'):
        return 'gloves'
    elif(content is 'Spodnie'):
        return 'pants'
    elif(content is 'Buty'):
        return 'boots'
    elif(content is 'Bron'):
        return 'weapon'  
     
class ListButton(ListItemButton):
    pass

class RecycleViewGridLayout(FocusBehavior, LayoutSelectionBehavior,RecycleGridLayout):
    pass

class RecycleView(Screen):
    columnID = ListProperty()
    columnName = ListProperty()
    columnArmorOrDamage = ListProperty()
    columnBonus = ListProperty()
    columnCost = ListProperty()
    AscendingOrDescending=0
    def sortByID(self,content):
        if self.AscendingOrDescending == 1:
            self.AscendingOrDescending = 0
        else:
            self.AscendingOrDescending =1
        stringList2=['ASC','DESC']
        if(content is 'Helm' or 'Naramienniki' or 'Zbroja' or 'Rekawiczki' or 'Spodnie' or 'Buty' or 'Bron'):
            _SQL ="select * from "+whichTable(content)+" order by id_"+whichTable(content)+ " "+stringList2[self.AscendingOrDescending]
        else:
            return None
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        self.columnID.clear()
        self.columnName.clear()
        self.columnArmorOrDamage.clear()
        self.columnBonus.clear()
        self.columnCost.clear()
        
        for i in range(0,len(list),1):
            self.columnID.append(str(list[i][0]))
            self.columnName.append(str(list[i][1]))
            self.columnArmorOrDamage.append(str(list[i][2]))
            self.columnBonus.append(str(list[i][3]))
            self.columnCost.append(str(list[i][4]))
    def sortElements(self,columnToSort,sortBy):
        if self.AscendingOrDescending == 1:
            self.AscendingOrDescending = 0
        else:
            self.AscendingOrDescending =1
        stringList2=['ASC','DESC']
        if(columnToSort is 'Helm' or 'Naramienniki' or 'Zbroja' or 'Rekawiczki' or 'Spodnie' or 'Buty' or 'Bron'):
            _SQL ="select * from "+whichTable(columnToSort)+" order by "+sortBy+" "+stringList2[self.AscendingOrDescending]
        else:
            return None
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        self.columnID.clear()
        self.columnName.clear()
        self.columnArmorOrDamage.clear()
        self.columnBonus.clear()
        self.columnCost.clear()
        for i in range(0,len(list),1):
            self.columnID.append(str(list[i][0]))
            self.columnName.append(str(list[i][1]))
            self.columnArmorOrDamage.append(str(list[i][2]))
            self.columnBonus.append(str(list[i][3]))
            self.columnCost.append(str(list[i][4]))
            
    def printChosenItems(self,content):
        _SQL = 'select * from '+whichTable(content)
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        self.columnID.clear()
        self.columnName.clear()
        self.columnArmorOrDamage.clear()
        self.columnBonus.clear()
        self.columnCost.clear()
        for i in range(0,len(list),1):
            self.columnID.append(str(list[i][0]))
            self.columnName.append(str(list[i][1]))
            self.columnArmorOrDamage.append(str(list[i][2]))
            self.columnBonus.append(str(list[i][3]))
            self.columnCost.append(str(list[i][4]))
    def searchForItems(self,content,search):
        _SQL ="select * from "+whichTable(content)+" where name like '%"+search+"%'"
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        self.columnID.clear()
        self.columnName.clear()
        self.columnArmorOrDamage.clear()
        self.columnBonus.clear()
        self.columnCost.clear()
        if(list == []):
            self.columnID.append('Brak')
            self.columnName.append('Brak')
            self.columnArmorOrDamage.append('Brak')
            self.columnBonus.append('Brak')
            self.columnCost.append('Brak')
        else:
            for i in range(0,len(list),1):
                self.columnID.append(str(list[i][0]))
                self.columnName.append(str(list[i][1]))
                self.columnArmorOrDamage.append(str(list[i][2]))
                self.columnBonus.append(str(list[i][3]))
                self.columnCost.append(str(list[i][4]))

class EquipOrDeleteItem(Screen):
    text = ''
    element = ''
    
    def changeStats(self):
        _SQL ='select bonus from '+whichTable(self.element)+' JOIN equipment ON equipment.id_'+whichTable(self.element)+'='+whichTable(self.element)+'.id_'+whichTable(self.element)+' where equipment.id_'+whichTable(self.element)+'=(select id_'+whichTable(self.element)+' from equipment JOIN player ON player.id_equipment=equipment.id_equipment)'
        cursor.execute(_SQL)  
        conn.commit()
        bonusBefore = str(cursor.fetchall()[0][0]) 
        whichStat=''
        if (bonusBefore ==''):
            pass
        elif (bonusBefore[-4:] == 'sily'):
            whichStat = 'strength'
        elif (bonusBefore[-10:]=='zrecznosci'):
            whichStat = 'dexterity'
        elif (bonusBefore[-10:] == 'witalnosci'):
            whichStat = 'vitality'
        elif (bonusBefore[-12:] == 'inteligencji'):
            whichStat = 'intelligence'
        else:
            pass

        if(whichStat != '' and bonusBefore[0] == '+'):
            _SQL ="select "+whichStat+" from playerStats"
            cursor.execute(_SQL)
            stat= int(cursor.fetchall()[0][0])
            help = int(bonusBefore[1])
            stat -= help
            _SQL ='UPDATE playerStats SET '+whichStat+'=%s WHERE id_player=1'
            cursor.execute(_SQL, (int(stat)))
            conn.commit()

        _SQL ="select bonus from "+whichTable(self.element)+" where id_"+whichTable(self.element)+"=%s"
        cursor.execute(_SQL, (int(self.text))) 
        bonus= str(cursor.fetchall()[0][0])
        whichStat=''
        if (bonus ==''):
            pass
        elif (bonus[-4:] == 'sily'):
            whichStat = 'strength'
        elif (bonus[-10:]=='zrecznosci'):
            whichStat = 'dexterity'
        elif (bonus[-10:] == 'witalnosci'):
            whichStat = 'vitality'
        elif (bonus[-12:] == 'inteligencji'):
            whichStat = 'intelligence'
        else:
            pass

        if(whichStat != '' and bonus[0] == '+'):
            _SQL ="select "+whichStat+" from playerStats"
            cursor.execute(_SQL)
            stat= int(cursor.fetchall()[0][0])
            help = int(bonus[1])
            stat += help
            _SQL ='UPDATE playerStats SET '+whichStat+'=%s WHERE id_player=1'
            cursor.execute(_SQL, (int(stat)))
            conn.commit()
        
    def changeItem(self):
        self.changeStats()
        _SQL ="select * from "+whichTable(self.element)
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        if(int(self.text) > list[-1][0] or self.text == self.getEquippedItemID()):
            pass
        else:
            _SQL= 'UPDATE equipment SET id_'+whichTable(self.element)+'=%s WHERE id_equipment=1'
            cursor.execute(_SQL, (int(self.text)))
            conn.commit()

    def deleteItem(self):
        _SQL ="select * from "+whichTable(self.element)
        cursor.execute(_SQL)  
        conn.commit()
        list=[]
        for row in cursor.fetchall():
            list.append(row)
        if(int(self.text) > list[-1][0] or self.text == self.getEquippedItemID()):
            pass
        else:
            _SQL='DELETE FROM '+whichTable(self.element)+' WHERE id_'+whichTable(self.element)+'=%s'
            cursor.execute(_SQL, (int(self.text)))
            conn.commit()

    def getEquippedItemID(self):
        _SQL ='select id_'+whichTable(self.element)+' from equipment JOIN player ON player.id_equipment=equipment.id_equipment'
        cursor.execute(_SQL)
        return str(cursor.fetchall()[0][0])

    def dism(self):
        global doItOnce
        doItOnce =0 
        equipOrDeleteItemPopup.dismiss()

class CustomPopup(Popup):
    def __init__(self,option, itemID, equipmentElement):
        super(CustomPopup,self).__init__()
        if option is 'CharactersStats':
            self.content = CharactersStats()
            self.title = 'Statystyki postaci'
            self.content.initStats()
            self.size_hint_x = .8
            self.size_hint_y= .8
        elif option is 'EquippedItems':
            self.content = EquippedItems()
            self.title = 'Zalozone przedmioty'
            self.content.initTable()
        elif option is 'AddItem':
            self.content = AddItem()
            self.size_hint_x = .9
            self.size_hint_y= .5
            self.title = 'Dodaj przedmiot'
        elif option is 'EquipOrDeleteItem':
            self.content = EquipOrDeleteItem()
            self.content.text = itemID
            self.content.element = equipmentElement
            self.size_hint_x = .5
            self.size_hint_y = .4
            self.title = 'Zaloz lub usun'
        elif option is 'DeleteItem':
            self.content = DeleteItem()
            self.title = 'Usun przedmiot'
        
#************************************** content, ktory przyjmuje popup

global firstStatsInit
firstStatsInit = 0

global firstStrengthBonus
firstStrengthBonus = 0
global firstDexterityBonus
firstDexterityBonus = 0
global firstIntelligenceBonus
firstIntelligenceBonus = 0
global firstVitalityBonus
firstVitalityBonus = 0


doItOnce = 0
class SelectableButton(RecycleDataViewBehavior, Button):
    element = ''
    def open_popup(self):
        global doItOnce 
        if is_int(self.text):
            if doItOnce == 0 and int(self.text) > 0 and int(self.text) < 99 and self.text != 'Brak':
                doItOnce = 1
                global equipOrDeleteItemPopup
                equipOrDeleteItemPopup = CustomPopup(option = 'EquipOrDeleteItem', itemID = self.text, equipmentElement = self.element)
                equipOrDeleteItemPopup.open()

    


class CharactersStats(Screen):
    def dism(self):
        charactersStatsPopup.dismiss()

    def initStats(self):
        global firstStatsInit
        global firstStrengthBonus
        global firstDexterityBonus
        global firstVitalityBonus
        global firstIntelligenceBonus

        if firstStatsInit == 0:
            firstStatsInit = 1
            _SQL ='select base_strength from playerstats'
            cursor.execute(_SQL)
            baseStrength = int(cursor.fetchall()[0][0])
            _SQL ='select base_dexterity from playerstats'
            cursor.execute(_SQL)
            baseDexterity = int(cursor.fetchall()[0][0])
            _SQL ='select base_intelligence from playerstats'
            cursor.execute(_SQL)
            baseIntelligence = int(cursor.fetchall()[0][0])
            _SQL ='select base_vitality from playerstats'
            cursor.execute(_SQL)
            baseVitality = int(cursor.fetchall()[0][0])

            stringList=['helm','shoulders','chestplate','gloves','pants','boots','weapon']
            for i in range(0,7,1):
                _SQL ='select bonus from '+stringList[i]+' JOIN equipment ON equipment.id_'+stringList[i]+'='+stringList[i]+'.id_'+stringList[i]+' where equipment.id_'+stringList[i]+'=(select id_'+stringList[i]+' from equipment JOIN player ON player.id_equipment=equipment.id_equipment)'
                cursor.execute(_SQL) 
                conn.commit()
                bonus = str(cursor.fetchall()[0][0]) 
                whichStat=''
                if (bonus ==''):
                    pass
                elif (bonus[-4:] == 'sily'):
                    whichStat = 'strength'
                elif (bonus[-10:]=='zrecznosci'):
                    whichStat = 'dexterity'
                elif (bonus[-10:] == 'witalnosci'):
                    whichStat = 'vitality'
                elif (bonus[-12:] == 'inteligencji'):
                    whichStat = 'intelligence'
                else:
                    pass

                if(whichStat != '' and bonus[0] == '+'):
                    if( whichStat == 'strength' and firstStrengthBonus == 0):
                        firstStrengthBonus = 1 
                        stat = baseStrength
                        stat += int(bonus[1])
                    elif( whichStat == 'dexterity' and firstDexterityBonus == 0):
                        firstDexterityBonus = 1
                        stat = baseDexterity
                        stat += int(bonus[1])
                    elif( whichStat == 'vitality' and firstVitalityBonus == 0):
                        firstVitalityBonus = 1
                        stat = baseVitality
                        stat += int(bonus[1])
                    elif( whichStat == 'intelligence' and firstIntelligenceBonus == 0):
                        firstIntelligenceBonus = 1
                        stat = baseIntelligence
                        stat += int(bonus[1])
                    else:
                        _SQL = "select "+whichStat+" from playerStats"
                        cursor.execute(_SQL)
                        stat = int(cursor.fetchall()[0][0])
                        stat += int(bonus[1])

                    
                    _SQL ='UPDATE playerStats SET '+whichStat+'=%s WHERE id_player=1'
                    cursor.execute(_SQL, (int(stat)))
                    conn.commit()
        else:
            pass
    def checkStats(self,content):
        _SQL ='select '+ content+ ' from playerstats'
        cursor.execute(_SQL)
        return int(cursor.fetchall()[0][0])

    def checkPlayer(self,content):
        _SQL ='select '+ content+ ' from player'
        cursor.execute(_SQL)
        return str(cursor.fetchall()[0][0])

class AddItem(Screen):
    def addItem(self,name,armorOrDamage,bonus,cost,element):
        if name=='' or armorOrDamage == '' or cost =='':
            pass
        else:
            _SQL ='insert into '+ whichTable(element)+ ' values(null,%s,%s,%s,%s)'
            cursor.execute(_SQL,(name,int(armorOrDamage),bonus,int(cost)))
            conn.commit()
    def dism(self):
        addItemPopup.dismiss()

class EquippedItems(Screen):
    column1 = ObjectProperty()
    column2 = ObjectProperty()
    column3 = ObjectProperty()
    column4 = ObjectProperty()
    column5 = ObjectProperty()

    column1weapon = ObjectProperty()
    column2weapon = ObjectProperty()
    column3weapon = ObjectProperty()
    column4weapon = ObjectProperty()
    column5weapon = ObjectProperty()

    def initTable(self):
        self.column1.adapter = ListAdapter(data=['ID'], cls=ListButton)
        self.column2.adapter = ListAdapter(data=['Name'], cls=ListButton)
        self.column3.adapter = ListAdapter(data=['Armor'], cls=ListButton)
        self.column4.adapter = ListAdapter(data=['Bonus'], cls=ListButton)
        self.column5.adapter = ListAdapter(data=['Cost'], cls=ListButton)

        self.column1weapon.adapter = ListAdapter(data=['ID'], cls=ListButton)
        self.column2weapon.adapter = ListAdapter(data=['Name'], cls=ListButton)
        self.column3weapon.adapter = ListAdapter(data=['Damage'], cls=ListButton)
        self.column4weapon.adapter = ListAdapter(data=['Bonus'], cls=ListButton)
        self.column5weapon.adapter = ListAdapter(data=['Cost'], cls=ListButton)
        
        elementsList=['helm','shoulders','chestplate','gloves','pants','boots']
        list=[]
        for i in range(0,len(elementsList),1):
            _SQL= 'select id_'+elementsList[i]+' from equipment JOIN player ON player.id_equipment=equipment.id_equipment'
            cursor.execute(_SQL)
            s = str(cursor.fetchall()[0][0])
            _SQL ='select * from '+elementsList[i]+' JOIN equipment ON equipment.id_'+elementsList[i]+'='+elementsList[i]+'.id_'+elementsList[i]+' where equipment.id_'+elementsList[i]+'='+s
            cursor.execute(_SQL)  

            list.append(cursor.fetchall())
            self.column1.adapter.data.extend([str(list[i][0][0])])
            self.column1._trigger_reset_populate()
            self.column2.adapter.data.extend([str(list[i][0][1])])
            self.column2._trigger_reset_populate()
            self.column3.adapter.data.extend([str(list[i][0][2])])
            self.column3._trigger_reset_populate()
            self.column4.adapter.data.extend([str(list[i][0][3])])
            self.column4._trigger_reset_populate()
            self.column5.adapter.data.extend([str(list[i][0][4])])
            self.column5._trigger_reset_populate()
        list=[]
        _SQL= 'select id_weapon from equipment JOIN player ON player.id_equipment=equipment.id_equipment'
        cursor.execute(_SQL)
        s = str(cursor.fetchall()[0][0])
        _SQL ='select * from weapon JOIN equipment ON equipment.id_weapon=weapon.id_weapon where equipment.id_weapon='+s
        cursor.execute(_SQL)  
        list.append(cursor.fetchall())
        self.column1weapon.adapter.data.extend([str(list[0][0][0])])
        self.column1weapon._trigger_reset_populate()
        self.column2weapon.adapter.data.extend([str(list[0][0][1])])
        self.column2weapon._trigger_reset_populate()
        self.column3weapon.adapter.data.extend([str(list[0][0][2])])
        self.column3weapon._trigger_reset_populate()
        self.column4weapon.adapter.data.extend([str(list[0][0][3])])
        self.column4weapon._trigger_reset_populate()
        self.column5weapon.adapter.data.extend([str(list[0][0][4])])
        self.column5weapon._trigger_reset_populate()
    def dism(self):
        equippedItemsPopup.dismiss()

#**************************************


class ScreenOne(Screen):
    labelHelm = ObjectProperty()
    labelShoulders = ObjectProperty()
    labelChestplate = ObjectProperty()
    labelGloves = ObjectProperty()
    labelPants = ObjectProperty()
    labelBoots = ObjectProperty()
    labelWeapon = ObjectProperty()
    def open_popup(self, option):
        if option is 'CharactersStats':
            global charactersStatsPopup
            charactersStatsPopup = CustomPopup(option = 'CharactersStats', itemID = '' , equipmentElement = '')
            charactersStatsPopup.open()
        elif option is 'EquippedItems':
            global equippedItemsPopup
            equippedItemsPopup = CustomPopup(option = 'EquippedItems', itemID = '' , equipmentElement = '') 
            equippedItemsPopup.open()
    def getEquippedItem(self,content):
        _SQL ='select name from '+content+' JOIN equipment ON equipment.id_'+content+'='+content+'.id_'+content+' where equipment.id_'+content+'=(select id_'+content+' from equipment JOIN player ON player.id_equipment=equipment.id_equipment)'
        cursor.execute(_SQL)  
        conn.commit()
        return str(cursor.fetchall()[0][0])
    def stopApplication(self):
        cursor.close()
        conn.close()
        Window.close()

class ScreenTwo(Screen):
    recycleView = RecycleView()
    def open_popup(self, option):
        if option is 'AddItem': 
            global addItemPopup
            addItemPopup = CustomPopup(option = 'AddItem', itemID = '' , equipmentElement = '' ) 
            addItemPopup.open()
    
 
class ProjectApp(App):
    screen_manager = None
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(ScreenOne(name="screen_one"))
        self.screen_manager.add_widget(ScreenTwo(name="screen_two"))
        return self.screen_manager

projectApp = ProjectApp()
if(__name__=='__main__'):
    projectApp.run()