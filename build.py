from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="vtpl1", channel="stable",
                                 upload="https://api.bintray.com/conan/vtpl1/conan")
    builder.add_common_builds(shared_option_name="Expat:shared")
    builder.run()
