# Copyright (C) 2014 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
def main():
    import argparse

    # Just picks them up from `sys.argv`.
    parser = argparse.ArgumentParser(
        description="Basic parser."
    )
    parser.parse_args()

    print("Manual entry point")
