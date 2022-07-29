#!/usr/bin/env python3
"""
Author : Me <okiemenprecious@gmail.com>
Date   : 30/07/2022
Purpose: Jump The Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump The Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    parser.add_argument(
        "-s",
        "--strings",
        action="store_true",
        help="Whether to encode numbers to string",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    strings = args.strings

    jumper = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    number_to_string = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
    }

    new_text = ""

    # is_last_number acts as a placeholder to hold the boolean value TRUE/FALSE
    is_last_number = False

    output = []
    if strings:
        for char in text:

            """the use of a trace table will help you understand & appreciate the
            beauty of this less-pretty IF statement.
            """
            if char in number_to_string:
                if is_last_number:
                    output.append("-")

                output.append(number_to_string[char])

                # this line handles the "-" in between the numbered word
                is_last_number = True

            else:
                output.append(char)

                # this line handles the "-" in the original text
                is_last_number = False

        print("".join(output))

    else:
        for i in text:
            new_text = jumper.get(i, i)
            print(new_text, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
