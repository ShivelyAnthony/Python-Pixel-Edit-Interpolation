'''A movie is created with many images that are in different
format which cycle through at a certain speed. Astrology pictures
are stacked for dust, clouds, all factors that can cause viewing issues
and the output result would be the best pixels for a single image.'''
#Anthony R Shively Mercer Ohio 1997

#python -m pip install psutil

# Python can read variables without global but cannot modifiy them..
'''
x = 10  # Global variable
def my_function():
    print(x)  # This WORKS - Python can READ global variables!
'''
import datetime
import gc
import glob
import json
import math
import numpy as np
import pickle
import psutil
import os
import random
import subprocess
import sys
import tempfile
import time
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
        r_x = []
        g_x = []
        b_x = []
        for line in x:
            r_x.append(line[0])
            g_x.append(line[1])
            b_x.append(line[2])
        r_m = pixel_mean(r_x)
        r_ma = pixel_mean(r_m)
        g_m = pixel_mean(g_x)
        g_ma = pixel_mean(g_x)
        b_m = pixel_mean(b_x)
        b_ma = pixel_mean(b_x)
        oa_r = (sum(r_ma) / len(r_ma))
        oa_g = (sum(g_ma) / len(g_ma))
        oa_b = (sum(b_ma) / len(b_ma))
        oa = [oa_r, oa_g, oa_b]
        return(oa)
    except Exception as e:
        print('Pixel Blender Issues:', e)
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

        b = [int(round(x)) for x in b]
        c = [int(round(x)) for x in c]
        e = [int(round(x)) for x in e]
        h = [int(round(x)) for x in h]
        i = [int(round(x)) for x in i]
        l = [int(round(x)) for x in l]
        n = [int(round(x)) for x in n]
        o = [int(round(x)) for x in o]
        f = [int(round(x)) for x in f]
        g = [int(round(x)) for x in g]
        j = [int(round(x)) for x in j]
        k = [int(round(x)) for x in k]
        block_v = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p]
        #print('A:', a)
        #print('D:', d)
        #print('M:', m)
        #print('P:', p)

        #print('')
        #print('A:', a)
        #print('B:', b)
        #print('C:', c)
        #print('D:', d)
        #print('E:', e)
        #print('F:', f)
        #print('G:', g)
        #print('H:', h)
        #print('I:', i)
        #print('J:', j)
        #print('K:', k)
        #print('L:', l)
        #print('M:', m)
        #print('N:', n)
        #print('O:', o)
        #print('P:', p)
        #input()
        return(block_v)
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
def mapper_to_array2():
    try:
        pixel_dic = {}
        desc = ("Processing..." + 'Core Using: ' + str(cores))
        #for block_name, coords in track(map.items(), description=desc):
        #track(map.items(), description=desc):
        #for block_name, coords in map.items():
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
                pixel_dic[block_name] = [pixel_a, pixel_d, pixel_m, pixel_p]
            except Exception as e:
                print('Mapper Array 2 Issues To Full Array:', e)
        return(pixel_dic)
    except Exception as e:
        print('Mapper To Array 2 Issues:', e)
