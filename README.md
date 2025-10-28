# IconSplashMaker

Hey guys! It's a python script to generate icons and screenshots for iOS and Android Apps.

## Environment

Python 3.10

PIL or Pillow

## How to use

To install and run the command

```bash
pip install pillow
python ./tool.py -h
```

> [!TIP]
> You need to prepare a `mask.png` to crop Android icon. It's size must be (512px,512px) and 70px cornerRadius.
>
> Dont worry, we've already prepare one for you in GitHub.
>
> When you generate screenshots,the script will scan all JPG/PNG file in current folder,and you don't need to worry about the orientation.

### Genicons

install

```bash
pip install -r ./requirements.txt
```

Generate mipmaps

```bash
python ./genicons.py -h
```

Best on work example:

```bash
./genicons.py run ./assets/rich.png icons -f
```

> [!NOTE]
> It was writen by AI, there are a few issues...

#### About @mipmap/ic_launcher

The `@mipmap/ic_launcher` files are the app icons generated for different screen densities.

This tool automatically creates all standard sizes **(mdpi, hdpi, xhdpi, xxhdpi, xxxhdpi)** from a single source icon.

Each generated icon is placed in its respective mipmap-<density> folder inside the res directory.

### Termux

install requirements:

```bash
pkg update && apt update
apt install python python-pillow -y
```

## About

Hello, I'm **Arsene**, from China.

I'm a individual full stack developer,I love evey kinds of codes,Ahahahahah...

My Blog: [winterfeel](http://www.winterfeel.com)
