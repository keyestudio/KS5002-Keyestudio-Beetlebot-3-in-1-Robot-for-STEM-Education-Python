# **Python Tutorials**


## Description：

The Beetlebot smart robot, compatible with LEGO building blocks, is a STEM educational product which can automatically dodge obstacles, follow black lines and light to move. Besides, it has three cool forms such as the soccer robot, the siege robot, the handling robot. As for beginners, they can create whatever
they want by LEGO building blocks.

Various improvements have been made on the Beetlebot car in comparison with other smart cars. It integrates a motor driver and a large number of sensors
and is easy to assemble.

Going forward, not only can it impart Micropython programming knowledge
and AI application to children and the youth, but also it can cultivate
their creativity, hands-on ability, problem-solving capability,
interpersonal communication as well as teamwork ability. With this kit,
you have a chance to experience soccer games using your own robots.

## Features：

  - Compatible with LEGO building blocks: generate diverse forms with
    LEGO blocks and sensors

  - Three forms: a soccer robot, a siege engine, a handling robot

  - Various functions: Pictures display, atmosphere light control, line
    tracking, obstacle avoidance, light following , IR control and WIFI
    control.

  - Easy to build: embedded design on car body; wire up the car body
    with a few steps

  - High compatibility: reserve ports for the Raspberry Pico board and
    the Arduino Nano board

  - Charging function: integrate a circuit for 18650 batteries, low-cost
    and effective

  - WiFi Control: adopt WiFi control, can finish tailor-made software
    development

  - App: compatible with Android and iOS systems, with aesthetic page
    and flexible control system


## 5\. How to install the Beetlebot car：

![](media/7daabc13c0fbac0ff936a5d26f300f3e.png)

## 6\. PCB Board：

![](media/7a101d142fecfe0d47e12a3897dd632d.png)

![](media/f30dfbb6347df2336aae511ecac5be31.png)

**Turn the DIP switch to the OFF end before installing or removing
batteries**

# **Projects：**

## Project 1: 6812 RGB

1.  **Description：**

There are 4 RGB LEDs can be widely used in the decoration of buildings,
bridges, roads, gardens, courtyards and so on by colors adjustment.

In this experiment, we will demonstrate different lighting effects with
them.

**2. Knowledge：**

**Working Principle**

From the schematic diagram, we can see that these four pixel lighting
beads are all connected in series. In fact, no matter how many they are,
we can use a pin to control a light and let it display any color. The
pixel point contains a data latch signal shaping amplifier drive
circuit, a high-precision internal oscillator and a 12V high-voltage
programmable constant current control part, which effectively ensures
the color of the pixel point light is highly consistent.

The data protocol adopts a single-wire zero-code communication method.
After the pixel is powered up and reset, the S terminal receives the
data transmitted from the controller. The first 24bit data sent is
extracted by the first pixel and sent to the data latch of the pixel.

![](media/86e292d0666046b72a1e0e68adfb17e8.png)

**3. Test Code：**

The SK6812RGB on the PCB board is controlled by the GPIO 14 of the ESP32
board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Run the test code：

Open“Thonny”and click“This computer”→“D:”→“Micropython\_Codes”

![](media/4674d56611de90ca71fd53d0987bbaba.png)

Click Project\_01\_6812\_RGB and double-click Project\_01\_6812\_RGB.py
as shown below:

![](media/980a34a4e95619d4f5175a7e93d96732.png)

<table>
<tbody>
<tr class="odd">
<td><p>#Import Pin, neopiexl and time modules.</p>
<p>from machine import Pin</p>
<p>import neopixel</p>
<p>import time</p>
<p>#Define the number of pin and LEDs connected to neopixel.</p>
<p>pin = Pin(14, Pin.OUT)</p>
<p>np = neopixel.NeoPixel(pin, 4)</p>
<p>#brightness :0-255</p>
<p>brightness=100</p>
<p>colors=[[brightness,0,0], #red</p>
<p>[0,brightness,0], #green</p>
<p>[0,0,brightness], #blue</p>
<p>[brightness,brightness,brightness], #white</p>
<p>[0,0,0]] #close</p>
<p>#Nest two for loops to make the module repeatedly display five states of red, green, blue, white and OFF.</p>
<p>while True:</p>
<p>for i in range(0,5):</p>
<p>for j in range(0,4):</p>
<p>np[j]=colors[i]</p>
<p>np.write()</p>
<p>time.sleep_ms(50)</p>
<p>time.sleep_ms(500)</p>
<p>time.sleep_ms(500)</p></td>
</tr>
</tbody>
</table>

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png) or
press **Reset**

![](media/0992edb2c1f480514f37688b14e115de.png)

![](media/bd314b9a2a2a583c13cd41cc41d45559.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png)“Run current script”, the Shell monitor
will show scripts and code will be run.

4 RGB lights will show red, green, blue and white color then go off,
loop alternately.

![](media/25faf5cece280adbeb84ee505f6fed6e.png)

Note：

Unplug the ESP32 board or press Reset, 4个RGB LEDs show the same color
and Thonny shows as follows;

![](media/4c086941abd3fc2fd20d3b51e2375430.png)

Upload the test code to the ESP32 board.（offline)

Right-click Project\_01\_6812\_RGB.py, select“Upload to /”to upload the
code

![](media/7729817d2e529043e54a748cd4f83e35.png)

You can upload the boot.py in same way and click“OK”.

![](media/b648e0e25c83e73df0d50c880baed8d4.png)

Press the Reset button on the ESP32 board, then the RGB LEDs will will
show red, green, blue and white color then go off, loop alternately

![](media/0d23e6891643e73ce98dc2f93def946d.jpeg)

Note：

If you want to stop running code, just click ![](media/7dfedd65a053d0174e2cfa88d048b685.png)

![](media/1479e2552446d8810501bf0c2320cd32.png)

## Project 2: Play Music

1.  **Description：**

There is a power amplifier component on the expansion board, which is
often used to play music and serve as an external amplifying device for
music playback devices.

In this experiment, we use the speaker amplifier component to play
music.

**2. Knowledge：**

Power amplifier modules(equivalent to a passive buzzer) don’t have
internal oscillation circuits.

The power amplifier module can chime sounds with different frequency
when power it up.

**3. Test Code：**

The speaker component on the PCB board is controlled by the GPIO 2 of
the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_02\_Buzzer”

Double-click Project\_02\_Buzzer.py”as shown below:

