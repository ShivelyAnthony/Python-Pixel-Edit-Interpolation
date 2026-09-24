import cpuinfo
import cv2
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
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from sympy import symbols as sym
from sympy import Eq, solve
from memory_profiler import profile
from multiprocessing import shared_memory
from datetime import datetime
from multiprocessing import Pool
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import piexif
from sympy import symbols as sym
from sympy import Eq, solve
from random import randint
from rich.progress import track
Image.MAX_IMAGE_PIXELS = None
'''def pixel_mean(n1):
    try:
        n1 = [float(x) for x in n1]
        m1 = (sum(n1) / len(n1))
        odd = max(n1, key=lambda x: abs(x - m1))
        n1.remove(odd)
        return(n1)
    except Exception as e:
        print('Pixel Mean Issues:', e)'''
def pixel_blender(x):
    try:
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
def pixel_maker_x1(pixel1, pixel2, pixel3, pixel4):
    try:
        a = pixel1
        c = pixel2
        g = pixel3
        i = pixel4
        a_r = int(pixel1[0])
        a_g = int(pixel1[1])
        a_b = int(pixel1[2])
        c_r = int(pixel2[0])
        c_g = int(pixel2[1])
        c_b = int(pixel2[2])
        g_r = int(pixel3[0])
        g_g = int(pixel3[1])
        g_b = int(pixel3[2])
        i_r = int(pixel4[0])
        i_g = int(pixel4[1])
        i_b = int(pixel4[2])
        d = [((a_r * .5) + (g_r * .5)), ((a_g * .5) + (g_g * .5)), ((a_b * .5) + (g_b * .5))] #A/G
        b = [((a_r * .5) + (c_r * .5)), ((a_g * .5) + (c_g * .5)), ((a_b * .5) + (c_b * .5))] #A/C
        h = [((i_r * .5) + (g_r * .5)), ((i_g * .5) + (g_g * .5)), ((i_b * .5) + (g_b * .5))] #G/I
        f = [((i_r * .5) + (c_r * .5)), ((i_g * .5) + (c_g * .5)), ((i_b * .5) + (c_b * .5))] #C/I
        e_1 = pixel_blender([pixel1, pixel2, pixel3, pixel4])
        e_2 = [(a_r * .25) + (c_r * .25) + (g_r * .25) + (i_r * .25), (a_g * .25) + (c_g * .25) + (g_g * .25) + (i_g * .25), (a_b * .25) + (c_b * .25) + (g_b * .25) + (i_b * .25)]
        e = [((e_1[0] * .5) + (e_2[0] * .5)), ((e_1[1] * .5) + (e_2[1] * .5)), ((e_1[2] * .5) + (e_2[2] * .5))]
        a = [round(x) for x in a]
        b = [round(x) for x in b]
        c = [round(x) for x in c]
        d = [round(x) for x in d]
        e = [round(x) for x in e]
        f = [round(x) for x in f]
        g = [round(x) for x in g]
        h = [round(x) for x in h]
        i = [round(x) for x in i]
        block_v = [[a, b, c], [d, e, f], [g, h, i]]
        return(block_v)
    except Exception as e:
        print('Pixel Maker x1 Issues:', e)
        input('Hmm')
def mapperx():
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
        for by in range(h - 1):
            for bx in range(w - 1):
                block_counter += 1
                block_name = f'block_{block_counter}'
                block_coords = []
                for dy in range(2):
                    for dx in range(2):
                        y, x = by + dy, bx + dx
                        block_coords.append([x, y])
                map[block_name] = block_coords
        return (map, h, w)
    except Exception as e:
        print('Mapperx Issues:', e)
def mapper_to_array2():
    try:
        positions = [
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2), (2, 2)
        ]
        pixel_dic = {}
        desc = ("Processing..." + 'Core Using: ' + str(cores))
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
def process_batch_x1(batch):
    return {key: pixel_maker_x1(*value) for key, value in batch.items()}
def mkv_converter():
    try:
        for path in glob.glob("*.mkv"):
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            type = 'PNG'
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print(type, ':', path, fps, total_frames)
            name = os.path.splitext(path)[0]
            name_type = name + '_' + type
            size = input('2k, 4k, 8k: ')
            name_up = name + '_null'
            if size == '2k':
                name_up = name + '_2k'
                up_width, up_height = (1920, 1080)
            elif size == '4k':
                name_up = name + '_4k'
                up_width, up_height = (3840, 2160)
            elif size == '8k':
                name_up = name + '_8k'
                up_width, up_height = (7680, 4320)
            os.makedirs(name_up, exist_ok=True)
            for frame_id in track(range(int(total_frames))):
                ret, frame = cap.read()
                if not ret:
                    break
                out_path_type = f"{name_type}/{frame_id:06d}.png"
                out_path_up = f"{name_up}/{frame_id:06d}.png"
                if size == '2k' or size == '4k' or size == '8k':
                    if os.path.exists(out_path_up):
                        continue
                    up = cv2.resize(frame, (up_width, up_height), interpolation=cv2.INTER_LANCZOS4)
                    cv2.imwrite(out_path_up, up, [cv2.IMWRITE_PNG_COMPRESSION, 1])
                frame_id += 1
        cap.release()
        print('Finished:', path)
    except Exception as e:
        print('MKV Converter Issues:', e)
