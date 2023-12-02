#!/usr/bin/env python3


import argparse
from pathlib import Path
from typing import List


def is_integer(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        return False

def calibrate(calibration_data: str) -> int:
    index = 0
    left_side = None
    right_side = None

    while index < len(calibration_data):
        character_left = calibration_data[index]
        character_right = calibration_data[-index-1]
        if left_side is None:
            left_side = character_left if is_integer(character_left) else None
        if right_side is None:
            right_side = character_right if is_integer(character_right) else None
        if left_side is not None and right_side is not None:
            break
        index += 1
    
    return int(left_side + right_side)

def summate_calibrations(calibrations: List[str]) -> int:
    return sum([calibrate(calibration) for calibration in calibrations])


def get_calibration_data(filename: Path) -> List[str]:
    return filename.read_text().splitlines()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=Path)
    args = parser.parse_args()
    path_file = args.input_file
    print(summate_calibrations(get_calibration_data(path_file)))