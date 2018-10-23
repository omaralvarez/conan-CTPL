from conans import ConanFile, CMake, tools
import os


class CTPLConan(ConanFile):
    name = "CTPL"
    version = "0.0.2"
    description = "Modern and efficient C++ Thread Pool Library https://github.com/omaralvarez/CTPL"
    license = "Apache License 2.0"
    url = "https://github.com/omaralvarez/conan-CTPL"
    repo_url = "https://github.com/omaralvarez/CTPL"
    author = "Vitaliy Vitsentiy, Omar Alvarez"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run_command("git clone %s" % (self.repo_url))
    
    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="CTPL")
        cmake.install()

    def package(self):
        #self.copy("*.h")
        pass

    def package_id(self):
        self.info.header_only()
