#!/usr/bin/python

import apt

import unittest
import sys
sys.path.insert(0, "..")

from softwareproperties.SoftwareProperties import shortcut_handler



class ShortcutsTestcase(unittest.TestCase):

    def setUp(self):
        # avoid polution from other tests
        apt.apt_pkg.config.set("Dir", "/")
        apt.apt_pkg.config.set("Dir::Etc", "etc/apt")
        apt.apt_pkg.config.set("Dir::Etc::sourcelist", "sources.list")
        apt.apt_pkg.config.set("Dir::Etc::sourceparts", "sources.list.d")

    def test_shortcut_none(self):
        line = "deb http://ubuntu.com/ubuntu trusty main"
        handler = shortcut_handler(line)
        self.assertEqual((line, None), handler.expand())

    def test_shortcut_ppa(self):
        line = "ppa:mvo"
        handler = shortcut_handler(line)
        self.assertEqual(
            ('deb http://ppa.launchpad.net/mvo/ppa/ubuntu trusty main',
             '/etc/apt/sources.list.d/mvo-ubuntu-ppa-trusty.list'),
            handler.expand("trusty", distro="ubuntu"))

    def test_shortcut_cloudarchive(self):
        line = "cloud-archive:folsom"
        handler = shortcut_handler(line)
        self.assertEqual(
            ('deb http://ubuntu-cloud.archive.canonical.com/ubuntu '\
             'precise-updates/folsom main',
             '/etc/apt/sources.list.d/cloudarchive-folsom.list'),
            handler.expand("precise", distro="ubuntu"))


if __name__ == "__main__":
    unittest.main()
