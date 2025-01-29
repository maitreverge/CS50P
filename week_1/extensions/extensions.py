def make_prompt():
    print("File name: ", end="")
    return input().lower().strip(" ")


import sys


def main():
    mimes_types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
        "default": "application/octet-stream",
    }

    prompt = make_prompt()

    if prompt.find(".") == -1:
        print(f"{mimes_types.get("default")}")
        sys.exit(1)

    # Extract only what's after the last '.'
    extension = prompt[prompt.rfind(".") + 1 :]

    final_mime = mimes_types.get(extension)

    if final_mime == None:
        print(f"{mimes_types.get("default")}")
    else:
        print(final_mime)


if __name__ == "__main__":
    main()
