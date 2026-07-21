'''A movie is created with many images that are in different
format which cycle through at a certain speed. Astrology pictures
are stacked for dust, clouds, all factors that can cause viewing issues
and the output result would be the best pixels for a single image.'''
#Anthony R Shively Mercer Ohio 1997

#python -m pip install psutil

#ffprobe -v quiet -print_format json -show_format -show_streams "movie.mp4" | grep -E '"codec_name"|"width"|"height"|"r_frame_rate"|"avg_frame_rate"|"duration"|"channels"|"bit_rate"'
#ffmpeg -i movie.mkv frames/frame_%06d.png
#ffmpeg -i original.mkv -vn -acodec copy audio.ac3
#ffmpeg -framerate 30 -i frame_%06d_x2.png -i audio.m4a -c:v av1_amf -usage transcoding -quality quality -c:a copy -shortest output.mkv
#ffmpeg -framerate 30 -i frame_%06d_x2.png -i audio.m4a -c:v libaom-av1 -cpu-used 2 -crf 10 -b:v 0 -pix_fmt yuv420p10le -c:a copy -shortest output.mkv

#for f in *.png; do convert "$f" -filter Point -resize 500% -fx "i%5==2 && j%5==2 ? p[0,0] : p[0,0]*(14.67/15.67) + (p[-1,0]+p[1,0]+p[0,-1]+p[0,1])*(0.25/15.67)" "${f%.png}_ev.png"; done

# Python can read variables without global but cannot modifiy them..
'''
x = 10  # Global variable
def my_function():
    print(x)  # This WORKS - Python can READ global variables!
'''
import cpuinfo
import datetime
import gc
import glob
import json
import math
import numpy as np
import pickle
import psutil
from pyadl import ADLManager
import pyperf
import os
import random
import subprocess
import sys
import tempfile
import time
import wmi
from memory_profiler import profile
from multiprocessing import shared_memory
from datetime import datetime
from multiprocessing import Pool
from PIL import Image
from sympy import symbols as sym
from sympy import Eq, solve
from random import randint
from rich.progress import track
Image.MAX_IMAGE_PIXELS = None
def loads(file_name, i=None):
    io = {}
    if i != None:
        if os.path.exists(file_name) == False:
            dumps(file_name, io)
    try:
        if os.path.exists(file_name) == True:
            while True:
                try:
                    with open(file_name, "r") as file:
                        io = json.load(file)
                        break
                except IOError:
                    print("File Waiting:", file_name)
                    time.sleep(1)
    except Exception as e:
        print("Issues with:", file_name, e)
    return (io)
def dumps(file_name, data, i=None):
    if i != None:
        if i == 'Clean':
            if os.path.exists(file_name) == True:
                os.remove(file_name)
        else:
            file_name = os.path.join(i, file_name)
    try:
        if len(data) == 0:
            print('File is empty!:', file_name)
    except:
        pass
    with open(file_name, "w") as config:
        json.dump(data, config, indent=4)
def closest_list(number, v, i=None):
    try:
        if i != None:
            a = v.values()
            n = 0
            n_n = 0
            if number not in a:
                for line in a:
                    u = ratio(number, line)
                    if u > n:
                        n = u
                        n_n = line
                number = n_n
            print(number)
            for line in v:
                if float(number) == float(v.get(line)):
                    return(line)
        io = {}
        o = []
        for line in v:
            x = abs(line - number)
            o.append(x)
            io[x] = (line)
        y = min(o)
        return(io.get(y))
    except Exception as e:
        print('Closest List Issues:', e)
def pixel_mean(n1):
    try:
        m1 = (sum(n1) / len(n1))
        odd = max(n1, key=lambda x: abs(x - m1))
        n1.remove(odd)
        return(n1)
    except Exception as e:
        print('Pixel Mean Issues:', e)
def pixel_blender(x):
    try:
        # x is lists of lists
        #x = list(set(x))
        if len(x) == 1:
            return(x[0])
        if len(set(tuple(pb) for pb in x)) == 1:
            return (x[0])
        r_x = []
        g_x = []
        b_x = []
        for line in x:
            r_x.append(line[0])
            g_x.append(line[1])
            b_x.append(line[2])
        if len(x) > 2:
            r_x = pixel_mean(r_x)
            g_x = pixel_mean(g_x)
            b_x = pixel_mean(b_x)
        oa_r = (sum(r_x) / len(r_x))
        oa_g = (sum(g_x) / len(g_x))
        oa_b = (sum(b_x) / len(b_x))
        oa = [oa_r, oa_g, oa_b]
        oa = [round(x) if isinstance(x, float) else x for x in oa]
        return(oa)
    except Exception as e:
        print('Pixel Blender Issues:', e, x)
        input('Stopped')
def pixel_shader(n1, n2):
    try:
        #print('N1:', n1)
        #print('N2:', n2)
        n1_r = n1[0]
        n1_g = n1[1]
        n1_b = n1[2]

        n2_r = n2[0]
        n2_g = n2[1]
        n2_b = n2[2]

        d_r = abs(n1_r - n2_r)
        d_g = abs(n1_g - n2_g)
        d_b = abs(n1_b - n2_b)
        
        r_max = (d_r * .625)
        r_min = (d_r * .375)
        g_max = (d_g * .625)
        g_min = (d_g * .375)
        b_max = (d_b * .625)
        b_min = (d_b * .375)

        if n1_r > n2_r:
            n3_r = (n1_r - r_min)
            n4_r = (n1_r - r_max)
        else:
            n3_r = (n2_r - r_max)
            n4_r = (n2_r - r_min)
        if n1_g > n2_g:
            n3_g = (n1_g - g_min)
            n4_g = (n1_g - g_max)
        else:
            n3_g = (n2_g - g_max)
            n4_g = (n2_g - g_min)
        if n1_b > n2_b:
            n3_b = (n1_b - b_min)
            n4_b = (n1_b - b_max)
        else:
            n3_b = (n2_b - b_max)
            n4_b = (n2_b - b_min)
        
        n3 = [n3_r, n3_g, n3_b]
        n4 = [n4_r, n4_g, n4_b]
        return(n3, n4)
    except Exception as e:
        print('Pixel Shader Issues:', e)