![](media/b077f0449284fa27a12a8d49e5bcc134.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, PWM</p>
<p>import time</p>
<p>beeper = PWM(Pin(2, Pin.OUT))</p>
<p>notes = [1915, 1700, 1519, 1432, 1275, 1136, 1014, 956, 834, 765, 593, 468, 346, 224, 655, 715]</p>
<p>for note in notes:</p>
<p>if note == 0:</p>
<p>beeper.duty(0)</p>
<p>else:</p>
<p>beeper.duty(512)</p>
<p>beeper.freq(note)</p>
<p>time.sleep(0.2)</p>
<p>beeper.duty(0)</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/568acf8b4accf4842e3f3f2ba934360c.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the
speaker module on the PCB will emit sounds; press“Ctrl+C”or click
![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/ac688b44314f16001f3e2b9d0be8d895.png)

## Project 3: 8\*8 Dot Matrix Display

1.  **Description：**
    
    Composed of LED emitting tube diodes, the 8\*8 LED dot matrix are
    applied widely to public information display like advertisement
    screen and bulletin board, by controlling LED to show words,
    pictures and videos, etc.
    
    **2. Knowledge：**

There are different types of matrices, including 4×4, 8×8 and 16×16 and
etc. It contains 64 LEDs.

The inner structure of 8×8 dot matrix is shown below.

![](media/df08c3a7c84497e429ce6fde7253d9b3.jpeg)

Every LED is installed on the cross point of row line and column line.
When the voltage on a row line increases, and the voltage on the column
line reduces, the LED on the cross point will light up. 8×8 dot matrix
has 16 pins. Put the silk-screened side down and the numbers are 1, 8, 9
and 16 in anticlockwise order as marked below.

![](media/6576aff8e8a7fb35335629c2f60de29b.jpeg)

The definition inner pins are shown below:

![](media/4b98c449bae6648d7719a58d9ab2efa7.jpeg)

For instance, to light up the LED on row 1 and column 1, you should
increase the voltage of pin 9 and reduce the voltage of pin 13.

**HT16K33 8X8 Dot Matrix**

The HT16K33 is a memory mapping and multi-purpose LED controller driver.
The max. Display segment numbers in the device is 128 patterns (16
segments and 8 commons) with a 13\*3 (MAX.) matrix key scan circuit. The
software configuration features of the HT16K33 makes it suitable for
multiple LED applications including LED modules and display subsystems.
The HT16K33 is compatible with most microcontrollers and communicates
via a two-line bidirectional I2C-bus.

The picture below is the working schematic of HT16K33 chip

![](media/fa5b7bd0d5ce98dbd4cb392dfb0b95e7.png)

We design the drive module of 8\*8 dot matrix based on the above
principle. We could control the dot matrix by I2C communication and two
pins of microcontroller, according to the above diagram.

**3. Specification:**

  - Input voltage: 5V    

  - Rated input frequency: 400KHZ 

  - Input power: 2.5W  

  - Input current: 500mA  
    
    **4. Introduction for Modulus Tool**

The online version of dot matrix modulus tool:

[http://dotmatrixtool.com/\#](http://dotmatrixtool.com/)

①Open the link to enter the following page.

![](media/354693b5679a2615c62e99b7025d6355.png)

②The dot matrix is 8\*8 in this project. So set the height to 8, width
to 8; as shown below.

![](media/501ba516e4be9c8ec4ca6f37e2b6915f.png)

**③**Click **Byte Order** to select **Row Major**

Click **Endian** to select **Big Endian**(MSB)

![](media/4da6da68aeb2cb71e95fe6ece173a5d5.png)

![](media/1215ba2c27a8c08e4a4bef90b2c53f7d.png)

③ Generate hexadecimal data from the pattern

As shown below, the left button of the mouse is for selection while the
right is for canceling. Thus you could use them to draw the pattern you
want, then click **Generate**, to yield the hexadecimal data needed.

![](media/32e674da893cc93cd1330a9da73269cb.png)

The generated hexadecimal code（0x00, 0x66, 0x00, 0x00, 0x18, 0x42, 0x3c,
0x00) is what will be displayed, so you need to save it for next
procedure.

**2. Wiring up：**

<table>
<tbody>
<tr class="odd">
<td>8*8 Dot matrix display</td>
<td>PCB Board</td>
</tr>
<tr class="even">
<td>G</td>
<td>G</td>
</tr>
<tr class="odd">
<td>5V</td>
<td>5V</td>
</tr>
<tr class="even">
<td>SDA</td>
<td>SDA</td>
</tr>
<tr class="odd">
<td>SCL</td>
<td>SCL</td>
</tr>
</tbody>
</table>

**3. Test Code：**

The 8\*8 dot matrix is controlled by GPIO21（SDA）and GPIO22（SCL）of the
ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_03\_8×8\_Dot\_Matrix\_Display”;
select“ht16k33.py” and“ht16k33matrix.py”and right-click“Upload to /”;
wait“ht16k33.py”and“ht16k33matrix.py”uploaded to the ESP32 board. Then
double-click

Click Project\_01\_6812\_RGB and double-click Project\_01\_6812\_RGB.py
as shown below:“Project\_03\_8×8\_Dot\_Matrix\_Display.py”

![](media/ebc71638ebd8d8316caa9e40386f8b4c.png)

![](media/64eddefa2d2c265f9fe99adc32cc6ae9.png)

![](media/d8cfe053b714d8f3d209b9e9a34f9cd9.png)

<table>
<tbody>
<tr class="odd">
<td><p># IMPORTS</p>
<p>import utime as time</p>
<p>from machine import I2C, Pin, RTC</p>
<p>from ht16k33matrix import HT16K33Matrix</p>
<p># CONSTANTS</p>
<p>DELAY = 0.01</p>
<p>PAUSE = 3</p>
<p># START</p>
<p>if __name__ == '__main__':</p>
<p>i2c = I2C(scl=Pin(22), sda=Pin(21))</p>
<p>display = HT16K33Matrix(i2c)</p>
<p>display.set_brightness(2)</p>
<p># Draw a custom icon on the LED</p>
<p>icon = b"\x00\x66\x00\x00\x18\x42\x3c\x00"</p>
<p>display.set_icon(icon).draw()</p>
<p># Rotate the icon</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p></td>
</tr>
</tbody>
</table>

Note: the code ![](media/b0cf48986eb2530a91a69ce69b1eb01a.png) changes into the code.

![](media/a9aee1521e3e842183824bb13d1f0036.png)

**Test Result**

Connect the ESP32 board to your PC and clock ![](media/6827818058b5d94c3e94e7a3f487afa5.png)or
press **Reset**

![](media/fa03a86a0c04c597411743c12f23c54c.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the 8\*8
module will show a smile pattern. Press“Ctrl+C”or click
![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/2fadc050b62aec8f9fc29f9fd60f5cba.png)

## Project 4: Servo Rotation

1.  **Description：**

There are two servos on the car. We take the servo connected to pin D9
as an example.

The servo is a motor that can rotate very accurately. It has been widely
applied to toy cars, remote control helicopters, airplanes, robots and
other fields. In this project, we will use the Nano motherboard to
control the servo to spin.

2.  **Knowledge：**

![](media/99830768916233a9c5900ac399006c17.png)

Servo motor is a position control rotary actuator. It mainly consists of
a housing, a circuit board, a core-less motor, a gear and a position
sensor. Its working principle is that the servo receives the signal sent
by MCU or receiver and produces a reference signal with a period of 20ms
and width of 1.5ms, then compares the acquired DC bias voltage to the
voltage of the potentiometer and obtain the voltage difference output.

When the motor speed is constant, the potentiometer is driven to rotate
through the cascade reduction gear, which leads that the voltage
difference is 0, and the motor stops rotating. Generally, the angle
range of servo rotation is 0° --180 °

The rotation angle of servo motor is controlled by regulating the duty
cycle of PWM (Pulse-Width Modulation) signal. The standard cycle of PWM
signal is 20ms (50Hz). Theoretically, the width is distributed
between 1ms-2ms, but in fact, it's between 0.5ms-2.5ms. The width
corresponds the rotation angle from 0° to 180°. But note that for
different brand motors, the same signal may have different rotation
angles. 

![](media/708316fde05c62113a3024e0efb0c237.jpeg)

In general, servo has three lines in brown, red and orange. The brown
wire is grounded, the red one is a positive pole line and the orange one
is a signal line.

![](media/35084ae289a08e35bdb8c89ceb134ba4.png)

3.  **Wire up：**

<table>
<tbody>
<tr class="odd">
<td>Servo</td>
<td>PCB Board</td>
</tr>
<tr class="even">
<td>Brown</td>
<td>G</td>
</tr>
<tr class="odd">
<td>Red</td>
<td>5V</td>
</tr>
<tr class="even">
<td>Orange</td>
<td>S1（GPIO4）</td>
</tr>
</tbody>
</table>

4.  **Test Code：**

The servo for controlling the ultrasonic sensor is controlled by the
GPIO4 of the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_04\_Servo\_Sweep”

Select myservo.py, right-click Upload to/ to upload myservo.py to the
ESP32;

Double-click“Project\_04\_Servo\_Sweep.py”as shown below:

![](media/79cb775e90cba153720c98c69080fc12.png)

![](media/897ce6c2f7666d31613260cf0a38ceb2.png)

<table>
<tbody>
<tr class="odd">
<td><p>from myservo import myServo #Import myservo module.</p>
<p>import time</p>
<p>#Initialize pins of the servo and set the starting point of the servo to 0 degree.</p>
<p>servo=myServo(4)</p>
<p>servo.myServoWriteAngle(0)</p>
<p>time.sleep_ms(1000)</p>
<p>try:</p>
<p>while True:</p>
<p>#Use two for loops. The first one controls the servo to rotate from 0 degree to 180 degrees</p>
<p>#while the other controls it to rotate back from 180 degrees to 0 degree.</p>
<p>for i in range(0,180,1):</p>
<p>servo.myServoWriteAngle(i) #Control the servo to rotate to a specified angle within the range of 0-180 degrees.</p>
<p>time.sleep_ms(15)</p>
<p>for i in range(180,0,-1):</p>
<p>servo.myServoWriteAngle(i)</p>
<p>time.sleep_ms(15)</p>
<p>except:</p>
<p>servo.deinit()</p></td>
</tr>
</tbody>
</table>

**Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/19a6e0becac6bb4b53bee420d1a30a80.png)

Place batteries in the battery holder, turn the power switch to ON end
and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the servo
rotate from 0° to 180°, then from 180° to 0°, loop alternately.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit.

![](media/4991039a1f318584a098e274663485b0.png)

## Project 5: Motor Driving and Speed Control 

1.  **Description：**

There are many ways to drive motors. This car uses the most commonly
used DRV8833 motor driver chip, which provides a dual-channel bridge
electric driver for toys, printers and other motor integration
applications.

In this experiment, we use the DRV8833 motor driver chip on the
expansion board to drive the two DC motors, and demonstrate the effect
of forward, backward, left-turning, and right-turning.

**2. Knowledge：**

DRV8833 motor driver chip: Dual H-bridge motor driver with current
control function, can drive two DC motors, one bipolar stepper motor,
solenoid valve or other inductive loads. Each H-bridge includes
circuitry to regulate or limit winding current.

An internal shutdown function with a fault output pin is used for
over-current and short circuit protection, under-voltage lockout and
over-temperature. A low-power sleep mode is also added. Let's take a
look at the schematic diagram of the DRV8833 motor driver chip driving
two DC motors:

![](media/bc839fa0f37fdc3003485b0398dd6d1f.png)

![](media/9cb8b7c00f814e367040f2ed4a3c9f4a.png)

If you want to get insight to it, you can check the specification of
this chip. Just browse it in the“Attachments”folder.

![](media/f7674a914ec2cbe10f1ec6446dc66c22.png)

**3. Specification：**

Input voltage of logic part: DC 5V

Input voltage of driving part : DC 5V

Working current of logic part: \<30mA

Operating current of driving part: \<2A

Maximum power dissipation: 10W (T=80℃)

Motor speed: 5V 200 rpm / min

Motor drive form: dual H-bridge drive

Control signal input level: high level 2.3V\<Vin\<5V, low level
-0.3V\<Vin\<1.5V

Working temperature: -25\~130℃

**4. Drive the car to move**

From the above diagram, the direction pin of the left motor is GPIO33;
the speed pin is GPIO26; GPIO32 is the direction pin of the right motor;
and GPIO25 is speed pin.

PWM drives the robot car. The PWM value is in the range of 0-255. The
more the PWM value is set, the faster the rotation of the motor.

<table>
<tbody>
<tr class="odd">
<td>Function</td>
<td>GPIO33</td>
<td>GPIO26（PWM)</td>
<td>Left motor</td>
<td>GPIO32</td>
<td>GPIO25（PWM)</td>
<td>Right motor</td>
</tr>
<tr class="even">
<td>forward</td>
<td>LOW</td>
<td>200</td>
<td>clockwise</td>
<td>LOW</td>
<td>200</td>
<td>clockwise</td>
</tr>
<tr class="odd">
<td>Go back</td>
<td>HIGH</td>
<td>50</td>
<td>anticlockwise</td>
<td>HIGH</td>
<td>50</td>
<td>anticlockwise</td>
</tr>
<tr class="even">
<td>Turn left</td>
<td>HIGH</td>
<td>200</td>
<td>anticlockwise</td>
<td>LOW</td>
<td>200</td>
<td>clockwise</td>
</tr>
<tr class="odd">
<td>Turn right</td>
<td>LOW</td>
<td>200</td>
<td>clockwise</td>
<td>HIGH</td>
<td>200</td>
<td>anticlockwise</td>
</tr>
<tr class="even">
<td>Stop</td>
<td>LOW</td>
<td>0</td>
<td>stop</td>
<td>LOW</td>
<td>0</td>
<td>stop</td>
</tr>
</tbody>
</table>

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_05\_Motor\_Drive\_And\_Speed\_Regulation”;

