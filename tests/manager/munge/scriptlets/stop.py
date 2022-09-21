#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Scriptlet to test stop is working."""

import sys

import charms.operator_libs_linux.v0.apt as apt
from charms.operator_libs_linux.v1.systemd import service_running
from munge import MungeManager


def test() -> None:
    # Check munge is installed.
    if not _is_munge_installed():
        sys.exit(1)

    # Stop munge.
    manager = MungeManager()
    manager.stop()

    # Check that service is active.
    if service_running("munge"):
        sys.exit(1)
    else:
        sys.exit(0)


def _is_munge_installed() -> bool:
    try:
        munge = apt.DebianPackage.from_installed_package("munge")
        return True
    except apt.PackageNotFoundError:
        return False


if __name__ == "__main__":
    test()
