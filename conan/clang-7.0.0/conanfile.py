import os
from conans import ConanFile
from conans.client import tools


class ClangConan(ConanFile):
    name = "Clang"
    version = "7.0.0"
    license = ""
    url = "self hosted"
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = "Clang compiler, LLD, libc++, compiler-rt, tools, etc."

    def configure(self):
        if self.settings.os_build not in ["Macos", "Linux", "Windows"]:
            raise Exception("Clang is only provided for Macos, Linux and Windows!")

    @property
    def clang_folder_name(self):
        if self.settings.os_build == "Macos":
            return "clang+llvm-{}-x86_64-apple-darwin".format(self.version)
        elif self.settings.os_build == "Linux":
            return "clang+llvm-{}-x86_64-linux-gnu-ubuntu-16.04".format(self.version)
        elif self.settings.os_build == "Windows":
            raise Exception("FIXME: for windows")
            return "LLVM-{}-win64".format(self.version)
        else:
            raise Exception("Clang is only provided for Macos, Linux and Windows!")

    @property
    def clang_zip_name(self):
        if self.settings.os_build == "Macos":
            return "{}.tar.xz".format(self.clang_folder_name)
        elif self.settings.os_build == "Linux":
            return "{}.tar.xz".format(self.clang_folder_name)
        elif self.settings.os_build == "Windows":
            raise Exception("FIXME: for windows")
            return "{}.exe".format(self.clang_folder_name)
        else:
            raise Exception("Clang is only provided for Macos, Linux and Windows!")

    def build(self):
        download_url = "http://releases.llvm.org/{}/{}".format(self.version, self.clang_zip_name)
        self.output.warn("Downloading '{}'...".format(download_url))
        tools.download(download_url, self.clang_zip_name)
        tools.unzip(self.clang_zip_name)
        os.unlink(self.clang_zip_name)

    def package(self):
        self.copy("*", dst="", keep_path=True)

    def package_info(self):
        self.output.info("Using Clang {}".format(self.version))
        self.env_info.path.append(os.path.join(self.package_folder, self.clang_folder_name, "bin"))
        self.env_info.CC = os.path.join(self.package_folder, self.clang_folder_name, "bin", "clang")
        self.env_info.CXX = os.path.join(self.package_folder, self.clang_folder_name, "bin", "clang++")