Click Project\_05\_Motor\_Drive\_And\_Speed\_Regulation.py as shown
below:

![](media/f1af9709fe4e8aef098a73ddb9a4c270.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,PWM</p>
<p>import time</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=12500)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=12500)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(1000)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(1000)</p>
<p># As a function of the car going backwards.</p>
<p>def car_back():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(250)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(250)</p>
<p># As a function of the car going left.</p>
<p>def car_left():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(1000)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(500)</p>
<p># As a function of the car going right.</p>
<p>def car_right():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(500)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(1000)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>try:</p>
<p>while True:</p>
<p>car_forward() #Car ahead</p>
<p>time.sleep(2) # delay 2s</p>
<p>car_back() # Car goes back</p>
<p>time.sleep(2)</p>
<p>car_left() # Car to the left</p>
<p>time.sleep(2)</p>
<p>car_right() # Car to the right</p>
<p>time.sleep(2)</p>
<p>car_stop() # Car stop</p>
<p>time.sleep(2)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

**6.Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/16c7f838329c508576a3ae59e77273da.png)

Place batteries, turn the power switch to ON end and power up. Click
![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, the car will move
forward for 2s, back for 2s, turn left for 2s, right for 2s and stops
for 2s, loop alternately.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/1abf8c357085069e213814914cc278ec.png)

## Project 6: Ultrasonic Sensor

There is an ultrasonic sensor on the car. It is a very affordable
distance-measuring sensor.

The ultrasonic sensor sends a high-frequency ultrasonic signal that
human hearing can’t hear. When encountering obstacles, these signals
will be reflected back immediately. After receiving the returned
information, the distance between the sensor and the obstacle will be
calculated by judging the time difference between the transmitted signal
and the received signal. It is mainly used for object avoidance and
ranging in various robotics projects.

### Project 6.1: Ultrasonic Ranging

**1.Description：**

In this experiment, we use an ultrasonic sensor to measure distance and
print the data on a serial monitor.

**2. Knowledge：**

The HC-SR04 ultrasonic sensor uses sonar to determine distance to an
object like what bats do. It offers excellent non-contact range
detection with high accuracy and stable readings in an easy-to-use
package. It comes complete with ultrasonic transmitter and receiver
modules.

The HC-SR04 or the ultrasonic sensor is being used in a wide range of
electronics projects for creating obstacle detection and distance
measuring application as well as various other applications. Here we
have brought the simple method to measure the distance with Arduino and
ultrasonic sensor and how to use ultrasonic sensor with Arduino.

![](media/e6f6037071e434febf7090b56ac35802.png)

**Use method and timing chart of ultrasonic module:**

1.  Setting the delay time of Trig pin of SR04 to 10μs at least, which
    can trigger it to detect distance.

2.  After triggering, the module will automatically send eight 40KHz
    ultrasonic pulses and detect whether there is a signal return. This
    step will be completed automatically by the module.

3.  If the signal returns, the Echo pin will output a high level, and
    the duration of the high level is the time from the transmission of
    the ultrasonic wave to the return.

![](media/4114885ac4b6214953e3224d8c1d52c4.png)

Time=Echo pulse width, unit: us

Distance（cm）=time/ 58

Distance(inch)=time/ 148

The HC-SR04 ultrasonic sensor has four pins: Vcc, Trig, Echo and GND.

The Vcc pin provides power generating ultrasonic pulses and is connected
to Vcc/+5V. The GND pin is grounded/GND.

The Trig pin is where the Arduino sends a signal to start the ultrasonic
pulse. The Echo pin is where the ultrasonic sensor sends information
about the duration of the ultrasonic pulse stroke to the Arduino control
board.

**Wiring Up**

<table>
<tbody>
<tr class="odd">
<td>Ultrasonic Sensor</td>
<td>PCB Board</td>
</tr>
<tr class="even">
<td>Vcc</td>
<td>5V</td>
</tr>
<tr class="odd">
<td>Trig</td>
<td>S2（GPIO5）</td>
</tr>
<tr class="even">
<td>Echo</td>
<td>S1（GPIO18）</td>
</tr>
<tr class="odd">
<td>Gnd</td>
<td>G</td>
</tr>
</tbody>
</table>

**3. Test Code：**

The pin Trig and Echo of the ultrasonic sensor are controlled by the
GPIO5 and GPIO18 of the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click This computer → D: →
Micropython\_Codes→“Project\_06.1\_Ultrasonic\_Ranging”

Then double-click Project\_06.1\_Ultrasonic\_Ranging.py