def pixel_shader_6x6(n1, n2):
    try:
        # print('N1:', n1)
        # print('N2:', n2)
        n1_r = n1[0]
        n1_g = n1[1]
        n1_b = n1[2]

        n2_r = n2[0]
        n2_g = n2[1]
        n2_b = n2[2]

        m_r = ((n1_r + n2_r) / 2)
        m_g = ((n1_g + n2_g) / 2)
        m_b = ((n1_b + n2_b) / 2)

        n3_r = ((n1_r * .7) + (m_r * .3))
        n3_g = ((n1_g * .7) + (m_g * .3))
        n3_b = ((n1_b * .7) + (m_b * .3))

        n4_r = ((n1_r * .3) + (m_r * .7))
        n4_g = ((n1_g * .3) + (m_g * .7))
        n4_b = ((n1_b * .3) + (m_b * .7))

        n5_r = ((n2_r * .3) + (m_r * .7))
        n5_g = ((n2_g * .3) + (m_g * .7))
        n5_b = ((n2_b * .3) + (m_b * .7))

        n6_r = ((n2_r * .7) + (m_r * .3))
        n6_g = ((n2_g * .7) + (m_g * .3))
        n6_b = ((n2_b * .7) + (m_b * .3))

        n3 = [n3_r, n3_g, n3_b]
        n4 = [n4_r, n4_g, n4_b]
        n5 = [n5_r, n5_g, n5_b]
        n6 = [n6_r, n6_g, n6_b]
        return (n3, n4, n5, n6)
    except Exception as e:
        print('Pixel Shader Issues:', e)
def pixel_trap(n1, n2, n3, n4):
    try:
        #Chinompa
        trap_r = ((n1[0] + n2[0] + n3[0] + n4[0]) / 4)
        trap_g = ((n1[1] + n2[1] + n3[1] + n4[1]) / 4)
        trap_b = ((n1[2] + n2[2] + n3[2] + n4[2]) / 4)
        trap_pixel = [trap_r, trap_g, trap_b]
        return(trap_pixel)
    except Exception as e:
        print('Pixel Trap Issues:', e)
def pixel_trap_half(n1, n2):
    try:
        #Chinompa
        trap_half_r = ((n1[0] * .5) + (n2[0] * .5))
        trap_half_g = ((n1[1] * .5) + (n2[1] * .5))
        trap_half_b = ((n1[2] * .5) + (n2[2] * .5))
        trap_pixel_half = [trap_r, trap_g, trap_b]
        return(trap_pixel_half)
    except Exception as e:
        print('Pixel Trap Issues:', e)
def pixel_middle(n1):
    try:
        pixel_middle_r = []
        pixel_middle_g = []
        pixel_middle_b = []
        for line in n1:
            pixel_middle_r.append(line[0])
            pixel_middle_g.append(line[1])
            pixel_middle_b.append(line[2])
        middle_r = (sum(pixel_middle_r) / len(pixel_middle_r))
        middle_g = (sum(pixel_middle_g) / len(pixel_middle_g))
        middle_b = (sum(pixel_middle_b) / len(pixel_middle_b))
        middle_pixel = [middle_r, middle_g, middle_b]
        return(middle_pixel)
    except Exception as e:
        print('Pixel Middle:', e)
