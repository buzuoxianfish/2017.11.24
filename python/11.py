import turtle
#设置函数，这是一个有四个参数的函数
def drawSnake(rad,angle,len,neckrad):
    #写一个计数循环
    for i in range(len):
        #调用turtle库里的circle方法，circle方法有两个参数，圆半径，弧度
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
        turtle.pencolor("red")
    turtle.circle(rad,angle/2)
    #表示小龟向前直线爬行，参数表示距离
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    #设置窗口大小及起始位置
    turtle.setup(1300,800,0,0)
    #设置一个变量存入30值
    pythonsize =30
    #设置线条的粗细，乌龟大小
    turtle.pensize(pythonsize)
    #设置乌龟颜色
    turtle.pencolor("blue")
    #设置乌龟运动方向轨迹
    turtle.seth(-40)
    #调用函数
    drawSnake(40,80,5,pythonsize/2)


main()    
