'''Prof. Luiz Henrique
Aula de match em outras linguagens conhecida como switch case não é muito utilizada
pois o if-ifelse-else são comando limpos e simples de se utilizar, noentanto segue
mais uma estratégica lógica, é ideal para questões de múltiplas escolhas e menu também.
segue o material retirado da dcumentação pyorg.
passDeclarações
A passdeclaração não faz nada. Pode ser usado quando uma instrução é necessária sintaticamente,
mas o programa não requer nenhuma ação. Por exemplo:


while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

Isso é comumente usado para criar classes mínimas:


class MyEmptyClass:
    pass

Outro lugar passque pode ser usado é como um espaço reservado para uma função ou corpo condicional quando você
está trabalhando em um novo código, permitindo que você continue pensando em um nível mais abstrato. O passé
silenciosamente ignorado:


def initlog(*args):
    pass   # Remember to implement this!

4.6. matchDeclarações
Uma matchinstrução pega uma expressão e compara seu valor a padrões sucessivos fornecidos como um ou mais blocos de
caso. Isso é superficialmente semelhante a uma instrução switch em C, Java ou JavaScript (e em muitas outras
linguagens), mas é mais semelhante à correspondência de padrões em linguagens como Rust ou Haskell. Somente o
primeiro padrão correspondente é executado e também pode extrair componentes (elementos de sequência ou atributos
de objeto) do valor em variáveis.

A forma mais simples compara um valor de assunto com um ou mais literais:

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
Observe o último bloco: o “nome da variável” _atua como um curinga e nunca deixa de corresponder.
Se nenhum caso corresponder, nenhuma das ramificações será executada.

Você pode combinar vários literais em um único padrão usando |(“ou”):

case 401 | 403 | 404:
    return "Not allowed"
Os padrões podem parecer atribuições de desempacotamento e podem ser usados ​​para vincular
variáveis:

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
Estude esse cuidadosamente! O primeiro padrão tem dois literais e pode ser pensado como uma extensão do padrão
literal mostrado acima. Mas os próximos dois padrões combinam um literal e uma variável, e a variável vincula um
valor do sujeito ( point). O quarto padrão captura dois valores, o que o torna conceitualmente semelhante à
atribuição de descompactação .(x, y) = point

Se você estiver usando classes para estruturar seus dados, poderá usar o nome da classe seguido por uma
lista de argumentos semelhante a um construtor, mas com a capacidade de capturar atributos em variáveis:

class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
Você pode usar parâmetros posicionais com algumas classes internas que fornecem uma ordem para seus atributos
(por exemplo, dataclasses). Você também pode definir uma posição específica para atributos em padrões
configurando o __match_args__atributo especial em suas classes. Se for definido como (“x”, “y”), os seguintes
padrões são todos equivalentes (e todos vinculam o yatributo à varvariável):

Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
Uma maneira recomendada de ler padrões é vê-los como uma forma estendida do que você colocaria à esquerda de
uma atribuição, para entender quais variáveis ​​seriam definidas para quê. Somente os nomes autônomos
(como varacima) são atribuídos por uma instrução de correspondência. Nomes pontilhados (como foo.bar), nomes
de atributo (o x=e y=acima) ou nomes de classe (reconhecidos pelo “(…)” ao lado deles, como Pointacima) nunca
são atribuídos.

Os padrões podem ser aninhados arbitrariamente. Por exemplo, se tivermos uma pequena lista de pontos, podemos
combiná-la assim:

match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
Podemos adicionar uma ifcláusula a um padrão, conhecido como “guarda”. Se a guarda for falsa, matchsegue para
tentar o próximo bloco de caso. Observe que a captura de valor ocorre antes que a guarda seja avaliada:

match point:
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case Point(x, y):
        print(f"Not on the diagonal")
Vários outros recursos importantes desta declaração:

Assim como as atribuições de descompactação, os padrões de tupla e lista têm exatamente o mesmo significado e,
na verdade, correspondem a sequências arbitrárias. Uma exceção importante é que eles não correspondem a
iteradores ou strings.

Os padrões de sequência suportam a descompactação estendida: e funcionam de maneira semelhante às atribuições
de desempacotamento. O nome depois também pode ser , portanto, corresponde a uma sequência de pelo menos dois
itens sem vincular os itens restantes.[x, y, *rest](x, y, *rest)*_(x, y, *_)

Padrões de mapeamento: captura os valores e de um dicionário. Ao contrário dos padrões de sequência, as chaves
extras são ignoradas. Um tipo de descompactação também é suportado. (Mas seria redundante, por isso não é
permitido.){"bandwidth": b, "latency": l}"bandwidth""latency"**rest**_

Os subpadrões podem ser capturados usando a aspalavra-chave:

case (Point(x1, y1), Point(x2, y2) as p2): ...
irá capturar o segundo elemento da entrada como p2(contanto que a entrada seja uma sequência de dois pontos)

A maioria dos literais é comparada por igualdade, porém os singletons Truesão Falsecomparados Nonepor identidade.

Os padrões podem usar constantes nomeadas. Estes devem ser nomes pontilhados para evitar que sejam interpretados
como variável de captura:

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
Para uma explicação mais detalhada e exemplos adicionais, você pode consultar PEP 636 que é escrito em
formato de tutorial.
'''
color =str(input("Enter your choice of 'red', 'blue' or 'green': ")).upper().strip()

match color:
    case 'RED':
        print("I see red!")
    case 'GREEN':
        print("Grass is green")
    case 'BLUE':
        print("I'm feeling the blues :)")
    case _: #_ o underline no caso é um default é um padrão
        print("Digite uma opão válida")