def pixel_maker(pixel1, pixel2, pixel3, pixel4):
    try:
        #print('Pixel Maker! - Anthony R Shively')
        #F = (4 of A, 2 of D, 2 of M, 1 of P)
        #G = (2 of A, 4 of D, 1 of M, 2 of P)
        #J = (2 of A, 1 of D, 4 of M, 2 of P)
        #K = (1 of A, 2 of D, 2 of M, 4 of P)
        #new_pixel = [128, 128, 128]
        #black = [0, 0, 0]
        #white = [255, 255, 255]
        #a = [114, 109, 89]
        #p0 = x[0][1]
        #p1 = x[1][1]
        #p2 = x[2][1]
        #p3 = x[3][1]
        #print(x)
        #print([p0, p1, p2, p3])
        a_r = int(pixel1[0])
        a_g = int(pixel1[1])
        a_b = int(pixel1[2])

        d_r = int(pixel2[0])
        d_g = int(pixel2[1])
        d_b = int(pixel2[2])

        m_r = int(pixel3[0])
        m_g = int(pixel3[1])
        m_b = int(pixel3[2])

        p_r = int(pixel4[0])
        p_g = int(pixel4[1])
        p_b = int(pixel4[2])

        a = [a_r, a_g, a_b]

        # a = [240, 255, 255]
        # d = [241, 255, 255]
        #Version 3 were pulling the color down in this bad pixel math
        #b = [((a_r * .625) + (d_r * .325)), ((a_g * .625) + (d_g * .325)), ((a_b * .625) + (d_b * .325))]
        #b = [228, 242, 242]
        #Version 1 uses b_1 synthetic and then b It is also not that great.
        #b_1 = [((a[0] + f[0]) / 2), ((a[1] + f[1]) / 2), ((a[2] + f[2]) / 2)]
        #b = [((a[0] + f[0] + c_1[0]) / 3), ((a[1] + f[1] + c_1[1]) / 3), ((a[2] + f[2] + c_1[2]) / 3)]

        #b = [((a_r * .625) + (d_r * .325)), ((a_g * .625) + (d_g * .325)), ((a_b * .625) + (d_b * .325))]

        #c = [((a_r * .325) + (d_r * .625)), ((a_g * .325) + (d_g * .625)), ((a_b * .325) + (d_b * .625))]
        d = [d_r, d_g, d_b]
        #e = [((a_r * .625) + (m_r * .325)), ((a_g * .625) + (m_g * .325)), ((a_b * .625) + (m_b * .325))]
        #h = [((p_r * .325) + (d_r * .625)), ((p_g * .325) + (d_g * .625)), ((p_b * .325) + (d_b * .625))]
        #i = [((a_r * .325) + (m_r * .625)), ((a_g * .325) + (m_g * .625)), ((a_b * .325) + (m_b * .625))]
        #l = [((p_r * .625) + (d_r * .325)), ((p_g * .625) + (d_g * .325)), ((p_b * .625) + (d_b * .325))]
        m = [m_r, m_g, m_b]
        #n = [((m_r * .625) + (p_r * .325)), ((m_g * .625) + (p_g * .325)), ((m_b * .625) + (p_b * .325))]
        #o = [((m_r * .325) + (p_r * .625)), ((m_g * .325) + (p_g * .625)), ((m_b * .325) + (p_b * .625))]
        p = [p_r, p_g, p_b]

        e, i = pixel_shader(a, m)

        b, c = pixel_shader(a, d)
        h, l = pixel_shader(d, p)
        n, o = pixel_shader(m, p)

        oa = pixel_blender([a, d, m, p])

        b_r = b[0]
        b_g = b[1]
        b_b = b[2]

        c_r = c[0]
        c_g = c[1]
        c_b = c[2]

        h_r = h[0]
        h_g = h[1]
        h_b = h[2]

        l_r = l[0]
        l_g = l[1]
        l_b = l[2]

        o_r = o[0]
        o_g = o[1]
        o_b = o[2]

        n_r = n[0]
        n_g = n[1]
        n_b = n[2]

        i_r = i[0]
        i_g = i[1]
        i_b = i[2]

        e_r = e[0]
        e_g = e[1]
        e_b = e[2]

        oa_r = oa[0]
        oa_g = oa[1]
        oa_b = oa[2]

        f1 = [((((oa_r + a_r) / 2) + b_r + e_r) / 3), ((((oa_g + a_g) / 2) + b_g + e_g) / 3), ((((oa_b + a_b) / 2) + b_b + e_b) / 3)]
        g1 = [((((oa_r + d_r) / 2) + c_r + h_r) / 3), ((((oa_g + d_g) / 2) + c_g + h_g) / 3), ((((oa_b + d_b) / 2) + c_b + h_b) / 3)]
        j1 = [((((oa_r + m_r) / 2) + i_r + n_r) / 3), ((((oa_g + m_g) / 2) + i_g + n_g) / 3), ((((oa_b + m_b) / 2) + i_b + n_b) / 3)]
        k1 = [((((oa_r + p_r) / 2) + o_r + l_r) / 3), ((((oa_g + p_g) / 2) + o_g + l_g) / 3), ((((oa_b + p_b) / 2) + o_b + l_b) / 3)]

        #f1 = [(((oa_r + a_r) * .225) + ((b_r + e_r) * .775)), (((oa_g + a_g) * .225) + ((b_g + e_g) * .775)), (((oa_b + a_b) * .225) + ((b_b + e_b) * .775))]
        #g1 = [(((oa_r + d_r) * .225) + ((c_r + h_r) * .775)), (((oa_g + d_g) * .225) + ((c_g + h_g) * .775)), (((oa_b + d_b) * .225) + ((c_b + h_b) * .775))]
        #j1 = [(((oa_r + m_r) * .225) + ((i_r + n_r) * .775)), (((oa_g + m_g) * .225) + ((i_g + n_g) * .775)), (((oa_b + m_b) * .225) + ((i_b + n_b) * .775))]
        #k1 = [(((oa_r + p_r) * .225) + ((o_r + l_r) * .775)), (((oa_g + p_g) * .225) + ((o_g + l_g) * .775)), (((oa_b + p_b) * .225) + ((o_b + l_b) * .775))]

        j1_r = j1[0]
        j1_g = j1[1]
        j1_b = j1[2]

        g1_r = g1[0]
        g1_g = g1[1]
        g1_b = g1[2]

        f1_r = f1[0]
        f1_g = f1[1]
        f1_b = f1[2]

        k1_r = k1[0]
        k1_g = k1[1]
        k1_b = k1[2]

        f2 = [((b_r + e_r) / 2), ((b_g + e_g) / 2), ((b_b + e_b) / 2)]
        g2 = [((c_r + h_r) / 2), ((c_g + h_g) / 2), ((c_b + h_b) / 2)]
        j2 = [((i_r + n_r) / 2), ((i_g + n_g) / 2), ((i_b + n_b) / 2)]
        k2 = [((o_r + l_r) / 2), ((o_g + l_g) / 2), ((o_b + l_b) / 2)]

        f3 = [((j1_r + b_r + e_r + g1_r) / 4), ((j1_g + b_g + e_g + g1_g) / 4), ((j1_b + b_b + e_b + g1_b) / 4)]
        g3 = [((f1_r + c_r + h_r + k1_r) / 4), ((f1_g + c_g + h_g + k1_g) / 4), ((f1_b + c_b + h_b + k1_b) / 4)]
        j3 = [((f1_r + n_r + i_r + k1_r) / 4), ((f1_g + n_g + i_g + k1_g) / 4), ((f1_b + n_b + i_b + k1_b) / 4)]
        k3 = [((g1_r + l_r + o_r + j1_r) / 4), ((g1_g + l_g + o_g + j1_g) / 4), ((g1_b + l_b + o_b + j1_b) / 4)]

        f4 = pixel_blender([b, e, g1, j1])
        g4 = pixel_blender([c, h, k1, f1])
        j4 = pixel_blender([i, n, k1, f1])
        k4 = pixel_blender([l, o, g1, j1])

        f5 = [(((a_r * 4) + (d_r * 2) + (m_r * 2) + (p_r * 1)) / 9), (((a_g * 4) + (d_g * 2) + (m_g * 2) + (p_g * 1)) / 9), (((a_b * 4) + (d_b * 2) + (m_b * 2) + (p_b * 1)) / 9)]
        g5 = [(((a_r * 2) + (d_r * 4) + (m_r * 1) + (p_r * 2)) / 9), (((a_g * 2) + (d_g * 4) + (m_g * 1) + (p_g * 2)) / 9), (((a_b * 2) + (d_b * 4) + (m_b * 1) + (p_b * 2)) / 9)]
        j5 = [(((a_r * 2) + (d_r * 1) + (m_r * 4) + (p_r * 2)) / 9), (((a_g * 2) + (d_g * 1) + (m_g * 4) + (p_g * 2)) / 9), (((a_b * 2) + (d_b * 1) + (m_b * 4) + (p_b * 2)) / 9)]
        k5 = [(((a_r * 1) + (d_r * 2) + (m_r * 2) + (p_r * 4)) / 9), (((a_g * 1) + (d_g * 2) + (m_g * 2) + (p_g * 4)) / 9), (((a_b * 1) + (d_b * 2) + (m_b * 2) + (p_b * 4)) / 9)]
        
        f6, k6 = pixel_shader(a, p)
        j6, g6 = pixel_shader(m, d)

        f7, g7 = pixel_shader(e, h)
        j7, k7 = pixel_shader(i, l)

        f8, j8 = pixel_shader(b, n)
        g8, k8 = pixel_shader(c, o)

        f = pixel_blender([f1, f2, f3, f4, f5, f6, f7, f8])
        g = pixel_blender([g1, g2, g3, g4, g5, g6, g7, g8])
        j = pixel_blender([j1, j2, j3, j4, j5, j6, j7, j8])
        k = pixel_blender([k1, k2, k3, k4, k5, k6, k7, k8])
        block_v = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
        return(block_v)
    except Exception as e:
        print('Pixel Maker Issues:', e)
