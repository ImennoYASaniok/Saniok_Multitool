from PIL import Image
import random

def del_border(path, type_save="save", new_name=""):
    if "." not in new_name: new_name = new_name + ".png"
    sheet = Image.open(path)

    data = sheet.load()
    crop_coords = []
    for y1 in range(sheet.size[1]):
        if list(filter(lambda x: x != 0, map(lambda x: data[x, y1][3], range(sheet.size[0])))) is not []:
            crop_coords.append(y1)
            break
    for x1 in range(sheet.size[0]):
        if list(filter(lambda y: y != 0, map(lambda y: data[x1, y][3], range(sheet.size[1]))))  is not []:
            crop_coords.append(x1)
            break
    for x2 in range(sheet.size[0]-1, 0, -1):
        if list(filter(lambda y: y != 0, map(lambda y: data[x2, y][3], range(sheet.size[1]-1, -1, -1)))) is not []:
            crop_coords.append(x2)
            break
    for y2 in range(sheet.size[1]-1, 0, -1):
        # print(list(filter(lambda x: x != 0, map(lambda x: data[x, y2][3], range(sheet.size[0]-1, -1, -1)))))
        if list(filter(lambda x: x != 0, map(lambda x: data[x, y2][3], range(sheet.size[0]-1, -1, -1)))) is not []:
            crop_coords.append(y2)
            break
    print("coords to crop:", *crop_coords)
    sheet = sheet.crop(crop_coords)

    print("/".join(path.split("/")[:-1]))
    if type_save == "save":
        sheet.save("/".join(path.split("/")[:-1]+[new_name]))
    elif type_save == "replace":
        sheet.save(path)


