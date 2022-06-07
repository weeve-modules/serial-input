"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "PORT": env("PORT","/dev/ttyUSB0"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
     "DATA_BITS": env("DATA_BITS","8"),
      "PARITY": env("PARITY","PARITY_NONE"),
         "STOP_BITS": env("STOP_BITS","STOPBITS_ONE")
      
}