def pixel_shader_x8(n1, n2):
    try:
        # print('N1:', n1)
        # print('N2:', n2)
        n1_r = n1[0]
        n1_g = n1[1]
        n1_b = n1[2]

        n2_r = n2[0]
        n2_g = n2[1]
        n2_b = n2[2]

        #n1_r, n1_g, n1_b = float(n1[0]), float(n1[1]), float(n1[2])
        #n2_r, n2_g, n2_b = float(n2[0]), float(n2[1]), float(n2[2])

        m_r = ((n1_r * .5) + (n2_r * .5))
        m_g = ((n1_g * .5) + (n2_g * .5))
        m_b = ((n1_b * .5) + (n2_b * .5))

        n3_r = ((n1_r * (6 / 7)) + (m_r * (1 / 7)))
        n3_g = ((n1_g * (6 / 7)) + (m_g * (1 / 7)))
        n3_b = ((n1_b * (6 / 7)) + (m_b * (1 / 7)))

        n4_r = ((n1_r * (4 / 7)) + (m_r * (3 / 7)))
        n4_g = ((n1_g * (4 / 7)) + (m_g * (3 / 7)))
        n4_b = ((n1_b * (4 / 7)) + (m_b * (3 / 7)))

        n5_r = ((n1_r * (2 / 7)) + (m_r * (5 / 7)))
        n5_g = ((n1_g * (2 / 7)) + (m_g * (5 / 7)))
        n5_b = ((n1_b * (2 / 7)) + (m_b * (5 / 7)))

        # Middle

        n6_r = ((n2_r * (1 / 7)) + (m_r * (6 / 7)))
        n6_g = ((n2_g * (1 / 7)) + (m_g * (6 / 7)))
        n6_b = ((n2_b * (1 / 7)) + (m_b * (6 / 7)))

        n7_r = ((n2_r * (3 / 7)) + (m_r * (4 / 7)))
        n7_g = ((n2_g * (3 / 7)) + (m_g * (4 / 7)))
        n7_b = ((n2_b * (3 / 7)) + (m_b * (4 / 7)))

        n8_r = ((n2_r * (5 / 7)) + (m_r * (2 / 7)))
        n8_g = ((n2_g * (5 / 7)) + (m_g * (2 / 7)))
        n8_b = ((n2_b * (5 / 7)) + (m_b * (2 / 7)))

        n3 = [n3_r, n3_g, n3_b]
        n4 = [n4_r, n4_g, n4_b]
        n5 = [n5_r, n5_g, n5_b]
        n6 = [n6_r, n6_g, n6_b]
        n7 = [n7_r, n7_g, n7_b]
        n8 = [n8_r, n8_g, n8_b]
        # 0 (3 4 5 - 6 7 8) 2
        # A (B C D - E F G) H
        return (n3, n4, n5, n6, n7, n8)
    except Exception as e:
        print('Pixel Shader Issues:', e)
def parabolas():
    try:
        pass
    except Exception as e:
        print('Parabola Issue:', e)
def pixel_diag_x3(n1, n2):
    try:
        n1_r = n1[0]
        n1_g = n1[1]
        n1_b = n1[2]

        n2_r = n2[0]
        n2_g = n2[1]
        n2_b = n2[2]

        m_r = ((n1_r * .5) + (n2_r * .5))
        m_g = ((n1_g * .5) + (n2_g * .5))
        m_b = ((n1_b * .5) + (n2_b * .5))

        n3_r = ((n1_r * (6 / 8)) + (n2_r * (2 / 8)))
        n3_g = ((n1_g * (6 / 8)) + (n2_g * (2 / 8)))
        n3_b = ((n1_b * (6 / 8)) + (n2_b * (2 / 8)))

        n4_r = ((n1_r * .5) + (n2_r * .5))
        n4_g = ((n1_g * .5) + (n2_g * .5))
        n4_b = ((n1_b * .5) + (n2_b * .5))

        n5_r = ((n1_r * (2 / 8)) + (n2_r * (6 / 8)))
        n5_g = ((n1_g * (2 / 8)) + (n2_g * (6 / 8)))
        n5_b = ((n1_b * (2 / 8)) + (n2_b * (6 / 8)))

        n3 = [n3_r, n3_g, n3_b]
        n4 = [n4_r, n4_g, n4_b]
        n5 = [n5_r, n5_g, n5_b]
        return(n3, n4, n5)
    except Exception as e:
        print('Pixel Diag x3 Issue:', e)
