# Package managers

Every package manager module should inherit `IPackageManger` class and implement its methods:

- `packages_newer_than(self, unix_time)`
- `package_files(self, pkg_name)`
- `package_info(self, app_name)`
- `provided_by(self, app_name)`

Also there should be unit test for every package manager. Please see [dnf test](https://github.com/FrostyX/tracer/blob/develop/tests/test_dnf.py) for example.
