import os

from pathlib import Path

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy, get, rename, rmdir


class PCRE2(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        cmake_layout(self, src_folder="src")

    def source(self):
        rmdir(self, "src")
        version = os.getenv("PCRE2_VERSION")
        assert version is not None, "PCRE2_VERSION environment variable is not set. Example value: '10.47'."
        url = f"https://github.com/PCRE2Project/pcre2/archive/refs/tags/pcre2-{version}.tar.gz"
        get(self, url, strip_root=True)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()

        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # `cmake.install` is using `self.package_folder`, which is based on `self.base_package`.
        installation_path = Path(self.package_folder) / "package"
        self.folders.set_base_package(installation_path.__str__())

        rmdir(self, installation_path)
        cmake.install()

        copy(self, "LICENCE.md", src=self.source_folder, dst=installation_path, keep_path=False)
        copy(self, "AUTHORS.md", src=self.source_folder, dst=installation_path, keep_path=False)
        copy(self, "README", src=self.source_folder, dst=installation_path, keep_path=False)
        rename(self, installation_path / "README", installation_path / "PCRE2_README.md")