def pixel_maker_x8(pixel1, pixel2, pixel3, pixel4):
    try:
        #p1 = pixel1
        #p8= pixel2
        #p57 = pixel3
        #p64 = pixel4
        #Here
        #print(type(p1))
        #print(type(p8))
        #print(type(p57))
        #print(type(p64))
        p1 = [int(pixel1[0]), int(pixel1[1]), int(pixel1[2])]
        p8 = [int(pixel2[0]), int(pixel2[1]), int(pixel2[2])]
        p57 = [int(pixel3[0]), int(pixel3[1]), int(pixel3[2])]
        p64 = [int(pixel4[0]), int(pixel4[1]), int(pixel4[2])]
        #input('Stopped')

        oa = pixel_blender([p1, p8, p57, p64])

        p10a, p19, p28 = pixel_diag_x3(p1, oa)
        p50a, p43, p36 = pixel_diag_x3(p57, oa)
        p55, p46, p37 = pixel_diag_x3(p64, oa)
        p15a, p22, p29 = pixel_diag_x3(p8, oa)

        p19a, p20a, p21a, p22a, p27a, p28a, p29b, p30a, p35a, p36b, p37b, p38a, p43a, p44a, p45a, p46a = pixel_maker(p19, p22, p43, p46)[0:16]

        p2, p3, p4, p5, p6, p7 = pixel_shader_x8(p1, p8)
        p9, p17, p25, p33, p41, p49 = pixel_shader_x8(p1, p57)
        p16, p24, p32, p40, p48, p56 = pixel_shader_x8(p8, p64)
        p58, p59, p60, p61, p62, p63 = pixel_shader_x8(p57, p64)

        p10b, p19b, p28b, p37c, p46b, p55a = pixel_shader_x8(p1, p64)
        p50b, p43b, p36c, p29c, p22b, p15b = pixel_shader_x8(p57, p8)

        p33a, p34, p35b, p36a, p41a, p42, p43c, p44b, p49a, p50c, p51, p52, p57, p58a, p59a, p60a = pixel_maker(p33, p36, p57, p60)[0:16]
        p1, p2a, p3a, p4a, p9a, p10c, p11, p12, p17a, p18, p19c, p20b, p25a, p26, p27b, p28c = pixel_maker(p1, p4, p25, p28)[0:16]
        p5a, p6a, p7a, p8, p13, p14, p15c, p16a, p21b, p22c, p23, p24a, p29a, p30b, p31, p32a = pixel_maker(p1, p8, p29, p32)[0:16]
        p37a, p38b, p39, p40a, p45b, p46c, p47, p48a, p53, p54, p55b, p56a, p61a, p62a, p63a, p64 = pixel_maker(p37, p40, p61, p64)[0:16] #

        #p1
        p2 = pixel_blender([p2, p2a])
        p3 = pixel_blender([p3, p3a])
        p4 = pixel_blender([p4, p4a])
        p5 = pixel_blender([p5, p5a])
        p6 = pixel_blender([p6, p6a])
        p7 = pixel_blender([p7, p7a])
        #p8
        p9 = pixel_blender([p9, p9a])
        p10 = pixel_blender([p10a, p10b, p10c])
        #p11 = pixel_blender([p11, ])
        #p12 = pixel_blender([p12, ])
        #p13 = pixel_blender([p13, ])
        #p14 = pixel_blender([p14, ])
        p15 = pixel_blender([p15a, p15b, p15c])
        p16 = pixel_blender([p16, p16a])
        p17 = pixel_blender([p17, p17a])
        #p18 = pixel_blender([p18])
        p19 = pixel_blender([p19, p19a, p19b, p19c])
        p20 = pixel_blender([p20a, p20b])
        p21 = pixel_blender([p21a, p21b])
        p22 = pixel_blender([p22, p22a, p22b, p22c])
        #p23 = pixel_blender([p23, ])
        p24 = pixel_blender([p24, p24a])
        p25 = pixel_blender([p25, p25a])
        #p26 = pixel_blender([p26])
        p27 = pixel_blender([p27a, p27b])
        p28 = pixel_blender([p28, p28a, p28b, p28c])
        p29 = pixel_blender([p29, p29a, p29b, p29c])
        p30 = pixel_blender([p30a, p30b])
        #p31 = pixel_blender([p31, ])
        p32 = pixel_blender([p32, p32a])
        p33 = pixel_blender([p33, p33a])
        #p34 = pixel_blender([p34, ])
        p35 = pixel_blender([p35a, p35b])
        p36 = pixel_blender([p36a, p36b, p36c])
        p37 = pixel_blender([p37a, p37b, p37c])
        p38 = pixel_blender([p38a, p38b])
        #p39 = pixel_blender([p39a, ])
        p40 = pixel_blender([p40, p40a])
        p41 = pixel_blender([p41, p41a])
        #p42 = pixel_blender([p42])
        p43 = pixel_blender([p43, p43a, p43b, p43c])
        p44 = pixel_blender([p44a, p44b])
        p45 = pixel_blender([p45a, p45b])
        p46 = pixel_blender([p46, p46a, p46b, p46c])
        #p47 = pixel_blender([p47, ])
        p48 = pixel_blender([p48, p48a])
        p49 = pixel_blender([p49, p49a])
        p50 = pixel_blender([p50a, p50b, p50c])
        #p51 = pixel_blender([p51])
        #p52 = pixel_blender([p52])
        #p53 = pixel_blender([p53])
        #p54 = pixel_blender([p54])
        p55 = pixel_blender([p55, p55a, p55b])
        p56 = pixel_blender([p56, p56a])
        #p57 = pixel_blender([p57])
        p58 = pixel_blender([p58, p58a])
        p59 = pixel_blender([p59, p59a])
        p60 = pixel_blender([p60, p60a])
        p61 = pixel_blender([p61, p61a])
        p62 = pixel_blender([p62, p62a])
        p63 = pixel_blender([p63, p63a])
        #p64 = pixel_blender([p64])

        block_v = [p1, p2, p3, p4, p5, p6, p7, p8,
                   p9, p10, p11, p12, p13, p14, p15, p16,
                   p17, p18, p19, p20, p21, p22, p23, p24,
                   p25, p26, p27, p28, p29, p30, p31, p32,
                   p33, p34, p35, p36, p37, p38, p39, p40,
                   p41, p42, p43, p44, p45, p46, p47, p48,
                   p49, p50, p51, p52, p53, p54, p55, p56,
                   p57, p58, p59, p60, p61, p62, p63, p64]
        #print(block_v)
        #input('Stopped')
        return(block_v)
    except Exception as e:
        print('Pixel Maker Issues:', e)
        input('Hmm')
