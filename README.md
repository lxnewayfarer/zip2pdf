## Batch images from multiple ZIP to single PDF converter

Unpacking sorted ZIP files with images (.png, .jpg, etc) to `/image` folder, giving unique name (0..N index) to each image.

Compiling all extracted images into single `result.pdf`.
___
### Use:

1. Load your ZIP files to `/zip` folder;

2. Run converter

    2.1 Windows:
    - Run `zip2pdf.exe`.

    2.2 Any platform/development:

    - Install Python 3.x+;

    - Install dependency `pip install Pillow`;
        
    - Run script `python zip2pdf.py`.

3. Check `/images` folder and `result.pdf`
___
### Example:

From this:

```text
/zip
   |_my_zip_1.zip
   |            |_1.png (A)
   |            |_2.png (B)
   |_my_zip_2.zip
   |            |_1.png (C)
   |            |_2.png (D)
   |            |_3.png (E)
```

To this:

```text
/images
      |_0.png (A)
      |_1.png (B)
      |_2.png (C)
      |_3.png (D)
      |_4.png (E)
+
result.pdf
```
