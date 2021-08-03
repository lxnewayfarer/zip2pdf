## Zip unpack

Unpacking sorted ZIP files with images to `/image` folder, giving unique name (0..N index) to each image.
___
### Use:

1. Load your ZIP files to `/zip` folder;
2. Run `python main.py` 
3. Check `/images` folder
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
```