![](media/1796f896c2e120a8e244bde33f07f5a2.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Define the control pins of the ultrasonic ranging module.</p>
<p>trigPin=Pin(5,Pin.OUT,0)</p>
<p>echoPin=Pin(18,Pin.IN,0)</p>
<p>#Set the speed of sound.</p>
<p>soundVelocity=340</p>
<p>distance=0</p>
<p>#Subfunction getSonar() is used to start the Ultrasonic Module to begin measurements,</p>
<p>#and return the measured distance in centimeters. In this function, first let trigPin</p>
<p>#send 10us high level to start the Ultrasonic Module. Then use pulseIn() to read</p>
<p>#the Ultrasonic Module and return the duration time of high level.</p>
<p>#Finally, the measured distance according to the time is calculated.</p>
<p>def getSonar():</p>
<p>trigPin.value(1)</p>
<p>time.sleep_us(10)</p>
<p>trigPin.value(0)</p>
<p>while not echoPin.value():</p>
<p>pass</p>
<p>pingStart=time.ticks_us()</p>
<p>while echoPin.value():</p>
<p>pass</p>
<p>pingStop=time.ticks_us()</p>
<p>pingTime=time.ticks_diff(pingStop,pingStart)</p>
<p>distance=pingTime*soundVelocity//2//10000</p>
<p>return int(distance)</p>
<p>#Delay for 2 seconds and wait for the ultrasonic module to stabilize,</p>
<p>#Print data obtained from ultrasonic module every 500 milliseconds.</p>
<p>time.sleep_ms(2000)</p>
<p>while True:</p>
<p>time.sleep_ms(500)</p>
<p>print('Distance: ',getSonar(),'cm' )</p></td>
</tr>
</tbody>
</table>

**Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/c27d46b9320ec8a985a647e660a51a44.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the shell
monitor will print distance value between the ultrasonic sensor and the
object; press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit.

![](media/8d2fe34f07c0705026a176b0fc1482b1.png)

![](media/ce873cf513307a15f9aa58078c8dd7d6.png)

### Project 6.2: Light Following

**1.Description：**

In the above experiments, we have learned about the 8\*8 dot matrix,
motor drivers and speed regulation, ultrasonic sensors, servos and other
hardware. In this experiment, we will combine them to create a follow
car with the ultrasonic sensor. The can can follow an object to move
through

measuring distance.

**2. Working Principle：**

<table>
<tbody>
<tr class="odd">
<td>Detection</td>
<td>Detect the front distance</td>
<td>Distance（unit：cm）</td>
</tr>
<tr class="even">
<td>Condition 1</td>
<td>Distance＜8</td>
<td></td>
</tr>
<tr class="odd">
<td>State</td>
<td>Go back（set PWM to 100）</td>
<td></td>
</tr>
<tr class="even">
<td>Condition 2</td>
<td>8≤distance&lt;13</td>
<td></td>
</tr>
<tr class="odd">
<td>State</td>
<td>stop</td>
<td></td>
</tr>
<tr class="even">
<td>Condition 3</td>
<td>13≤distance&lt;35</td>
<td></td>
</tr>
<tr class="odd">
<td>State</td>
<td>Go forward（set PWM to 200）</td>
<td></td>
</tr>
<tr class="even">
<td>Condition 4</td>
<td>distance≥35</td>
<td></td>
</tr>
<tr class="odd">
<td>State</td>
<td>stop</td>
<td></td>
</tr>
</tbody>
</table>

**3. Flow Chart：**

![](media/e1ded45b4454e64b7ff419bad285cb3a.png)

**4. Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click “This
computer”→“D:”→→“Micropython\_Codes”→“Project\_06.2\_Follow\_Me”，

Double-click“Project\_06.2\_Follow\_Me.py”as shown below:

![](media/9ab21c4ee1d5cccb0aebb5a95e7ed380.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, PWM</p>
<p>import time</p>
<p>#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM</p>
<p>servoPin = Pin(4)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(1)</p>
<p>#Set the pin and sound speed of the ultrasonic sensor</p>
<p>trigPin=Pin(5,Pin.OUT,0)</p>
<p>echoPin=Pin(18,Pin.IN,0)</p>
<p>soundVelocity=340</p>
<p>distance=0</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=50,duty=0)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=50,duty=0)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(800)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(800)</p>
<p># As a function of the car going backwards.</p>
<p>def car_back():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(550)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(550)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin2.deinit()</p>
<p>pin4.deinit()</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>#Subfunction getSonar() is used to start the Ultrasonic Module to begin measurements,</p>
<p>#and return the measured distance in centimeters. In this function, first let trigPin</p>
<p>#send 10us high level to start the Ultrasonic Module. Then use pulseIn() to read</p>
<p>#the Ultrasonic Module and return the duration time of high level.</p>
<p>#Finally, the measured distance according to the time is calculated.</p>
<p>def getSonar():</p>
<p>trigPin.value(1)</p>
<p>time.sleep_us(10)</p>
<p>trigPin.value(0)</p>
<p>while not echoPin.value():</p>
<p>pass</p>
<p>pingStart=time.ticks_us()</p>
<p>while echoPin.value():</p>
<p>pass</p>
<p>pingStop=time.ticks_us()</p>
<p>pingTime=time.ticks_diff(pingStop,pingStart)</p>
<p>distance=pingTime*soundVelocity//2//10000</p>
<p>time.sleep_ms(10)</p>
<p>return int(distance)</p>
<p>while True:</p>
<p>Distance=getSonar() #Get the distance measured by ultrasound.</p>
<p>print(Distance) #Send a pulse to calculate the distance in centimeters and print the result.</p>
<p>if Distance&lt;8: #If the distance is less than 8</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_back() #Car goes back</p>
<p>elif Distance&gt;=8 and Distance&lt;13: #If the distance is greater than or equal to 8, it's less than 13.</p>
<p>car_stop() # Car stop</p>
<p>elif Distance&gt;=13 and Distance&lt;35: #If the distance is greater than or equal to 13, it's less than 35.</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_forward() #Car ahead</p>
<p>else:</p>
<p>car_stop()</p></td>
</tr>
</tbody>
</table>

**5.Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/4954b24643d494ae3258bf96da847578.png)

Place batteries, turn the power switch to ON end and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the car
will follow the obstacle to move.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/169099e3ee48e585f65963c01687873f.png)

### Project 6.3: Dodge obstacles

1.  **Description：**

In this project, we will take advantage of the ultrasonic sensor to
detect the distance away from the obstacle so as to avoid them

2.  **Working Principle：**

<table>
<tbody>
<tr class="odd">
<td></td>
<td>8*8 Dot matrix display</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Set servo to 90°</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>loop</strong></td>
<td>Detect the distance away from the obstacle（unit: cm）</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Condition 1</td>
<td>State</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>0&lt;distance＜10</strong></td>
<td>Stop</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Show the“stop”pattern</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Set the servo to 180°</td>
<td>Distance away form the obstacle：a1（unit：cm）</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Set the servo to 0°</td>
<td>Distance away form the obstacle：a2（unit：cm）</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Condition 2</td>
<td>State</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>a1＜a2</strong></td>
<td>Car turns right（set PWM to 200）</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>show“turning right”pattern</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>Set servo to 90°</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>a1≥a2</strong></td>
<td>Turn left（set PWM to 200）</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>display“left turning”pattern</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>Set servo to 90°</td>
</tr>
<tr class="even">
<td></td>
<td><strong>distance≥10</strong></td>
<td>The 8*8 dot matrix display shows“going forward”pattern</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Go forward（set PWM to 200）</td>
<td></td>
</tr>
</tbody>
</table>

**3. Flow Chart：**

![](media/62cafb9417859896368e046396c58495.png)

**4. Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_06.3\_Avoid\_Obstacles”

Select“ht16k33.py”and“ht16k33matrix.py”and right-click“Upload to /”and
upload them to the ESP32；

Double-click Project\_06.3\_Avoid\_Obstacles.py as shown below:

![](media/869461073ab04890b1e78d223a41a3bc.png)

![](media/89cb668817a369d4dedf7ec16af72c8d.png)

![](media/cd784f85579f95c5f90735606e1a2b45.png)

<table>
<tbody>
<tr class="odd">
<td><p>import utime as time</p>
<p>from machine import I2C, Pin, RTC, PWM</p>
<p>from ht16k33matrix import HT16K33Matrix</p>
<p>#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.</p>
<p>servoPin = Pin(4)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(1)</p>
<p>#Set the pin and sound speed of the ultrasonic sensor.</p>
<p>trigPin=Pin(5,Pin.OUT,0)</p>
<p>echoPin=Pin(18,Pin.IN,0)</p>
<p>soundVelocity=340</p>
<p>distance=0</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=50,duty=0)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=50,duty=0)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(200)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(250)</p>
<p># As a function of the car going left.</p>
<p>def car_left():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(500)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(500)</p>
<p># As a function of the car going right.</p>
<p>def car_right():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(500)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(500)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin2.deinit()</p>
<p>pin4.deinit()</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>#Subfunction getSonar() is used to start the Ultrasonic Module to begin measurements,</p>
<p>#and return the measured distance in centimeters. In this function, first let trigPin</p>
<p>#send 10us high level to start the Ultrasonic Module. Then use pulseIn() to read</p>
<p>#the Ultrasonic Module and return the duration time of high level.</p>
<p>#Finally, the measured distance according to the time is calculated.</p>
<p>def getSonar():</p>
<p>trigPin.value(1)</p>
<p>time.sleep_us(10)</p>
<p>trigPin.value(0)</p>
<p>while not echoPin.value():</p>
<p>pass</p>
<p>pingStart=time.ticks_us()</p>
<p>while echoPin.value():</p>
<p>pass</p>
<p>pingStop=time.ticks_us()</p>
<p>pingTime=time.ticks_diff(pingStop,pingStart)</p>
<p>distance=pingTime*soundVelocity//2//10000</p>
<p>time.sleep_ms(10)</p>
<p>return int(distance)</p>
<p># CONSTANTS</p>
<p>DELAY = 0.01</p>
<p>PAUSE = 3</p>
<p># START</p>
<p>if __name__ == '__main__':</p>
<p>i2c = I2C(scl=Pin(22), sda=Pin(21))</p>
<p>display = HT16K33Matrix(i2c)</p>
<p>display.set_brightness(2)</p>
<p>while True:</p>
<p>Distance=getSonar() #Get the distance measured by ultrasound.</p>
<p>if Distance&gt;0 and Distance&lt;10: #If the distance is greater than 0, it's less than 10.</p>
<p>car_stop() # Car stop</p>
<p># Draw a custom icon on the LED</p>
<p>icon = b"\x18\x18\x18\x18\x18\x00\x00\x18"</p>
<p>display.set_icon(icon).draw()</p>
<p># Rotate the icon</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(0.2)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(128)</p>
<p>time.sleep(0.3)</p>
<p>a1=getSonar()</p>
<p>time.sleep(0.2)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(25)</p>
<p>time.sleep(0.3)</p>
<p>a2=getSonar()</p>
<p>time.sleep(0.2)</p>
<p>if a1&gt;a2:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_left()</p>
<p>icon = b"\x48\x24\x12\x09\x09\x12\x24\x48"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(0.3)</p>
<p>icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>else:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_right()</p>
<p>icon = b"\x12\x24\x48\x90\x90\x48\x24\x12"</p>
<p>display.set_icon(icon).draw()</p>
<p># Rotate the icon</p>
<p>display.set_angle(0).draw()</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(0.3)</p>
<p>icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>else:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_forward() #Car ahead</p>
<p>icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p></td>
</tr>
</tbody>
</table>

**Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/4d24f10f141f140d6aa8a92df437fe5c.png)

Place batteries, turn the power switch to ON end and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then the car
can automatically dodge obstacles; press“Ctrl+C”or click
![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/2f3701b99abc5f4a2129105c9ab06115.png)

## Project 7: Line Tracking Sensor

There are two IR line tracking sensors on the car. They are actually two
pairs of ST188L3 infrared tubes and used to detect black and white
lines. In this project, we will make a line tracking car

### **Project 7.1: Reading Values**

**1.Description：**

In this experiment, we use ST188L3 infrared tubes to detect black and
white lines, then print the data on the serial monitor.

**2. Knowledge：**

**Infrared line tracking:**

The IR line tracking sensor boasts a pair of ST188L3 infrared tubes.
ST188L3 tubes has an infrared emitting diode and a receiver tube. When
the emitting diode emits an infrared signal then received by the
receiving tube after being reflected by the white object. Once the
receiving tube receives the signal, the output terminal will output a
low level (0); when the infrared emitting diode emits an infrared
signal, and the infrared signal is absorbed by the black object, a high
level (1) will be output, thus realizing the function of detecting
signals through infrared rays.

Warning: Reflective optical sensors (including IR line tracking sensors)
shouldn’t be applied under sunlight as there is a lot of invisible light
such as infrared and ultraviolet.

Values detected by the line tracking sensor are shown in the table.

The value will be 1 if detecting black or no objects and the value 0
will appear if detecting white objects.

he detected black object or no object represents 1, and the detected
white object represents 0.

<table>
<tbody>
<tr class="odd">
<td>Left</td>
<td>Right</td>
<td>Value（Binary ）</td>
</tr>
<tr class="even">
<td>0</td>
<td>0</td>
<td>00</td>
</tr>
<tr class="odd">
<td>0</td>
<td>1</td>
<td>01</td>
</tr>
<tr class="even">
<td>1</td>
<td>0</td>
<td>10</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>11</td>
</tr>
</tbody>
</table>

**3. Test Code：**

The line tracking sensors of the PCB board are controlled by GPIO17 and
GPIO16 of the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_07.1\_Tracking\_Sensor\_Read\_Value”

Double-click Project\_07.1\_Tracking\_Sensor\_Read\_Value.py as shown
below:

![](media/f9f193dfef247772704a233bf1f79994.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>tracking_left = Pin(17, Pin.IN)</p>
<p>tracking_right = Pin(16, Pin.IN)</p>
<p>while True:</p>
<p>L_value = tracking_left.value()</p>
<p>R_value = tracking_right.value()</p>
<p>print("L_value:%d, R_value:%d" %(L_value, R_value))</p>
<p>time.sleep(0.5)</p></td>
</tr>
</tbody>
</table>

**4.Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/06d5ee6ddfd9754e2fab76eedcf3aadc.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, Put a black
thing under the line tracking sensor of the car and move it, you will
see different indicators light up, and at the same time you will see the
value on the serial monitor.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit.

The sensitivity can be adjusted by rotating the potentiometer. When the
indicator light is adjusted to the critical point of on and off state,
the sensitivity is the highest.

![](media/3f5408865f10f90c607d14066df7671e.png)

![](media/7b57898ccc7423695e6078a3e015fb90.png)

### Project 7.2: Line Tracking

**1.Description：**

We’ve introduced the knowledge of motor drivers, speed regulation, and
infrared line tracking. In this experiment, the car will perform
different actions according to the values transmitted by the infrared
tracking.

2.  **Working Principle：**

<table>
<tbody>
<tr class="odd">
<td>Left</td>
<td>Right</td>
<td>Value（Binary ）</td>
<td>State</td>
</tr>
<tr class="even">
<td>0</td>
<td>0</td>
<td>00</td>
<td>Stop</td>
</tr>
<tr class="odd">
<td>0</td>
<td>1</td>
<td>01</td>
<td>Turn right</td>
</tr>
<tr class="even">
<td>1</td>
<td>0</td>
<td>10</td>
<td>Turn left</td>
</tr>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>11</td>
<td>Move forward</td>
</tr>
</tbody>
</table>

3.  **Flow Chart：**

![](media/c6a0ace5faa949e4fb24fc511d179e08.png)

**4. Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_07.2\_Follow\_Line\_To\_Walk”;

Double-click Project\_07.2\_Follow\_Line\_To\_Walk.py as shown below:

![](media/2539a33fe74cc42180abd567f6ff9ba6.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, PWM</p>
<p>import time</p>
<p>#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.</p>
<p>servoPin = Pin(4)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(1)</p>
<p>#Set the pin of the tracking sensor</p>
<p>tracking_left = Pin(17, Pin.IN)</p>
<p>tracking_right = Pin(16, Pin.IN)</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=50,duty=0)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=50,duty=0)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(200)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(200)</p>
<p># As a function of the car going left.</p>
<p>def car_left():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(180)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(1023)</p>
<p># As a function of the car going right.</p>
<p>def car_right():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(1023)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(220)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin2.deinit()</p>
<p>pin4.deinit()</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>while True:</p>
<p>L_value = tracking_left.value() #Left infrared tracking value is assigned to the variable L_value.</p>
<p>R_value = tracking_right.value() #Right infrared tracking value is assigned to the variable R_value.</p>
<p>if L_value == 1 and R_value == 1: #Black lines were detected in both left and right infrared tracking.</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_forward() #Car ahead</p>
<p>elif L_value == 1 and R_value == 0:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_left()</p>
<p>elif L_value == 0 and R_value == 1:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_right()</p>
<p>else:</p>
<p>car_stop()</p></td>
</tr>
</tbody>
</table>

**Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/d08dd452d73a74fa2227be92b6d3752f.png)

Place batteries, turn the power switch to ON end and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, then it will
perform different functions via values sent by line tracking sensors;
press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit.

![](media/12e5251cdcaf5274e64a5b8e865c61b2.png)

## Project 8: Light Following

There are two photoresistors on the car. They can vary with the light
intensity and send information to the Nano board to control the car.

Photoresistors can determine and conduct the car to move by detecting
light

### Project 8.1 Read Values

1.  **Description：**

In this experiment, we will learn the working principle of the
photoresistor

**2. Knowledge：**

**Photoresistor:**

It mainly uses a photosensitive resistance element whose resistance
varies from the light intensity. The signal terminal of the sensor is
connected to the analog port of the microcontroller. When the light is
stronger, the analog value at the analog port will increase; on the
contrary, when the light intensity is weaker, the analog value of the
microcontroller will reduce. In this way, the corresponding analog value
can reflect the ambient light intensity.

**3. Wire up：**

Through the wiring-up diagram, signal pins of two photoresistors are
connected to GPIO34 and GPIO35 of the ESP32 board.

For the following experiment, we use the photoresistor connected to
GPIO34 to finish experiments. First, let’s read analog values.

<table>
<tbody>
<tr class="odd">
<td>Left photoresistor</td>
<td>PCB board</td>
</tr>
<tr class="even">
<td>G</td>
<td>G</td>
</tr>
<tr class="odd">
<td>V</td>
<td>V</td>
</tr>
<tr class="even">
<td>S</td>
<td>S（GPIO34）</td>
</tr>
</tbody>
</table>

**4. Test Code：**

The left photoresistor is controlled by the GPIO34 of the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_08.1\_Read\_Photosensor\_Value”

Double-click Project\_08.1\_Read\_Photosensor\_Value.py as shown below:

![](media/d676bb3f5dde82f66582974b7d95e7e8.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the photoresistance to pin 34 (ADC function)</p>
<p>adc = ADC(Pin(34))</p>
<p>adc.atten(ADC.ATTN_11DB)</p>
<p>adc.width(ADC.WIDTH_10BIT)</p>
<p># Print the current adc value of the photoresistance cyclically</p>
<p>try:</p>
<p>while True:</p>
<p>adcValue = adc.read() # read the ADC value of photoresistance</p>
<p>print("ADC Value:", adcValue) #Send the ADC value of photoresistance and print the result.</p>
<p>time.sleep(0.5)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

**5. Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/88cf8e65abed62409b7d25a32c9dce60.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png)“Run current script”, the Shell monitor
will show scripts and code will be run.

