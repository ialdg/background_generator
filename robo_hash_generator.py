# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 14:19:41 2022

@author: ivan.lorenzo
"""

import string as st
import sys
import random as rd
# from random import choices
from robohash import Robohash


def hash_generator():
    hash_string = st.punctuation + st.ascii_lowercase + st.digits + st.ascii_uppercase
    n = rd.randint(1, 100)
    # print(n)
    s = "".join(rd.choices(hash_string, k=n))
    # print("La contraseña de %d caracteres es %s" % (n, s))
    return s


def file_name_generator():
    file_name = st.ascii_lowercase + st.digits + st.ascii_uppercase
    n = rd.randint(1, 100)
    s = "robo_" + "".join(rd.choices(file_name, k=n))
    print(s)
    return s


hash_string = hash_generator()
file_name = file_name_generator()
path_file_name = "C:\\Users\\ivan.lorenzo\\Downloads\\prgs\\nuevas\\Udemy Complete Python Developer In 2020 Zero To Mastery\\my_python_server\\robohash\\" + file_name + ".png"
rh = Robohash(hash_string)
rh.assemble(roboset='any')
with open(path_file_name, "wb") as f:
    rh.img.save(f, format="png")
