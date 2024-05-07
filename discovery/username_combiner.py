import argparse


def combine(p1, p2):
    c = {
        p1 + p2,
        p1 + "." + p2,
        p1 + "_" + p2,
        p1 + p2[0],
        p1[0] + p2,
        p1[0] + "." + p2,
        p1[0] + "_" + p2,
    }
    return set(map(lambda x: x + "\n", c))


def switch(first, last, fileName):
    file = open(fileName, "a")
    file.writelines(combine(first, last) | (combine(last, first)))
    file.close()


def addDomain(domain, fileName):
    file = open(fileName, "a+")
    file.seek(0)
    lines = file.readlines()
    file.writelines([f"{line.strip()}@{domain}\n" for line in lines])
    file.close()


def main():
    parser = argparse.ArgumentParser(description="Build a list of usernames")
    parser.add_argument("first_name", type=str, help="The first name of the user")
    parser.add_argument("last_name", type=str, help="The last name of the user")
    parser.add_argument(
        "--domain",
        type=str,
        help="The domain the user may be using",
        default=None,
        required=False,
    )
    args = parser.parse_args()
    # Retrieve the command line arguments

    first_name = args.first_name
    last_name = args.last_name
    domain = args.domain
    print(domain)

    output_file = f"{first_name}_{last_name}.list"

    try:
        open(output_file, "x")
    except OSError:
        print(
            f"Error creating the file outout: {output_file}. Either it already exsit or you don't have permission to create it."
        )
        return

    switch(first_name, last_name, output_file)
    if domain:
        addDomain(domain, output_file)

    print("Done")


if __name__ == "__main__":
    main()
