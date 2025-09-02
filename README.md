# computer-project
computer project of helli1 dore2
حتماً! مار بازی (Snake Game) یکی از بازی‌های کلاسیکیه که می‌تونه با پایتون و کتابخونه‌ی `turtle` پیاده‌سازی بشه. اینم یه نمونه کد ساده و قابل فهم با توضیحات خط به خط برای شروع:

---

### 🐍 کد ساده مار بازی با `turtle` در Python

```python
import turtle
import time
import random

# تنظیمات اولیه صفحه
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # صفحه رو دستی آپدیت می‌کنیم

# ساختن مار
snake = []
for i in range(3):  # شروع با ۳ بخش
    part = turtle.Turtle()
    part.shape("square")
    part.color("green")
    part.penup()
    part.goto(x=-20*i, y=0)
    snake.append(part)

# ساختن غذا
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# حرکت مار
direction = "right"

def go_up():
    global direction
    if direction != "down":
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

# کنترل‌ها با کیبورد
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# حلقه اصلی بازی
while True:
    win.update()
    time.sleep(0.1)

    # حرکت بخش‌های مار
    for i in range(len(snake)-1, 0, -1):
        x = snake[i-1].xcor()
        y = snake[i-1].ycor()
        snake[i].goto(x, y)

    if direction == "up":
        snake[0].sety(snake[0].ycor() + 20)
    elif direction == "down":
        snake[0].sety(snake[0].ycor() - 20)
    elif direction == "left":
        snake[0].setx(snake[0].xcor() - 20)
    elif direction == "right":
        snake[0].setx(snake[0].xcor() + 20)

    # برخورد با غذا
    if snake[0].distance(food) < 20:
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        new_part = turtle.Turtle()
        new_part.shape("square")
        new_part.color("green")
        new_part.penup()
        snake.append(new_part)

    # برخورد با دیوارها
    if abs(snake[0].xcor()) > 290 or abs(snake[0].ycor()) > 290:
        time.sleep(1)
        win.clear()
        win.bgcolor("black")
        win.title("Game Over")
        break
```

---

### 🧠 توضیحات:
- از `turtle` برای رسم اشکال و کنترل مار استفاده شده.
- مار با لیست بخش‌ها ساخته شده که از پشت به جلو حرکت می‌کنن.
- غذا یه نقطه قرمزه که با برخورد، مار بزرگتر می‌شه.
- از کلیدهای جهت‌دار برای تغییر جهت حرکت استفاده می‌شه.
- اگر مار به دیواره برخورد کنه، بازی پایان می‌یابه.

اگه دوست داشته باشی، می‌تونیم امتیاز‌دهی، برخورد با خودش یا افکت‌های گرافیکی هم اضافه کنیم تا بازی حرفه‌ای‌تر بشه. بگی کجاش برات گنگه، برات بازش می‌کنم! 😄
