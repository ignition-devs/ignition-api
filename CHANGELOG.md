# Changelog

All notable changes to this project will be documented in this file.

## [8.0.17.post6] - 2022-04-14

### Bug Fixes

- update type hint for `html` arg (#17) ([7012e4f](https://github.com/ignition-api/8.0/commit/7012e4fe0feb0e2fb499a9f29b6913d443ef86d5))

### CI

- fix packaging issues (#2) ([f1359c7](https://github.com/ignition-api/8.0/commit/f1359c724d8f62c2662acc4616e6d14c74b3fab5))
- update build action (#4) ([d3dff81](https://github.com/ignition-api/8.0/commit/d3dff812debbf4f2073ece1e6829134e9076b02f))
- add dependabot (#6) ([2317873](https://github.com/ignition-api/8.0/commit/2317873384e11fa7830c713fdf478b2bae553fd0))
- use `deps` scope for pre-commit.ci (#9) ([e0e6d54](https://github.com/ignition-api/8.0/commit/e0e6d5449eebb57b06f7f2da83a39c6d5edd176e))

### Documentation

- update downloads badge ([a999278](https://github.com/ignition-api/8.0/commit/a999278eaf5cc9ac8afcde8de4d89177920ce637))
- update project title (#3) ([61891b1](https://github.com/ignition-api/8.0/commit/61891b1d8cc46c1f53604e88edc268522aa85d70))
- replace old project name (#5) ([a9c6967](https://github.com/ignition-api/8.0/commit/a9c6967f8224de4a8ec6e6a03ea8f61e85ab111f))
- use pepy.tech for counting downloads (#12) ([1aeb699](https://github.com/ignition-api/8.0/commit/1aeb69993490b20ff6800c40ebd3a40fd9b40e29))
- add link to org CONTRIBUTING.md (#13) ([d559e6c](https://github.com/ignition-api/8.0/commit/d559e6ccb7b1155fa61de04219d746d642898862))

### Miscellaneous Tasks

- cleanup `.pylintrc` ([111e5bd](https://github.com/ignition-api/8.0/commit/111e5bd90478a17f7c5c72637bfb62e71437c7b4))
- move project to github org ([d947b00](https://github.com/ignition-api/8.0/commit/d947b00d9b7db209d28599fe49839169735b9711))

### Refactor

- Sourcery refactored main branch (#1) ([339de11](https://github.com/ignition-api/8.0/commit/339de11cfee09666adadd81d351d3eb83e70c8c5))
- improve Version comparison logic (#10) ([0fdb0e4](https://github.com/ignition-api/8.0/commit/0fdb0e48669bbebe7652545c9697f051415ec128))

### Styling

- format `pyproject.toml` with `pyproject-fmt` ([c5a65c7](https://github.com/ignition-api/8.0/commit/c5a65c7ecd634297a5e8b44282db1688eb83acd5))
- sort `__all__` ([414b74b](https://github.com/ignition-api/8.0/commit/414b74b1f398b7ec659dfb757e8328b34bc4701c))

### Build

- update black from 21.12b0 to 22.1.0 ([23c517d](https://github.com/ignition-api/8.0/commit/23c517dea2eb5913d276e2a1f7591e39d9ee4f4a))
- add `sort-all@v1.2.0` ([071969e](https://github.com/ignition-api/8.0/commit/071969e5033231d5c9b374864b5192111d5c1963))
- bump actions/setup-python from 2 to 3 (#7) ([98b2d9a](https://github.com/ignition-api/8.0/commit/98b2d9af2bc3227d64a909017410162c01e7ab2b))
- bump actions/checkout from 2 to 3 (#8) ([6689190](https://github.com/ignition-api/8.0/commit/6689190606b119e606d6ca37ca7c9112966b3236))
- bump .pylintrc from 2.12.2 to 2.13.2 (#11) ([e9b002b](https://github.com/ignition-api/8.0/commit/e9b002b4357175f2298128849c896384232fd7cb))
- pre-commit autoupdate (#14) ([ef4bd83](https://github.com/ignition-api/8.0/commit/ef4bd8385414a7caaabdd7511db17e12a0924f33))
- update pylint configuration (#15) ([74de37d](https://github.com/ignition-api/8.0/commit/74de37dc9017db88d383f46dfecff9de7c952176))

## [8.0.17.post5] - 2022-01-21

### Features

- update type hinting on `translate` ([96fa579](https://github.com/ignition-api/8.0/commit/96fa579adc6fc1f7a9ae5e10cdff3388363c63f7))

### Miscellaneous Tasks

- format `setup.cfg` ([7d3918b](https://github.com/ignition-api/8.0/commit/7d3918b4a1f822420d5ecbf875d6c9fdb54a8748))
- ignore pyenv file ([4f41b07](https://github.com/ignition-api/8.0/commit/4f41b07f3dde698b478328e326785b1e2fe04ae8))
- update .gitignore ([4ea9c74](https://github.com/ignition-api/8.0/commit/4ea9c741210d58521b210d4aeb6378d7dba263a3))

### Refactor

- define ColType as a type alias ([33ac2a7](https://github.com/ignition-api/8.0/commit/33ac2a7e940d9f0bfd237e938eaa548877c5dc68))
- move `String` alias to `java.util` ([0992a8c](https://github.com/ignition-api/8.0/commit/0992a8ce00318ddc08b125b2a74f5154e5edb7f9))

### Build

- remove files from `MANIFEST.in` ([c9a7b7c](https://github.com/ignition-api/8.0/commit/c9a7b7c0e60652549684df51428ae255196665df))

### Revert

- undo java.lang.String ([739c194](https://github.com/ignition-api/8.0/commit/739c194f46f1d17e0f9a8de120c7170f2db40190))

## [8.0.17.post4] - 2021-12-07

### CI

- update PyPI upload workflow ([42896c5](https://github.com/ignition-api/8.0/commit/42896c564b1ab4ff940d16396611952197f73ffa))

### Features

- improve `date.format` ([d29f20d](https://github.com/ignition-api/8.0/commit/d29f20d3cbdd49a755e0806ef3d911a2bb5cd1b8))
- add typing and supporting packages ([7e813d3](https://github.com/ignition-api/8.0/commit/7e813d3b660a6f7f3c3042cb4573a5953b23297a))

### Miscellaneous Tasks

- prepare for next release ([fe608c9](https://github.com/ignition-api/8.0/commit/fe608c95ebd52b21c108f6b6aaff4c5496f0cc09))
- mirror changes from main ([9105155](https://github.com/ignition-api/8.0/commit/9105155ca4bbd08c97676d4ee3bb11ff37d44529))
- add `cliff.toml` ([0446f00](https://github.com/ignition-api/8.0/commit/0446f00a52e28afb037003e66ef8cc86a8a88706))

### Refactor

- switch to informal interfaces ([6f16b00](https://github.com/ignition-api/8.0/commit/6f16b00e6a071ef7ede43b8390b7819342a418d3))
- informal interfaces ([6e433ea](https://github.com/ignition-api/8.0/commit/6e433ea7964ef12907b9f35b359b0789f2e19cd7))

### Build

- update pre-commit config and pyint workflow ([7eb692f](https://github.com/ignition-api/8.0/commit/7eb692f9443ac52b2eb09c7058c72bb33216ccef))
- update workflows ([50a6f83](https://github.com/ignition-api/8.0/commit/50a6f83778d71f9abacc16bab82c35e9d8fea95c))
- pre-commit autoupdate ([8e279b6](https://github.com/ignition-api/8.0/commit/8e279b693d7d8af5387af934f138b7fd8b4839c8))
- pre-commit autoupdate ([51fd6e1](https://github.com/ignition-api/8.0/commit/51fd6e187cb0237b2ffd2500c0cba11a245c50b6))
- deprecate Python 2.7 ([7dd8592](https://github.com/ignition-api/8.0/commit/7dd8592f812676b8a1bbe4067647cf53990d7931))
- pre-commit autoupdate ([ac5f4c7](https://github.com/ignition-api/8.0/commit/ac5f4c729a149501d84dbaa1bcc445718b061e46))
- pre-commit autoupdate ([33295f4](https://github.com/ignition-api/8.0/commit/33295f4f52d261d0f88b19b4797cf309cd643748))
- pre-commit autoupdate ([9c6d342](https://github.com/ignition-api/8.0/commit/9c6d3428f4de13a028e1d80ad49021a72fb5e513))
- use Python 2.7 for building package ([656324b](https://github.com/ignition-api/8.0/commit/656324b0d7394fa9af2399fa2476e4c376af6bd7))

## [8.0.17.post3] - 2021-09-21

### Features

- make PyDataSet iterable ([3d8186c](https://github.com/ignition-api/8.0/commit/3d8186c6b78dcdca0c9d981b5d2d943aa3d5757a))

## [8.0.17.post2] - 2021-09-20

### Bug Fixes

- correct typo in docstring ([23107c1](https://github.com/ignition-api/8.0/commit/23107c1ce86fcf8de5adc9b1a557836eca41de14))

### CI

- disable consider-using-f-string ([82594e0](https://github.com/ignition-api/8.0/commit/82594e043e2e5d0c03d3ca35d1c5daaa05954bed))

### Documentation

- update the copyright notice date ([330d7ef](https://github.com/ignition-api/8.0/commit/330d7ef4e79a2c78feeebf4658871a7b68197123))
- update README.md ([c7d6fb6](https://github.com/ignition-api/8.0/commit/c7d6fb612d7a5f459ada541ef1ca072c729aa883))
- update README.md ([a278d70](https://github.com/ignition-api/8.0/commit/a278d7055567b55a121377dc7cf93b4392549235))
- replaced datetime for Date ([fe6b4f7](https://github.com/ignition-api/8.0/commit/fe6b4f7aa1decf2c0c7efe5bd4991437f614dabe))
- :pencil2: fix typo ([7e14deb](https://github.com/ignition-api/8.0/commit/7e14deb83a18f97f407b456518a6f963a3d3cced))

### Features

- add build number and update all references ([43793ac](https://github.com/ignition-api/8.0/commit/43793acaf263bf3383b2ed981f30a986a657c781))
- add toParseableString implementation ([228a823](https://github.com/ignition-api/8.0/commit/228a823526ea4f982685d1f2238a284eea068aca))
- bump flake8 to 3.9.1 ([e7c3428](https://github.com/ignition-api/8.0/commit/e7c342805cb733112a9b0a4ea235e2224d9cf20e))
- update black 20.8b1 -> 21.4b0 ([935230c](https://github.com/ignition-api/8.0/commit/935230cc4af85d3c5b7f22669dccc70ee2e7874b))
- update black 21.4b0 -> 21.4b1 ([35e8d09](https://github.com/ignition-api/8.0/commit/35e8d09db6ba7197411518e25950d1d68b5d8c5f))
- update black 21.4b1 -> 21.4b2 ([e79334d](https://github.com/ignition-api/8.0/commit/e79334d99becc5f78372f5111033eb4897e59aa9))
- update black 21.4b2 -> 21.5b0 ([15c4ffc](https://github.com/ignition-api/8.0/commit/15c4ffc74674af97267b8c895e22305a4138977e))
- update flake8 3.9.1 -> 3.9.2 ([90dced2](https://github.com/ignition-api/8.0/commit/90dced229fa2fe7f17c9284c6fb78a62d89eb222))
- update black 21.5b0 -> 21.5b1 ([8406ab8](https://github.com/ignition-api/8.0/commit/8406ab8ae45b40bf2cb74a4362082b3f50dee522))
- add setup.py ([ae671d5](https://github.com/ignition-api/8.0/commit/ae671d512d0bb7ab06d8f88f4060a8ddc8a1155f))
- disallow installation on Python 3 ([20b5d0a](https://github.com/ignition-api/8.0/commit/20b5d0a5b1f2a67ee5a76f7dc1dc9938a5c9931c))
- add `com` package to `pip` release ([8237aa5](https://github.com/ignition-api/8.0/commit/8237aa534b4cadcbec0dd0c22ab2ace6dfed2f3b))

### Miscellaneous Tasks

- update .gitignore ([5a19721](https://github.com/ignition-api/8.0/commit/5a19721e7266428a0983c07d2832c4a3fabb9a2a))
- update .gitignore ([8763bbf](https://github.com/ignition-api/8.0/commit/8763bbfca677d0d1c87487bcaf3044d3a57d6dbc))
- add .wakatime-project ([d4261e2](https://github.com/ignition-api/8.0/commit/d4261e26a684c9880d603136c106f6a9437bf12e))

### Refactor

- java.util.Date ([91f164e](https://github.com/ignition-api/8.0/commit/91f164e9ccfdbad7161e0b015b4d9568efa32835))
- add pylint ([e893adb](https://github.com/ignition-api/8.0/commit/e893adb9b4d8ff653088259bbefab9c118cdf73c))
- add `com` package ([2a7fa49](https://github.com/ignition-api/8.0/commit/2a7fa49178f0f0844b3f21ad1e0f90155568f842))
- improve code quality ([a96322a](https://github.com/ignition-api/8.0/commit/a96322add85ef5f75f036d4d5aafb1aa437a836f))

### Styling

- :art: tell isort to use Python27 ([201abcb](https://github.com/ignition-api/8.0/commit/201abcb59aeac7da0635456e76676fdb949e1885))
- remove blank line ([bba432e](https://github.com/ignition-api/8.0/commit/bba432e308684b8961f17d818194e5abae03ade6))
- update docstrings ([ec13618](https://github.com/ignition-api/8.0/commit/ec13618ebe53123c44ccc77411d217adfcf549f0))
- change from single quotes to double quotes ([dcc38dd](https://github.com/ignition-api/8.0/commit/dcc38ddbcf6c2d816c40c77ba451c87d614f36b2))
- fix pylint found errors ([3887b4a](https://github.com/ignition-api/8.0/commit/3887b4a55ab21c0976872bacbfb45ccba1786c5e))

### Build

- bump flake8 and isort to latest version ([fe27c71](https://github.com/ignition-api/8.0/commit/fe27c7160dcae40443355dd58dffa9865ddae639))
- rearrange hooks ([f293b1c](https://github.com/ignition-api/8.0/commit/f293b1c522a76f6ae1b730587c4e844349fbbbe0))
- add pydocstyle hook ([4f14a9d](https://github.com/ignition-api/8.0/commit/4f14a9d2046c036ef696a85135199ab9a79655fe))
- remove D209 from ignored codes ([a9b7d12](https://github.com/ignition-api/8.0/commit/a9b7d121cff4dce642ada185d7bed646c0fa0645))
- remove E211 and E99 from ignore ([0e2318f](https://github.com/ignition-api/8.0/commit/0e2318f0acd2134932ab80c4a3aa01e57caad504))
- remove W503 from ignore ([04947ec](https://github.com/ignition-api/8.0/commit/04947ec983027f2e44b85f409215143a653e565e))
- update black 21.5b1 → 21.5b2 ([7addd05](https://github.com/ignition-api/8.0/commit/7addd05ae5c3b26ffa769e133b060bb64b12f7a4))
- pre-commit autoupdate ([11d5f53](https://github.com/ignition-api/8.0/commit/11d5f532612357261efbca9127ccfb91af5c5786))
- pre-commit autoupdate ([d854978](https://github.com/ignition-api/8.0/commit/d8549785457fba3287e0cb1b34cf08edc51441a7))
- check max complexity ([eeaa271](https://github.com/ignition-api/8.0/commit/eeaa271029d51ca17b5929efe5755c91e4ba8095))
- pre-commit autoupdate ([ad46b0a](https://github.com/ignition-api/8.0/commit/ad46b0a4a2ea5bbbf68e9ad26bb0cbeff6056514))
- update black from 21.6b0 to 21.7b0 ([3b57423](https://github.com/ignition-api/8.0/commit/3b57423a67fa74dbb14118913321fafab9973220))
- pre-commit autoupdate ([5c6ba18](https://github.com/ignition-api/8.0/commit/5c6ba18f7aa7e7397cd1f2aeaab3afd40a87d703))
- pre-commit autoupdate ([d19a279](https://github.com/ignition-api/8.0/commit/d19a2792b486f902a201bf7e5f881377f960f342))
- add pylint workflow ([477d799](https://github.com/ignition-api/8.0/commit/477d799486e6ca1fe9b35f4855f3de879576c177))
- skip pylint ([0905053](https://github.com/ignition-api/8.0/commit/090505332aeb43aab0b74ae946670b9cf3106e12))
- pre-commit autoupdate ([26d7332](https://github.com/ignition-api/8.0/commit/26d7332367780f58e113a7ccfd43c331e1a0d6c6))

## [8.0.17-fix] - 2021-02-13

### Features

- add flake8 to pre-commit hooks ([741e994](https://github.com/ignition-api/8.0/commit/741e99446f5ce1c445c0b6104319073915e3c2da))

### Miscellaneous Tasks

- modify .py files permission ([d0b17b4](https://github.com/ignition-api/8.0/commit/d0b17b468fb8a5f98fabe60917e4bcc2a86df0e3))
- add targeted Ignition version ([835fc55](https://github.com/ignition-api/8.0/commit/835fc55b3552485ea8d328d706a397f661240ef4))

### Styling

- Black ([5a8ad81](https://github.com/ignition-api/8.0/commit/5a8ad81bd485d0fb189c8df7fff6165e78536139))
- flake8 ([c686ba6](https://github.com/ignition-api/8.0/commit/c686ba69de97cd1a1ad082d7c70e25511767343d))
- add flake8 and isort badges ([3a38821](https://github.com/ignition-api/8.0/commit/3a38821f225486285df7a65d66ecdfed6dc8deae))
- :art: make isort compatible with black ([7547df1](https://github.com/ignition-api/8.0/commit/7547df1bc2f43d08fd8fea5a770729045b6d1cfc))

## [8.0.15] - 2020-09-04

### All

- Updated copyright legend. ([31c53f7](https://github.com/ignition-api/8.0/commit/31c53f7ad1f937a402cd52dd7fb0447fa508412f))

### Db

- Added getConnectionInfo and setDataSeourceEnabled. ([db6dfd6](https://github.com/ignition-api/8.0/commit/db6dfd69490d541557ca2cc15a11301ef746a331))

### File

- Fixed docstring. ([7f8a07d](https://github.com/ignition-api/8.0/commit/7f8a07d195ce4d77dbba7ab0732bdd54fc573f72))

### Incendium.gui

- added warning, modified error. Added java.lang, and javax.swing packages. Opting for JOptionPane over Ignition's own errorBox and warningBox. ([ff1c03e](https://github.com/ignition-api/8.0/commit/ff1c03edae7fb1bde5c4b9bc4cd67a6e439449c3))
- Modified info method in order to use JOptionPane. ([487231e](https://github.com/ignition-api/8.0/commit/487231e922023311c949f54093556c804c722567))
- Added input function. ([0d8320a](https://github.com/ignition-api/8.0/commit/0d8320a3dab50c997c95690f1b1105b7c064d54d))

### Incendium.util

- Added get_timer ([d9b0a70](https://github.com/ignition-api/8.0/commit/d9b0a706a8d011b43511708f16a3f28d1ea0c5d0))

### Java

- Updated copyright legend. ([b7a2f31](https://github.com/ignition-api/8.0/commit/b7a2f31b137d1cff24f55d97eb213dfd94a4485e))

### Javax

- Updated copyright legend. ([ab859d3](https://github.com/ignition-api/8.0/commit/ab859d36e2000bc7f2f737a5068216073a319e4c))

### Lang

- Throwable now inherits from BaseException. ([5f19240](https://github.com/ignition-api/8.0/commit/5f192403bad2fdea48f0103ec633c33772a4f942))

### Perspective

- Added missing methos to __all__ ([1f2dc97](https://github.com/ignition-api/8.0/commit/1f2dc9733ef33de55869cecb4888134a4a6f3a49))

### System

- Updated copyright legend. ([7b4852d](https://github.com/ignition-api/8.0/commit/7b4852d0a374777ec796bbf899d29f674f77be77))

### Tag

- Update docstring. ([f5e3cbc](https://github.com/ignition-api/8.0/commit/f5e3cbc981f252b025d77916d557f83eb748f12f))
- Code clean-up. ([fb53d8e](https://github.com/ignition-api/8.0/commit/fb53d8e0f1d5a2f1bfc2fdf217311d77f781cb8e))

### Util

- Added argument to winsound.MessageBeep funciton call. ([d06c492](https://github.com/ignition-api/8.0/commit/d06c492955347f2ca3b43ae7ad9ad442298c3638))

### Validate_form

- For numbers and collections we should compare to None. ([7a07ba5](https://github.com/ignition-api/8.0/commit/7a07ba5c278d40c620c189711be4a4f319858114))

<!-- generated by git-cliff -->
