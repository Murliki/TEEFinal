from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from compile import *
code1 = ['0', '0', '0']

global TEEApp
class TEEApp(MDApp):
    global code1
    global R1Input, R2Input, R3Input, E1Input, E2Input, E3Input
    code1 = ['0', '0', '0']
    global var1, var2, var3
    var1 = 0
    var2 = 0
    var3 = 0
    global default_color
    global ResResScreen
    default_color = [0.5, 0.7, 0, 1]

    global varkir
    varkir = 0

    def Back(self, instance):
        self.root.current = 'MainScreen'

    def ToThreePhaseScreen(self, instance):
        self.root.current = 'ThreePhaseScreen'

    def ToResScreen(self, instance):
        self.root.current = 'ResScreen'
        ResResScreen.clear_widgets()

    def ToResResScreen(self, instance):
        self.root.current = 'ResResScreen'

    def ToThreePhaseResScreen(self, instance):
        self.root.current = 'ThreePhaseResScreen'


    def ChangeIcons(self, instance):
        if instance.icon == 'down.png':
            instance.icon = 'up.png'
            instance.parent.children[2].text = var222
        elif instance.icon == 'up.png':
            instance.icon = 'down.png'
            instance.parent.children[2].text = var111
        else:
            instance.icon = 'back.png'

    def ChangeIconsPhase(self, instance):
        if instance.icon == 'down.png':
            instance.icon = 'up.png'
            instance.parent.children[2].text = var133
        elif instance.icon == 'up.png':
            instance.icon = 'down.png'
            instance.parent.children[2].text = var122
        else:
            instance.icon = 'back.png'

    def ChangeIconsKir(self, instance):
        global varkir
        try:
            if varkir == 0:
                varkir += 1
                instance.parent.children[2].text = var000[(len(var000)//3):(len(var000)//3)*2]
            elif varkir == 1:
                varkir += 1
                instance.parent.children[2].text = var000[((len(var000)//3)*2):-1]
                instance.icon = 'up.png'
            elif varkir == 2:
                varkir = 0
                instance.parent.children[2].text = var000[0:len(var000)//3]
                instance.icon = 'down.png'
            else:
                instance.parent.children[2].text = 'Беда'
        except:
            varkir = 0
            


    
    def ChangeColor3(self, instance):
        instance.md_bg_color = [0, 1, 0, 1]
        global code1
        global var3
        if var3 == 0:
            code1[2] = '1'
            instance.icon = 'up.png'    
            var3 = 1
        elif var3 == 1:
            code1[2] = 'm'
            instance.icon = 'down.png'
            var3 = 2
        elif var3 == 2:
            code1[2] = '0'
            instance.md_bg_color = default_color 
            instance.icon = 'round.png'
            var3=0

    def ChangeColor2(self, instance):
        instance.md_bg_color = [0, 1, 0, 1]
        global code1
        global var2
        if var2 == 0:
            code1[1] = '1'
            instance.icon = 'up.png'    
            var2 = 1
        elif var2 == 1:
            code1[1] = 'm'
            instance.icon = 'down.png'
            var2 = 2
        elif var2 == 2:
            code1[1] = '0'
            instance.md_bg_color = default_color  
            instance.icon = 'round.png'
            var2=0


    def ChangeColor1(self, instance):
        instance.md_bg_color = [0, 1, 0, 1]
        global code1
        global var1
        if var1 == 0:
            code1[0] = '1'
            instance.icon = 'up.png'    
            var1 = 1
        elif var1 == 1:
            code1[0] = 'm'
            instance.icon = 'down.png'
            var1 = 2
        elif var1 == 2:
            code1[0] = '0'
            instance.md_bg_color = default_color  
            instance.icon = 'round.png'
            var1=0


    def FinalResContur(self, instance):
        ResResScreen.clear_widgets()
        global var111, var222, var000
        var000 = str(count('THREERES', instance.parent.children[12].text, instance.parent.children[11].text, instance.parent.children[10].text, 'CONTUR', instance.parent.children[9].text, instance.parent.children[8].text, instance.parent.children[7].text, 0, ''.join(code1)))
        
        var111 = var000[0:len(var000)//2]
        var222 = var000[len(var000)//2:-1]
        TextButton = MDFloatingActionButton(
            icon = 'down.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.9, 'center_y': 0.05},
            on_press = self.ChangeIcons
        )
        TextVar = MDTextField(text=var111, 
                              font_size=14, 
                              multiline=True, 
                              readonly=True, 
                              size_hint=[0.95,  0.9], 
                              pos_hint = {'center_x': 0.5, 
                                          'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToResScreen          
        )
        )
        ResResScreen.add_widget(TextButton)

    def FinalResNodal(self, instance):
        ResResScreen.clear_widgets()
        global var111, var222, var000
        var111 = ''
        var222 = ''
        var000 = str(count('THREERES', instance.parent.children[12].text, instance.parent.children[11].text, instance.parent.children[10].text, 'NODAL', instance.parent.children[9].text, instance.parent.children[8].text, instance.parent.children[7].text, 0, ''.join(code1)))
        
        var111 = var000[0:len(var000)//2]
        var222 = var000[len(var000)//2:-1]
        TextButton = MDFloatingActionButton(
            icon = 'down.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.9, 'center_y': 0.05},
            on_press = self.ChangeIcons
        )
        TextVar = MDTextField(text=var111, 
                              font_size=14, 
                              multiline=True, 
                              readonly=True, 
                              size_hint=[0.95,  0.9], 
                              pos_hint = {'center_x': 0.5, 
                                          'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToResScreen          
        )
        )
        ResResScreen.add_widget(TextButton)

    def FinalResKirchhoff(self, instance):
        ResResScreen.clear_widgets()
        global var111, var222, var000
        var111 = ''
        var222 = ''
        var000 = str(count('THREERES', instance.parent.children[12].text, instance.parent.children[11].text, instance.parent.children[10].text, 'Kirchhoff', instance.parent.children[9].text, instance.parent.children[8].text, instance.parent.children[7].text, 0, ''.join(code1)))
        var111 = var000[0:len(var000)//2]
        var222 = var000[len(var000)//2:-1]
        TextButton = MDFloatingActionButton(
            icon = 'down.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.9, 'center_y': 0.05},
            on_press = self.ChangeIconsKir
        )
        TextVar = MDTextField(text=var000[0:len(var000)//3], 
                              font_size=14, 
                              multiline=True, 
                              readonly=True, 
                              size_hint=[0.95,  0.9], 
                              pos_hint = {'center_x': 0.5, 
                                          'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToResScreen          
        )
        )
        ResResScreen.add_widget(TextButton)

    def FinalResTriangle(self, instance):
        ResResScreen.clear_widgets()
        global var122, var133, var144
        var122 = ''
        var133 = ''
        try:
            var144 = str(count('THREEPHASE', complex(instance.parent.children[6].text), complex(instance.parent.children[5].text), complex(instance.parent.children[4].text), method='TRIANGLE', UU=float(instance.parent.children[7].text)))
        except:
            var144 = 'Ошибочка вышла, скорее всего введены кривые данные'
        
        TextVar = MDTextField(text=var144, 
                            font_size=14, 
                            multiline=True, 
                            readonly=True, 
                            size_hint=[0.95,  0.9], 
                            pos_hint = {'center_x': 0.5, 
                                            'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToThreePhaseScreen          
        )
        )

    def FinalResNeutral(self, instance):
        ResResScreen.clear_widgets()
        global var122, var133, var144
        var122 = ''
        var133 = ''
        try:
            var144 = str(count('THREEPHASE', complex(instance.parent.children[6].text), complex(instance.parent.children[5].text), complex(instance.parent.children[4].text), method='STARNEUTRAL', UU=float(instance.parent.children[7].text)))
        except:
            var144 = 'Ошибочка вышла, скорее всего введены кривые данные'
        
        TextVar = MDTextField(text=var144, 
                            font_size=14, 
                            multiline=True, 
                            readonly=True, 
                            size_hint=[0.95,  0.9], 
                            pos_hint = {'center_x': 0.5, 
                                            'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToThreePhaseScreen          
        )
        )

    def FinalResNoNeutral(self, instance):
        ResResScreen.clear_widgets()
        global var122, var133, var144
        var122 = ''
        var133 = ''
        try:
            var144 = str(count('THREEPHASE', complex(instance.parent.children[6].text), complex(instance.parent.children[5].text), complex(instance.parent.children[4].text), method='STARNONEUTRAL', UU=float(instance.parent.children[7].text)))
            var122 = var144[0:len(var144)//2]
            var133 = var144[len(var144)//2:-1]
        except:
            var144 = 'Ошибочка вышла, скорее всего введены кривые данные'
        TextButton = MDFloatingActionButton(
            icon = 'down.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.9, 'center_y': 0.05},
            on_press = self.ChangeIconsPhase
        )
        TextVar = MDTextField(text=var144[0:len(var144)//2], 
                            font_size=14, 
                            multiline=True, 
                            readonly=True, 
                            size_hint=[0.95,  0.9], 
                            pos_hint = {'center_x': 0.5, 
                                            'center_y': 0.5})
        ResResScreen.add_widget(TextVar)
        ResResScreen.add_widget(MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToThreePhaseScreen          
        )
        )
        ResResScreen.add_widget(TextButton)

        
        

    def build(self):

        # self.root = Builder.load_string(KV)

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Orange'
        global CurrentScreen
        CurrentScreen = MDScreenManager()

        MainScreen = MDScreen(FitImage(source='HuTaoBlured.png'), name='MainScreen')

        CurrentScreen.add_widget(MainScreen)

        ThreePhaseResScreen = MDScreen(name='ThreePhaseResScreen')

        ResLabel = MDLabel()
        ThreePhaseResScreen.add_widget(ResLabel)
        CurrentScreen.add_widget(ThreePhaseResScreen)
        global ResResScreen
        ResResScreen = MDScreen(name='ResResScreen')


        CurrentScreen.add_widget(ResResScreen)

        # MainScreen.add_widget(FitImage(source='orange.jpg', opacity=90, pos_hint={'center_x': 0.5, 'center_y': 0.25}))

        ThreePhaseBut = MDRectangleFlatButton(
            text='Трехфазная\nцепь',
            size_hint=[0.8, 0.4],
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            font_size = 30,
            md_bg_color = [0.6, 0.6, 0.0, 0.25],
            text_color = [0, 0, 0, 1],
            on_press = self.ToThreePhaseScreen
        )

        ThreeResBut = MDRectangleFlatButton(
            # FitImage(source='orange.jpg', opacity = 0.5),
            text='Цепь с тремя\nрезисторами',
            size_hint=[0.8, 0.4],
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            text_color = [0, 0, 0, 1],
            md_bg_color = [0.6, 0.6, 0.0, 0.25],
            font_size = 30,
            on_press = self.ToResScreen
            )
        

        MainScreen.add_widget(ThreeResBut)
        
        MainScreen.add_widget(ThreePhaseBut)
        
        

        ThreePhaseScreen = MDScreen(name='ThreePhaseScreen')
        
        CurrentScreen.add_widget(ThreePhaseScreen)
        UInput = MDTextField(
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            helper_text = '380',
            hint_text = 'Напряжение(U)',
            multiline = False
        )
        ThreePhaseScreen.add_widget(UInput)
        
        ZAInput = MDTextField(
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.72},
            helper_text = '2+7j',
            hint_text = 'ZA',
            multiline = False,
        )
        ThreePhaseScreen.add_widget(ZAInput)

        ZBInput = MDTextField(
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.64},
            helper_text = '2+0j',
            hint_text = 'ZB',
            multiline = False,
        )
        ThreePhaseScreen.add_widget(ZBInput)

        ZCInput = MDTextField(
            size_hint=[0.7, 0.10],
            pos_hint={'center_x': 0.5, 'center_y': 0.56},
            helper_text = '0+7j',
            hint_text = 'ZC',
            multiline = False,

        )
        ThreePhaseScreen.add_widget(ZCInput)
        
        NeutralButton = MDRectangleFlatButton(
            text = 'Рассчитать соединение\nзвездой',
            font_size = '14',
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_press = self.FinalResNeutral,
            on_release = self.ToResResScreen
        )
        ThreePhaseScreen.add_widget(NeutralButton)

        NonNeutralButton = MDRectangleFlatButton(
            text = 'Рассчитать соединение\nзвездой с обрывом',
            font_size = '14',
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            on_press = self.FinalResNoNeutral,
            on_release = self.ToResResScreen
        )
        ThreePhaseScreen.add_widget(NonNeutralButton)

        TriangleButton = MDRectangleFlatButton(
            text = 'Рассчитать соеденение\nтреугольником',
            font_size = '14',
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press = self.FinalResTriangle,
            on_release = self.ToResResScreen
        )
        ThreePhaseScreen.add_widget(TriangleButton)

        BackButton1 =  MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.Back
        )
        ThreePhaseScreen.add_widget(BackButton1)

        ResScreen = MDScreen(name='ResScreen')
        CurrentScreen.add_widget(ResScreen)

        R1Input = MDTextField(

            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.25, 'center_y': 0.85},
            hint_text = ' R1',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '1'
        )
        ResScreen.add_widget(R1Input)

        R2Input = MDTextField(

            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.85},
            hint_text = ' R2',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '1'
        )
        ResScreen.add_widget(R2Input)

        R3Input = MDTextField(

            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.75, 'center_y': 0.85},
            hint_text = ' R3',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '1'
        )
        ResScreen.add_widget(R3Input)   

        E1Input = MDTextField(

            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.25, 'center_y': 0.75},
            hint_text = ' E1',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '0'
        )
        ResScreen.add_widget(E1Input) 
        

        E2Input = MDTextField(

            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            hint_text = ' E2',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '0'
        )
        ResScreen.add_widget(E2Input)  

        E3Input = MDTextField(
            size_hint=[0.1, 0.1],
            pos_hint={'center_x': 0.75, 'center_y': 0.75},
            hint_text = ' E3',
            multiline = False,
            halign = 'center',
            input_type = 'number',
            input_filter = 'int',
            text = '0'
        )
        ResScreen.add_widget(E3Input)   

         



        Middle1Button = MDFloatingActionButton(
            icon = 'round.png',
            size=[40, 40],
            pos_hint={'center_x': 0.25, 'center_y': 0.65},     
            on_press = self.ChangeColor1,
            md_bg_color = default_color  
        )
        ResScreen.add_widget(Middle1Button)

        Middle2Button = MDFloatingActionButton(
            icon = 'round.png',
            size=[40, 40],
            pos_hint={'center_x': 0.5, 'center_y': 0.65}, 
            on_press = self.ChangeColor2,
            md_bg_color = default_color      
        )
        ResScreen.add_widget(Middle2Button)

        Middle3Button = MDFloatingActionButton(
            icon = 'round.png',
            size=[40, 40],
            pos_hint={'center_x': 0.75, 'center_y': 0.65},
            on_press = self.ChangeColor3,
            md_bg_color = default_color         
        )
        ResScreen.add_widget(Middle3Button)


        ConturButton = MDRectangleFlatButton(
            text = 'Рассчитать методом\nконтурных токов',
            font_size = '14',
            size_hint=[0.7, 0.10],
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            on_press = self.FinalResContur,
            on_release = self.ToResResScreen
            
        )
        ResScreen.add_widget(ConturButton)
        
        NodleButton = MDRectangleFlatButton(
            text = 'Рассчитать методом\nузловых потенциалов',

            font_size = '14',
            size_hint=[0.7, 0.10],
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            on_press = self.FinalResNodal,
            on_release = (self.ToResResScreen)
        )
        ResScreen.add_widget(NodleButton)

        KirchhoffButton = MDRectangleFlatButton(
            text = 'Рассчитать методом Киргофа',
            font_size = '14',
            size_hint=[0.7, 0.1],
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_release = (self.ToResResScreen),
            on_press = self.FinalResKirchhoff
        )
        ResScreen.add_widget(KirchhoffButton)

        BackButton2 =  MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.Back
        )

        ResScreen.add_widget(BackButton2)

        BackButton5 =  MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToThreePhaseScreen
        )
        ThreePhaseResScreen.add_widget(BackButton5)



        BackButton6 =  MDFloatingActionButton(
            icon = 'back.png',
            size_hint = [0.2, 0.07],
            pos_hint = {'center_x': 0.05, 'center_y': 0.95},
            on_press = self.ToResScreen,
        )
 
        

        return CurrentScreen







if __name__ == '__main__':
    TEEApp().run()
    
