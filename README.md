##Explicación de los códigos 
#analog.py 
Configura el pin 32 como entrada ADC (Conversor Analógico-Digital) para leer valores del potenciómetro. Muestra el valor crudo de 12 bits (0 a 4095) por consola.

#leds.py
 Inicializa los pines 12, 13, 18 y 19 como salidas digitales. Enciende los 4 LEDs por 2 segundos y luego los apaga, en la placa estos leds representan a los motores y se pueden ver si estan prendidos o apagados.

#libmotor.py
Define funciones de alto nivel (carro_adelante, carro_atras, carro_parar, etc.) que gestionan la secuencia de encendido y apagado de los 4 pines de control para realizar movimientos específicos del vehículo.

#motor.py
Script principal que importa y utiliza las funciones de libmotor.py. Ejecuta el movimiento carro_izquierda durante 2 segundos y luego detiene el vehículo.

#oled.py
Inicializa el bus I2C y la pantalla SSD1306. Muestra mensajes de texto estáticos en la pantalla. Este script confirma la detección de dispositivos I2C en los pines (SCL 22, SDA 21).

#rgbneopixel.py
Inicializa 3 LEDs NeoPixel en el Pin 4 y les asigna un color específico a cada uno confirmando su correcto funcionamiento.