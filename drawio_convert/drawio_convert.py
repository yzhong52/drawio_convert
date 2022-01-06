import argparse
import glob
import os
import os.path
from datetime import datetime
from shutil import copyfile
from pathlib import Path

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "--force",
    dest="force",
    required=False,
    action="store_true",
    help="Always regenerate images regardless whether we have new updates or not. This is particularly useful when you have updated your Draw.io Application, for example",
)
parser.set_defaults(force=False)
args = parser.parse_args()
print(args)


def _format_ts(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S")


def convert_file(file: str, format: str) -> int:
    # Filename here is the output path without extension
    full_filename, extension = os.path.splitext(file)

    # Split the pathname path into a pair, (head, tail) where tail is the last
    # pathname component and head is everything leading up to that.
    _, target_filename = os.path.split(file)

    target_file = f"{full_filename}.generated.{format}"
    source_ts = os.path.getmtime(file)

    # Ensure that we don't re-convert the file if it is not edited
    target_ts = os.path.getmtime(target_file) if os.path.isfile(target_file) else 0
    if source_ts > target_ts or args.force:
        print("Converting file ...")
        print(f"Source file: [{_format_ts(source_ts)}] {file} ")
        if target_ts:
            print(f"Target file: [{_format_ts(target_ts)}] {target_file} (overwrite)")
        else:
            now = datetime.now().microsecond
            print(f"Target file: [{_format_ts(now)}] {target_file} (create)")
        # https://j2r2b.github.io/2019/08/06/drawio-cli.html
        command = "/Applications/draw.io.app/Contents/MacOS/draw.io"
        command += " --export"
        command += f" --format {format}"
        # command += " --transparent"   # since medium has dark theme
        command += f" --output '{target_file}' '{file}'"
        os.system(command)

        # Copy file to desktop
        home = str(Path.home())
        desktop_file_path = f"{home}/Desktop/{target_filename}.generated.{format}"
        print(f"Copy file from {target_file} to {desktop_file_path}")
        copyfile(target_file, desktop_file_path)

        print("-+" * 40)
        return 1
    return 0


def convert():
    converted_count = 0
    skiped_count = 0

    for file in glob.glob("**/*.drawio", recursive=True):
        result = convert_file(file=file, format="png")
        if result:
            converted_count += 1
        else:
            skiped_count += 1

    print(f"\nConverted {converted_count}. Skipped {skiped_count}.")


if __name__ == "__main__":
    convert()
