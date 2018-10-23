from conans import ConanFile, CMake, tools
import os

class CTPLTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "CTPL/0.0.2@omaralvarez/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)