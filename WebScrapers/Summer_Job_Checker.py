# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import turtle
import time

wn = turtle.Screen()
wn.title("Do you have a job?")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 0)


# To check if there is a job
def SummerOfTech_Jobs():
    link = "https://app.summeroftech.co.nz/jobs?q=&organisation_interested=1&order=default&job_types%5B4%5D=1" \
           "&job_types%5B3%5D=1&job_types%5B12%5D=1&regions%5B1%5D=1 "
    f = requests.get(link)
    if f.text.find("No jobs match your search criteria"):
        pen.write("Nope no jobs for you today", align="center", font=("Courier", 24, "normal"))
    else:
        pen.write("Today is your lucky day, there is a job for you", align="center", font=("Courier", 24, "normal"))


# Running the python method
if __name__ == '__main__':
    SummerOfTech_Jobs()

# While True method
while True:
    wn.update()
