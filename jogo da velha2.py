from turtle import Turtle,onscreenclick, onkey, listen, Screen
lu = Turtle ()
tela = Screen()
lu.speed(0)
resultado = 0
numero = 0
x=0
y=0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2

    tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]
jogo_ativo = True


lu.pensize(5)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.left(180)
lu.forward(100)
lu.forward(100)
lu.backward(100)
lu.left(90)
lu.forward(100)
lu.left(180)
lu.forward(200)
lu.left(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.right(90)
lu.forward(200)
lu.backward(300)
lu.forward(100)
lu.left(90)
lu.forward(100)
lu.backward(100)
lu.right(90)
lu.forward(100)
lu.left(90)
lu.forward(100)

def reiniciar_jogo():
    global tabuleiro
    global jogo_ativo
    tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]
    jogo_ativo = True
    lu.clear()

    
    # Verificar linhas e colunas
    for   i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] is not None:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] is not None:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] is not None:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] is not None:
        return True

    return False


def empate():
    for linha in tabuleiro:
        for elemento in linha:
            if elemento is None:
                return False
    return True

def jogar(x, y):
    global jogo_ativo

def jogar(x, y): 
    lu.penup()
    lu.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    if resultado == 0:
        x2()
    if resultado == 1:
        trocar()
  

def jogar(x,y):
    lu.penup()
    lu.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    corx = lu.xcor()
    cory = lu.ycor()


    if resultado == 0:
        if -170 < corx < 170:
            if -170 < cory < 170:
                x2()
    if resultado == 1:
        if -170 < corx < 170:
            if -170 < cory < 170:
                circulo()
            
                print(f'Jogador {resultado + 0} venceu!')
                jogo_ativo = False
            elif empate():
                print('Empate!')
                jogo_ativo = ()


 
    trocar()
def circulo():
    lu.pensize(10)
    lu.color('blue')
    lu.right(90)
    lu.forward(40)
    lu.left(90)
    r = 40

    lu.pendown()
    lu.circle(r)

def x2():
    lu.pensize(20)
    lu.color('red')
    lu.pendown()
    lu.right(45)
    for _ in range(4):
        lu.forward(50)
        lu.forward(-50)
        lu.right(90)
    lu.left(45)

tela.onscreenclick(jogar)
listen()
tela.mainloop()