When the light intensifies, the analog value will get increased; on the
contrary, the analog value will get reduced.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/62a7dd0249ec8b7b72dfa159c62cf093.png)

![](media/2779d2006487d514963e0c9b095864be.png)

### Project 8.2: Light Following Car

1.  **Description：**

We have learned the working principle of photoresistor, motor and speed
regulation. In this experiment, we will use a photoresistor to detect
the intensity of light as as to achieve the light following effect.

2.  **Working Principle：**

<table>
<tbody>
<tr class="odd">
<td>Analog value of the left sensor</td>
<td>Analog value of the right sensor</td>
<td>Function</td>
</tr>
<tr class="even">
<td>&gt;700</td>
<td>&gt;700</td>
<td>Move forward</td>
</tr>
<tr class="odd">
<td>&gt;700</td>
<td>≤700</td>
<td>Move to left</td>
</tr>
<tr class="even">
<td>≤700</td>
<td>&gt;700</td>
<td>Move to right</td>
</tr>
<tr class="odd">
<td>&lt;700</td>
<td>&lt;700</td>
<td>Stop</td>
</tr>
</tbody>
</table>

3.  **Wiring up：**

<table>
<tbody>
<tr class="odd">
<td>Left Photoresistor</td>
<td><p>PCB</p>
<p>Board</p></td>
<td></td>
<td>Right photoresistor</td>
<td><p>PCB</p>
<p>Board</p></td>
</tr>
<tr class="even">
<td>G</td>
<td>G</td>
<td></td>
<td>G</td>
<td>G</td>
</tr>
<tr class="odd">
<td>V</td>
<td>V</td>
<td></td>
<td>V</td>
<td>V</td>
</tr>
<tr class="even">
<td>S</td>
<td>S（GPIO34）</td>
<td></td>
<td>S</td>
<td>S（GPIO35）</td>
</tr>
</tbody>
</table>

![](media/8a5840a7da0fc461c19be88f0283ce50.png)

4.  **Test Code：**

The left and right photoresistors are controlled by GPIO34 and GPIO35 of
the ESP32 board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_08.2\_Light\_Following\_Car”

Double-click Project\_08.2\_Light\_Following\_Car.py as shown below:

![](media/768b68238bdc80be671774f37310d996.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC, PWM</p>
<p>import time</p>
<p>#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.</p>
<p>servoPin = Pin(4)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(1)</p>
<p># Initialize the left photoresistance to pin 34 (ADC function)</p>
<p>adc1 = ADC(Pin(34))</p>
<p>adc1.atten(ADC.ATTN_11DB)</p>
<p>adc1.width(ADC.WIDTH_10BIT)</p>
<p># Initialize the right photoresistance to pin 35 (ADC function)</p>
<p>adc2 = ADC(Pin(35))</p>
<p>adc2.atten(ADC.ATTN_11DB)</p>
<p>adc2.width(ADC.WIDTH_10BIT)</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=50,duty=0)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=50,duty=0)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(300)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(300)</p>
<p># As a function of the car going backwards.</p>
<p>def car_back():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(200)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(200)</p>
<p># As a function of the car going left.</p>
<p>def car_left():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(200)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(900)</p>
<p># As a function of the car going right.</p>
<p>def car_right():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(900)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(200)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin2.deinit()</p>
<p>pin4.deinit()</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>while True:</p>
<p>adcValue1 = adc1.read() # read the ADC value of the left photoresistance.</p>
<p>adcValue2 = adc2.read() # read the ADC value of the right photoresistance.</p>
<p>print("ADC Value1:", adcValue1 ,"ADC Value2:", adcValue2)</p>
<p>time.sleep(0.5)</p>
<p>if adcValue1 &gt; 700 and adcValue2 &gt; 700: #Range values measured by left and right photoresistances.</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_forward() #Car ahead</p>
<p>elif adcValue1 &gt; 700 and adcValue2 &lt;= 700:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_left()</p>
<p>elif adcValue1 &lt;= 700 and adcValue2 &gt; 700:</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_right()</p>
<p>else:</p>
<p>car_stop()</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/16289bb619de08ee4683854562acc43b.png)

Place batteries, turn the power switch to ON end and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, the car will
follow the light to move.; press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png)
to exit

![](media/3f77abefe6509f442a9a856526233e12.png)

## Project 9: IR Remote Control

Infrared remote controls are everywhere in daily life. It is used to
control various home appliances, such as TV, speakers, video recorders
and satellite signal receivers.

The remote control is composed of an IR emitter, an IR receiver and a
decoding MCU. In this project, we will make a IR remote control car.

### Project 9.1: IR Remote and Reception

**1.Description：**

In this experiment, we will combine the IR receiver and the IR remote
control to read key values and show them on the serial monitor.

2.  **Knowledge：**

**IR Remote Control：**

It is a device with buttons. When the key is pressed, IR signals will be
sent.

Infrared remote control technology is widely used, such as TVs, air
conditioners and so on. And it can control air conditioners and TVs

The infrared remote control adopts NEC coding, and the signal period is
110ms.

The remote control is shown below:

![](media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

Infrared (IR) receiver:

It can receive infrared light and be used to detect the infrared signal
emitted by the infrared remote control.

It can demodulate the received infrared light signal and convert it back
to binary, and then transmit the information to the microcontroller.

![](media/3da1969e509f53706643c77d0534eb73.png)

**NEC Infrared communication protocol：**

**NEC Protocol**

To my knowledge the protocol I describe here was developed by NEC (Now
Renesas). I've seen very similar protocol descriptions on the internet,
and there the protocol is called Japanese Format.

I do admit that I don't know exactly who developed it. What I do know is
that it was used in my late VCR produced by Sanyo and was marketed under
the name of Fisher. NEC manufactured the remote control IC.

This description was taken from my VCR's service manual. Those were the
days, when service manuals were filled with useful information\!

**Features**

  - 8 bit address and 8 bit command length.

  - Extended mode available, doubling the address size.

  - Address and command are transmitted twice for reliability.

  - Pulse distance modulation.

  - Carrier frequency of 38kHz.

  - Bit time of 1.125ms or 2.25ms.

**Modulation**

![](media/da33571c6f0afb94b1ec1d91caba3edb.png)

The NEC protocol uses pulse distance encoding of the bits. Each pulse is
a 560µs long 38kHz carrier burst (about 21 cycles). A logical "1" takes
2.25ms to transmit, while a logical "0" is only half of that, being
1.125ms. The recommended carrier duty-cycle is 1/4 or 1/3

**Protocol**

![](media/f970404e7bbfb5711fea5c776f689f3a.png)

The picture above shows a typical pulse train of the NEC protocol. With
this protocol the LSB is transmitted first. In this case Address $59 and
Command $16 is transmitted. A message is started by a 9ms AGC burst,
which was used to set the gain of the earlier IR receivers. This AGC
burst is then followed by a 4.5ms space, which is then followed by the
Address and Command. Address and Command are transmitted twice. The
second time all bits are inverted and can be used for verification of
the received message. The total transmission time is constant because
every bit is repeated with its inverted length. If you're not interested
in this reliability you can ignore the inverted values, or you can
expand the Address and Command to 16 bits each\!

Keep in mind that one extra 560µs burst has to follow at the end of the
message in order to be able to determine the value of the last bit.

![](media/63364daf21e5522c64eb8dfa82f2cef2.png)

A command is transmitted only once, even when the key on the remote
control remains pressed. Every 110ms a repeat code is transmitted for as
long as the key remains down. This repeat code is simply a 9ms AGC pulse
followed by a 2.25ms space and a 560µs burst.

![](media/afea92a3b5cc1aa2457d2b118b157c84.png)

**Extended NEC protocol**

The NEC protocol is so widely used that soon all possible addresses were
used up. By sacrificing the address redundancy the address range was
extended from 256 possible values to approximately 65000 different
values. This way the address range was extended from 8 bits to 16 bits
without changing any other property of the protocol.

By extending the address range this way the total message time is no
longer constant. It now depends on the total number of 1's and 0's in
the message. If you want to keep the total message time constant you'll
have to make sure the number 1's in the address field is 8 (it
automatically means that the number of 0's is also 8). This will reduce
the maximum number of different addresses to just about 13000.

The command redundancy is still preserved. Therefore each address can
still handle 256 different commands.

![](media/2f78d1ce7f001926f6b90ad966796e91.png)

Keep in mind that 256 address values of the extended protocol are
invalid because they are in fact normal NEC protocol addresses. Whenever
the low byte is the exact inverse of the high byte it is not a valid
extended address.

**3.Test Code：**

The IR receiver on the PCB board is controlled by GPIO19 of the ESP32
board.

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_09.1\_Infrared\_Remote\_And\_Receiver”.
Select“irrecvdata.py”and right-click“Upload to /” and upload
irrecvdata.py to ESP32

Double-click Project\_09.1\_Infrared\_Remote\_And\_Receiver.py as shown
below:

![](media/e95de21ef0aeb594084d91ccffa448e8.png)

![](media/831e338e52e6a3858e2b2d0d4425db87.png)

<table>
<tbody>
<tr class="odd">
<td><p>from irrecvdata import irGetCMD #Import the infrared decoder.</p>
<p>recvPin = irGetCMD(19) #Associate the infrared decoder with Pin(19).</p>
<p>#When infrared key value is obtained, print it out in"Shell" repetitively.</p>
<p>try:</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.</p>
<p>if irValue:</p>
<p>print(irValue) # Send the irValue of Infrared Receiver and print the result.</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

**5.Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/ed9ccd76f451e3cc3ff89529f09c6ad2.png)

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running. Point the IR
remote control at the IR receiver and press keys on the remote control,
then the monitor will display key values.

