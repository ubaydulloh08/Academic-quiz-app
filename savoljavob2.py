import tkinter as tk
import random
barcha_savollar = [
    {"savol": "Which famous company produced uniforms for the Nazis?", "javoblar": ["A) NIKE ", "B) HUGO BOSS", "C) ADIDAS ", "D) REEBOK"], "togri": 2},
    {"savol": "What is the capital of South Korea", "javoblar": ["A) Tokyo", "B) Busan", "C) Seoul", "D) Incheon"], "togri": 3},
    {"savol": "What is the name of the largest ocean in the world?", "javoblar": ["A) Pacific", "B) Atlantic", "C) Indian", "D) North"], "togri": 1},
    {"savol": "What is sodium chloride?", "javoblar": ["A) Water", "B) Sugar", "C) atmosphere", "D) salt"], "togri": 4},
    {"savol": "The largest planet in the solar system?", "javoblar": ["A) Mars", "B) Venus", "C) Jupiter", "D) Saturn"], "togri": 3},
    {"savol": "What is the rarest naturally occurring element in the Earth's crust?", "javoblar": ["A) Francium", "B) Astatine", "C) Osmium", "D) Promethium"], "togri": 2},
    {"savol": "Which particle is responsible for granting mass to other particles?", "javoblar": ["A) Graviton", "B) Tachyon", "C) Higgs Boson", "D) Fermion"], "togri": 3},
    {"savol": "What is the precise value of the Planck length in meters?", "javoblar": ["A) 1.6 x 10^-35", "B) 6.6 x 10^-34", "C) 3.0 x 10^8", "D) 9.1 x 10^-31"], "togri": 1},
    {"savol": "Which law states that the entropy of an isolated system always increases?", "javoblar": ["A) Newton's 3rd Law", "B) 1st Law of Thermodynamics", "C) 2nd Law of Thermodynamics", "D) Hooke's Law"], "togri": 3},
    {"savol": "What is the most abundant protein in the human body?", "javoblar": ["A) Keratin", "B) Hemoglobin", "C) Actin", "D) Collagen"], "togri": 4},
    {"savol": "Which isotope is used in radiocarbon dating?", "javoblar": ["A) Carbon-12", "B) Carbon-13", "C) Carbon-14", "D) Uranium-235"], "togri": 3},
    {"savol": "What is the chemical formula for sulfuric acid?", "javoblar": ["A) HCl", "B) H2SO4", "C) HNO3", "D) H2CO3"], "togri": 2},
    {"savol": "Who formulated the uncertainty principle in quantum mechanics?", "javoblar": ["A) Niels Bohr", "B) Max Planck", "C) Werner Heisenberg", "D) Erwin Schrödinger"], "togri": 3},
    {"savol": "What biological order do bats belong to?", "javoblar": ["A) Rodentia", "B) Chiroptera", "C) Primates", "D) Carnivora"], "togri": 2},
    {"savol": "Which organelle is known as the powerhouse of the cell?", "javoblar": ["A) Nucleus", "B) Ribosome", "C) Mitochondrion", "D) Golgi apparatus"], "togri": 3},
    {"savol": "What is the name of the largest volcano in the solar system?", "javoblar": ["A) Mauna Loa", "B) Mount Everest", "C) Olympus Mons", "D) Valles Marineris"], "togri": 3},
    {"savol": "Which moon of Jupiter is considered the most volcanically active body in the solar system?", "javoblar": ["A) Europa", "B) Ganymede", "C) Callisto", "D) Io"], "togri": 4},
    {"savol": "What defines the boundary around a black hole beyond which no light can escape?", "javoblar": ["A) Event Horizon", "B) Accretion Disk", "C) Photon Sphere", "D) Singularity"], "togri": 1},
    {"savol": "Which galaxy is on a collision course with the Milky Way?", "javoblar": ["A) Triangulum", "B) Andromeda", "C) Sombrero", "D) Whirlpool"], "togri": 2},
    {"savol": "What is the term for a star that has collapsed into a dense core of neutrons?", "javoblar": ["A) White Dwarf", "B) Red Giant", "C) Neutron Star", "D) Pulsar"], "togri": 3},
    {"savol": "Who discovered the cosmic microwave background radiation?", "javoblar": ["A) Hubble", "B) Einstein", "C) Penzias and Wilson", "D) Hawking"], "togri": 3},
    {"savol": "What is the closest star system to the Solar System?", "javoblar": ["A) Sirius", "B) Alpha Centauri", "C) Proxima Centauri", "D) Betelgeuse"], "togri": 2},
    {"savol": "What phenomenon causes time to pass slower near massive objects?", "javoblar": ["A) Time Dilation", "B) Length Contraction", "C) Quantum Entanglement", "D) Doppler Effect"], "togri": 1},
    {"savol": "Which spacecraft was the first to enter interstellar space?", "javoblar": ["A) Pioneer 10", "B) Voyager 1", "C) New Horizons", "D) Cassini"], "togri": 2},
    {"savol": "What is the hypothetical sphere of icy objects surrounding the solar system?", "javoblar": ["A) Kuiper Belt", "B) Asteroid Belt", "C) Oort Cloud", "D) Heliosphere"], "togri": 3},
    {"savol": "In what year did the Western Roman Empire fall?", "javoblar": ["A) 410 AD", "B) 476 AD", "C) 1453 AD", "D) 395 AD"], "togri": 2},
    {"savol": "Who was the founder of the Mongol Empire?", "javoblar": ["A) Kublai Khan", "B) Ogedei Khan", "C) Genghis Khan", "D) Batu Khan"], "togri": 3},
    {"savol": "Which treaty ended the Thirty Years' War in 1648?", "javoblar": ["A) Treaty of Versailles", "B) Peace of Westphalia", "C) Treaty of Tordesillas", "D) Treaty of Paris"], "togri": 2},
    {"savol": "Who was the last Pharaoh of ancient Egypt?", "javoblar": ["A) Ramses II", "B) Hatshepsut", "C) Cleopatra VII", "D) Tutankhamun"], "togri": 3},
    {"savol": "Which civilization built the ancient city of Machu Picchu?", "javoblar": ["A) Maya", "B) Aztec", "C) Inca", "D) Olmec"], "togri": 3},
    {"savol": "In which battle was Napoleon Bonaparte finally defeated?", "javoblar": ["A) Austerlitz", "B) Leipzig", "C) Waterloo", "D) Borodino"], "togri": 3},
    {"savol": "Who was the primary author of the US Declaration of Independence?", "javoblar": ["A) George Washington", "B) Thomas Jefferson", "C) Benjamin Franklin", "D) John Adams"], "togri": 2},
    {"savol": "The Peloponnesian War was fought between Athens and which other city-state?", "javoblar": ["A) Sparta", "B) Troy", "C) Thebes", "D) Corinth"], "togri": 1},
    {"savol": "Which English king signed the Magna Carta in 1215?", "javoblar": ["A) Richard the Lionheart", "B) Henry VIII", "C) King John", "D) Edward I"], "togri": 3},
    {"savol": "Who led the Bolshevik Revolution in Russia in 1917?", "javoblar": ["A) Joseph Stalin", "B) Leon Trotsky", "C) Vladimir Lenin", "D) Karl Marx"], "togri": 3},
    {"savol": "What is the deepest oceanic trench on Earth?", "javoblar": ["A) Tonga Trench", "B) Mariana Trench", "C) Kuril Trench", "D) Puerto Rico Trench"], "togri": 2},
    {"savol": "Which country has the most islands in the world?", "javoblar": ["A) Indonesia", "B) Philippines", "C) Sweden", "D) Canada"], "togri": 3},
    {"savol": "What is the longest river in Asia?", "javoblar": ["A) Mekong", "B) Yellow", "C) Yangtze", "D) Ganges"], "togri": 3},
    {"savol": "Which is the smallest independent state in the world by area?", "javoblar": ["A) Monaco", "B) Nauru", "C) Tuvalu", "D) Vatican City"], "togri": 4},
    {"savol": "What is the capital city of Australia?", "javoblar": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"], "togri": 3},
    {"savol": "Which mountain range separates Europe from Asia?", "javoblar": ["A) Alps", "B) Andes", "C) Himalayas", "D) Ural Mountains"], "togri": 4},
    {"savol": "What is the largest desert in the world (including polar regions)?", "javoblar": ["A) Sahara", "B) Arabian", "C) Gobi", "D) Antarctic Desert"], "togri": 4},
    {"savol": "Which river flows through the Grand Canyon?", "javoblar": ["A) Mississippi", "B) Colorado", "C) Rio Grande", "D) Snake"], "togri": 2},
    {"savol": "What is the highest waterfall in the world?", "javoblar": ["A) Niagara Falls", "B) Victoria Falls", "C) Angel Falls", "D) Iguazu Falls"], "togri": 3},
    {"savol": "In which country is the historical city of Petra located?", "javoblar": ["A) Egypt", "B) Syria", "C) Lebanon", "D) Jordan"], "togri": 4},
    {"savol": "Who wrote 'One Hundred Years of Solitude'?", "javoblar": ["A) Jorge Luis Borges", "B) Gabriel García Márquez", "C) Mario Vargas Llosa", "D) Julio Cortázar"], "togri": 2},
    {"savol": "In George Orwell's '1984', what is the name of the totalitarian state's leader?", "javoblar": ["A) Big Brother", "B) The Commander", "C) The Chairman", "D) The Overseer"], "togri": 1},
    {"savol": "Who is the author of 'The Divine Comedy'?", "javoblar": ["A) Homer", "B) Virgil", "C) Dante Alighieri", "D) Geoffrey Chaucer"], "togri": 3},
    {"savol": "Which philosopher proposed the 'Categorical Imperative'?", "javoblar": ["A) Friedrich Nietzsche", "B) Immanuel Kant", "C) René Descartes", "D) John Locke"], "togri": 2},
    {"savol": "What is the pen name of Samuel Langhorne Clemens?", "javoblar": ["A) Charles Dickens", "B) Mark Twain", "C) George Orwell", "D) Lewis Carroll"], "togri": 2},
    {"savol": "Who wrote the philosophical work 'Thus Spoke Zarathustra'?", "javoblar": ["A) Arthur Schopenhauer", "B) Karl Marx", "C) Friedrich Nietzsche", "D) Jean-Paul Sartre"], "togri": 3},
    {"savol": "Which epic poem features the hero Gilgamesh?", "javoblar": ["A) The Iliad", "B) The Odyssey", "C) Epic of Gilgamesh", "D) Beowulf"], "togri": 3},
    {"savol": "Who wrote the tragedy 'Hamlet'?", "javoblar": ["A) Christopher Marlowe", "B) William Shakespeare", "C) John Milton", "D) Ben Jonson"], "togri": 2},
    {"savol": "What is the longest novel ever written according to Guinness World Records?", "javoblar": ["A) War and Peace", "B) In Search of Lost Time", "C) Les Misérables", "D) Don Quixote"], "togri": 2},
    {"savol": "Which Greek philosopher was a student of Socrates and teacher of Aristotle?", "javoblar": ["A) Pythagoras", "B) Heraclitus", "C) Epicurus", "D) Plato"], "togri": 4},
    {"savol": "Who painted 'The Starry Night'?", "javoblar": ["A) Claude Monet", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Salvador Dalí"], "togri": 2},
    {"savol": "Which composer wrote the 'Symphony No. 9' while completely deaf?", "javoblar": ["A) Mozart", "B) Bach", "C) Beethoven", "D) Chopin"], "togri": 3},
    {"savol": "In which museum is the 'Mona Lisa' displayed?", "javoblar": ["A) British Museum", "B) The Met", "C) Uffizi Gallery", "D) The Louvre"], "togri": 4},
    {"savol": "Who sculpted 'David'?", "javoblar": ["A) Donatello", "B) Leonardo da Vinci", "C) Michelangelo", "D) Raphael"], "togri": 3},
    {"savol": "What art movement was Salvador Dalí associated with?", "javoblar": ["A) Impressionism", "B) Cubism", "C) Surrealism", "D) Realism"], "togri": 3},
    {"savol": "Who painted 'The Persistence of Memory'?", "javoblar": ["A) Pablo Picasso", "B) Salvador Dalí", "C) Frida Kahlo", "D) Rene Magritte"], "togri": 2},
    {"savol": "Which architect designed the Sagrada Família in Barcelona?", "javoblar": ["A) Frank Lloyd Wright", "B) Zaha Hadid", "C) Antoni Gaudí", "D) Le Corbusier"], "togri": 3},
    {"savol": "What period of music includes composers like Bach and Vivaldi?", "javoblar": ["A) Classical", "B) Romantic", "C) Baroque", "D) Renaissance"], "togri": 3},
    {"savol": "Who composed the ballet 'The Nutcracker'?", "javoblar": ["A) Stravinsky", "B) Tchaikovsky", "C) Prokofiev", "D) Shostakovich"], "togri": 2},
    {"savol": "Which artist is famous for his Campbell's Soup Cans?", "javoblar": ["A) Jackson Pollock", "B) Roy Lichtenstein", "C) Andy Warhol", "D) Mark Rothko"], "togri": 3},
    {"savol": "Who is considered the first computer programmer?", "javoblar": ["A) Alan Turing", "B) Charles Babbage", "C) Ada Lovelace", "D) Grace Hopper"], "togri": 3},
    {"savol": "What does CPU stand for?", "javoblar": ["A) Central Process Unit", "B) Computer Personal Unit", "C) Central Processor Unit", "D) Central Processing Unit"], "togri": 4},
    {"savol": "In what year was the World Wide Web invented?", "javoblar": ["A) 1989", "B) 1991", "C) 1985", "D) 1995"], "togri": 1},
    {"savol": "Which company developed the Java programming language?", "javoblar": ["A) Microsoft", "B) Apple", "C) Sun Microsystems", "D) IBM"], "togri": 3},
    {"savol": "What is the foundational concept behind Bitcoin's security?", "javoblar": ["A) Quantum Computing", "B) Blockchain", "C) Cloud Storage", "D) Neural Networks"], "togri": 2},
    {"savol": "Who cracked the Enigma code during WWII?", "javoblar": ["A) John von Neumann", "B) Alan Turing", "C) Richard Feynman", "D) Claude Shannon"], "togri": 2},
    {"savol": "What was the first commercially successful personal computer?", "javoblar": ["A) IBM PC", "B) Apple II", "C) Commodore PET", "D) Altair 8800"], "togri": 4},
    {"savol": "Which protocol is used to transfer web pages across the internet?", "javoblar": ["A) FTP", "B) SMTP", "C) HTTP", "D) TCP"], "togri": 3},
    {"savol": "What does HTML stand for?", "javoblar": ["A) Hyper Text Markup Language", "B) High Tech Modern Language", "C) Hyperlinks Text Mark Language", "D) Hyper Tool Multi Language"], "togri": 1},
    {"savol": "Who founded the Linux operating system kernel?", "javoblar": ["A) Steve Jobs", "B) Bill Gates", "C) Linus Torvalds", "D) Ken Thompson"], "togri": 3},
    {"savol": "What is the only even prime number?", "javoblar": ["A) 0", "B) 1", "C) 2", "D) 4"], "togri": 3},
    {"savol": "Who proved Fermat's Last Theorem in 1994?", "javoblar": ["A) Andrew Wiles", "B) Grigori Perelman", "C) Terence Tao", "D) Srinivasa Ramanujan"], "togri": 1},
    {"savol": "What is the value of Pi to 4 decimal places?", "javoblar": ["A) 3.1415", "B) 3.1416", "C) 3.1425", "D) 3.1412"], "togri": 2}, 
    {"savol": "Which constant is the base of the natural logarithm?", "javoblar": ["A) Pi", "B) Golden Ratio", "C) Euler's Number (e)", "D) Planck's Constant"], "togri": 3},
    {"savol": "What defines a sequence where each number is the sum of the two preceding ones?", "javoblar": ["A) Prime Sequence", "B) Arithmetic Progression", "C) Fibonacci Sequence", "D) Geometric Progression"], "togri": 3},
    {"savol": "Who formulated the incompleteness theorems?", "javoblar": ["A) David Hilbert", "B) Kurt Gödel", "C) Bertrand Russell", "D) Alan Turing"], "togri": 2},
    {"savol": "What is the highest possible hand in standard poker?", "javoblar": ["A) Four of a Kind", "B) Straight Flush", "C) Royal Flush", "D) Full House"], "togri": 3},
    {"savol": "In geometry, how many degrees are in a nonagon?", "javoblar": ["A) 1080", "B) 1260", "C) 1440", "D) 900"], "togri": 2},
    {"savol": "What mathematical symbol was introduced by Robert Recorde in 1557?", "javoblar": ["A) Plus (+)", "B) Minus (-)", "C) Equals (=)", "D) Infinity (∞)"], "togri": 3},
    {"savol": "What is the study of properties preserved under continuous deformation?", "javoblar": ["A) Calculus", "B) Algebra", "C) Topology", "D) Geometry"], "togri": 3},
    {"savol": "What is the study of flags called?", "javoblar": ["A) Philately", "B) Numismatics", "C) Vexillology", "D) Cartography"], "togri": 3},
    {"savol": "Which country is the only one in the world to not have a rectangular flag?", "javoblar": ["A) Switzerland", "B) Vatican City", "C) Nepal", "D) Bhutan"], "togri": 3},
    {"savol": "What is the hardest natural substance on Earth?", "javoblar": ["A) Graphene", "B) Diamond", "C) Lonsdaleite", "D) Corundum"], "togri": 2},
    {"savol": "What is the term for a word that is spelled the same forwards and backwards?", "javoblar": ["A) Anagram", "B) Palindrome", "C) Acronym", "D) Synonym"], "togri": 2},
    {"savol": "Which chemical element has the atomic number 1?", "javoblar": ["A) Helium", "B) Oxygen", "C) Hydrogen", "D) Carbon"], "togri": 3},
    {"savol": "What is the national animal of Scotland?", "javoblar": ["A) Lion", "B) Eagle", "C) Unicorn", "D) Dragon"], "togri": 3},
    {"savol": "Which blood type is the universal donor?", "javoblar": ["A) A positive", "B) AB negative", "C) O positive", "D) O negative"], "togri": 4},
    {"savol": "What is the fear of long words called?", "javoblar": ["A) Arachnophobia", "B) Hippopotomonstrosesquippedaliophobia", "C) Agoraphobia", "D) Claustrophobia"], "togri": 2},
    {"savol": "Who holds the record for the most Olympic gold medals?", "javoblar": ["A) Usain Bolt", "B) Mark Spitz", "C) Michael Phelps", "D) Carl Lewis"], "togri": 3},
    {"savol": "What is the rarest blood type in the world?", "javoblar": ["A) AB negative", "B) O negative", "C) Rh-null", "D) B negative"], "togri": 3}
]

tanlangan_savollar = []
joriy_savol = 0

def oyni_boshlash():
    global tanlangan_savollar, joriy_savol
    
    if len(barcha_savollar) >= 15:
        tanlangan_savollar = random.sample(barcha_savollar, 15)
    else:
        tanlangan_savollar = random.sample(barcha_savollar, len(barcha_savollar))
        
    joriy_savol = 0
    
    qayta_boshlash_tugmasi.pack_forget()
    tugmalar_paneli.pack(side="bottom", pady=20, fill="both", padx=20)
    
    savolni_yuklash()

def savolni_yuklash():
    ma_lumot = tanlangan_savollar[joriy_savol]
    
    savol_matni.config(text=ma_lumot["savol"], fg="white")
    tugma_1.config(text=ma_lumot["javoblar"][0], bg="white", state="normal")
    tugma_2.config(text=ma_lumot["javoblar"][1], bg="white", state="normal")
    tugma_3.config(text=ma_lumot["javoblar"][2], bg="white", state="normal")
    tugma_4.config(text=ma_lumot["javoblar"][3], bg="white", state="normal")

def javobni_tekshirish(javob_raqami):
    togri_javob = tanlangan_savollar[joriy_savol]["togri"]
    
    tugmalar = {1: tugma_1, 2: tugma_2, 3: tugma_3, 4: tugma_4}
    
  
    for t in tugmalar.values():
        t.config(state="disabled")
        
    if javob_raqami == togri_javob:
        tugmalar[javob_raqami].config(bg="green")
      
        oyna.after(1500, keyingi_qadam)
    else:
        tugmalar[javob_raqami].config(bg="red")
        tugmalar[togri_javob].config(bg="blue")
     
        oyna.after(1500, yutqazish_holati)

def keyingi_qadam():
    global joriy_savol
    joriy_savol += 1
    
    if joriy_savol < len(tanlangan_savollar):
        savolni_yuklash()
    else:
     
        tugmalar_paneli.pack_forget()
        savol_matni.config(text="Finally , YOU ARE SMARTER THAN 90% OF PEOPLE", fg="blue")
        qayta_boshlash_tugmasi.pack(pady=20)

def yutqazish_holati():
 
    tugmalar_paneli.pack_forget()
    savol_matni.config(text="Failed!", fg="red")
    qayta_boshlash_tugmasi.pack(pady=20)


oyna = tk.Tk()
from PIL import Image, ImageTk
import pygame
oyna.title("Savol-Javob")
oyna.geometry("700x450")
asl_rasm = Image.open("fon.jpg")
fon_label = tk.Label(oyna)
fon_label.place(x=0, y=0, relwidth=1, relheight=1)

def fonni_moslashtirish(event):
    if event.widget == oyna:
        yangi_eni = event.width
        yangi_boyi = event.height
        if yangi_eni > 0 and yangi_boyi > 0:
            moslangan_rasm = asl_rasm.resize((yangi_eni, yangi_boyi))
            yangi_fon = ImageTk.PhotoImage(moslangan_rasm)
            fon_label.config(image=yangi_fon)
            fon_label.image = yangi_fon

oyna.bind("<Configure>", fonni_moslashtirish)
savol_matni = tk.Label(
    oyna,
    text="",
    font=("Arial", 16, "bold"),
    bg="black",
    fg="white",
    wraplength=600,
    anchor="center",
)
savol_matni.pack(pady=(150,20), fill="both", expand=True)

qayta_boshlash_tugmasi = tk.Button(
    oyna, 
    text="RETRY", 
    font=("Arial", 14, "bold"), 
    bg="#3498db", 
    fg="white", 
    command=oyni_boshlash
)

tugmalar_paneli = tk.Frame(oyna, bg="black")
import pygame


pygame.mixer.init()


pygame.mixer.music.load("musiqa.mp3")


pygame.mixer.music.play(-1)


pygame.mixer.music.set_volume(0.5)

tugmalar_paneli.grid_columnconfigure(0, weight=1)
tugmalar_paneli.grid_columnconfigure(1, weight=1)
tugmalar_paneli.grid_rowconfigure(0, weight=1)
tugmalar_paneli.grid_rowconfigure(1, weight=1)

tugma_1 = tk.Button(tugmalar_paneli, font=("Arial", 12), wraplength=250, command=lambda: javobni_tekshirish(1))
tugma_2 = tk.Button(tugmalar_paneli, font=("Arial", 12), wraplength=250, command=lambda: javobni_tekshirish(2))
tugma_3 = tk.Button(tugmalar_paneli, font=("Arial", 12), wraplength=250, command=lambda: javobni_tekshirish(3))
tugma_4 = tk.Button(tugmalar_paneli, font=("Arial", 12), wraplength=250, command=lambda: javobni_tekshirish(4))

tugma_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tugma_2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
tugma_3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
tugma_4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

oyni_boshlash()

oyna.mainloop()