def pixel_maker_6x6(pixel1, pixel2, pixel3, pixel4):
    try:
        a = pixel1
        f = pixel2
        e1 = pixel3
        j1 = pixel4

        b, c, d, e = pixel_shader_6x6(a, f)
        g, m, s, y = pixel_shader_6x6(a, e1)
        l, r, xa, d1 = pixel_shader_6x6(f, j1)
        f1, g1, h1, i1 = pixel_shader_6x6(e1, j1)

        h_1, o_1, v_1, c1_1 = pixel_shader_6x6(a, j1)
        z_1, u_1, p_1, k_1 = pixel_shader_6x6(e1, f)
        h_2, i_1, j_1, k_2 = pixel_shader_6x6(g, l)
        n_1, o_2, p_2, q_1 = pixel_shader_6x6(m, r)
        t_1, u_2, v_2, w_1 = pixel_shader_6x6(s, xa)
        z_2, a1_1, b1_1, c1_2 = pixel_shader_6x6(y, d1)
        h_3, n_2, t_2, z_3 = pixel_shader_6x6(b, f1)
        i_2, o_3, u_3, a1_2 = pixel_shader_6x6(c, g1)
        j_2, p_3, v_3, b1_2 = pixel_shader_6x6(d, h1)
        k_3, q_2, w_2, c1_3 = pixel_shader_6x6(e, i1)

        h = pixel_blender([h_1, h_2, h_3])
        k = pixel_blender([k_1, k_2, k_3])
        o = pixel_blender([o_1, o_2, o_3])
        p = pixel_blender([p_1, p_2, p_3])
        u = pixel_blender([u_1, u_2, u_3])
        v = pixel_blender([v_1, v_2, v_3])
        z = pixel_blender([z_1, z_2, z_3])
        c1 = pixel_blender([c1_1, c1_2, c1_3])

        i = pixel_middle([i_1, i_2])
        j = pixel_middle([j_1, j_2])
        n = pixel_middle([n_1, n_2])
        q = pixel_middle([q_1, q_2])
        t = pixel_middle([t_1, t_2])
        w = pixel_middle([w_1, w_2])
        a1 = pixel_middle([a1_1, a1_2])
        b1 = pixel_middle([b1_1, b1_2])

        b = [int(round(x)) for x in b]
        c = [int(round(x)) for x in c]
        d = [int(round(x)) for x in d]
        e = [int(round(x)) for x in e]
        g = [int(round(x)) for x in g]
        h = [int(round(x)) for x in h]
        i = [int(round(x)) for x in i]
        j = [int(round(x)) for x in j]
        k = [int(round(x)) for x in k]
        l = [int(round(x)) for x in l]
        m = [int(round(x)) for x in m]
        n = [int(round(x)) for x in n]
        o = [int(round(x)) for x in o]
        p = [int(round(x)) for x in p]
        q = [int(round(x)) for x in q]
        r = [int(round(x)) for x in r]
        s = [int(round(x)) for x in s]
        t = [int(round(x)) for x in t]
        u = [int(round(x)) for x in u]
        v = [int(round(x)) for x in v]
        w = [int(round(x)) for x in w]
        xa = [int(round(x)) for x in xa]
        y = [int(round(x)) for x in y]
        z = [int(round(x)) for x in z]

        a1 = [int(round(x)) for x in a1]
        b1 = [int(round(x)) for x in b1]
        c1 = [int(round(x)) for x in c1]
        d1 = [int(round(x)) for x in d1]
        e1 = [int(round(x)) for x in e1]
        f1 = [int(round(x)) for x in f1]
        g1 = [int(round(x)) for x in g1]
        h1 = [int(round(x)) for x in h1]
        i1 = [int(round(x)) for x in i1]
        j1 = [int(round(x)) for x in j1]

        block_v = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, xa, y, z, a1, b1, c1, d1, e1, f1, g1, h1, i1, j1]
        return (block_v)
    except Exception as e:
        print('Pixel Maker Issues:', e)
def mapper():
    try:
        h, w = arr.shape[:2]
        if h % 2 == 0:
            pass
        else:
            h = (h - 1)
        if w % 2 == 0:
            pass
        else:
            w = (w - 1)
        map = {}
        block_counter = 0
        for by in range(0, h, 2):
            for bx in range(0, w, 2):
                block_counter += 1
                block_name = f'block_{block_counter}'
                block_coords = []
                for dy in range(2):
                    for dx in range(2):
                        y, x = by + dy, bx + dx
                        if y < h and x < w:
                            block_coords.append([x, y])
                map[block_name] = block_coords
        return (map, h, w)
    except Exception as e:
        print('Mapper Issues:', e)
