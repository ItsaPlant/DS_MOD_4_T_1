input = '''Na początku było Słowo.
Było ono u Boga i było Bogiem.
2 Od samego początku było razem z Bogiem.
3 Ono powołało wszystko do istnienia.
I nic, co zostało stworzone, nie zaistniało bez Niego.
4 W Nim było życie, a życie jest dla ludzi światłem.
5 To Światło świeci w ciemnościach,
a mrok nie był w stanie Go pochłonąć.
6 Bóg posłał swojego człowieka, imieniem Jan,
7 aby powiedział ludziom o prawdziwym Świetle
i aby dzięki niemu wszyscy uwierzyli.
8 Sam Jan nie był Światłem,
lecz miał o Nim opowiedzieć.
9 I nadeszło prawdziwe Światło,
które oświeca każdego człowieka,
przychodzącego na świat.
10 Pojawiło się na świecie,
który dzięki Niemu powstał,
ale świat Go nie rozpoznał.
11 Przyszło do swojej własności,
ale swoi Go nie przyjęli.
12 Tym jednak, którzy Je przyjęli, i uwierzyli Mu
dało prawo stać się dziećmi Bożymi,
13 które narodziły się nie fizycznie
—w wyniku namiętności
czy ludzkich planów—ale z Boga.
14 Słowo stało się ciałem i jako człowiek
zamieszkało wśród nas.
Ujrzeliśmy więc Jego chwałę—chwałę,
jaką Ojciec obdarzył swojego jedynego Syna,
pełnego łaski i prawdy. Kajak'''

def is_palin(word):
    """
    Checks if word is a palindrom. Case sensitive.
    input: string (a word to be checked)
    output: bool (True if palindrom)
    """
    return word == word[::-1]

for word in input.upper().split():
    check = is_palin(word)
    print(word + ':', check)