def mkv_upscaler():
    try:
        cv2.setNumThreads(cores)
        for path in glob.glob("*.mkv"):
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            size = input("2k, 4k, 8k: ")
            if size == "2k":
                width, height = 1920, 1080
            elif size == "4k":
                width, height = 3840, 2160
            elif size == "8k":
                width, height = 7680, 4320
            else:
                cap.release()
                continue
            name = os.path.splitext(path)[0]
            output = f"{name}_{size}.mkv"
            writer = cv2.VideoWriter(
                output,
                cv2.VideoWriter_fourcc(*"FFV1"),
                fps,
                (width, height)
            )
            for frame_id in track(range(total_frames), description=f"Upscaling {path}"):
                ret, frame = cap.read()
                if not ret:
                    break
                up = cv2.resize(
                    frame,
                    (width, height),
                    interpolation=cv2.INTER_LANCZOS4
                )
                writer.write(up)
            cap.release()
            writer.release()
            print("Finished:", output)
    except Exception as e:
        print('Movie Upscaler Issues:', e)
def mkv_upscaler2(height, width):
    try:
        cv2.setNumThreads(cores)
        for path in glob.glob("*.mkv"):
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            name = os.path.splitext(path)[0]
            output = f"{name}_{size}.mkv"
            writer = cv2.VideoWriter(
                output,
                cv2.VideoWriter_fourcc(*"FFV1"),
                fps,
                (width, height)
            )

            def resize(frame):
                return cv2.resize(
                    frame,
                    (width, height),
                    interpolation=cv2.INTER_CUBIC
                )
            with ThreadPoolExecutor(max_workers=WORKERS) as executor:
                pending = []
                for frame_id in track(range(total_frames), description=f"Upscaling {path}"):
                #for frame_id in range(total_frames):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    pending.append(executor.submit(resize, frame))
                    # Keep memory under control
                    if len(pending) >= WORKERS:
                        up = pending.pop(0).result()
                        writer.write(up)
            for job in pending:
                writer.write(job.result())

            cap.release()
            writer.release()

            print("Finished:", output)
        input('Finsihed MKVs')
    except Exception as e:
        print('MKV Movie Upscaler 2 Issues:', e)
