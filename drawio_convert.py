import glob
import os
import os.path
from datetime import datetime


def convert_file(file: str, format: str) -> int:
    filename, _ = os.path.splitext(file)

    target_file = f"{filename}.generated.{format}"
    source_ts = os.path.getmtime(file)

    # Ensure that we don't re-convert the file if it is not edited
    target_ts = os.path.getmtime(target_file) if os.path.isfile(target_file) else 0
    if source_ts > target_ts:
        print("Converting file ...")
        print(f"from: [{datetime.fromtimestamp(source_ts)}] {file} ")
        if target_ts:
            print(f"to  : [{datetime.fromtimestamp(target_ts)}] {target_file}")
        # https://j2r2b.github.io/2019/08/06/drawio-cli.html
        command = "/Applications/draw.io.app/Contents/MacOS/draw.io"
        command += " --export"
        command += f" --format {format}"
        # command += " --transparent"   # since medium has dark theme
        command += f" --output '{target_file}' '{file}'"
        os.system(command)
        print("-+" * 40)
        return 1
    return 0


counter = 0

for file in glob.glob("**/*.drawio", recursive=True):
    for format in ["png"]:
        counter += convert_file(file=file, format=format)


print(f"Complete with all {counter} documents.")
