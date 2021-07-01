from draw import Draw
class Game:
        def __init__(self):
            # Intentos por defecto
            self.__atemps = 6
            # Palabra oculta
            hide_word = '' # usamos 'get_hide_word()'
            # Convertir string en list de caracteres en minúscula
            char_list_elements = list(hide_word.lower())
            # Inicializar lista para los carácteres que vamos introduciendo
            input_char_list = list()

            draw_picture = Draw()
            draw_picture.image(self.__atemps, 'ddddd')


            
            """
          
            // Inicializar lista para los carácteres que vamos introduciendo
            InputCharsList = new List<char>();

            HideWordChars = new List<char>(charListElements);

            CorrectChars = new List<char>(charListElements);

            for(int i = 0; i < HideWordChars.Count; i++) {
                if (HideWordChars[i] != ' ') {
                    HideWordChars[i] = '_';
                    GameWordChardsShow += "_ ";
                } else {
                    GameWordChardsShow += "  ";
                }
            }
            Draw.Image(Attemps, HideWord);
            Draw.HideWord(GameWordChardsShow);
            """
        def get_hide_word(self):
            pass
        