def mapper_to_array():
    try:
        positions = [
            (0, 0), (1, 0), (2, 0), (3, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),
            (0, 3), (1, 3), (2, 3), (3, 3)
        ]
        desc = ("Processing..." + 'Core Using: ' + str(cores))
        #for block_name, coords in track(map.items(), description=desc):
        for block_name, coords in map.items():
            try:
                x0, y0 = coords[0]
                x1, y1 = coords[1]
                x2, y2 = coords[2]
                x3, y3 = coords[3]
                pixel_a = arr[y0, x0]
                pixel_d = arr[y1, x1]
                pixel_m = arr[y2, x2]
                pixel_p = arr[y3, x3]
                pm = pixel_maker(pixel_a, pixel_d, pixel_m, pixel_p)
                block_num = int(block_name.split('_')[1]) - 1
                block_x = ((block_num % blocks_wide) * 4)
                block_y = ((block_num // blocks_wide) * 4)
                for idx, (dx, dy) in enumerate(positions):
                    r, g, b = pm[idx]
                    px = block_x + dx
                    py = block_y + dy
                    if px < output_w and py < output_h:
                        full_arr[py, px] = [r, g, b]
            except Exception as e:
                print('Mapper Array Issues To Full Array:', e)
    except Exception as e:
        print('Mapper To Array Issues:', e)
def mapper_to_array2():
    try:
        pixel_dic = {}
        desc = ("Processing..." + 'Core Using: ' + str(cores))
        #for block_name, coords in track(map.items(), description=desc):
        #track(map.items(), description=desc):
        #for block_name, coords in map.items():
        #for block_name, coords in track(map.items(), description=desc):
        for block_name, coords in map.items():
            try:
                x0, y0 = coords[0]
                x1, y1 = coords[1]
                x2, y2 = coords[2]
                x3, y3 = coords[3]
                pixel_a = arr[y0, x0]
                pixel_d = arr[y1, x1]
                pixel_m = arr[y2, x2]
                pixel_p = arr[y3, x3]
                pixel_dic[block_name] = [pixel_a, pixel_d, pixel_m, pixel_p]
            except Exception as e:
                print('Mapper Array 2 Issues To Full Array:', e)
        return(pixel_dic)
    except Exception as e:
        print('Mapper To Array 2 Issues:', e)
#def process_batch(batch):
#return {key: pixel_maker_x8(*value) for key, value in batch.items()}
def process_batch(batch):
    return {key: pixel_maker_x8(*value) for key, value in batch.items()}
def process_batch_x2(batch):
    return {key: pixel_maker(*value) for key, value in batch.items()}
def mapper_to_array_single():
    try:
        positions = [
            (0, 0), (1, 0), (2, 0), (3, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
            (0, 2), (1, 2), (2, 2), (3, 2),
            (0, 3), (1, 3), (2, 3), (3, 3)
        ]
        desc = ("Processing..." + 'Core Using: 1')
        for block_name, coords in track(map.items(), description=desc):
            try:
                x0, y0 = coords[0]
                x1, y1 = coords[1]
                x2, y2 = coords[2]
                x3, y3 = coords[3]
                pixel_a = arr[y0, x0]
                pixel_d = arr[y1, x1]
                pixel_m = arr[y2, x2]
                pixel_p = arr[y3, x3]
                pm = pixel_maker(pixel_a, pixel_d, pixel_m, pixel_p)
                block_num = int(block_name.split('_')[1]) - 1
                block_x = ((block_num % blocks_wide) * 4)
                block_y = ((block_num // blocks_wide) * 4)
                for idx, (dx, dy) in enumerate(positions):
                    r, g, b = pm[idx]
                    px = block_x + dx
                    py = block_y + dy
                    if px < output_w and py < output_h:
                        full_arr[py, px] = [r, g, b]
            except Exception as e:
                print('Mapper Array Issues To Full Array:', e)
    except Exception as e:
        print('Mapper To Array Issues:', e)
if __name__ == '__main__':
    try:
        cores = os.cpu_count()
        ram = psutil.virtual_memory()
        cores = psutil.cpu_count(logical=False)
        ram_gb = (ram.available / (1024 ** 3))
        ram_bytes = ((1000000000) * ram_gb)
        folder = "v14 Output"
        folder_comp = folder.replace('Output', 'Compression')
        print('############################################################')
        print('######## Pixel Edit - Anthony R Shively (Ohio, USA) ########')
        print('############################################################')
        print('Note: This version does not support transparency, RGB only.')
        print('Note: Converts Grayscale to RGB')
        l2 = cpuinfo.get_cpu_info()['l2_cache_size']
        l2_mem = (l2 / 1000000)
        l3 = cpuinfo.get_cpu_info()['l3_cache_size']
        l3_mem = (l3 / 1000000)
        print(cores, 'Core L2:', format(l2_mem, ".2f"), 'MB', 'L3:', format(l3_mem, ".2f"), 'MB', 'Available RAM: ', format(ram_gb, ".2f"), 'GB')
        try:
            gpu_name, gpu_bits = subprocess.run(['powershell', '-c', '(gwmi Win32_VideoController).Name,(gwmi Win32_VideoController).CurrentBitsPerPixel'],capture_output=True, text=True).stdout.strip().split('\n')
            print(gpu_name, gpu_bits,'- Bits')
            devices = ADLManager.getInstance().getDevices()
            for device in devices:
                print(f"GPU {device.adapterIndex}: {device.getCurrentTemperature()}°C")
        except:
            pass
        print('')
        v2 = input('Pictures in a Folder? If not press Enter to skip: ')
        if v2 != '':
            location_png = (v2 + '/*.png')
            location_jpg = (v2 + '/*.jpg')
        else:
            location_png = '*.png'
            location_jpg = '*.jpg'
        pics = glob.glob(location_png) + glob.glob(location_jpg)
        pics.sort(key=os.path.getsize)
        pics_have = []
        pics2 = []
        for line in pics:
            if '\\' in line:
                name_x2 = (line.replace((v2+'\\'), '')).replace('.png', '_x2.png')
                name_x8 = (line.replace((v2 + '\\'), '')).replace('.png', '_x8.png')
            else:
                name_x2 = line.replace('.png', '_x2.png')
                name_x8 = line.replace('.png', '_x8.png')
            if os.path.exists(folder + '/' + name_x2) or os.path.exists(folder + '/' + name_x8):
                pics_have.append(line)
            else:
                pics2.append(line)
        pics = pics2
        if len(pics_have) > 0:
            print('Existing Photos in ' + folder + ': ', len(pics_have))
            print('')
        if len(pics) > 20:
            print('Folder Contains A Lot Of Photos To Convert:', len(pics))
            print('')
            pics_min = pics[0]
            pics_max = pics[len(pics) - 1]
            picsx = [pics_min, pics_max]
            for f in picsx:
                img = Image.open(f)
                width, height = img.size
                block_size = ((width * height) / 4)
                output_size = ((block_size * 1435) / 1000000)
                print(f, '(', width, 'x', height, ')', 'Block Size:', block_size, '( ~Est MB:', output_size, ')')
        else:
            for f in pics:
                img = Image.open(f)
                width, height = img.size
                block_size = ((width * height) / 4)
                output_size = ((block_size * 1435) / 1000000)
                print(f, '(', width, 'x', height, ')', 'Block Size:', block_size, '( ~Est MB:', output_size, ')')
        print('')
        print('Types: x2, x8 (Use x2 as x8 is blocky)')
        print('Types: comp (Compression)')
        v1 = input('Type: ')
        v3 = ('_' + v1 + '.png')
        print('')
        batch_optimizer_a = []
        batch_optimizer_b = []
        batch_time = {}
        for f in track(pics, description="Processing images..."):
            with open(f) as file:
                iox = {}
                if '.png' in f:
                    img_mod = (f.replace('.png', v3)).replace(v2+'\\', '')
                if '.jpg' in f:
                    img_mod = (f.replace('.jpg', v3)).replace(v2+'\\', '')
                img = Image.open(f).convert('RGB')
                arr = np.array(img)
                blocks_wide, blocks_tall = img.size
                try:
                    while True:
                        temp = ADLManager.getInstance().getDevices()[0].getCurrentTemperature()
                        if temp <= 67:
                            break
                        time.sleep(5)
                except:
                    pass
                if blocks_wide % 2 == 0:
                    pass
                else:
                    blocks_wide = (blocks_wide - 1)
                if blocks_tall % 2 == 0:
                    pass
                else:
                    blocks_tall = (blocks_tall - 1)
                blocks_wide = ((blocks_wide + 1) // 2)
                blocks_tall = ((blocks_tall + 1) // 2)
                if v1 == 'comp':
                    os.makedirs(folder_comp, exist_ok=True)
                    img.save((folder_comp + '/' + img_mod))
                    time.sleep(1)
                    img = Image.open((folder_comp + '/' + img_mod))
                    time.sleep(1)
                    img.save((folder_comp + '/' + img_mod))
                    continue
                elif v1 == 'x2':
                    output_w = (blocks_wide * 4)
                    output_h = (blocks_tall * 4)
                elif v1 == 'x8':
                    output_w = (blocks_wide * 8)
                    output_h = (blocks_tall * 8)
                if blocks_wide > 5000 or blocks_tall > 5000:
                    #########################################
                    ############## Single Core ##############
                    #########################################
                    output_w = (blocks_wide * 4)
                    output_h = (blocks_tall * 4)

                    full_arr = np.zeros((output_h, output_w, 3), dtype=np.uint8)

                    height, length = arr.shape[:2]
                    map, h, w = mapper()
                    usage = (sys.getsizeof(map) / 1000000)
                    print("Image:", f, '=>', img_mod, '(', length, 'x', height, ')', format(usage, ".2f"), 'MB')
                    dic = {}

                    process_start = time.time()
                    mapper_to_array()
                    process_end = time.time()

                    saving_start = time.time()
                    for step in track(range(1), description="Saving Image & Compressing PNG..."):
                        img = Image.fromarray(full_arr)
                        # img.save('output.png')
                        os.makedirs(folder, exist_ok=True)
                        img.save((folder + '/' + img_mod), compress_level=9)
                        #time.sleep(1)
                        #img = Image.open((folder + '/' + img_mod))
                        #time.sleep(1)
                        #img.save((folder + '/' + img_mod))
                    saving_stop = time.time()
                    p_time = (abs(process_start - process_end))
                    s_time = (abs(saving_start - saving_stop))
                    print('Processing Time:', p_time, 'Saving Time:', s_time, 'Batches:', 'All')
                else:
                    ############################################
                    ##############   Multi Core   ##############
                    ############################################
                    full_arr = np.zeros((output_h, output_w, 3), dtype=np.uint8)
                    height, length = arr.shape[:2]
                    map, h, w = mapper()
                    usage = (sys.getsizeof(map) / 1000000)
                    print("Image:", f, '=>', img_mod, '(',length, 'x', height,')', format(usage, ".2f"), 'MB')
                    dic = {}
                    batch_time = {}
                    process_start = time.time()
                    pixel_dic = mapper_to_array2()
                    pixel_items = list(pixel_dic.items())
                    del pixel_dic
                    batch_optimizer_a = []
                    batch_optimizer_b = []
                    batches = []
                    len_pixel_items = len(pixel_items)
                    l2_batch_size = round((len_pixel_items / math.sqrt(l2)))
                    l3_batch_size = round((len_pixel_items / math.sqrt(l3)))
                    split_batches = round((len_pixel_items / cores))
                    cache_batches = [l2_batch_size, l3_batch_size, split_batches]
                    core_optimizer = randint(min(cache_batches), max(cache_batches))
                    batch_optimizer_b.append(core_optimizer)
                    if len(batch_optimizer_b) > 100:
                        for i in range(10):
                            batch_optimizer_b = pixel_mean(batch_optimizer_b)
                    batch_size = round((sum(batch_optimizer_b) / len(batch_optimizer_b)))
                    if batch_size == 0:
                        batch_size = 1
                    for i in range(0, len_pixel_items, batch_size):
                        batches.append(dict(pixel_items[i:i + batch_size]))
                    if v1 == 'x2':
                        positions = [
                            (0, 0), (1, 0), (2, 0), (3, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1),
                            (0, 2), (1, 2), (2, 2), (3, 2),
                            (0, 3), (1, 3), (2, 3), (3, 3)
                        ]
                        desc = ("x2 Processing..." + 'Core Using: ' + str(cores))
                        # Batches are given to 8 Cores
                        with Pool(cores) as pl:
                            for batch_result in track(pl.imap_unordered(process_batch_x2, batches), total=len(batches), description=desc):
                                # iox.update(batch_result)
                                for block_name, pm in batch_result.items():
                                    block_num = int(block_name.split('_')[1]) - 1
                                    block_x = ((block_num % blocks_wide) * 4)
                                    block_y = ((block_num // blocks_wide) * 4)
                                    full_arr[block_y:block_y + 4, block_x:block_x + 4] = np.array(pm, dtype=np.uint8).reshape(4, 4, 3)
                        process_end = time.time()
                        saving_start = time.time()
                        #for step in track(range(1), description="Saving Image & Compressing PNG..."):
                        img = Image.fromarray(full_arr)
                        os.makedirs(folder, exist_ok=True)
                        img.save((folder + '/' + img_mod), compress_level=9)
                        saving_stop = time.time()
                        p_time = (abs(process_start - process_end))
                        s_time = (abs(saving_start - saving_stop))
                        print('Processing Time:', format(p_time, ".2f"), 'Saving Time:', format(s_time, ".2f"), 'Batches:', batch_size, 'of', len_pixel_items)
                        if len(batch_optimizer_a) == 0:
                            batch_optimizer_a.append(p_time)
                        avg_worktime = (sum(batch_optimizer_a) / len(batch_optimizer_a))
                        if p_time < avg_worktime:
                            batch_optimizer_a.append(p_time)
                            batch_optimizer_b.append(batch_size)
                            batch_time[p_time] = (batch_size)
                            batch_optimizer_b.append(batch_time.get(min(batch_time.keys())))
                    else:
                        positions = [
                            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1),
                            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3),
                            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
                            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
                            (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)
                        ]
                        desc = ("x8 Processing..." + 'Core Using: ' + str(cores))
                        # Batches are given to 8 Cores
                        with Pool(cores) as pl:
                            for batch_result in track(pl.imap_unordered(process_batch, batches), total=len(batches), description=desc):
                                #iox.update(batch_result)
                                for block_name, pm in batch_result.items():
                                    block_num = int(block_name.split('_')[1]) - 1
                                    block_x = ((block_num % blocks_wide) * 8)
                                    block_y = ((block_num // blocks_wide) * 8)
                                    full_arr[block_y:block_y + 8, block_x:block_x + 8] = np.array(pm, dtype=np.uint8).reshape(8, 8, 3)
                        process_end = time.time()
                        saving_start = time.time()
                        #for step in track(range(1), description="Saving Image & Compressing PNG..."):
                        img = Image.fromarray(full_arr)
                        os.makedirs(folder, exist_ok=True)
                        img.save((folder + '/' + img_mod))
                        #time.sleep(1)
                        #img = Image.open((folder + '/' + img_mod))
                        #time.sleep(1)
                        #img.save((folder + '/' + img_mod))
                        saving_stop = time.time()
                        p_time = (abs(process_start - process_end))
                        s_time = (abs(saving_start - saving_stop))
                        print('Processing Time:', format(p_time, ".2f"), 'Saving Time:', format(s_time, ".2f"), 'Batches:', batch_size, 'of', len_pixel_items)
                        if len(batch_optimizer_a) == 0:
                            batch_optimizer_a.append(p_time)
                        avg_worktime = (sum(batch_optimizer_a) / len(batch_optimizer_a))
                        if p_time < avg_worktime:
                            batch_optimizer_a.append(p_time)
                            batch_optimizer_b.append(batch_size)
                            batch_time[p_time] = (batch_size)
                            batch_optimizer_b.append(batch_time.get(min(batch_time.keys())))
                        gc.collect()
        input('Program Finished...')
    except Exception as e:
        print('Issues:', e)
        input('Error')