def mp4_upscaler(height, width):
    try:
        cv2.setNumThreads(cores)
        for path in glob.glob("*.mp4"):
            cap = cv2.VideoCapture(path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            #size = input("2k, 4k, 8k: ")
            #else:
            #cap.release()
            #continue
            name = os.path.splitext(path)[0]
            temp = f"{name}_{size}_temp.mkv"
            output = f"{name}_{size}.mkv"
            writer = cv2.VideoWriter(
                temp,
                cv2.VideoWriter_fourcc(*"FFV1"),
                fps,
                (width, height)
            )
            if not writer.isOpened():
                print("Could not open writer:", temp)
                cap.release()
                continue

            def resize(frame):
                return cv2.resize(
                    frame,
                    (width, height),
                    interpolation=cv2.INTER_CUBIC
                )
            with ThreadPoolExecutor(max_workers=cores) as executor:
                pending = []
                for frame_id in track(range(total_frames), description=f"Upscaling {path}"):
                #for frame_id in range(total_frames):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    pending.append(executor.submit(resize, frame))
                    # Keep memory under control
                    if len(pending) >= (cores * 4):
                        up = pending.pop(0).result()
                        writer.write(up)
            for job in pending:
                writer.write(job.result())

            cap.release()
            writer.release()

            print("Finished:", temp)
            subprocess.run([
                "ffmpeg",
                "-i", temp,
                "-i", path,

                # New FFV1 video
                "-map", "0:v:0",

                # Original audio streams
                "-map", "1:a?",

                # Original subtitle streams
                "-map", "1:s?",

                # Original attachments/data
                "-map", "1:d?",

                # Original metadata
                "-map_metadata", "1",

                # Original chapters
                "-map_chapters", "1",

                # Copy everything without re-encoding
                "-c:v", "copy",
                "-c:a", "copy",
                "-c:s", "copy",
                "-c:d", "copy",

                output
            ], check=True)
            os.remove(temp)
            print("Finished:", output)
        input('Finsihed MP4s')
    except Exception as e:
        print('MP4 Movie Upscaler Issues:', e)
def motion_interpolate(frame0, frame1, t):
    """
    t = 0.0 → frame0
    t = 1.0 → frame1
    """

    gray0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(
        gray0,
        gray1,
        None,
        0.5,
        3,
        15,
        3,
        5,
        1.2,
        0
    )

    h, w = gray0.shape

    x, y = np.meshgrid(
        np.arange(w),
        np.arange(h)
    )

    # Position halfway through the motion
    map_x = (x + flow[:, :, 0] * t).astype(np.float32)
    map_y = (y + flow[:, :, 1] * t).astype(np.float32)

    interpolated = cv2.remap(
        frame0,
        map_x,
        map_y,
        cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT
    )

    return interpolated
def fps_fixer_mp4():
    try:
        for path in glob.glob("*.mp4"):
            print(path)
            cap = cv2.VideoCapture(path)
            if not cap.isOpened():
                print("Could not open:", path)
                continue
            fps = cap.get(cv2.CAP_PROP_FPS)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print(f"FPS: {fps}")
            print(f"Frames: {total_frames}")
            print(f"Target FPS: {fps * 4}")
            cap.release()
    except Exception as e:
        print('FPS Fixer MP4 Issues:', e)
def fps_fixer_mkv():
    try:
        for path in glob.glob("*.mkv"):
            print(path)
    except Exception as e:
        print('FPS Fixer MKV Issues:', e)
def pixel_mean(n1, i=None):
    try:
        n1 = [float(x) for x in n1]
        m1 = (sum(n1) / len(n1))
        odd = max(n1, key=lambda x: abs(x - m1))
        n1.remove(odd)
        if i != None:
            return(round(sum(n1) / len(n1)))
        else:
            return(n1)
    except Exception as e:
        print('Pixel Mean Issues:', e)
def movie_shader():
    try:
        name = 'V22'
        os.makedirs(name, exist_ok=True)
        files = (glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.jp2"))
        print('Total Images:', len(files))
        for path in track(files, description="Processing Images"):
            out_path = (name + '/' + path)
            if not os.path.exists(out_path):
                img = Image.open(path)
                metadata = img.info.copy()
                arr = np.array(img.convert('RGB'))
                for y in track(range(arr.shape[0]), description=('V22/'+path)):
                    for x in range(arr.shape[1]):
                        try:
                            r, g, b = arr[y, x]
                            left_r, left_g, left_b = arr[y, x - 1]
                            right_r, right_g, right_b = arr[y, x + 1]
                            up_r, up_g, up_b = arr[y - 1, x]
                            down_r, down_g, down_b = arr[y + 1, x]
                            p_r = pixel_mean([left_r, right_r, up_r, down_r], 'Y')
                            p_g = pixel_mean([left_g, right_g, up_g, down_g], 'Y')
                            p_b = pixel_mean([left_b, right_b, up_b, down_b], 'Y')
                            arr[y, x] = [((p_r * .75) + (r * .25)), ((p_g * .75) + (g * .25)), ((p_b * .75) + (b * .25))]
                        except:
                            pass
                Image.fromarray(arr).save(out_path, **metadata)
        cv2.setNumThreads(cores)
        files = (glob.glob("*.mp4"))
        print('Total Movies:', len(files))
        for path in track(files, description="Processing Movies"):
            out_path = (name + '/' + path)
            base, ext = os.path.splitext(out_path)
            temp = (base + "_temp" + ext)
            output = (base + "_Remastered" + ext)
            if not os.path.exists(temp):
                cap = cv2.VideoCapture(path)
                fps = cap.get(cv2.CAP_PROP_FPS)
                total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                #total_frames = 250
                width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
                codec = ''.join(map(chr, fourcc.to_bytes(4, 'little')))
                writer = cv2.VideoWriter(
                    temp,
                    cv2.VideoWriter_fourcc(*codec),
                    fps,
                    (width, height)
                )
                if not writer.isOpened():
                    print("Could not open writer:", temp)
                    cap.release()
                    continue
                def shade(frame):
                    #frame2 = frame
                    #i = np.std(cv2.Laplacian(frame, cv2.CV_64F))
                    '''for y in range(frame.shape[0]):
                        for x in range(frame.shape[1]):
                            try:
                                r, g, b = frame[y, x]
                                left_r, left_g, left_b = frame[y, x - 1]
                                right_r, right_g, right_b = frame[y, x + 1]
                                up_r, up_g, up_b = frame[y - 1, x]
                                down_r, down_g, down_b = frame[y + 1, x]
                                p_r = pixel_mean([left_r, right_r, up_r, down_r], 'Y')
                                p_g = pixel_mean([left_g, right_g, up_g, down_g], 'Y')
                                p_b = pixel_mean([left_b, right_b, up_b, down_b], 'Y')
                                frame[y, x] = [((p_r * .75) + (r * .25)), ((p_g * .75) + (g * .25)),((p_b * .75) + (b * .25))]
                            except:
                                pass'''
                    arr = frame.astype(np.float32)
                    left = arr[1:-1, :-2]
                    right = arr[1:-1, 2:]
                    up = arr[:-2, 1:-1]
                    down = arr[2:, 1:-1]
                    neighbors = np.stack([left, right, up, down], axis=0)
                    current = arr[1:-1, 1:-1]
                    distance = np.abs(neighbors - current)
                    order = np.argsort(distance, axis=0)
                    closest3 = np.take_along_axis(neighbors, order[:3], axis=0)
                    average = closest3.mean(axis=0)
                    result = arr.copy()
                    result[1:-1, 1:-1] = ((average * 0.8) + (current * 0.20))
                    frame2 = np.clip(result, 0, 255).astype(np.uint8)
                    #i2 = np.std(cv2.Laplacian(frame2, cv2.CV_64F))
                    #if i2 < i:
                    #print('Yes:', i, i2)
                    '''if i2 > i:
                        return(frame2)
                    else:
                        return(frame)'''
                    return(frame2)
                with ThreadPoolExecutor(max_workers=cores) as executor:
                    pending = []
                    for frame_id in track(range(total_frames), description=f"Upscaling {path}"):
                        ret, frame = cap.read()
                        if not ret:
                            break
                        pending.append(executor.submit(shade, frame))
                        if len(pending) >= (cores * 16):
                            up = pending.pop(0).result()
                            writer.write(up)
                for job in pending:
                    writer.write(job.result())
                cap.release()
                writer.release()
                print("Finished:", temp)
            if not os.path.exists(output):
                subprocess.run([
                    "ffmpeg",
                    "-i", temp,
                    "-i", path,
                    "-map", "0:v:0",
                    "-map", "1:a?",
                    "-map", "1:s?",
                    "-map", "1:d?",
                    "-map_metadata", "1",
                    "-map_chapters", "1",
                    "-c:v", "copy",
                    "-c:a", "copy",
                    "-c:s", "copy",
                    "-c:d", "copy",
                    output
                ], check=True)
                #os.remove(temp)
                print("Finished:", path)
        input('Finsihed MP4s')

    except Exception as e:
        print('Movie Shader Issues:', e)
if __name__ == '__main__':
    try:
        cores = os.cpu_count()
        ram = psutil.virtual_memory()
        cores = psutil.cpu_count(logical=False)
        ram_gb = (ram.available / (1024 ** 3))
        ram_bytes = ((1000000000) * ram_gb)
        folder = "v19 Output"
        print('############################################################')
        print('######## Pixel Edit - Anthony R Shively (Ohio, USA) ########')
        print('############################################################')
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
        movie_shader()
        print('Aspect Ratios')
        print('(7680 x 4320) 16:9 8K UHD')
        print('(3840 x 2160) 16:9 4k UHD')
        print('(3200 x 2400) 4:3 QUXGA')
        print('(2560 x 1440) 16:9 2k Quad HD')
        print('(1920 x 1440) 4:3 QHD (Max 4:3 on 2560 x 1440)')
        print('(1920 x 1080) 16:9 FHD')
        print('(1440 x 1080) 4:3 HDV2')
        print('(1280 x 720) 16:9 HD')
        print('(640 x 480) 4:3 SD / VGA')
        print('(320 x 240) 4:3 QVGA')
        print('File Source => Upscale => Encode FFV1 => .MKV')
        size = input("FHD, QHD, 4k, 8k: ")
        if size == "8k":
            width, height = 7680, 4320
        elif size == "4k":
            width, height = 3840, 2160
        elif size == "QHD":
            width, height = 1920, 1440
        elif size == "FHD":
            width, height = 1920, 1080
        # mkv_converter()
        i = input('Video Type (MKV, MP4): ')
        if i == 'mkv':
            mkv_upscaler2(width, height)
        elif i == 'mp4':
            mp4_upscaler(width, height)
        else:
            mkv_upscaler2(width, height)
            mp4_upscaler(width, height)
        input('Finished Upscaling')
        print('')
        print('FPS Fixer')
        
        print('Finished FPS Fixer')
    except Exception as e:
        print('Main Issues:', e)