#!/usr/bin/env python3
# encoding=utf-8
# by 不灭的小灯灯 (updated for Python3 & argparse)
# create date 2016/5/22
# update 2025/8/18
# support iOS 10+
# site www.winterfeel.com

import os
import argparse
from PIL import Image

# iOS icon sizes
iosSizes = [
    "20@1x",
    "20@2x",
    "20@3x",
    "29@1x",
    "29@2x",
    "29@3x",
    "40@1x",
    "40@2x",
    "40@3x",
    "60@2x",
    "60@3x",
    "76@1x",
    "76@2x",
    "167@1x",
]

# Android icon sizes
androidSizes = [32, 48, 72, 96, 144, 192]
androidNames = ["ldpi", "mdpi", "hdpi", "xhdpi", "xxhdpi", "xxxhdpi"]

# Screenshot sizes
sizesiOS = [
    (640, 960),
    (640, 1136),
    (750, 1334),
    (1242, 2208),
    (1536, 2048),
    (2048, 2732),
]
foldersiOS = ["iPhone4s", "iPhone5", "iPhone6", "iPhone6plus", "iPad", "iPadLarge"]

sizesAndroid = [(480, 800), (720, 1280), (1080, 1920)]
foldersAndroid = ["480x800", "720x1280", "1080x1920"]


def processIcon(filename, platform):
    """Generate icons for iOS or Android"""
    icon = Image.open(filename).convert("RGBA")
    if icon.size[0] != icon.size[1]:
        print("Error: Icon file must be a square!")
        return

    if platform == "android":
        # Apply Android mask (if exists)
        if os.path.exists("mask.png"):
            mask = Image.open("mask.png")
            _, _, _, a = mask.split()
            icon.putalpha(a)

        outdir = os.path.join("media", "android", "icons")
        os.makedirs(outdir, exist_ok=True)

        for index, size in enumerate(androidSizes):
            im = icon.resize((size, size), Image.Resampling.BILINEAR)
            im.save(os.path.join(outdir, f"icon-{androidNames[index]}.png"))

    else:  # iOS
        outdir = os.path.join("media", "ios", "icons")
        os.makedirs(outdir, exist_ok=True)

        for size in iosSizes:
            originalSize = int(size.split("@")[0])
            multiply = int(size.split("@")[1][0:1])
            im = icon.resize(
                (originalSize * multiply, originalSize * multiply),
                Image.Resampling.BILINEAR,
            )
            im.save(os.path.join(outdir, f"icon{size}.png"))

    print(f"{platform.capitalize()} icons generated at {outdir}")


def walk_dir(directory, platform):
    """Process all images in a folder as screenshots"""
    files = os.listdir(directory)
    for name in files:
        if name.lower().endswith((".jpg", ".png")):
            produceImage(os.path.join(directory, name), platform)

    print(
        f"{platform.capitalize()} screenshots generated under media/{platform}/screenshots/"
    )


def produceImage(filename, platform):
    """Resize screenshots for iOS or Android"""
    print(f"Processing: {filename}")
    img = Image.open(filename)

    if platform == "android":
        sizes, folders = sizesAndroid, foldersAndroid
    else:
        sizes, folders = sizesiOS, foldersiOS

    for index, size in enumerate(sizes):
        outdir = os.path.join("media", platform, "screenshots", folders[index])
        os.makedirs(outdir, exist_ok=True)

        if img.size[0] > img.size[1]:  # landscape
            im = img.resize((size[1], size[0]), Image.Resampling.BILINEAR)
        else:
            im = img.resize(size, Image.Resampling.BILINEAR)

        im.save(os.path.join(outdir, os.path.basename(filename)))


def main():
    parser = argparse.ArgumentParser(
        description="Generate app icons or screenshots for iOS/Android."
    )
    subparsers = parser.add_subparsers(dest="action", required=True)

    # Icon subcommand
    icon_parser = subparsers.add_parser("icon", help="Generate icons")
    icon_parser.add_argument("filename", help="Source image file (must be square)")
    icon_parser.add_argument(
        "platform", choices=["ios", "android"], help="Target platform"
    )

    # Screenshot subcommand
    screenshot_parser = subparsers.add_parser("screenshot", help="Generate screenshots")
    screenshot_parser.add_argument(
        "platform", choices=["ios", "android"], help="Target platform"
    )
    screenshot_parser.add_argument(
        "--dir", default="./", help="Directory containing images (default: ./)"
    )

    args = parser.parse_args()

    if args.action == "icon":
        if not os.path.exists(args.filename):
            print("Error: File not found!")
            return
        processIcon(args.filename, args.platform)

    elif args.action == "screenshot":
        walk_dir(args.dir, args.platform)


if __name__ == "__main__":
    main()
