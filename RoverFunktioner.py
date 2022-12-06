import RPi.GPIO as G
import time as T

delay=0

def frem():
    v1.ChangeDutyCycle(0)
    v2.ChangeDutyCycle(100)
    v3.ChangeDutyCycle(0)
    v4.ChangeDutyCycle(100)
    T.sleep(delay)

def bag():
    v1.ChangeDutyCycle(100)
    v2.ChangeDutyCycle(0)
    v3.ChangeDutyCycle(100)
    v4.ChangeDutyCycle(0)
    T.sleep(delay)

def venstre():
    v1.ChangeDutyCycle(0)
    v2.ChangeDutyCycle(25)
    v3.ChangeDutyCycle(0)
    v4.ChangeDutyCycle(100)
    T.sleep(delay)

def højre():
    v1.ChangeDutyCycle(0)
    v2.ChangeDutyCycle(100)
    v3.ChangeDutyCycle(0)
    v4.ChangeDutyCycle(25)
    T.sleep(delay)


def fremV():
    v1.ChangeDutyCycle(0)
    v2.ChangeDutyCycle(50)
    v3.ChangeDutyCycle(0)
    v4.ChangeDutyCycle(100)
    T.sleep(delay)

def fremH():
    v1.ChangeDutyCycle(0)
    v2.ChangeDutyCycle(100)
    v3.ChangeDutyCycle(0)
    v4.ChangeDutyCycle(50)
    T.sleep(delay)


def bagV():
    v1.ChangeDutyCycle(25)
    v2.ChangeDutyCycle(0)
    v3.ChangeDutyCycle(100)
    v4.ChangeDutyCycle(0)
    T.sleep(delay)

def bagH():
    v1.ChangeDutyCycle(100)
    v2.ChangeDutyCycle(0)
    v3.ChangeDutyCycle(25)
    v4.ChangeDutyCycle(0)
    T.sleep(delay)