def sprite_crop(path, type_sprites, sprite, grid, inacurr=[0, 0, 0, 0], sep=(), single_inacurr={}):
    path = path.replace("\\", "/")
    sheet = Image.open(path)

    print("start_path:", path)
    path = "/".join(path.split("/")[:-1])
    cond = path.split("/")[-1]
    print("cond:", cond)

    if len(inacurr) == 0: inacurr = [0, 0, 0, 0]
    elif len(inacurr) == 1: inacurr += [0, inacurr[0], 0]
    elif len(inacurr) == 2: inacurr += [inacurr[0], inacurr[1]]
    elif len(inacurr) == 3:  inacurr += [inacurr[1]]
    for k, v in single_inacurr.items():
        if len(v) == 0: single_inacurr[k] = [0, 0, 0, 0]
        elif len(v) == 1: single_inacurr[k] += [0, v[0], 0]
        elif len(v) == 2: single_inacurr[k] += [v[0], v[1]]
        elif len(v) == 3: single_inacurr[k] += [v[1]]

    if sep is None or sep == (): sep = (sheet.size[0]//grid[1], sheet.size[1]//grid[0])
    print("sep:", sep)
    count = 0
    for y in range(1, grid[0] + 1):
        for x in range(1, grid[1] + 1):
            name = f"{path}/{cond}_{type_sprites[y-1]}_{count}.png"
            res_x = x * sep[0]
            res_y = y * sep[1]
            res_x1 = res_x-sep[0]+(sep[0]-sprite[0])/2
            res_y1 = res_y-sep[1]+(sep[1]-sprite[1])/2
            res_x2 = res_x-(sep[0]-sprite[0])/2
            res_y2 = res_y-(sep[1]-sprite[1])/2
            for k, v in single_inacurr.items():
                if k == f"{cond}_{type_sprites[y-1]}_{count}":
                    res_x1 += v[0]
                    res_y1 += v[1]
                    res_x2 += v[2]
                    res_y2 += v[3]
                    print("single inacurr", name)
                    break
            else:
                res_x1 += inacurr[0]
                res_y1 += inacurr[1]
                res_x2 += inacurr[2]
                res_y2 += inacurr[3]
                print("standart inacurr", name)
            icon = sheet.crop((res_x1, res_y1, res_x2, res_y2))
            icon.save(name)
            count += 1
        count = 0



def set_image_expansion(input_path, output_path, k=None, size=None, type_side="width", quality=95): # изменение расширение картинки
    if k is None and size is None:
        raise ValueError("параметр k или side должен присутствовать")
    image = Image.open(input_path)
    if (k is not None and size is None) or (k is not None and size is not None):
        image = image.reduce(k)
    elif k is None and size is not None:
        if type(size) == int:
            if type_side == "width":
                image = image.resize((size, int(image.size[1] / (image.size[0] / size))))
            elif type_side == "height":
                image = image.resize((int(image.size[0] // (image.size[1] / size)), size))
            else:
                raise ValueError("type_side должен быть равен или width, или height")
        elif type(size) in (tuple, list):
            if len(size) >= 2:
                size = list(size)
                image = image.resize((size[0], size[1]))
            else:
                raise ValueError("Если size имеет списочный тип данных, то у него должно быть как минимум 2 элемента")
        else:
            raise ValueError("Неправильный тип у size, должен быть int, tuple, list")
    image.save(output_path, quality=quality)



def make_floor(input_path, output_path, size, random_flip=("horizontal", "vertical")):
    # random_dir:
    # "horizontal" - Image.Transpose.FLIP_LEFT_RIGHT - зеркаливание по горизонтали
    # "vertical" - Image.Transpose.FLIP_TOP_BOTTOM - зеркаливание по вертикале
    input_img = Image.open(input_path)
    ramdom_data = [1]
    if "horizontal" in random_flip: ramdom_data.append(2)
    if "vertical" in random_flip: ramdom_data.append(3)
    res_img = Image.new("RGB", size, "white")
    for k_x in range(0, int(size[0]/input_img.size[0])+1):
        for k_y in range(0, int(size[1] / input_img.size[1])+1):
            res_input_img = input_img
            random_val = random.choice(ramdom_data)
            print(random_val)
            if random_val == 1:
                res_input_img = input_img
            elif random_val == 2:
                res_input_img = input_img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            elif random_val == 3:
                res_input_img = input_img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            res_img.paste(res_input_img, (k_x*input_img.size[0], k_y*input_img.size[1]))
    res_img.save(output_path)


def color_image(input_path, output_path, color=(20, 0, 0)):
    img = Image.open(input_path)
    # img = img.convert("L")
    # img = img.convert("RGBA")
    all_pxs = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if len(all_pxs[x, y]) > 3:
                r, g, b, a = all_pxs[x, y]
                if len(color) > 3: a += color[3]
            else:
                r, g, b = all_pxs[x, y]
            r += color[0]
            g += color[1]
            b += color[2]
            if len(all_pxs[x, y]) > 3:
                all_pxs[x, y] = (min(r, 255), min(g, 255), min(b, 255), min(a, 255))
            else:
                all_pxs[x, y] = (min(r, 255), min(g, 255), min(b, 255))
    img.save(output_path)

############################## ПРОСТРАНСТВО РЕДАКТОРА ##############################
# set_image_expansion(input_path="background.png", output_path="background.png", size=340, type_side="width", quality=95)

# set_image_expansion(input_path="mars.png", output_path="mars.png", size=240, type_side="width", quality=95)

# set_image_expansion(input_path="another.png", output_path="another.png", size=240, type_side="width", quality=95)
# set_image_expansion(input_path="builder.png", output_path="builder.png", size=240, type_side="width", quality=95)
# set_image_expansion(input_path="engineer.png", output_path="engineer.png", size=240, type_side="width", quality=95)

# set_image_expansion(input_path="alien_young.png", output_path="alien_young.png", size=150, type_side="width", quality=95)

set_image_expansion(input_path="img.png", output_path="img_RES.png", size=600, type_side="width", quality=95)
set_image_expansion(input_path="img_1.png", output_path="img_1_RES.png", size=600, type_side="width", quality=95)