def process_batch(batch):
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
        folder = "v11 Output"
        print('############################################################')
        print('######## Pixel Edit - Anthony R Shively (Ohio, USA) ########')
        print('############################################################')
        print('Note: This version does not support transparency, RGB only.')
        print('Note: Converts Grayscale to RGB')
        print(cores, 'Core - Available RAM: ', format(ram_gb, ".2f"), 'GB')
        try:
            gpu_name, gpu_bits = subprocess.run(['powershell', '-c', '(gwmi Win32_VideoController).Name,(gwmi Win32_VideoController).CurrentBitsPerPixel'],capture_output=True, text=True).stdout.strip().split('\n')
            print(gpu_name, gpu_bits,'- Bits')
        except:
            pass
        print('')
        pics = glob.glob('*.png') + glob.glob('*.jpg')
        pics.sort(key=os.path.getsize)
        pics_have = []
        pics2 = []
        for line in pics:
            if os.path.exists(folder + '/' + line.replace('.png', '_mod.png')):
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
        input('Press Enter If Above Looks Correct')
        print('')
        batch_optimizer_a = []
        batch_optimizer_b = []
        batch_time = {}
        for f in pics:
            with open(f) as file:
                iox = {}
                if '.png' in f:
                    img_mod = (f.replace('.png', '_mod.png'))
                if '.jpg' in f:
                    img_mod = (f.replace('.jpg', '_mod.jpg'))
                img = Image.open(f).convert('RGB')
                arr = np.array(img)

                blocks_wide, blocks_tall = img.size
                if blocks_wide > 5000 or blocks_tall > 5000:
                    #########################################
                    ############## Single Core ##############
                    #########################################
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
                        img.save((folder + '/' + img_mod))
                        time.sleep(1)
                        img = Image.open((folder + '/' + img_mod))
                        time.sleep(1)
                        img.save((folder + '/' + img_mod))
                    saving_stop = time.time()
                    p_time = (abs(process_start - process_end))
                    s_time = (abs(saving_start - saving_stop))
                    print('Processing Time:', p_time, 'Saving Time:', s_time, 'Batches:', 'All')
                else:
                    ############################################
                    ##############   Multi Core   ##############
                    ############################################
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
                    output_w = (blocks_wide * 4)
                    output_h = (blocks_tall * 4)
                    full_arr = np.zeros((output_h, output_w, 3), dtype=np.uint8)
                    height, length = arr.shape[:2]
                    map, h, w = mapper()
                    usage = (sys.getsizeof(map) / 1000000)
                    print("Image:", f, '=>', img_mod, '(',length, 'x', height,')', format(usage, ".2f"), 'MB')
                    dic = {}
                    process_start = time.time()
                    pixel_dic = mapper_to_array2()
                    positions = [
                        (0, 0), (1, 0), (2, 0), (3, 0),
                        (0, 1), (1, 1), (2, 1), (3, 1),
                        (0, 2), (1, 2), (2, 2), (3, 2),
                        (0, 3), (1, 3), (2, 3), (3, 3)
                    ]
                    pixel_items = list(pixel_dic.items())
                    del pixel_dic
                    batch_optimizer_a = []
                    batch_optimizer_b = []
                    batch_time = {}

                    ram_bytes = ram.available
                    work_size = (blocks_wide * blocks_tall)
                    max_batches = math.floor(((ram_bytes / work_size) * .8))
                    
                    if len(batch_optimizer_b) > 2:
                        core_sizer = randint(min(batch_optimizer_b), max(batch_optimizer_b))
                        avg_batches = int(((sum(batch_optimizer_b) / len(batch_optimizer_b)) + min(batch_time.keys())) * .5)
                        if (avg_batches + core_sizer) < max_batches and (avg_batches - core_sizer) > 1:
                            batch_size = randint((avg_batches - core_sizer), (avg_batches + core_sizer))
                    else:
                        batch_size = randint(1, max_batches)
                    if len(batch_optimizer_b) > 3:
                        for i in range(20):
                            batch_optimizer_b = pixel_mean(batch_optimizer_b)
                    batches = []
                    len_pixel_items = len(pixel_items)
                    work_load = round(len_pixel_items / cores)
                    if work_load < batch_size:
                        batch_size = work_load
                    for i in range(0, len_pixel_items, batch_size):
                        batches.append(dict(pixel_items[i:i + batch_size]))
                    desc = ("Processing..." + 'Core Using: ' + str(cores))
                    # Batches are given to 8 Cores
                    with Pool(cores) as pl:
                        for batch_result in track(pl.imap_unordered(process_batch, batches), total=len(batches), description=desc):
                            iox.update(batch_result)
                    for block_name, pm in iox.items():
                        block_num = int(block_name.split('_')[1]) - 1
                        block_x = ((block_num % blocks_wide) * 4)
                        block_y = ((block_num // blocks_wide) * 4)
                        for idx, (dx, dy) in enumerate(positions):
                            r, g, b = pm[idx]
                            px = block_x + dx
                            py = block_y + dy
                            if px < output_w and py < output_h:
                                full_arr[py, px] = [r, g, b]
                    process_end = time.time()
                    saving_start = time.time()
                    for step in track(range(1), description="Saving Image & Compressing PNG..."):
                        img = Image.fromarray(full_arr)
                        os.makedirs(folder, exist_ok=True)
                        img.save((folder + '/' + img_mod))
                        time.sleep(1)
                        img = Image.open((folder + '/' + img_mod))
                        time.sleep(1)
                        img.save((folder + '/' + img_mod))
                    saving_stop = time.time()
                    p_time = (abs(process_start - process_end))
                    s_time = (abs(saving_start - saving_stop))
                    print('Processing Time:', p_time, 'Saving Time:', s_time, 'Batches:', batch_size)
                    if len(batch_optimizer_a) == 0:
                        batch_optimizer_a.append(p_time)
                        batch_optimizer_b.append(batch_size)
                    avg_worktime = (sum(batch_optimizer_a) / len(batch_optimizer_a))
                    if p_time < avg_worktime:
                        batch_optimizer_a.append(p_time)
                        batch_optimizer_b.append(batch_size)
                        batch_time[p_time] = (batch_size)
        input('Program Finished...')
    except Exception as e:
        print('Issues:', e)
        input('Error')