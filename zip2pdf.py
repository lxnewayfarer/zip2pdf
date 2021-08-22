from os import walk, mkdir
from shutil import move, rmtree
import zipfile
from PIL import Image
from functools import cmp_to_key


def compare(x, y):
    x_name = x.split('.')[0]
    y_name = y.split('.')[0]
    if x_name.isdigit() and y_name.isdigit():
        return int(x_name) - int(y_name)
    else:
        return (x_name > y_name) - (x_name < y_name)


def unpack_zips_from_zip_folder(foldername="./zip"):
    zips = files_list_from_folder(foldername)

    counter = 0

    print("ZIPs left: ", end="")
    for zip in zips:
        print("[ ]", end="")
    print("\n___________", end="")

    # each archive
    for zip in sorted(zips, key=cmp_to_key(compare)):
        with zipfile.ZipFile(foldername + "/" + zip, "r") as zip_ref:
            zip_ref.extractall("./temp")
        # unziped to ./temp
        temp_files = files_list_from_folder("./temp")
        # now move and rename every file in temp folder to images with index [counter] name

        for file in sorted(temp_files, key=cmp_to_key(compare)):
            file_extension = file.split(".")[-1]
            move("temp/" + file, "images/" + str(counter) + "." + file_extension)
            counter += 1

        print("[✓]", end="")
    print("\nDone. Check /images folder or result.pdf")


def aliens():
    print(open(".aliens", "r").read(), end="\n")


def files_list_from_folder(foldername="./zip"):
    files = []
    for dirpath, dirnames, filenames in walk(foldername):
        files.extend(filenames)
        break
    return files


def image_open(name):
    image = Image.open(name)
    try:
        image.load()  # required for png.split()
        rgb = Image.new("RGB", image.size, (255, 255, 255))
        rgb.paste(image, mask=image.split()[3])  # 3 is the alpha channel
    except Exception:
        return image
    return rgb


def to_pdf():
    images_names = files_list_from_folder("./images")
    first_image = image_open("./images/" + images_names[0])

    images = list(image_open("./images/" + image_name)
                  for image_name in images_names[1:])

    first_image.save("result.pdf", "PDF", resolution=100.0,
                     save_all=True, append_images=images)


def clear_folders():
    try:
        rmtree("images")
    except Exception:
        pass
    try:
        rmtree("temp")
    except Exception:
        pass
    mkdir("images")


if __name__ == "__main__":
    aliens()
    clear_folders()
    unpack_zips_from_zip_folder()
    to_pdf()

    print("Press [ENTER] to exit")
    input()
