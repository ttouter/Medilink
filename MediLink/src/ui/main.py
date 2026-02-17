import customtkinter as ctk
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import config

class MediLinkApp(ctk.CTk):
    def __init__(self):
        self.title(config.APP_N)