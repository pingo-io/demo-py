===================================
Using mini-UART on the Raspberry Pi
===================================

Among the GPIO pins in the Raspberry Pi (all models, up to RPi 2), GPIO14 @ location 8 and GPIO15 @ location 10 are UART TX and RX pins controlled by the Linux kernel serial driver as ``/dev/ttyAMA0``. That interface is called "mini UART". 

In order to use the mini-UART in user programs, you must disable it in the ``raspi-config`` utility, or use a script such as https://github.com/lurch/rpi-serial-console. Disabling the mini-UART means it will no longer be available for connection by a remote terminal to monitor boot messages and for shell access, making it available to user programs via ``/dev/ttyAMA0``.
