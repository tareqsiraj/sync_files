import os
from conans import ConanFile
from conans.client import tools


class CMakeConan(ConanFile):
    name = "CMake"
    version = "3.12.4"
    license = ""
    url = "self hosted"
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = "CMake"

    def configure(self):
        if self.settings.os_build not in ["Macos", "Linux", "Windows"]:
            raise Exception("CMake is only provided for Macos, Linux and Windows!")

    @property
    def cmake_major_minor(self):
        return ".".join(self.version.split(".")[:2])

    @property
    def cmake_folder_name(self):
        if self.settings.os_build == "Macos":
            return "cmake-{}-Darwin-x86_64".format(self.version)
        elif self.settings.os_build == "Linux":
            return "cmake-{}-Linux-x86_64".format(self.version)
        elif self.settings.os_build == "Windows":
            return "cmake-{}-win64-x64".format(self.version)
        else:
            raise Exception("CMake is only provided for Macos, Linux and Windows!")

    @property
    def cmake_zip_name(self):
        if self.settings.os_build == "Macos":
            return "{}.tar.gz".format(self.cmake_folder_name)
        elif self.settings.os_build == "Linux":
            return "{}.tar.gz".format(self.cmake_folder_name)
        elif self.settings.os_build == "Windows":
            raise Exception("FIXME: for windows")
            return "{}.zip".format(self.cmake_folder_name)
        else:
            raise Exception("Clang is only provided for Macos, Linux and Windows!")

    @property
    def cmake_bin_dir(self):
        if self.settings.os_build == "Macos":
            return os.path.join(self.package_folder, self.cmake_folder_name, "CMake.app", "Contents", "bin")
        elif self.settings.os_build == "Linux":
            raise Exception("FIXME: for linux")
            return os.path.join(self.package_folder, self.cmake_folder_name, "bin")
        elif self.settings.os_build == "Windows":
            raise Exception("FIXME: for windows")
            return os.path.join(self.package_folder, self.cmake_folder_name, "bin")
        else:
            raise Exception("Clang is only provided for Macos, Linux and Windows!")

    def build(self):

        download_url = "https://cmake.org/files/v{}/{}".format(self.cmake_major_minor, self.cmake_zip_name)
        self.output.warn("Downloading '{}'...".format(download_url))
        tools.download(download_url, self.cmake_zip_name)
        tools.unzip(self.cmake_zip_name)
        os.unlink(self.cmake_zip_name)

    def package(self):
        self.copy("*", dst="", keep_path=True)

    def package_info(self):
        self.output.info("Using CMake {}".format(self.version))
        self.env_info.path.append(os.path.join(self.package_folder, self.cmake_bin_dir))
