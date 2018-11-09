import os
from conans import ConanFile
from conans.client import tools


class BoostConan(ConanFile):
    name = "Boost"
    version = "1.68.0"
    license = ""
    url = "self hosted"
    settings = "os", "compiler", "build_type", "arch"
    description = "Boost"
    build_requires = "Clang/7.0.0@tareqsiraj/stable"
    boost_libs = ["fiber", "filesystem", "program_options", "stacktrace"]

    @property
    def boost_folder_name(self):
        return "boost_{}".format(self.version.replace(".", "_"))

    @property
    def boost_zip_name(self):
        return "{}.tar.bz2".format(self.boost_folder_name)

    def source(self):
        download_url = "https://dl.bintray.com/boostorg/release/{}/source/{}".format(
            self.version, self.boost_zip_name
        )
        self.output.warn("Downloading '{}'...".format(download_url))
        tools.get(
            download_url,
            filename=self.boost_zip_name,
            sha256="7f6130bc3cf65f56a618888ce9d5ea704fa10b462be126ad053e80e553d6d8b7",
        )

    def boost_user_config_jam_contents(self):
        return "using clang : 7.0 : {} : <cxxflags>-std=c++2a ;".format("")

    def build(self):
        with open(os.path.join(self.boost_folder_name, "user-config.jam"), "w") as f:
            f.write(self.boost_user_config_jam_contents())

        command_line = "cd {} && ./bootstrap.sh".format(self.boost_folder_name)
        self.output.info(command_line)
        self.run(command_line)

        b2 = "./b2"
        if self.settings.os == "Windows":
            b2 = "b2.exe"
        command_line = f"""cd {self.boost_folder_name} && \
                           {b2} \
                                toolset=clang \
                                variant=release \
                                link=static \
                                --user-config=user-config.jam \
                                --prefix=install-boost \
                                -j {tools.cpu_count()} \
                                install \
                        """
        for lib in self.boost_libs:
            command_line = command_line + " --with-" + lib

        self.output.info(command_line)
        self.run(command_line)

    def package(self):
        self.copy(
            "*",
            dst="",
            src=os.path.join(f"{self.boost_folder_name}", "install-boost"),
            keep_path=True,
        )

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = [
            "libboost_fiber.a",
            "libboost_filesystem.a",
            "libboost_program_options.a",
            "libboost_stacktrace_addr2line.a",
            "libboost_stacktrace_basic.a",
            "libboost_stacktrace_noop.a",
            "libboost_system.a",
        ]
