import time

# Clean file
with open("/home/adrian/file123",'w') as file:
    pass

f = open("/home/adrian/file123")
a_flag = 0
s_flag = 0
d_flag = 0
f_flag = 0

while True:
    line123 = f.read()  
    if any(x in line123 for x in ["(KEY_A)", "(KEY_S)", "(KEY_D)", "(KEY_F)", "(KEY_SPACE)"]):
        if "value 1" in line123:
            if "(KEY_A)" in line123:
                a_flag = 1
            if "(KEY_S)" in line123:
                s_flag = 1
            if "(KEY_D)" in line123:
                d_flag = 1
            if "(KEY_F)" in line123:
                f_flag = 1
            if "(KEY_SPACE)" in line123:
                a_flag = 0
                s_flag = 0
                d_flag = 0
                f_flag = 0
        if "value 0" in line123:
            output = f_flag*1 + d_flag*2 + s_flag*4 + a_flag*8
            if output>0:
                print(f'{output:x}')

            a_flag = 0
            s_flag = 0
            d_flag = 0
            f_flag = 0

    time.sleep(0.1)

# sudo evtest /dev/input/event8 > file123
