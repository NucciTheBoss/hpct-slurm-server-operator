#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Scriptlet to test install is working."""

import sys

import charms.operator_libs_linux.v0.apt as apt
from munge import MungeManager


def test() -> None:
    # Install munge.
    manager = MungeManager()
    manager.install()

    # Test that package is present on system.
    try:
        apt.DebianPackage.from_installed_package("munge")
        sys.exit(0)
    except apt.PackageNotFoundError:
        sys.exit(1)


if __name__ == "__main__":
    test()
