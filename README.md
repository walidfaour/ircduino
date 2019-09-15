# ircduino
IRC Connected LCD/LED using Arduino

This is initially just a fun project. You connect to an IRC server, join a channel and send commands to an IRC connected Arduino UNO board that has 3 LEDs (Green, Red, Orange) and a 16x2 LCD screen. You can watch this on a live stream on YouTube and the link is provided in the channel because it changes. 

<b>Connect to IRC with below details:</b><br>

IRC Server: irc.freenode.net<br>
IRC Port: 6667<br>
IRC Channel: ##robot<br>
<br>
Once you join the ##robot channel you can type @help to see available commands as below:<br>
IRC Arduino LCD/LED Control System v1.1:<br>
@help - to show this help menu.<br>
@LED<number> - to control LEDs.<br>
@LCD1<text> - Print to LCD, first line.<br>
@LCD2<text> - Print to LCD, second line.<br>
@LCDCLR - Clear the LCD.<br>
Available LEDs:.<br>
Green LED - Command: @LED1.<br>
Red LED - Command @LED2.<br>
Orange LED - Command @LED3.<br>
You can control multiple LEDs for ex: @LED123.<br>
<br>
New ideas and code changes/pull requests are welcomed. You can see both the IRC bot code and the Arduino C code as well.<br>
<br>
<b>Components used:</b><br>
-Arduino UNO<br>
-Qapass 1602a 16x2 LCD screen<br>
-3 LEDs (Green, Red, Orange)<br>
-3 resistors<br>
-Jumper wires<br>
-GL-36 Breadboard<br>
-USB cable (serial/power)<br>
-Computer connected the Arduino via USB cable<br>
<br>
<b>Code:</b><br>
-IRC Bot v1.0: Python 2.7<br>
-Arduino v1.0: Arduino C<br>
<br>
<b>Circuit Diagram:</b><br>
<img src="ircduino.jpg">
