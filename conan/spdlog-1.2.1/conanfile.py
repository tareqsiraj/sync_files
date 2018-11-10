import os
from conans import ConanFile
from conans.client import tools


class SpdLogConan(ConanFile):
    name = "spdlog"
    version = "1.2.1"
    license = ""
    url = "self hosted"
    description = "SpdLog"

    @property
    def spdlog_folder_name(self):
        return f"spdlog-{self.version}"

    @property
    def spdlog_tar_gz_name(self):
        return f"v{self.version}.tar.gz"

    def source(self):
        download_url = (
            f"https://github.com/gabime/spdlog/archive/{self.spdlog_tar_gz_name}"
        )
        self.output.info(f"Downloading {download_url} ...")
        tools.get(
            download_url,
            filename=self.spdlog_tar_gz_name,
            sha256="867a4b7cedf9805e6f76d3ca41889679054f7e5a3b67722fe6d0eae41852a767",
        )

    def package(self):
        self.copy(
            "*",
            dst="include",
            src=os.path.join(self.spdlog_folder_name, "include"),
            keep_path=True,
        )

    def package_info(self):
        self.cpp_info.inclucedirs = ["include"]