Press“Ctrl+C”or click ![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit

![](media/4a071eb7da0b45b94c0fe70b8d4f9e77.png)

![](media/623f8fa842b90a093d286954835483c6.png)

**Code of each key**

![](media/ebcf0cb2055f7784505f76ceeaef9f47.jpeg)

### Project 9.2: IR Remote Control Car

**1.Description：**

In the above experiment, we have learned about the knowledge of the 8\*8
dot matrix display, the motor driver and speed regulation, the infrared
receiver and the infrared remote control. In this experiment, we will
use the infrared remote control and the infrared receiver to control the
car.

**2. Working Principle：**

<table>
<tbody>
<tr class="odd">
<td>Keys</td>
<td>Keys Code</td>
<td>Functions</td>
</tr>
<tr class="even">
<td><img src="media/e471ee4e3fd5a9daafc9d97460124119.png" style="width:0.38542in;height:0.36458in" /></td>
<td>FF629D</td>
<td>Go forward</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Display “forward”pattern</td>
</tr>
<tr class="even">
<td><img src="media/ace76021618d9ae6107a0f9b69dc47fc.png" style="width:0.38542in;height:0.36458in" /></td>
<td>FFA857</td>
<td>Go back</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Display “back”pattern</td>
</tr>
<tr class="even">
<td><img src="media/813f77055aefe6ee0fce22e14fbf093c.png" style="width:0.39583in;height:0.38542in" /></td>
<td>FF22DD</td>
<td>Turn left</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Show“left” pattern</td>
</tr>
<tr class="even">
<td><img src="media/9eb9042aace52c96a86379dbac70ee2d.png" style="width:0.38542in;height:0.375in" /></td>
<td>FFC23D</td>
<td>Turn right</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Show“right turning”pattern</td>
</tr>
<tr class="even">
<td><img src="media/68cbb08d230ef50b2f69c66c685414f6.png" style="width:0.35417in;height:0.35417in" /></td>
<td>FF02FD</td>
<td>stop</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>show“stop”pattern</td>
</tr>
</tbody>
</table>

3.  **Flow Chart：**

![](media/b8ecdfd8dbc04c43021b09bd2c6a48f0.png)

4.  **Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_04\_Servo\_Sweep”，select“ht16k33.py,”,“ht16k33matrix.py”and“irrecvdata.py”,
right-click Upload to /”to upload them to the ESP32

Double-click Project\_09.2\_Infrared\_Remote\_Control\_Car.py as shown
below:

![](media/730418c6b30b9e80239ecb55a391e921.png)

![](media/9a83a8fb4cb6ee1dbaff78924a68c07d.png)

![](media/0aedf4393e6efb4ad202db366aeab168.png)

![](media/98ce81a4d2e4b1a0ddd8c890cce55fcb.png)

<table>
<tbody>
<tr class="odd">
<td><p>#Import libraries</p>
<p>import utime as time</p>
<p>from machine import I2C, Pin, RTC, PWM</p>
<p>from ht16k33matrix import HT16K33Matrix</p>
<p>from irrecvdata import irGetCMD</p>
<p>recvPin = irGetCMD(19) #Associate the infrared decoder with Pin(19).</p>
<p>#Define GPIO4’s output frequency as 50Hz and its duty cycle as 77, and assign them to PWM.</p>
<p>servoPin = Pin(4)</p>
<p>pwm = PWM(servoPin, freq=50)</p>
<p>pwm.duty(77)</p>
<p>time.sleep(1)</p>
<p># right wheel</p>
<p>pin1=Pin(32,Pin.OUT)</p>
<p>pin2=PWM(Pin(25),freq=50,duty=0)</p>
<p># left wheel</p>
<p>pin3=Pin(33,Pin.OUT)</p>
<p>pin4=PWM(Pin(26),freq=50,duty=0)</p>
<p># CONSTANTS</p>
<p>DELAY = 0.01</p>
<p>PAUSE = 3</p>
<p># START</p>
<p>if __name__ == '__main__':</p>
<p>i2c = I2C(scl=Pin(22), sda=Pin(21))</p>
<p>display = HT16K33Matrix(i2c)</p>
<p>display.set_brightness(2)</p>
<p># As a function of the car going forward.</p>
<p>def car_forward():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(1000)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(1000)</p>
<p># As a function of the car going backwards.</p>
<p>def car_back():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(250)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(250)</p>
<p># As a function of the car going left.</p>
<p>def car_left():</p>
<p>pin1.value(0)</p>
<p>pin2.duty(1000)</p>
<p>pin3.value(1)</p>
<p>pin4.duty(500)</p>
<p># As a function of the car going right.</p>
<p>def car_right():</p>
<p>pin1.value(1)</p>
<p>pin2.duty(500)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(1000)</p>
<p># As a function of the car stopping.</p>
<p>def car_stop():</p>
<p>pin2.deinit()</p>
<p>pin4.deinit()</p>
<p>pin1.value(0)</p>
<p>pin2.duty(0)</p>
<p>pin3.value(0)</p>
<p>pin4.duty(0)</p>
<p>def handleControl(value):</p>
<p>if value == '0xff629d':</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_forward() #Car ahead</p>
<p># Dot matrix shows a forward pattern</p>
<p>icon = b"\x18\x24\x42\x99\x24\x42\x81\x00"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p>
<p>elif value == '0xffa857':</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_back() # Car goes back</p>
<p># Dot matrix shows a backward pattern</p>
<p>icon = b"\x00\x81\x42\x24\x99\x42\x24\x18"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p>
<p>elif value == '0xff22dd':</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_left() # Car to the left</p>
<p># Dot matrix shows a left pattern</p>
<p>icon = b"\x48\x24\x12\x09\x09\x12\x24\x48"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p>
<p>elif value == '0xffc23d':</p>
<p>pin2=PWM(Pin(25),freq=50)</p>
<p>pin4=PWM(Pin(26),freq=50)</p>
<p>car_right() # Car to the right</p>
<p># Dot matrix displays a right pattern</p>
<p>icon = b"\x12\x24\x48\x90\x90\x48\x24\x12"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p>
<p>elif value == '0xff02fd':</p>
<p>car_stop() # Car to the right</p>
<p># Dot matrix displays a stop pattern</p>
<p>icon = b"\x18\x18\x18\x18\x18\x00\x00\x18"</p>
<p>display.set_icon(icon).draw()</p>
<p>display.set_angle(0).draw()</p>
<p>time.sleep(PAUSE)</p>
<p>try:</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.</p>
<p>if irValue:</p>
<p>print(irValue)</p>
<p>handleControl(irValue)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

**Test Result**

Connect the ESP32 board to your PC and click ![](media/6827818058b5d94c3e94e7a3f487afa5.png)

![](media/ab27a23f4a2ff11379bfaf50390036bb.png)

Place batteries, turn the power switch to ON end and power up.

Click ![](media/c005d91eb85d5c58566746609ab80254.png), the script starts running, point the
remote control at the IR receiver and press keys, then the car will make
the corresponding movement.; press“Ctrl+C”or click
![](media/27451c8a9c13e29d02bc0f5831cfaf1f.png) to exit.

![](media/3f865d7066ed13b720b4311adf913e4d.png)

## Project 10: WIFI Working Mode

In this chapter, we will focus on the WiFi infrastructure of the ESP32.
ESP32 has 3 different WiFi working modes: Station mode, AP mode and
AP+Station mode. All WiFi programming projects must configure WiFi
operating mode before using WiFi, otherwise WiFi cannot be used.

### Project 10.1：WIFI Station Mode

1.  **Components**

<table>
<tbody>
<tr class="odd">
<td><img src="media/729232b0c2d2c01984808289b222890c.png" style="width:1.8125in;height:0.86458in" /></td>
<td><img src="media/53f17b0de2d98d4714e8fe9043a346ca.jpeg" style="width:2.43681in;height:1.13472in" alt="IMG_256" /></td>
</tr>
<tr class="even">
<td>USB Cable x1</td>
<td>ESP32*1</td>
</tr>
</tbody>
</table>

Plug the ESP32 to the USB port of your PC

![](media/53f17b0de2d98d4714e8fe9043a346ca.jpeg)

**Component Knowledge：**

**Station mode：**

When setting Station mode, the ESP32 is taken as a WiFi client. It can
connect to the router network and communicate with other devices on the
router via a WiFi connection. As shown in the figure below, the PC and
the router have been connected. If the ESP32 wants to communicate with
the PC, the PC and the router need to be connected.

![](media/f74baff97695aa2ee33a8c19370d2547.png)

**2. Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_10.1\_WiFi\_Station\_Mode”

Double-click Project\_10.1\_WiFi\_Station\_Mode.py as shown below:

![](media/d1b2b721282f80d6ea9fa621777b6565.png)

<table>
<tbody>
<tr class="odd">
<td><p>import time</p>
<p>import network #Import network module</p>
<p>#Enter correct router name and password</p>
<p>ssidRouter = '********' #Enter the router name</p>
<p>passwordRouter = '********' #Enter the router password</p>
<p>def STA_Setup(ssidRouter,passwordRouter):</p>
<p>print("Setup start")</p>
<p>sta_if = network.WLAN(network.STA_IF) #Set ESP32 in Station mode</p>
<p>if not sta_if.isconnected():</p>
<p>print('connecting to',ssidRouter)</p>
<p>#Activate ESP32’s Station mode, initiate a connection request to the router</p>
<p>#and enter the password to connect.</p>
<p>sta_if.active(True)</p>
<p>sta_if.connect(ssidRouter,passwordRouter)</p>
<p>#Wait for ESP32 to connect to router until they connect to each other successfully.</p>
<p>while not sta_if.isconnected():</p>
<p>pass</p>
<p>#Print the IP address assigned to ESP32 in “Shell”.</p>
<p>print('Connected, IP address:', sta_if.ifconfig())</p>
<p>print("Setup End")</p>
<p>try:</p>
<p>STA_Setup(ssidRouter,passwordRouter)</p>
<p>except:</p>
<p>sta_if.disconnect()</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**
    
    Since the router name and password are different in various places,
    before running the code, the user needs to enter the correct router
    name and password in the red box shown above.

After entering the correct router name and password, click
![](media/c005d91eb85d5c58566746609ab80254.png), the code will be run.

The Shell monitor will print the IP address of the ESP32 when connecting
the ESP32 to your router.

![](media/5cc4b54fc4c812b29e7aa6bcf8b89aa7.png)

![](media/93283ae7cb7a82e51f252d2cf2607c7e.png)

### Project 10.2：WIFI AP Mode

**Component Knowledge：**

**AP Mode:**

When setting AP mode, a hotspot network will be created, waiting for
other WiFi devices to connect. As shown below;

take the ESP32 as the hotspot. If a phone or PC needs to communicate
with the ESP32, it must be connected to the ESP32's hotspot.
Communication is only possible after a connection is established via the
ESP32.

![](media/35d90f1ce10814ea1897ba63f8bd7ad9.png)

**3. Test Code:**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”“Project\_10.2\_WiFi\_AP\_Mode”

Double-click“Project\_10.2\_WiFi\_AP\_Mode”as shown below:

![](media/4f82ee64e7ede3527fb2665f84bdd719.png)

<table>
<tbody>
<tr class="odd">
<td><p>import network</p>
<p>#Enter correct AP name and password.</p>
<p>ssidAP = 'ESP32_WiFi' #Enter the router name</p>
<p>passwordAP = '12345678' #Enter the router password</p>
<p>local_IP = '192.168.1.149'</p>
<p>gateway = '192.168.1.1'</p>
<p>subnet = '255.255.255.0'</p>
<p>dns = '8.8.8.8'</p>
<p>#Set ESP32 in AP mode.</p>
<p>ap_if = network.WLAN(network.AP_IF)</p>
<p>def AP_Setup(ssidAP,passwordAP):</p>
<p>ap_if.ifconfig([local_IP,gateway,subnet,dns]) #Configure IP address, gateway and subnet mask for ESP32.</p>
<p>print("Setting soft-AP ... ")</p>
<p>#Turn on an AP in ESP32, whose name is set by ssid_AP and password is set by password_AP</p>
<p>ap_if.config(essid=ssidAP,authmode=network.AUTH_WPA_WPA2_PSK, password=passwordAP)</p>
<p>ap_if.active(True)</p>
<p>print('Success, IP address:', ap_if.ifconfig())</p>
<p>print("Setup End\n")</p>
<p>try:</p>
<p>AP_Setup(ssidAP,passwordAP)</p>
<p>except:</p>
<p>print("Failed, please disconnect the power and restart the operation.")</p>
<p>ap_if.disconnect() #If the program is running abnormally, the AP disconnection function will be called.</p></td>
</tr>
</tbody>
</table>

**4.Test Result**

You can modify the AP name and password or keep them unchanged

Click ![](media/c005d91eb85d5c58566746609ab80254.png)“Run current script”, the code will be run.
Open the AP function of the ESP32, the Shell monitor will print the
information

![](media/a4251953446fb4db686be9ec0f411bf5.png)

![](media/2292bb8b4e64b975df8bcea39d308f08.png)

Enable Wifi, then you can see the ssid\_AP which is called "ESP32\_Wifi"
in this code. You can enter the password "12345678" to connect it, or
you can modify its AP name and password by code.

![](media/3e0ad895bea7f5100cc02a415adcace7.png)

### Project 10.3：WIFI AP+Station Mode

1.  **Component Knowledge：**

**AP+Station mode**

In addition to the AP mode and the Station mode, **AP+Station mode** can
be used at the same time. Turn on the Station mode of the ESP32, connect
it to the router network, and it can communicate with the Internet
through the router. Then turn on the AP mode to create a hotspot
network. Other WiFi devices can be connected to the router network or
the hotspot network to communicate with the ESP32.

**2. Test Code：**

You can download test code from a link
[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02 You
can save the code anywhere. We save the code in the drive D of our
computer.

As shown below: D:\\Micropython\_Codes.

![](media/e56fd1a0dcc907d61032fced715aa4cb.png)

Open“Thonny”and click“This
computer”→“D:”→“Micropython\_Codes”→“Project\_10.3\_WiFi\_AP\_Station\_Mode”

Double-click Project\_10.3\_WiFi\_AP\_Station\_Mode.py as shown below:

![](media/45b948254791582cce92e179807b59a2.png)

<table>
<tbody>
<tr class="odd">
<td><p>import network</p>
<p>ssidRouter = '********' #Enter the router name</p>
<p>passwordRouter = '********' #Enter the router password</p>
<p>ssidAP = 'ESP32_WiFi'#Enter the AP name</p>
<p>passwordAP = '12345678' #Enter the AP password</p>
<p>local_IP = '192.168.1.149'</p>
<p>gateway = '192.168.1.1'</p>
<p>subnet = '255.255.255.0'</p>
<p>dns = '8.8.8.8'</p>
<p>sta_if = network.WLAN(network.STA_IF)</p>
<p>ap_if = network.WLAN(network.AP_IF)</p>
<p>def STA_Setup(ssidRouter,passwordRouter):</p>
<p>print("Setting soft-STA ... ")</p>
<p>if not sta_if.isconnected():</p>
<p>print('connecting to',ssidRouter)</p>
<p>sta_if.active(True)</p>
<p>sta_if.connect(ssidRouter,passwordRouter)</p>
<p>while not sta_if.isconnected():</p>
<p>pass</p>
<p>print('Connected, IP address:', sta_if.ifconfig())</p>
<p>print("Setup End")</p>
<p>def AP_Setup(ssidAP,passwordAP):</p>
<p>ap_if.ifconfig([local_IP,gateway,subnet,dns])</p>
<p>print("Setting soft-AP ... ")</p>
<p>ap_if.config(essid=ssidAP,authmode=network.AUTH_WPA_WPA2_PSK, password=passwordAP)</p>
<p>ap_if.active(True)</p>
<p>print('Success, IP address:', ap_if.ifconfig())</p>
<p>print("Setup End\n")</p>
<p>try:</p>
<p>AP_Setup(ssidAP,passwordAP)</p>
<p>STA_Setup(ssidRouter,passwordRouter)</p>
<p>except:</p>
<p>sta_if.disconnect()</p>
<p>ap_if.idsconnect()</p></td>
</tr>
</tbody>
</table>

**3. Test Result**

Before running the code, you need to modify ssidRouter, passwordRouter,
ssidAP, and passwordAP. After making sure that the code is modified
correctly, click ![](media/da852227207616ccd9aff28f19e02690.png), the code starts to run, and
the "Shell" window will display the following:

![](media/60b8b6fd07996f5bfdc9573bd1c94071.png)

![](media/0b01aeeebb9fae819d6a1133b3a8cf69.png)

Enable WiFi, then you can see ssid\_AP on the ESP 32 board.

# ![](media/3e0ad895bea7f5100cc02a415adcace7.png)

**8. Resources**

Download code,libraries and more details, please refer to the following
link:

[https://fs.keyestudio.com/KS50](https://fs.keyestudio.com/KS0470)02
