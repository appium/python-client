# CHANGELOG

<!-- version list -->

## v5.2.1 (2025-08-14)

### Chores

- Revert version created by release script checking
  ([#1164](https://github.com/appium/python-client/pull/1164),
  [`04a8580`](https://github.com/appium/python-client/commit/04a8580f999843bc9d121c1ed4ce872761350f31))

- Use semantic release changelog instead of gitchangelog
  ([#1163](https://github.com/appium/python-client/pull/1163),
  [`dd3709e`](https://github.com/appium/python-client/commit/dd3709e084e802d6534d51151be1bd45456a4ebd))

- Use semantic-release for most of release script execution
  ([#1165](https://github.com/appium/python-client/pull/1165),
  [`f6c4687`](https://github.com/appium/python-client/commit/f6c46878c12ae0a8a9ff82e1e9755f325eb8e7cf))

### Documentation

- Manage sphinx stuff via uv ([#1162](https://github.com/appium/python-client/pull/1162),
  [`df66645`](https://github.com/appium/python-client/commit/df66645ab284193f8f673d491c8daddcce381a71))

- Update readme ([#1165](https://github.com/appium/python-client/pull/1165),
  [`f6c4687`](https://github.com/appium/python-client/commit/f6c46878c12ae0a8a9ff82e1e9755f325eb8e7cf))


## Unreleased

### Chores

- Revert version created by release script checking
  ([#1164](https://github.com/appium/python-client/pull/1164),
  [`04a8580`](https://github.com/appium/python-client/commit/04a8580f999843bc9d121c1ed4ce872761350f31))

- Use semantic release changelog instead of gitchangelog
  ([#1163](https://github.com/appium/python-client/pull/1163),
  [`dd3709e`](https://github.com/appium/python-client/commit/dd3709e084e802d6534d51151be1bd45456a4ebd))

### Documentation

- Manage sphinx stuff via uv ([#1162](https://github.com/appium/python-client/pull/1162),
  [`df66645`](https://github.com/appium/python-client/commit/df66645ab284193f8f673d491c8daddcce381a71))


## v5.2.0 (2025-08-07)

### Bug Fixes

- Restore mypy linting ([#1156](https://github.com/appium/python-client/pull/1156),
  [`d3c7511`](https://github.com/appium/python-client/commit/d3c7511d6cf6de3a4717b6c691d047785106bed5))

### Chores

- Update uv version ([#1160](https://github.com/appium/python-client/pull/1160),
  [`ee8af97`](https://github.com/appium/python-client/commit/ee8af97dcbfe7e129fedce066ccb4138c6c43329))

- Use uv build to build the package ([#1159](https://github.com/appium/python-client/pull/1159),
  [`c095f79`](https://github.com/appium/python-client/commit/c095f79997171ab076584fea94d6fac0bd3e23ce))

- Use uv for version ([#1160](https://github.com/appium/python-client/pull/1160),
  [`ee8af97`](https://github.com/appium/python-client/commit/ee8af97dcbfe7e129fedce066ccb4138c6c43329))

- Use version via uv ([#1160](https://github.com/appium/python-client/pull/1160),
  [`ee8af97`](https://github.com/appium/python-client/commit/ee8af97dcbfe7e129fedce066ccb4138c6c43329))

### Continuous Integration

- Add a script to automatically update uv.lock upon dependabot updates
  ([#1158](https://github.com/appium/python-client/pull/1158),
  [`1a1cf34`](https://github.com/appium/python-client/commit/1a1cf34975224a47b6365a5524d19a409a2ccffd))

### Features

- Switch package management from pipenv to uv
  ([#1155](https://github.com/appium/python-client/pull/1155),
  [`7af0fd4`](https://github.com/appium/python-client/commit/7af0fd4c1ffc3b52e912dae662199033b6c55f58))


## v5.1.3 (2025-08-07)

### Chores

- Fix some mypy ([#1153](https://github.com/appium/python-client/pull/1153),
  [`4e1aafd`](https://github.com/appium/python-client/commit/4e1aafd9a0580d9ce3e5aaaa0eb223dad16e4881))

- Fix some mypy errors ([#1153](https://github.com/appium/python-client/pull/1153),
  [`4e1aafd`](https://github.com/appium/python-client/commit/4e1aafd9a0580d9ce3e5aaaa0eb223dad16e4881))

- Revert protocol ([#1152](https://github.com/appium/python-client/pull/1152),
  [`ab6c7bb`](https://github.com/appium/python-client/commit/ab6c7bb5aa01ca1be729dfa85cd604c591af0615))

- Wrong usage of CanFindElements #1148 ([#1152](https://github.com/appium/python-client/pull/1152),
  [`ab6c7bb`](https://github.com/appium/python-client/commit/ab6c7bb5aa01ca1be729dfa85cd604c591af0615))

- **deps-dev**: Update pytest-cov requirement from ~=5.0 to ~=6.2
  ([#1136](https://github.com/appium/python-client/pull/1136),
  [`5e14916`](https://github.com/appium/python-client/commit/5e149160132d7a83d21d3a3252aeb2fe3f630306))

- **deps-dev**: Update ruff requirement from ~=0.12.4 to ~=0.12.5
  ([#1149](https://github.com/appium/python-client/pull/1149),
  [`1457866`](https://github.com/appium/python-client/commit/145786676474211a27f7ab1763afc73d545da2b2))

- **deps-dev**: Update ruff requirement from ~=0.12.5 to ~=0.12.7
  ([#1151](https://github.com/appium/python-client/pull/1151),
  [`abf210a`](https://github.com/appium/python-client/commit/abf210ab77015e475200f3db42f61e4eaa2a6773))

### Testing

- Add bidi example in test ([#1154](https://github.com/appium/python-client/pull/1154),
  [`f8922da`](https://github.com/appium/python-client/commit/f8922daa965e25db4322c7d77369a2e5c133e61e))

- Add bidi log example test ([#1154](https://github.com/appium/python-client/pull/1154),
  [`f8922da`](https://github.com/appium/python-client/commit/f8922daa965e25db4322c7d77369a2e5c133e61e))


## v5.1.2 (2025-07-23)

### Chores

- Fix typos ([#1133](https://github.com/appium/python-client/pull/1133),
  [`a1b33c3`](https://github.com/appium/python-client/commit/a1b33c3e632382316b73540a7339a51ad57b9a2b))

- Inherit CanFindElements ([#1148](https://github.com/appium/python-client/pull/1148),
  [`7ca9425`](https://github.com/appium/python-client/commit/7ca942533786b5e9fb991cee3bd4c373fc1e99b4))

- Remove unused commands ([#1132](https://github.com/appium/python-client/pull/1132),
  [`a5f0147`](https://github.com/appium/python-client/commit/a5f0147dabe7cf7c927b9ffeabb41a7672bef801))

- **deps**: Bump selenium from 4.32.0 to 4.33.0
  ([#1130](https://github.com/appium/python-client/pull/1130),
  [`617ba6c`](https://github.com/appium/python-client/commit/617ba6cd943ad4ca15148fae6ee1aed949d123ff))

- **deps-dev**: Update pytest requirement from ~=8.3 to ~=8.4
  ([#1134](https://github.com/appium/python-client/pull/1134),
  [`0f9dd3b`](https://github.com/appium/python-client/commit/0f9dd3bc22274998add55fb0c6fa4ba956f0a47f))

- **deps-dev**: Update ruff requirement from ~=0.11.10 to ~=0.11.11
  ([#1128](https://github.com/appium/python-client/pull/1128),
  [`2f2205f`](https://github.com/appium/python-client/commit/2f2205f1763a62992279c71e5e3cc518e7fc05c0))

- **deps-dev**: Update ruff requirement from ~=0.11.11 to ~=0.11.12
  ([#1131](https://github.com/appium/python-client/pull/1131),
  [`ba38ccd`](https://github.com/appium/python-client/commit/ba38ccdf2afd9b13641a8bcfb171329acf937b32))

- **deps-dev**: Update ruff requirement from ~=0.11.12 to ~=0.11.13
  ([#1135](https://github.com/appium/python-client/pull/1135),
  [`0887cc1`](https://github.com/appium/python-client/commit/0887cc1d6bb9d6accb46542ad83504f5f0718e1b))

- **deps-dev**: Update ruff requirement from ~=0.11.13 to ~=0.12.1
  ([#1139](https://github.com/appium/python-client/pull/1139),
  [`e75c58f`](https://github.com/appium/python-client/commit/e75c58f5548e930003d0c4fac485ad2a05cda8cb))

- **deps-dev**: Update ruff requirement from ~=0.11.8 to ~=0.11.10
  ([#1127](https://github.com/appium/python-client/pull/1127),
  [`128666e`](https://github.com/appium/python-client/commit/128666e7d858b52e75fb3778c7de95c39b0182db))

- **deps-dev**: Update ruff requirement from ~=0.12.1 to ~=0.12.2
  ([#1142](https://github.com/appium/python-client/pull/1142),
  [`884062d`](https://github.com/appium/python-client/commit/884062d045ea47e58d33478e2d0ad477c4aeffe5))

- **deps-dev**: Update ruff requirement from ~=0.12.2 to ~=0.12.3
  ([#1144](https://github.com/appium/python-client/pull/1144),
  [`772723b`](https://github.com/appium/python-client/commit/772723babc06888141163fd90c893fda1bd73996))

- **deps-dev**: Update ruff requirement from ~=0.12.3 to ~=0.12.4
  ([#1146](https://github.com/appium/python-client/pull/1146),
  [`d43a190`](https://github.com/appium/python-client/commit/d43a190cc99dcae31f13c074b7f7ac9e7552f9d9))

- **deps-dev**: Update tox requirement from ~=4.25 to ~=4.26
  ([#1126](https://github.com/appium/python-client/pull/1126),
  [`157ec01`](https://github.com/appium/python-client/commit/157ec011c279a56ebceb7bf5becd733c562ce9f3))

- **deps-dev**: Update tox requirement from ~=4.26 to ~=4.27
  ([#1138](https://github.com/appium/python-client/pull/1138),
  [`c0ed394`](https://github.com/appium/python-client/commit/c0ed394765cc8f7567edd069b36903b2bbde3883))

### Continuous Integration

- Apply prebuilt wda ([#1141](https://github.com/appium/python-client/pull/1141),
  [`e3bcc37`](https://github.com/appium/python-client/commit/e3bcc3768d44b1ff1c85711f5553141443f40d0b))

### Documentation

- Re-run the gen code ([#1129](https://github.com/appium/python-client/pull/1129),
  [`3457e49`](https://github.com/appium/python-client/commit/3457e499f04e3d34d881ef6362cabe0751dd7a2d))


## v5.1.1 (2025-05-06)

### Chores

- **deps**: Bump selenium from 4.31.0 to 4.32.0
  ([#1124](https://github.com/appium/python-client/pull/1124),
  [`9e27a99`](https://github.com/appium/python-client/commit/9e27a998113a31fcc1440e08f52cb79cd26a81d7))

### Documentation

- Update compatibility matrix
  ([`9e42c7f`](https://github.com/appium/python-client/commit/9e42c7faf7c298dec1b32d25d8e71328ec17c073))

- Update README.md
  ([`48371a7`](https://github.com/appium/python-client/commit/48371a7714fbdbb6bd7dabc5ae5762eb80be6fc6))


## v5.1.0 (2025-05-05)

### Chores

- **deps**: Bump selenium from 4.29.0 to 4.30.0
  ([#1108](https://github.com/appium/python-client/pull/1108),
  [`96f7e6b`](https://github.com/appium/python-client/commit/96f7e6bf2377bf1e07b30f8b3571fc24bdff9c7e))

- **deps**: Bump selenium from 4.30.0 to 4.31.0
  ([#1113](https://github.com/appium/python-client/pull/1113),
  [`f59f23d`](https://github.com/appium/python-client/commit/f59f23df08e7e3c4f64d63afcb81d22445d21010))

- **deps**: Update typing-extensions requirement
  ([#1115](https://github.com/appium/python-client/pull/1115),
  [`24f9f7f`](https://github.com/appium/python-client/commit/24f9f7f8530abf376f833ea73541288f569c9f31))

- **deps**: Update typing-extensions requirement
  ([#1112](https://github.com/appium/python-client/pull/1112),
  [`e3add90`](https://github.com/appium/python-client/commit/e3add903b79921bc2dc315affadb4571014f2e48))

- **deps-dev**: Update ruff requirement from ~=0.10.0 to ~=0.11.2
  ([#1107](https://github.com/appium/python-client/pull/1107),
  [`bfaefa1`](https://github.com/appium/python-client/commit/bfaefa1c458c5d98842a3c786d466a5094a824b8))

- **deps-dev**: Update ruff requirement from ~=0.11.2 to ~=0.11.3
  ([#1111](https://github.com/appium/python-client/pull/1111),
  [`c403235`](https://github.com/appium/python-client/commit/c4032354223833ccc62869f059233cb188f56774))

- **deps-dev**: Update ruff requirement from ~=0.11.3 to ~=0.11.4
  ([#1114](https://github.com/appium/python-client/pull/1114),
  [`d27b924`](https://github.com/appium/python-client/commit/d27b924185736524e24558575b1100e1b333b39a))

- **deps-dev**: Update ruff requirement from ~=0.11.4 to ~=0.11.7
  ([#1118](https://github.com/appium/python-client/pull/1118),
  [`c3b86b8`](https://github.com/appium/python-client/commit/c3b86b8adb26c0155ec4b72ffc295f7fbe57fd00))

- **deps-dev**: Update ruff requirement from ~=0.11.7 to ~=0.11.8
  ([#1122](https://github.com/appium/python-client/pull/1122),
  [`2680a28`](https://github.com/appium/python-client/commit/2680a28e16259089b370d747ef0d90fb8b043198))

- **deps-dev**: Update tox requirement from ~=4.24 to ~=4.25
  ([#1109](https://github.com/appium/python-client/pull/1109),
  [`a46dd88`](https://github.com/appium/python-client/commit/a46dd88500e48ac89ac05db0f066560eedb38730))

### Continuous Integration

- Tune CC title script
  ([`c37352a`](https://github.com/appium/python-client/commit/c37352ad2753aa6005fa5e52e56683335551d039))

### Features

- Add method for interacting with the Flutter integration driver
  ([#1123](https://github.com/appium/python-client/pull/1123),
  [`635e762`](https://github.com/appium/python-client/commit/635e762678dcfff721dab5e52da41e4609c1d114))

### Testing

- Use timeout in client_config instead of the global var
  ([#1120](https://github.com/appium/python-client/pull/1120),
  [`727631d`](https://github.com/appium/python-client/commit/727631d33087beca86ccacc6b931e162fd5b8c49))


## v5.0.0 (2025-03-24)

### Chores

- **deps-dev**: Update mock requirement from ~=5.1 to ~=5.2
  ([#1100](https://github.com/appium/python-client/pull/1100),
  [`bbc1e91`](https://github.com/appium/python-client/commit/bbc1e91543986724f86a07ffa3a2218c38b8d0d8))

- **deps-dev**: Update pre-commit requirement from ~=4.1 to ~=4.2
  ([#1104](https://github.com/appium/python-client/pull/1104),
  [`d2326b9`](https://github.com/appium/python-client/commit/d2326b9cc82a5be18feb191852061a5596393c70))

- **deps-dev**: Update ruff requirement from ~=0.9.10 to ~=0.10.0
  ([#1102](https://github.com/appium/python-client/pull/1102),
  [`6707365`](https://github.com/appium/python-client/commit/670736582711df1a5303c794ff58aa7d7127d649))

- **deps-dev**: Update ruff requirement from ~=0.9.5 to ~=0.9.7
  ([#1097](https://github.com/appium/python-client/pull/1097),
  [`74224e0`](https://github.com/appium/python-client/commit/74224e090e6ccbba51fa9fca4a7d097ea242ff4c))

- **deps-dev**: Update ruff requirement from ~=0.9.7 to ~=0.9.9
  ([#1099](https://github.com/appium/python-client/pull/1099),
  [`5605d9b`](https://github.com/appium/python-client/commit/5605d9b4bc07554bd66c9d339aeee9bda010aa55))

- **deps-dev**: Update ruff requirement from ~=0.9.9 to ~=0.9.10
  ([#1101](https://github.com/appium/python-client/pull/1101),
  [`4d8abfa`](https://github.com/appium/python-client/commit/4d8abfa041c67b0cd05f1ce7d7ea96572cb10a58))

### Features

- Define AppiumClientConfig ([#1070](https://github.com/appium/python-client/pull/1070),
  [`525d5b8`](https://github.com/appium/python-client/commit/525d5b8b5d8c9919470c4c5a191a6d5c1090027e))


## v4.5.1 (2025-02-22)

### Bug Fixes

- Prevent warning log when initialize a webdriver using version 4.5.0 (selenium v4.26+)
  ([#1098](https://github.com/appium/python-client/pull/1098),
  [`68ceca7`](https://github.com/appium/python-client/commit/68ceca73ac83cef40ec90bdbb73305e384073983))

### Chores

- **deps**: Bump selenium from 4.28.0 to 4.28.1
  ([#1088](https://github.com/appium/python-client/pull/1088),
  [`a1ead29`](https://github.com/appium/python-client/commit/a1ead29fc1c0aa156f1144b8f24bddb42358770a))

- **deps**: Bump selenium from 4.28.1 to 4.29.0
  ([#1096](https://github.com/appium/python-client/pull/1096),
  [`f53deb3`](https://github.com/appium/python-client/commit/f53deb3440a8b06a7f83726596eacc52eb1cfef4))

- **deps-dev**: Update pre-commit requirement from ~=3.5 to ~=4.1
  ([#1085](https://github.com/appium/python-client/pull/1085),
  [`e5201fd`](https://github.com/appium/python-client/commit/e5201fdb3028df44c993f0375680f605702e8369))

- **deps-dev**: Update ruff requirement from ~=0.9.2 to ~=0.9.3
  ([#1089](https://github.com/appium/python-client/pull/1089),
  [`f8a4f56`](https://github.com/appium/python-client/commit/f8a4f5693185d7f59156e55f13d80bc002b198a5))

- **deps-dev**: Update ruff requirement from ~=0.9.3 to ~=0.9.5
  ([#1092](https://github.com/appium/python-client/pull/1092),
  [`82c40b5`](https://github.com/appium/python-client/commit/82c40b50577d4155c3215724babc3ca56b587ac2))

- **deps-dev**: Update tox requirement from ~=4.23 to ~=4.24
  ([#1086](https://github.com/appium/python-client/pull/1086),
  [`121be97`](https://github.com/appium/python-client/commit/121be9769cd8bd631fd6423a341be9dfb7e1658c))

### Documentation

- Update README.md
  ([`733504e`](https://github.com/appium/python-client/commit/733504e8304ca6901363351ec29770fcf9719fe7))

### Testing

- Pytest does not require test classes unless you need grouping or fixtures with class scope.
  ([#1094](https://github.com/appium/python-client/pull/1094),
  [`2218933`](https://github.com/appium/python-client/commit/22189335caccd89daffc3519bba8c90360be5fd1))

- Use pytest without class-based structures, using parameterization for better reusability.
  ([#1095](https://github.com/appium/python-client/pull/1095),
  [`c2732dd`](https://github.com/appium/python-client/commit/c2732ddc85b7362de3fc9e59d0c97b4e3bd02496))


## v4.5.0 (2025-01-22)

### Chores

- Update tags
  ([`aa486f3`](https://github.com/appium/python-client/commit/aa486f3bd287fe00185bebb254b5b9b6bc0440fb))

- **deps**: Bump selenium from 4.27.1 to 4.28.0
  ([#1084](https://github.com/appium/python-client/pull/1084),
  [`b10a11e`](https://github.com/appium/python-client/commit/b10a11e051e5741db7c91bf05f390ce178a2e0bd))

- **deps-dev**: Update ruff requirement from ~=0.8.1 to ~=0.8.3
  ([#1074](https://github.com/appium/python-client/pull/1074),
  [`2605001`](https://github.com/appium/python-client/commit/2605001d5c1952779d289038966577cb4d2298b4))

- **deps-dev**: Update ruff requirement from ~=0.8.3 to ~=0.8.4
  ([#1078](https://github.com/appium/python-client/pull/1078),
  [`6d4c633`](https://github.com/appium/python-client/commit/6d4c633901a18c5797c1d84c1c06bf5652fc328b))

- **deps-dev**: Update ruff requirement from ~=0.8.4 to ~=0.8.5
  ([#1079](https://github.com/appium/python-client/pull/1079),
  [`5db72cf`](https://github.com/appium/python-client/commit/5db72cfb12b5e3c07f3280ad7fb006ceb04ee5b2))

- **deps-dev**: Update ruff requirement from ~=0.8.5 to ~=0.8.6
  ([#1080](https://github.com/appium/python-client/pull/1080),
  [`a1986d4`](https://github.com/appium/python-client/commit/a1986d4821d2878456eb2760be9487ee83c99c17))

- **deps-dev**: Update ruff requirement from ~=0.8.6 to ~=0.9.0
  ([#1081](https://github.com/appium/python-client/pull/1081),
  [`4cdbed7`](https://github.com/appium/python-client/commit/4cdbed78c9d45f9b59c0cfabfbcb5acb91901de1))

- **deps-dev**: Update ruff requirement from ~=0.9.0 to ~=0.9.1
  ([#1082](https://github.com/appium/python-client/pull/1082),
  [`8117add`](https://github.com/appium/python-client/commit/8117add172b4cfd0ad03c96d09873eb0162d649d))

- **deps-dev**: Update ruff requirement from ~=0.9.1 to ~=0.9.2
  ([#1083](https://github.com/appium/python-client/pull/1083),
  [`0ea049a`](https://github.com/appium/python-client/commit/0ea049af1db4f4cd89ce169879e38a6be354ca90))


## v4.4.0 (2024-11-29)

### Bug Fixes

- Adding selenium typing ([#1071](https://github.com/appium/python-client/pull/1071),
  [`00e9a6e`](https://github.com/appium/python-client/commit/00e9a6e6e934ab9c9cc1e92aacb05b6bbefd08ff))

- Using single quotes ([#1071](https://github.com/appium/python-client/pull/1071),
  [`00e9a6e`](https://github.com/appium/python-client/commit/00e9a6e6e934ab9c9cc1e92aacb05b6bbefd08ff))

### Chores

- Dump ruff
  ([`e4f06ab`](https://github.com/appium/python-client/commit/e4f06abf1f6bc302bde373071d1e3c007a67c03a))

- **deps**: Bump selenium from 4.26.1 to 4.27.0
  ([#1067](https://github.com/appium/python-client/pull/1067),
  [`ea61c2e`](https://github.com/appium/python-client/commit/ea61c2e8f80c64365610321ef0e6f512280fdbc0))

- **deps**: Bump selenium from 4.27.0 to 4.27.1
  ([#1068](https://github.com/appium/python-client/pull/1068),
  [`dd8ef74`](https://github.com/appium/python-client/commit/dd8ef742e850cb74fc0d2ed897e638278d696d42))

- **deps-dev**: Update ruff requirement from ~=0.7.3 to ~=0.7.4
  ([#1063](https://github.com/appium/python-client/pull/1063),
  [`fef190e`](https://github.com/appium/python-client/commit/fef190ed8064c9e6fe717fb1bdfee5019edc28f3))

### Features

- Added typing for AppiumBy ([#1071](https://github.com/appium/python-client/pull/1071),
  [`00e9a6e`](https://github.com/appium/python-client/commit/00e9a6e6e934ab9c9cc1e92aacb05b6bbefd08ff))

- Added typing for AppiumBy types ([#1071](https://github.com/appium/python-client/pull/1071),
  [`00e9a6e`](https://github.com/appium/python-client/commit/00e9a6e6e934ab9c9cc1e92aacb05b6bbefd08ff))


## v4.3.0 (2024-11-12)

### Chores

- Update pre-commit ([#1058](https://github.com/appium/python-client/pull/1058),
  [`cd1070a`](https://github.com/appium/python-client/commit/cd1070af807d7ff1c42e4d2270452560738e254d))

- **deps-dev**: Update ruff requirement from ~=0.7.0 to ~=0.7.2
  ([#1057](https://github.com/appium/python-client/pull/1057),
  [`86f4d48`](https://github.com/appium/python-client/commit/86f4d4847d09e9a1077d3126ebad6e0faca2b3b0))

- **deps-dev**: Update ruff requirement from ~=0.7.2 to ~=0.7.3
  ([#1060](https://github.com/appium/python-client/pull/1060),
  [`f26f763`](https://github.com/appium/python-client/commit/f26f763f138813781bb8d5382bf3c7c8ae61adf5))

### Documentation

- Update CHANGELOG.rst
  ([`6bd041a`](https://github.com/appium/python-client/commit/6bd041a8812bdf5a6a35a44ab4d207efab4a6854))

- Update the readme ([#1054](https://github.com/appium/python-client/pull/1054),
  [`94a6da7`](https://github.com/appium/python-client/commit/94a6da755ef3e3af88b0fba6322a2e69dc123d37))

### Features

- Require selenium 4.26+ ([#1054](https://github.com/appium/python-client/pull/1054),
  [`94a6da7`](https://github.com/appium/python-client/commit/94a6da755ef3e3af88b0fba6322a2e69dc123d37))

- Support selenium 4.26+: support ClientConfig and refactoring internal implementation
  ([#1054](https://github.com/appium/python-client/pull/1054),
  [`94a6da7`](https://github.com/appium/python-client/commit/94a6da755ef3e3af88b0fba6322a2e69dc123d37))


## v4.2.1 (2024-10-31)


## v4.1.1 (2024-10-31)

### Chores

- Allow selenium binging up to 4.25 ([#1055](https://github.com/appium/python-client/pull/1055),
  [`a22306e`](https://github.com/appium/python-client/commit/a22306ea1eb035148d8c801ff2c3321f4c02708c))

- Revert unnecessary change ([#1046](https://github.com/appium/python-client/pull/1046),
  [`27595c4`](https://github.com/appium/python-client/commit/27595c40cceb33219cecd28c14c0e8fbdb566a37))

- Update precommit config
  ([`b8daf2c`](https://github.com/appium/python-client/commit/b8daf2c67cbcdbbc10a75b9a45f4a415a5057b95))

- Update release script
  ([`7ac1fd9`](https://github.com/appium/python-client/commit/7ac1fd9bcdba2fa29bea8c2f746da30f5420920f))

- Use proper type declarations for methods returning self instances
  ([#1039](https://github.com/appium/python-client/pull/1039),
  [`be51520`](https://github.com/appium/python-client/commit/be51520d2e204a63035fc99eaa1f796db3fed615))

- Use ruff (isort, pylint and pyflakes) instead of individual isort, pylint and black libraries
  ([#1043](https://github.com/appium/python-client/pull/1043),
  [`8f2b059`](https://github.com/appium/python-client/commit/8f2b059586f9e73fb431043a655729f655719884))

- **deps**: Update selenium requirement from ~=4.24 to ~=4.25
  ([#1026](https://github.com/appium/python-client/pull/1026),
  [`5778a50`](https://github.com/appium/python-client/commit/5778a502fb6203395bc1e5043ddb430342593493))

- **deps**: Update sphinx requirement from <7.0,>=4.0 to >=4.0,<9.0
  ([#1009](https://github.com/appium/python-client/pull/1009),
  [`2dab159`](https://github.com/appium/python-client/commit/2dab159ef8cfd7d1b70ea382d4fd65246c7bc61e))

- **deps**: Update sphinx-rtd-theme requirement from <3.0 to <4.0
  ([#1040](https://github.com/appium/python-client/pull/1040),
  [`fdbd03a`](https://github.com/appium/python-client/commit/fdbd03ab6a966601223c1d3dadbff21363c2e1d3))

- **deps-dev**: Update pytest-cov requirement from ~=4.1 to ~=5.0
  ([#975](https://github.com/appium/python-client/pull/975),
  [`2c775ee`](https://github.com/appium/python-client/commit/2c775ee518c17b8a95d8ec1302d9fb1654498d12))

- **deps-dev**: Update ruff requirement from ~=0.6.9 to ~=0.7.0
  ([#1049](https://github.com/appium/python-client/pull/1049),
  [`36786ef`](https://github.com/appium/python-client/commit/36786ef9c504e06f16212a5730e0d9274dca8fad))

- **deps-dev**: Update tox requirement from ~=4.20 to ~=4.21
  ([#1037](https://github.com/appium/python-client/pull/1037),
  [`e4b40ae`](https://github.com/appium/python-client/commit/e4b40aefc573429d40d51b60ac03ca2961b3313e))

- **deps-dev**: Update tox requirement from ~=4.21 to ~=4.22
  ([#1047](https://github.com/appium/python-client/pull/1047),
  [`0a403bc`](https://github.com/appium/python-client/commit/0a403bcd650ae3e759b55ef370618364f897ccfa))

- **deps-dev**: Update tox requirement from ~=4.22 to ~=4.23
  ([#1048](https://github.com/appium/python-client/pull/1048),
  [`7ac6bb8`](https://github.com/appium/python-client/commit/7ac6bb833022b7dd6c753fd806904ab9f3e9fb79))

### Documentation

- Add options matrix in readme ([#1046](https://github.com/appium/python-client/pull/1046),
  [`27595c4`](https://github.com/appium/python-client/commit/27595c40cceb33219cecd28c14c0e8fbdb566a37))

- Add tweak pathds ([#1046](https://github.com/appium/python-client/pull/1046),
  [`27595c4`](https://github.com/appium/python-client/commit/27595c40cceb33219cecd28c14c0e8fbdb566a37))

- Update selenium compatibility matrix
  ([`f3632a6`](https://github.com/appium/python-client/commit/f3632a6a1f413dbabff1fd5b7c1f605b5b33fb8b))

### Features

- Add a separate function for service startup validation
  ([#1038](https://github.com/appium/python-client/pull/1038),
  [`90b9978`](https://github.com/appium/python-client/commit/90b9978601e834518b19092b3d66f241d6c420a5))

### Testing

- Cleanup duplicated tests more ([#1032](https://github.com/appium/python-client/pull/1032),
  [`fea88d1`](https://github.com/appium/python-client/commit/fea88d1397d2721fa4da8a48a1a1a5cd6bbde6c7))

- Cleanup func tests for ios more ([#1036](https://github.com/appium/python-client/pull/1036),
  [`2b48a09`](https://github.com/appium/python-client/commit/2b48a09a707e669b1d8caa9d48ca578ecc34f3e4))

- Cleanup functional tests and move to unit test to CI stable
  ([#1024](https://github.com/appium/python-client/pull/1024),
  [`9cdfe5c`](https://github.com/appium/python-client/commit/9cdfe5c7cb58c4cd9495a15658ed17a5681b79d6))

- Cleanup ios ([#1034](https://github.com/appium/python-client/pull/1034),
  [`8773351`](https://github.com/appium/python-client/commit/877335152c0e0e705e36867d4449631d5385925a))

- Cleanup test more ([#1032](https://github.com/appium/python-client/pull/1032),
  [`fea88d1`](https://github.com/appium/python-client/commit/fea88d1397d2721fa4da8a48a1a1a5cd6bbde6c7))

- Cleanup tests more ([#1033](https://github.com/appium/python-client/pull/1033),
  [`9a3a633`](https://github.com/appium/python-client/commit/9a3a6337c375d3ece124df459e231fbfd0f2d8b1))

- Just remove existing ones ([#1032](https://github.com/appium/python-client/pull/1032),
  [`fea88d1`](https://github.com/appium/python-client/commit/fea88d1397d2721fa4da8a48a1a1a5cd6bbde6c7))

- Remove some functional test which is tested in unit tets
  ([#1033](https://github.com/appium/python-client/pull/1033),
  [`9a3a633`](https://github.com/appium/python-client/commit/9a3a6337c375d3ece124df459e231fbfd0f2d8b1))

- Remvoe location tests ([#1033](https://github.com/appium/python-client/pull/1033),
  [`9a3a633`](https://github.com/appium/python-client/commit/9a3a6337c375d3ece124df459e231fbfd0f2d8b1))


## v4.2.0 (2024-09-23)

### Bug Fixes

- Add missing __init__.py ([#1029](https://github.com/appium/python-client/pull/1029),
  [`25da847`](https://github.com/appium/python-client/commit/25da8476e2826bf8d495030a395080ddc83bc7a7))

### Chores

- **deps**: Update selenium requirement from ~=4.23 to ~=4.24
  ([#1018](https://github.com/appium/python-client/pull/1018),
  [`8d53160`](https://github.com/appium/python-client/commit/8d531601d2ed0d2abf1a0ed253214afe630a418f))

- **deps-dev**: Update black requirement from <24.0.0 to <25.0.0
  ([#950](https://github.com/appium/python-client/pull/950),
  [`87ec961`](https://github.com/appium/python-client/commit/87ec96177e9a4bcec67099fbd3acb6d3e0a838fb))

- **deps-dev**: Update pylint requirement from ~=3.2.6 to ~=3.2.7
  ([#1019](https://github.com/appium/python-client/pull/1019),
  [`d8c1260`](https://github.com/appium/python-client/commit/d8c126009be3916058b926f1ea38770486fe7a10))

- **deps-dev**: Update tox requirement from ~=4.18 to ~=4.19
  ([#1020](https://github.com/appium/python-client/pull/1020),
  [`54a9ef1`](https://github.com/appium/python-client/commit/54a9ef17d349d7978b391825a9c0fe2a8ca266bf))

- **deps-dev**: Update tox requirement from ~=4.19 to ~=4.20
  ([#1021](https://github.com/appium/python-client/pull/1021),
  [`bb8d509`](https://github.com/appium/python-client/commit/bb8d50920f6dc417f38f7ee5fd74a783e9558b72))

### Documentation

- Modify readme
  ([`d0ad068`](https://github.com/appium/python-client/commit/d0ad06893d3b1635eacfa06e50a74cdcf874d019))

### Features

- Add flutter integration driver commands and tests
  ([#1022](https://github.com/appium/python-client/pull/1022),
  [`2ffa930`](https://github.com/appium/python-client/commit/2ffa930270b455131217c2d8373fd32096b2c95c))


## v4.1.0 (2024-08-17)

### Chores

- Remove non-reference variables, import and fix test names to run them properly
  ([#1006](https://github.com/appium/python-client/pull/1006),
  [`e34ca80`](https://github.com/appium/python-client/commit/e34ca80812713d16806ab09af7f35f98e5b7a846))

- **deps**: Update selenium requirement from ~=4.22 to ~=4.23
  ([#1003](https://github.com/appium/python-client/pull/1003),
  [`1c5321a`](https://github.com/appium/python-client/commit/1c5321abaf238ea752dc9a3581143328ce8b5b03))

- **deps-dev**: Update pylint requirement from ~=3.2.2 to ~=3.2.5
  ([#1000](https://github.com/appium/python-client/pull/1000),
  [`d20db86`](https://github.com/appium/python-client/commit/d20db86741220b9d155bf16391f41260cc0d552b))

- **deps-dev**: Update pylint requirement from ~=3.2.5 to ~=3.2.6
  ([#1005](https://github.com/appium/python-client/pull/1005),
  [`6d66d92`](https://github.com/appium/python-client/commit/6d66d92673956c3e077ecf6909b4662cc182dd72))

- **deps-dev**: Update pytest requirement from ~=8.2 to ~=8.3
  ([#1004](https://github.com/appium/python-client/pull/1004),
  [`e75f8e9`](https://github.com/appium/python-client/commit/e75f8e9274a80a17f324b112c55698b0b298d53c))

- **deps-dev**: Update tox requirement from ~=4.15 to ~=4.16
  ([#1002](https://github.com/appium/python-client/pull/1002),
  [`3f3f11a`](https://github.com/appium/python-client/commit/3f3f11aa5ab27a96e22fab10c74863b0380d2349))

- **deps-dev**: Update tox requirement from ~=4.16 to ~=4.18
  ([#1013](https://github.com/appium/python-client/pull/1013),
  [`f7b0256`](https://github.com/appium/python-client/commit/f7b0256d7821eab0d302995765a6bde34931164a))

### Continuous Integration

- Move Azure to GHA (Android) ([#1007](https://github.com/appium/python-client/pull/1007),
  [`b148174`](https://github.com/appium/python-client/commit/b148174f14e014ac961f185d3bac715e5c8e32c3))

- Moving to GHA ([#1010](https://github.com/appium/python-client/pull/1010),
  [`fb06ca1`](https://github.com/appium/python-client/commit/fb06ca12dbe4c1be936f0c0525a864ee932a5614))

- Run func_test_android4 ([#1010](https://github.com/appium/python-client/pull/1010),
  [`fb06ca1`](https://github.com/appium/python-client/commit/fb06ca12dbe4c1be936f0c0525a864ee932a5614))

- Run other android tests on GHA ([#1008](https://github.com/appium/python-client/pull/1008),
  [`0e13381`](https://github.com/appium/python-client/commit/0e13381c7c7b7b0f7a00d8a5145fd2b591a3763d))

- Run other android tests on GHA a few more
  ([#1008](https://github.com/appium/python-client/pull/1008),
  [`0e13381`](https://github.com/appium/python-client/commit/0e13381c7c7b7b0f7a00d8a5145fd2b591a3763d))

### Documentation

- Replace badge source ([#1012](https://github.com/appium/python-client/pull/1012),
  [`834c854`](https://github.com/appium/python-client/commit/834c8549b82ef0dd0d5a8307fe6635045b6c3ac0))

### Features

- Add app_path property ("appPath") to Mac2Options
  ([#1014](https://github.com/appium/python-client/pull/1014),
  [`18c4723`](https://github.com/appium/python-client/commit/18c4723e7f7ebfca104bff92a720c667f1269223))

### Testing

- Fix tests ([#1010](https://github.com/appium/python-client/pull/1010),
  [`fb06ca1`](https://github.com/appium/python-client/commit/fb06ca12dbe4c1be936f0c0525a864ee932a5614))


## v4.0.1 (2024-07-08)

### Bug Fixes

- Typo and update test ([#992](https://github.com/appium/python-client/pull/992),
  [`a9af896`](https://github.com/appium/python-client/commit/a9af896bc08735e2927c8ace90be2e420b09ce5e))

### Chores

- Add mobile: replacements to clipboard API wrappers
  ([#998](https://github.com/appium/python-client/pull/998),
  [`19d4f4b`](https://github.com/appium/python-client/commit/19d4f4b2ab02caed0dcbe781196698e279230d5b))

- Remove IOS_UIAUTOMATION ([#979](https://github.com/appium/python-client/pull/979),
  [`9e63569`](https://github.com/appium/python-client/commit/9e63569b570d7a897264110a18c621c7a25f72ae))

- **deps**: Update selenium requirement from ~=4.18 to ~=4.19
  ([#976](https://github.com/appium/python-client/pull/976),
  [`7bd1b06`](https://github.com/appium/python-client/commit/7bd1b0665028771d06036b2b31fe76d9d32490a4))

- **deps**: Update selenium requirement from ~=4.19 to ~=4.20
  ([#981](https://github.com/appium/python-client/pull/981),
  [`cdc715b`](https://github.com/appium/python-client/commit/cdc715b686e41ab39c61e37448b934f32aa498af))

- **deps**: Update selenium requirement from ~=4.20 to ~=4.21
  ([#991](https://github.com/appium/python-client/pull/991),
  [`850055d`](https://github.com/appium/python-client/commit/850055db9b5a44f30b0821f73672b19611173a27))

- **deps**: Update selenium requirement from ~=4.21 to ~=4.22
  ([#996](https://github.com/appium/python-client/pull/996),
  [`6e06805`](https://github.com/appium/python-client/commit/6e06805dc80f382a54442fa5a30de4ce4d3388c2))

- **deps**: Update sphinx-rtd-theme requirement from <2.0 to <3.0
  ([#935](https://github.com/appium/python-client/pull/935),
  [`81a50e3`](https://github.com/appium/python-client/commit/81a50e344d26e4124e8019d0736f6240ac46267b))

- **deps-dev**: Update pylint requirement from ~=3.1.0 to ~=3.2.2
  ([#993](https://github.com/appium/python-client/pull/993),
  [`fa7e6d4`](https://github.com/appium/python-client/commit/fa7e6d44e13ea586bcbe73a1ba4464b97516ff51))

- **deps-dev**: Update pytest requirement from ~=8.1 to ~=8.2
  ([#983](https://github.com/appium/python-client/pull/983),
  [`9c142b8`](https://github.com/appium/python-client/commit/9c142b8916269e420e5feb11b869feabf3eb583b))

- **deps-dev**: Update tox requirement from ~=4.14 to ~=4.15
  ([#982](https://github.com/appium/python-client/pull/982),
  [`7551deb`](https://github.com/appium/python-client/commit/7551deb2c2bd4331385f8a6fb7dd60762d113865))

- **deps-dev**: Update types-python-dateutil requirement
  ([#973](https://github.com/appium/python-client/pull/973),
  [`1871e4a`](https://github.com/appium/python-client/commit/1871e4af09dd54e66f4483d0951d1df09b60faa0))

### Continuous Integration

- Add initial gha to run by manual ([#984](https://github.com/appium/python-client/pull/984),
  [`328c8d3`](https://github.com/appium/python-client/commit/328c8d3d941352503d9ff69baa9dddea40eddfe4))

- Bump conventional-pr-action to v3 ([#989](https://github.com/appium/python-client/pull/989),
  [`f256501`](https://github.com/appium/python-client/commit/f2565016b4a6f4a5fe5381d843960f46a71a1b02))

- Enable trigger
  ([`f6e2b53`](https://github.com/appium/python-client/commit/f6e2b5335af8aef0e07c1d444fc85a0d7be6481d))

- Move the file
  ([`85e921c`](https://github.com/appium/python-client/commit/85e921c8a1149d27f5136f723140f9770ee692dd))

- Use gha instead of Azure for iOS in Azure
  ([#987](https://github.com/appium/python-client/pull/987),
  [`5442e60`](https://github.com/appium/python-client/commit/5442e60b6c219cfb539d73c3d2277148b9f8311c))

### Documentation

- Fix typo ([#992](https://github.com/appium/python-client/pull/992),
  [`a9af896`](https://github.com/appium/python-client/commit/a9af896bc08735e2927c8ace90be2e420b09ce5e))

- Missing appium python client version in the compatibility matrix
  ([`91aa2a1`](https://github.com/appium/python-client/commit/91aa2a11de3d4d9a7f36e062a932d7aba8d77ba1))

- Update docstring ([#986](https://github.com/appium/python-client/pull/986),
  [`67a561d`](https://github.com/appium/python-client/commit/67a561d40b814b68b76381731a4da99805d79b3f))

### Testing

- Fix one test ([#992](https://github.com/appium/python-client/pull/992),
  [`a9af896`](https://github.com/appium/python-client/commit/a9af896bc08735e2927c8ace90be2e420b09ce5e))


## v4.0.0 (2024-03-11)

### Chores

- Remove deprecated AppiumBy.WINDOWS_UI_AUTOMATION
  ([#968](https://github.com/appium/python-client/pull/968),
  [`706f3f5`](https://github.com/appium/python-client/commit/706f3f5e91b666f91f197e9149d959d6126b8b44))

- **deps-dev**: Update pylint requirement from ~=3.0.3 to ~=3.1.0
  ([#966](https://github.com/appium/python-client/pull/966),
  [`3330b9a`](https://github.com/appium/python-client/commit/3330b9ae75f67b8c1b572f837d7f3f1e2cfe7a82))

- **deps-dev**: Update pytest requirement from ~=8.0 to ~=8.1
  ([#969](https://github.com/appium/python-client/pull/969),
  [`9136957`](https://github.com/appium/python-client/commit/9136957c42190da413aa8ebf5173cbfe9b5fb39b))

- **deps-dev**: Update python-dateutil requirement from ~=2.8 to ~=2.9
  ([#967](https://github.com/appium/python-client/pull/967),
  [`08d7fbb`](https://github.com/appium/python-client/commit/08d7fbb4c0346744d34c383ec849fcbcfedb0c09))

- **deps-dev**: Update tox requirement from ~=4.12 to ~=4.13
  ([#957](https://github.com/appium/python-client/pull/957),
  [`12200e7`](https://github.com/appium/python-client/commit/12200e7adf18cfe145a735de7f083974a19d902f))

- **deps-dev**: Update tox requirement from ~=4.13 to ~=4.14
  ([#972](https://github.com/appium/python-client/pull/972),
  [`6492c27`](https://github.com/appium/python-client/commit/6492c27339b661b4fcd518a92c1c45d288d9de88))

### Documentation

- Update readme
  ([`aca3593`](https://github.com/appium/python-client/commit/aca359309c6e16c0848ca27489458035e72f0c4a))

### Features

- Remove MultiAction and TouchAction ([#960](https://github.com/appium/python-client/pull/960),
  [`4d8db65`](https://github.com/appium/python-client/commit/4d8db65bfb672180a9bd0a52a3254ddd1f4c5eb0))

### Breaking Changes

- Remove MultiAction and TouchAction as non-w3c WebDriver-defined methods. Please use w3c actions
  instead.


## v3.2.1 (2024-02-25)

### Bug Fixes

- Unclosed file <_io.BufferedReader name error by proper cleanup of subprocess.Popen process
  ([#965](https://github.com/appium/python-client/pull/965),
  [`ac9965d`](https://github.com/appium/python-client/commit/ac9965da3839d4709625d2912abc577f52bc2dc1))


## v3.2.0 (2024-02-23)

### Bug Fixes

- Add return self in MultiAction#add ([#964](https://github.com/appium/python-client/pull/964),
  [`2e0ff4e`](https://github.com/appium/python-client/commit/2e0ff4e043eb8efd114d0f9f1f9f5c99a7d08d96))

### Chores

- **deps**: Update selenium requirement from ~=4.15 to ~=4.17
  ([#948](https://github.com/appium/python-client/pull/948),
  [`bdac0b8`](https://github.com/appium/python-client/commit/bdac0b89b51d70ffea12df15adaec86ba4a986a2))

- **deps**: Update selenium requirement from ~=4.17 to ~=4.18
  ([#958](https://github.com/appium/python-client/pull/958),
  [`1c6dcdf`](https://github.com/appium/python-client/commit/1c6dcdf642aaaa46facc6174d80a339fa49684f4))

- **deps-dev**: Update pytest requirement from ~=7.4 to ~=8.0
  ([#953](https://github.com/appium/python-client/pull/953),
  [`92583ce`](https://github.com/appium/python-client/commit/92583ce39003b740bb5e57bbf2114d283d884d22))

- **deps-dev**: Update tox requirement from ~=4.11 to ~=4.12
  ([#947](https://github.com/appium/python-client/pull/947),
  [`5be0ea0`](https://github.com/appium/python-client/commit/5be0ea08ef291cff4651b23fb820812562e8cf0d))

### Documentation

- Tweak docstring ([#961](https://github.com/appium/python-client/pull/961),
  [`686d486`](https://github.com/appium/python-client/commit/686d4864185b86bc61038099be116ec68fe3c0c9))

- Update example in readme ([#945](https://github.com/appium/python-client/pull/945),
  [`e2d238e`](https://github.com/appium/python-client/commit/e2d238e10a526ab041e9fed428d996e14adde1ce))

- Update links ([#944](https://github.com/appium/python-client/pull/944),
  [`39a89c8`](https://github.com/appium/python-client/commit/39a89c86357d00ee12db2af74ea3906c118fdec0))

- Update W3C actions example in readme ([#946](https://github.com/appium/python-client/pull/946),
  [`ea9e09e`](https://github.com/appium/python-client/commit/ea9e09e45c0650a39b7861b15ece85f8a77fdbc9))

### Features

- Add pause in drag_and_drop ([#961](https://github.com/appium/python-client/pull/961),
  [`686d486`](https://github.com/appium/python-client/commit/686d4864185b86bc61038099be116ec68fe3c0c9))


## v3.1.1 (2023-12-14)

### Bug Fixes

- Self.command_executor instance in _update_command_executor
  ([#940](https://github.com/appium/python-client/pull/940),
  [`17639ea`](https://github.com/appium/python-client/commit/17639ea682c06fe5ea23fb5999dcf009b7baa36c))

- Typo in ActionHelpers ([#937](https://github.com/appium/python-client/pull/937),
  [`63770e8`](https://github.com/appium/python-client/commit/63770e8cba8c1d9d4bb3324b621bc96b037d242f))

### Chores

- **deps**: Update selenium requirement from ~=4.14 to ~=4.15
  ([#933](https://github.com/appium/python-client/pull/933),
  [`876233e`](https://github.com/appium/python-client/commit/876233e115ef68839f614e89f3dd7bd523222d36))

- **deps-dev**: Update pylint requirement from ~=3.0.1 to ~=3.0.3
  ([#939](https://github.com/appium/python-client/pull/939),
  [`69ca059`](https://github.com/appium/python-client/commit/69ca0595727043645d5c0d9488e2b51e77784075))

### Documentation

- Address options in the migration guide ([#929](https://github.com/appium/python-client/pull/929),
  [`1e281bf`](https://github.com/appium/python-client/commit/1e281bf085138ee85187770c263ffd91e5a83e58))

- Adress options in the migration guide ([#929](https://github.com/appium/python-client/pull/929),
  [`1e281bf`](https://github.com/appium/python-client/commit/1e281bf085138ee85187770c263ffd91e5a83e58))

- Update changelog
  ([`1a81153`](https://github.com/appium/python-client/commit/1a811534c92427885dfc1954deef4c2976d1c5b3))


## v3.1.0 (2023-10-13)

### Chores

- **deps**: Update selenium requirement from ~=4.12 to ~=4.13
  ([#915](https://github.com/appium/python-client/pull/915),
  [`894380b`](https://github.com/appium/python-client/commit/894380b697bef35f98510b41a8ddafb2a3d21aa8))

- **deps**: Update selenium requirement from ~=4.13 to ~=4.14
  ([#923](https://github.com/appium/python-client/pull/923),
  [`6f1cf34`](https://github.com/appium/python-client/commit/6f1cf34aa61551aaf37eb68a534ce4f8aca6a683))

- **deps-dev**: Update pylint requirement from ~=2.17.5 to ~=3.0.1
  ([#922](https://github.com/appium/python-client/pull/922),
  [`3d7324e`](https://github.com/appium/python-client/commit/3d7324e4aeae731e5eb01d3881f246a5bb753798))

### Continuous Integration

- Use appium from the release branch
  ([`8d58eb7`](https://github.com/appium/python-client/commit/8d58eb7e31331ea473d209c5bc42346fd7b8fe3d))

### Documentation

- Update README.md ([#912](https://github.com/appium/python-client/pull/912),
  [`fa7ba6e`](https://github.com/appium/python-client/commit/fa7ba6ee5ee91c914f69e34547993af62995462f))

- Update README.md for v3 ([#912](https://github.com/appium/python-client/pull/912),
  [`fa7ba6e`](https://github.com/appium/python-client/commit/fa7ba6ee5ee91c914f69e34547993af62995462f))

### Features

- Add missing platformVersion and browserName options
  ([#925](https://github.com/appium/python-client/pull/925),
  [`d93a6ca`](https://github.com/appium/python-client/commit/d93a6caadb071598454fb7af0569576258ac4093))


## v3.0.0 (2023-09-08)

### Bug Fixes

- Add missing dependencies for types-python-dateutil
  ([#891](https://github.com/appium/python-client/pull/891),
  [`78bbb73`](https://github.com/appium/python-client/commit/78bbb73fdea80eac98468096d8e187f2def8f866))

- Handle the situation where payload is already a dictionary
  ([#892](https://github.com/appium/python-client/pull/892),
  [`9edf6eb`](https://github.com/appium/python-client/commit/9edf6ebfff75d4b2d84b67e6601bed764613aa8e))

### Chores

- Run pre-commit autoupdate ([#890](https://github.com/appium/python-client/pull/890),
  [`0cf35fc`](https://github.com/appium/python-client/commit/0cf35fc2be341beae51e5ec14407ca73f16eb29e))

- Update isort revision to 5.12.0 ([#889](https://github.com/appium/python-client/pull/889),
  [`2853ac0`](https://github.com/appium/python-client/commit/2853ac0b8814cea4a6192c69b56b508a667042c8))

- **deps**: Update selenium requirement from ~=4.10 to ~=4.11
  ([#899](https://github.com/appium/python-client/pull/899),
  [`2223f11`](https://github.com/appium/python-client/commit/2223f11b213162b21984fbece871a210fea48e39))

- **deps-dev**: Update mock requirement from ~=5.0 to ~=5.1
  ([#893](https://github.com/appium/python-client/pull/893),
  [`5f11530`](https://github.com/appium/python-client/commit/5f11530f93306a3c4c669fce327b2aef30c5e58c))

- **deps-dev**: Update pylint requirement from ~=2.17.3 to ~=2.17.5
  ([#897](https://github.com/appium/python-client/pull/897),
  [`60b8ed5`](https://github.com/appium/python-client/commit/60b8ed5f9e50d056171f45994d811f6970a3f7d9))

- **deps-dev**: Update pytest requirement from ~=7.2 to ~=7.4
  ([#884](https://github.com/appium/python-client/pull/884),
  [`fb8415e`](https://github.com/appium/python-client/commit/fb8415edf11e5f7302e24df5c3354c0c69fe8776))

- **deps-dev**: Update tox requirement from ~=4.6 to ~=4.8
  ([#902](https://github.com/appium/python-client/pull/902),
  [`d5b84b8`](https://github.com/appium/python-client/commit/d5b84b899e4abad6afd914d0e5342476cb955de2))

- **deps-dev**: Update tox requirement from ~=4.8 to ~=4.11
  ([#906](https://github.com/appium/python-client/pull/906),
  [`e344b7a`](https://github.com/appium/python-client/commit/e344b7a27a55dceebcfda22842efa6dfe965e39b))

- **deps-dev**: Update typing-extensions requirement
  ([#885](https://github.com/appium/python-client/pull/885),
  [`43ad4db`](https://github.com/appium/python-client/commit/43ad4db272b8115e752177a8336a05dc3943e79e))

### Continuous Integration

- Add pylint_quotes for pylint to use single quote as primary method
  ([#886](https://github.com/appium/python-client/pull/886),
  [`b142e00`](https://github.com/appium/python-client/commit/b142e00e3f47065752c80f71f2f8cb80bf2500f7))

### Documentation

- Update changelogs and version
  ([`6496619`](https://github.com/appium/python-client/commit/64966198b542cabd7bdb4d0dd6bdb1a4f8f0bf08))

- Update README.md ([#898](https://github.com/appium/python-client/pull/898),
  [`a1792ff`](https://github.com/appium/python-client/commit/a1792ffa51f472dd631c406dcf2f92fe78ae47e5))

### Features

- Update selenium dependency to 4.12 ([#908](https://github.com/appium/python-client/pull/908),
  [`2e49569`](https://github.com/appium/python-client/commit/2e49569ed45751df4c6953466f9769336698c033))

### Refactoring

- Remove several previously deprecated APIs
  ([#909](https://github.com/appium/python-client/pull/909),
  [`264f202`](https://github.com/appium/python-client/commit/264f202ca5cd5cbcb1a139ef5cc29095d12e2cce))

### Testing

- Fix broken TestContextSwitching by replacing selendroid with ApiDemos
  ([#895](https://github.com/appium/python-client/pull/895),
  [`06fe1b5`](https://github.com/appium/python-client/commit/06fe1b5e558059c3608df9dcf3f66420e60952ee))

- Remove selendroid-test-app.apk from apps folder
  ([#895](https://github.com/appium/python-client/pull/895),
  [`06fe1b5`](https://github.com/appium/python-client/commit/06fe1b5e558059c3608df9dcf3f66420e60952ee))

- Remove unused import pytest from applications_tests.py
  ([#895](https://github.com/appium/python-client/pull/895),
  [`06fe1b5`](https://github.com/appium/python-client/commit/06fe1b5e558059c3608df9dcf3f66420e60952ee))

- Replace usage of selendroid app from 'test_install_app' in applications_tests.py
  ([#895](https://github.com/appium/python-client/pull/895),
  [`06fe1b5`](https://github.com/appium/python-client/commit/06fe1b5e558059c3608df9dcf3f66420e60952ee))

- Replace usage of selendroid app from 'test_install_app' in applications_tests.py
  ([#891](https://github.com/appium/python-client/pull/891),
  [`78bbb73`](https://github.com/appium/python-client/commit/78bbb73fdea80eac98468096d8e187f2def8f866))

- Selendroid cleanup ([#895](https://github.com/appium/python-client/pull/895),
  [`06fe1b5`](https://github.com/appium/python-client/commit/06fe1b5e558059c3608df9dcf3f66420e60952ee))

### Breaking Changes

- Removed obsolete all_sessions and session properties BREAKING CHANGE: Removed the obsolete
  start_activity method BREAKING CHANGE: Removed the obsolete end_test_coverage method BREAKING
  CHANGE: Removed the following obsolete arguments from the driver constructor:
  desired_capabilities, browser_profile, proxy BREAKING CHANGE: Removed obsolete set_value and
  set_text methods BREAKING CHANGE: Removed the obsolete MobileBy class BREAKING CHANGE: Removed
  obsolete application management methods: launch_app, close_app, reset BREAKING CHANGE: Removed
  obsolete IME methods: available_ime_engines, is_ime_active, activate_ime_engine,
  deactivate_ime_engine, active_ime_engine

- The minimum supported Python version set to 3.8 BREAKING CHANGE: The minimum supported selenium
  version set to 4.12


## v2.11.1 (2023-06-13)

### Chores

- Left a comment
  ([`54a082e`](https://github.com/appium/python-client/commit/54a082e3fd2b20cb505a9464d51c6be91c16a926))


## v2.11.0 (2023-06-09)

### Chores

- Set version with / ([#793](https://github.com/appium/python-client/pull/793),
  [`f304f65`](https://github.com/appium/python-client/commit/f304f6509796580111240770a5f310fa6536f11c))

- Update comment ([#793](https://github.com/appium/python-client/pull/793),
  [`f304f65`](https://github.com/appium/python-client/commit/f304f6509796580111240770a5f310fa6536f11c))

### Features

- Make the UA format with same as other clients
  ([#793](https://github.com/appium/python-client/pull/793),
  [`f304f65`](https://github.com/appium/python-client/commit/f304f6509796580111240770a5f310fa6536f11c))


## v2.10.2 (2023-06-08)

### Bug Fixes

- Update the constructor for compatibility with python client 4.10
  ([#879](https://github.com/appium/python-client/pull/879),
  [`c0f38bf`](https://github.com/appium/python-client/commit/c0f38bf293fbae141bed8a9c49643a7b8b75efed))

### Chores

- Nump the version
  ([`8bb7b4c`](https://github.com/appium/python-client/commit/8bb7b4ccac8f54d2922e90ace30108ef7dd70057))

- Remove duplicated clean command ([#809](https://github.com/appium/python-client/pull/809),
  [`2f45ef9`](https://github.com/appium/python-client/commit/2f45ef935c12dec2ab8de044ce6a1c1e0b9aa46f))

- Set the max selenium deps version ([#874](https://github.com/appium/python-client/pull/874),
  [`2e7a6a3`](https://github.com/appium/python-client/commit/2e7a6a3e80852883d30d3d5e3859a5fdd1e29eb6))

- **deps-dev**: Update pytest-cov requirement from ~=4.0 to ~=4.1
  ([#872](https://github.com/appium/python-client/pull/872),
  [`74f39ed`](https://github.com/appium/python-client/commit/74f39eda8129a45a9798b948733d726b76237973))

- **deps-dev**: Update tox requirement from ~=4.5 to ~=4.6
  ([#877](https://github.com/appium/python-client/pull/877),
  [`a4e4118`](https://github.com/appium/python-client/commit/a4e411848f7e46af4d0484925dbbc55061aee5f7))

- **deps-dev**: Update typing-extensions requirement
  ([#871](https://github.com/appium/python-client/pull/871),
  [`1e4c574`](https://github.com/appium/python-client/commit/1e4c574718bdbbb00fb6c81b7499f1a746294ab3))

### Continuous Integration

- Add py11 for the unit test ([#875](https://github.com/appium/python-client/pull/875),
  [`5a4b6d0`](https://github.com/appium/python-client/commit/5a4b6d0729601b3fdb821e93ebe24bf2d248c65b))

- Add python 11 ([#874](https://github.com/appium/python-client/pull/874),
  [`2e7a6a3`](https://github.com/appium/python-client/commit/2e7a6a3e80852883d30d3d5e3859a5fdd1e29eb6))

### Documentation

- Address version management recommendation in the readme
  ([#874](https://github.com/appium/python-client/pull/874),
  [`2e7a6a3`](https://github.com/appium/python-client/commit/2e7a6a3e80852883d30d3d5e3859a5fdd1e29eb6))

- Improve usage examples ([#873](https://github.com/appium/python-client/pull/873),
  [`1f6dec3`](https://github.com/appium/python-client/commit/1f6dec384e7c911a134662ee2393221d0af298b9))

- Merge the matrix pr into README.md ([#874](https://github.com/appium/python-client/pull/874),
  [`2e7a6a3`](https://github.com/appium/python-client/commit/2e7a6a3e80852883d30d3d5e3859a5fdd1e29eb6))


## v2.10.1 (2023-05-20)

### Bug Fixes

- W3C errors to exception classes mapping ([#869](https://github.com/appium/python-client/pull/869),
  [`5c20a35`](https://github.com/appium/python-client/commit/5c20a358ae94c996ea3ddd4964ad828005b17801))


## v2.10.0 (2023-05-11)

### Bug Fixes

- Update connection manager creation ([#864](https://github.com/appium/python-client/pull/864),
  [`2dbce79`](https://github.com/appium/python-client/commit/2dbce790fe6b87ff489a3dcf1d4872f9e2873595))

### Chores

- Bump and correct version
  ([`49d38dd`](https://github.com/appium/python-client/commit/49d38ddb18fc7341bb901a6642f15823a7bc80b6))

- **deps**: Update selenium requirement from ~=4.7 to ~=4.9
  ([#852](https://github.com/appium/python-client/pull/852),
  [`0cfa3ef`](https://github.com/appium/python-client/commit/0cfa3ef79ae93cb917ff76d446b57cefbec5ed8f))

- **deps-dev**: Update mypy requirement from ~=1.1 to ~=1.2
  ([#848](https://github.com/appium/python-client/pull/848),
  [`bb76339`](https://github.com/appium/python-client/commit/bb76339bc6b9bc3ae8eab7de1c416a1ff906317e))

- **deps-dev**: Update pylint requirement from ~=2.17.1 to ~=2.17.2
  ([#847](https://github.com/appium/python-client/pull/847),
  [`37e357b`](https://github.com/appium/python-client/commit/37e357b1371f0e76ddbe3d0954d3315df19c15d1))

- **deps-dev**: Update pylint requirement from ~=2.17.2 to ~=2.17.3
  ([#853](https://github.com/appium/python-client/pull/853),
  [`4031de2`](https://github.com/appium/python-client/commit/4031de2aad7918da0e3b083fc2be5a37865e4d79))

- **deps-dev**: Update tox requirement from ~=4.4 to ~=4.5
  ([#854](https://github.com/appium/python-client/pull/854),
  [`790ffed`](https://github.com/appium/python-client/commit/790ffedc4440db92666fb1a5b17193e7b5b88343))

### Refactoring

- Move driver-specific commands to use extensions (part1)
  ([#856](https://github.com/appium/python-client/pull/856),
  [`622f3df`](https://github.com/appium/python-client/commit/622f3df7f3871e7f3442af29ff274d855b10bb49))

- Move driver-specific commands to use extensions (part2)
  ([#859](https://github.com/appium/python-client/pull/859),
  [`d988f3c`](https://github.com/appium/python-client/commit/d988f3c51c03f61cca39289450c009aafb0fe30a))


## v2.9.0 (2023-04-01)

### Bug Fixes

- Set_value and set_text sent incorrect data
  ([#831](https://github.com/appium/python-client/pull/831),
  [`91dc04b`](https://github.com/appium/python-client/commit/91dc04bd4313227b860158cd0d72d45723bcc664))

### Chores

- **deps-dev**: Update mypy requirement from ~=0.991 to ~=1.0
  ([#828](https://github.com/appium/python-client/pull/828),
  [`2e19f0d`](https://github.com/appium/python-client/commit/2e19f0d8139c2ab265346f033b809cac4b49d118))

- **deps-dev**: Update mypy requirement from ~=1.0 to ~=1.1
  ([#836](https://github.com/appium/python-client/pull/836),
  [`8c845c1`](https://github.com/appium/python-client/commit/8c845c1a33c9ed6045e7f60884608ba1f7430817))

- **deps-dev**: Update pylint requirement from ~=2.15.10 to ~=2.16.0
  ([#826](https://github.com/appium/python-client/pull/826),
  [`6acf1f0`](https://github.com/appium/python-client/commit/6acf1f0577940c3cdf216d27ba1cedf122abee60))

- **deps-dev**: Update pylint requirement from ~=2.16.0 to ~=2.16.1
  ([#827](https://github.com/appium/python-client/pull/827),
  [`cb7d8c5`](https://github.com/appium/python-client/commit/cb7d8c508a23e5a57e70cfd6d942255c9109ef65))

- **deps-dev**: Update pylint requirement from ~=2.16.1 to ~=2.16.2
  ([#829](https://github.com/appium/python-client/pull/829),
  [`0cb646d`](https://github.com/appium/python-client/commit/0cb646d28053afa82b16a3daea0a408498893de8))

- **deps-dev**: Update pylint requirement from ~=2.16.2 to ~=2.16.3
  ([#834](https://github.com/appium/python-client/pull/834),
  [`11beb71`](https://github.com/appium/python-client/commit/11beb71f7b9d9ae4b96abac62a8ef901165bff06))

- **deps-dev**: Update pylint requirement from ~=2.16.3 to ~=2.17.0
  ([#838](https://github.com/appium/python-client/pull/838),
  [`cbcc539`](https://github.com/appium/python-client/commit/cbcc539827658c7aaa16147f8da7907405c59031))

- **deps-dev**: Update pylint requirement from ~=2.17.0 to ~=2.17.1
  ([#843](https://github.com/appium/python-client/pull/843),
  [`6d558c0`](https://github.com/appium/python-client/commit/6d558c0411e3e46d06f03c7fe72337e72699e599))

- **deps-dev**: Update tox requirement from ~=4.3 to ~=4.4
  ([#823](https://github.com/appium/python-client/pull/823),
  [`ec81af5`](https://github.com/appium/python-client/commit/ec81af5cec22ea1f9b390b8147d95895040789bb))

- **deps-dev**: Update typing-extensions requirement
  ([#830](https://github.com/appium/python-client/pull/830),
  [`c2a80fa`](https://github.com/appium/python-client/commit/c2a80fa716d3ff12b850019dd6638bfde909408f))

### Features

- Can provide a custom connection ([#844](https://github.com/appium/python-client/pull/844),
  [`2c92c04`](https://github.com/appium/python-client/commit/2c92c04b3d470ec00ce96d2696483ae02f4df0d8))

- Respect the given executor ([#844](https://github.com/appium/python-client/pull/844),
  [`2c92c04`](https://github.com/appium/python-client/commit/2c92c04b3d470ec00ce96d2696483ae02f4df0d8))


## v2.8.1 (2023-01-20)

### Chores

- Update docstring in touch_action.py ([#797](https://github.com/appium/python-client/pull/797),
  [`c8cb24a`](https://github.com/appium/python-client/commit/c8cb24a1a7c7e60821ef25462110283b4bc0408e))

- Update precommit ([#787](https://github.com/appium/python-client/pull/787),
  [`c78e240`](https://github.com/appium/python-client/commit/c78e2406b07ffefceff35ed3ffd52e89ef521dfd))

- **deps**: Update selenium requirement from ~=4.5 to ~=4.7
  ([#801](https://github.com/appium/python-client/pull/801),
  [`ab13d72`](https://github.com/appium/python-client/commit/ab13d7265d2956995806f73368e242170395d2b3))

- **deps**: Update sphinx requirement from <6.0,>=4.0 to >=4.0,<7.0
  ([#814](https://github.com/appium/python-client/pull/814),
  [`8b96d05`](https://github.com/appium/python-client/commit/8b96d054f2474f1a2349f144cd3f30d8613962b3))

- **deps-dev**: Update black requirement from ~=22.10.0 to ~=22.12.0
  ([#807](https://github.com/appium/python-client/pull/807),
  [`8c51dc3`](https://github.com/appium/python-client/commit/8c51dc3d06f6ffdfe6f556176012998fe8db524f))

- **deps-dev**: Update isort requirement from ~=5.10 to ~=5.11
  ([#808](https://github.com/appium/python-client/pull/808),
  [`8d8fb02`](https://github.com/appium/python-client/commit/8d8fb02bdb081f06cd51b8c39b74971c1ab81a55))

- **deps-dev**: Update mock requirement from ~=4.0 to ~=5.0
  ([#812](https://github.com/appium/python-client/pull/812),
  [`3c59823`](https://github.com/appium/python-client/commit/3c59823e94b5c19e60b00addc3454868897ac1df))

- **deps-dev**: Update mypy requirement from ~=0.982 to ~=0.991
  ([#798](https://github.com/appium/python-client/pull/798),
  [`47db483`](https://github.com/appium/python-client/commit/47db48349d7b90bc18f0df1b926e24287ccb5a06))

- **deps-dev**: Update pre-commit requirement from ~=2.20 to ~=2.21
  ([#811](https://github.com/appium/python-client/pull/811),
  [`55ac01f`](https://github.com/appium/python-client/commit/55ac01faaff90dd14a87b94193fb30bb8511f124))

- **deps-dev**: Update pylint requirement from ~=2.15.3 to ~=2.15.4
  ([#788](https://github.com/appium/python-client/pull/788),
  [`a41b2fc`](https://github.com/appium/python-client/commit/a41b2fc6c42a6f6318a08b0a7c19f0785cff41d4))

- **deps-dev**: Update pylint requirement from ~=2.15.4 to ~=2.15.5
  ([#790](https://github.com/appium/python-client/pull/790),
  [`6c27689`](https://github.com/appium/python-client/commit/6c2768931fc11a17dbed9f2b635ba4628c3426cc))

- **deps-dev**: Update pylint requirement from ~=2.15.5 to ~=2.15.6
  ([#799](https://github.com/appium/python-client/pull/799),
  [`63464f8`](https://github.com/appium/python-client/commit/63464f8a1c1e85afa2b03897e745f1c17d2fcb6c))

- **deps-dev**: Update pylint requirement from ~=2.15.6 to ~=2.15.7
  ([#800](https://github.com/appium/python-client/pull/800),
  [`36c602c`](https://github.com/appium/python-client/commit/36c602c4efc8385ae0cbf916cfa4e8e50b7868c9))

- **deps-dev**: Update pylint requirement from ~=2.15.7 to ~=2.15.8
  ([#804](https://github.com/appium/python-client/pull/804),
  [`3903e29`](https://github.com/appium/python-client/commit/3903e29d73cc6bd69fc9bf353a6c32714ec5ab97))

- **deps-dev**: Update pylint requirement from ~=2.15.8 to ~=2.15.9
  ([#810](https://github.com/appium/python-client/pull/810),
  [`644aa72`](https://github.com/appium/python-client/commit/644aa724b7939aae01bdcd055b0541bf879bde2b))

- **deps-dev**: Update pylint requirement from ~=2.15.9 to ~=2.15.10
  ([#816](https://github.com/appium/python-client/pull/816),
  [`01d96fd`](https://github.com/appium/python-client/commit/01d96fd8a4645c1ba0df89a8bdd372693f5c98b0))

- **deps-dev**: Update pytest requirement from ~=7.1 to ~=7.2
  ([#791](https://github.com/appium/python-client/pull/791),
  [`d5f7a25`](https://github.com/appium/python-client/commit/d5f7a2571f3bed15ad26edb5d1fd907c4508f965))

- **deps-dev**: Update tox requirement from ~=3.26 to ~=3.27
  ([#792](https://github.com/appium/python-client/pull/792),
  [`df5bcb8`](https://github.com/appium/python-client/commit/df5bcb8725e3fead2ada8e0f368fa9cd24ac3555))

- **deps-dev**: Update tox requirement from ~=3.27 to ~=4.0
  ([#806](https://github.com/appium/python-client/pull/806),
  [`45ca8cf`](https://github.com/appium/python-client/commit/45ca8cf6069dd515c1bd6bc4ae7656f7e2e7ed3a))

- **deps-dev**: Update tox requirement from ~=4.0 to ~=4.1
  ([#813](https://github.com/appium/python-client/pull/813),
  [`827011e`](https://github.com/appium/python-client/commit/827011e2dbe39c887edfb562848b9fb3eff54a1b))

- **deps-dev**: Update tox requirement from ~=4.1 to ~=4.2
  ([#815](https://github.com/appium/python-client/pull/815),
  [`7941203`](https://github.com/appium/python-client/commit/79412033c600a1369559d8b5cce084c471f072d9))

- **deps-dev**: Update tox requirement from ~=4.2 to ~=4.3
  ([#817](https://github.com/appium/python-client/pull/817),
  [`0651afc`](https://github.com/appium/python-client/commit/0651afcf2350e8dec41779d242d7c5972b39b174))

### Features

- Add status tentatively ([#820](https://github.com/appium/python-client/pull/820),
  [`431aba1`](https://github.com/appium/python-client/commit/431aba1de859df4d5b34bd1d0216d4a9caa53a0d))


## v2.7.1 (2022-10-11)

### Chores

- **deps**: Update selenium requirement from ~=4.4 to ~=4.5
  ([#780](https://github.com/appium/python-client/pull/780),
  [`905eca6`](https://github.com/appium/python-client/commit/905eca69daa252238def9618ddd52588e5a28976))

- **deps-dev**: Update black requirement from ~=22.8.0 to ~=22.10.0
  ([#784](https://github.com/appium/python-client/pull/784),
  [`c9e2632`](https://github.com/appium/python-client/commit/c9e2632e64214c96c1c19aad53734016dff59dfc))

- **deps-dev**: Update mypy requirement from ~=0.971 to ~=0.981
  ([#777](https://github.com/appium/python-client/pull/777),
  [`38c1fb3`](https://github.com/appium/python-client/commit/38c1fb31199cb22952e1089cb5a8da583f1dfff9))

- **deps-dev**: Update mypy requirement from ~=0.981 to ~=0.982
  ([#782](https://github.com/appium/python-client/pull/782),
  [`d7edba4`](https://github.com/appium/python-client/commit/d7edba49973613d5d6d74bebdb6e3c7b75f0dcec))

- **deps-dev**: Update pylint requirement from ~=2.15.2 to ~=2.15.3
  ([#774](https://github.com/appium/python-client/pull/774),
  [`7d82821`](https://github.com/appium/python-client/commit/7d82821a03a42827ebe13c71c2742e175545a192))

- **deps-dev**: Update pytest-cov requirement from ~=3.0 to ~=4.0
  ([#779](https://github.com/appium/python-client/pull/779),
  [`62bc72c`](https://github.com/appium/python-client/commit/62bc72ca114967490784823b1e1da6d11791f492))

- **deps-dev**: Update typing-extensions requirement
  ([#783](https://github.com/appium/python-client/pull/783),
  [`1848fdf`](https://github.com/appium/python-client/commit/1848fdf915dc57d22cc04964b69239f6bc3c7250))

### Continuous Integration

- Comment out win for now ([#773](https://github.com/appium/python-client/pull/773),
  [`46a09b8`](https://github.com/appium/python-client/commit/46a09b81028c0d1b87f21d4d1c42de674c074e07))

- Remove unit test section ([#773](https://github.com/appium/python-client/pull/773),
  [`46a09b8`](https://github.com/appium/python-client/commit/46a09b81028c0d1b87f21d4d1c42de674c074e07))

- Run unit tests on actions ([#773](https://github.com/appium/python-client/pull/773),
  [`46a09b8`](https://github.com/appium/python-client/commit/46a09b81028c0d1b87f21d4d1c42de674c074e07))

- Tweak trigger ([#773](https://github.com/appium/python-client/pull/773),
  [`46a09b8`](https://github.com/appium/python-client/commit/46a09b81028c0d1b87f21d4d1c42de674c074e07))

### Refactoring

- Make service startup failures more helpful
  ([#786](https://github.com/appium/python-client/pull/786),
  [`033071d`](https://github.com/appium/python-client/commit/033071d0603b9bade3bc49c92459b064ae574a02))


## v2.7.0 (2022-09-22)

### Bug Fixes

- Move dev-only dependencies to [dev-packages] section
  ([#772](https://github.com/appium/python-client/pull/772),
  [`1a0246c`](https://github.com/appium/python-client/commit/1a0246cec0c3bf5f98fbf8ac20e1d5258f8e3e4f))

### Chores

- **deps**: Update pylint requirement from ~=2.15.2 to ~=2.15.3
  ([#770](https://github.com/appium/python-client/pull/770),
  [`83f3c81`](https://github.com/appium/python-client/commit/83f3c817bd6f979b1febdf4d643640b2d6c49d82))

### Continuous Integration

- Fix runner name
  ([`02a39a3`](https://github.com/appium/python-client/commit/02a39a31b9829635e91498ceea2099af5a4a493f))

### Documentation

- Update changelog for 2.6.2
  ([`7a5fa26`](https://github.com/appium/python-client/commit/7a5fa26f3d066d311952a1b39983afa3e2c44547))

### Features

- Add appArguments option to WindowsOptions
  ([#768](https://github.com/appium/python-client/pull/768),
  [`85cb104`](https://github.com/appium/python-client/commit/85cb1042373012d4c21fab2482090fe25a9422ac))


## v2.6.2 (2022-09-16)

### Bug Fixes

- Use total_seconds property of timedelta ([#767](https://github.com/appium/python-client/pull/767),
  [`b31b5eb`](https://github.com/appium/python-client/commit/b31b5ebe19eeeaf4216c712d213ae93f576f5943))

### Chores

- **deps**: Bump black from 22.6.0 to 22.8.0
  ([#763](https://github.com/appium/python-client/pull/763),
  [`806d5df`](https://github.com/appium/python-client/commit/806d5dff7f5b60723d68f249e5da7656db6a836b))

- **deps**: Update astroid requirement from ~=2.9 to ~=2.12
  ([#762](https://github.com/appium/python-client/pull/762),
  [`89193b9`](https://github.com/appium/python-client/commit/89193b9b677cd4bb7c163a778450d17723c89798))

- **deps**: Update pylint requirement from ~=2.14.5 to ~=2.15.0
  ([#761](https://github.com/appium/python-client/pull/761),
  [`130766c`](https://github.com/appium/python-client/commit/130766c97910d44c997bffbb563edb2c8d6629b3))

- **deps**: Update pylint requirement from ~=2.15.0 to ~=2.15.2
  ([#765](https://github.com/appium/python-client/pull/765),
  [`7734ea2`](https://github.com/appium/python-client/commit/7734ea2fe3668809545db2729bb41c0f383a77cb))

- **deps**: Update tox requirement from ~=3.25 to ~=3.26
  ([#766](https://github.com/appium/python-client/pull/766),
  [`fbfccca`](https://github.com/appium/python-client/commit/fbfcccab17b49aa77063a80969a013b8246be861))

### Continuous Integration

- Add Conventional commit format validation
  ([#764](https://github.com/appium/python-client/pull/764),
  [`047e927`](https://github.com/appium/python-client/commit/047e9277db99c97b00f3fed7e008e3227a8e9f34))

- Update Conventional Commits config preset
  ([`98ab48d`](https://github.com/appium/python-client/commit/98ab48d6a3ebf108a4c45de20ef55b4aec5b09ea))

### Documentation

- Update changelog for 2.6.1
  ([`0a929c6`](https://github.com/appium/python-client/commit/0a929c6dc3a98a191995d70ba0160aaf256313f7))


## v2.6.1 (2022-08-11)

### Bug Fixes

- Backwards compatible behaviour of swipe and scroll in action_helpers
  ([#744](https://github.com/appium/python-client/pull/744),
  [`677c1a2`](https://github.com/appium/python-client/commit/677c1a2121053a0435f3e0d8f7798077a41aa067))

- Fix options in mac2 ([#759](https://github.com/appium/python-client/pull/759),
  [`0b711ae`](https://github.com/appium/python-client/commit/0b711aeb304e272f7b1a84ba59aa2bbd1edb4fb0))

- Move py.typed to the hierarchy root ([#751](https://github.com/appium/python-client/pull/751),
  [`af83bba`](https://github.com/appium/python-client/commit/af83bba3b75d501bb063313e7edb3216765a9042))

- Typos/copypaste in various options ([#750](https://github.com/appium/python-client/pull/750),
  [`c0b80dc`](https://github.com/appium/python-client/commit/c0b80dc8e8acf2f1c79a9e871f4ca23fb6d0b71d))

### Chores

- **deps**: Update mypy requirement from ~=0.961 to ~=0.971
  ([#749](https://github.com/appium/python-client/pull/749),
  [`2a41c39`](https://github.com/appium/python-client/commit/2a41c398b588d88030f5fd128487b9d3eeb0afb5))

- **deps**: Update pylint requirement from ~=2.14.3 to ~=2.14.4
  ([#742](https://github.com/appium/python-client/pull/742),
  [`23ed3be`](https://github.com/appium/python-client/commit/23ed3be57d613aae4dc7b1737f35e2577ffcc706))

- **deps**: Update pylint requirement from ~=2.14.4 to ~=2.14.5
  ([#747](https://github.com/appium/python-client/pull/747),
  [`8e10ad8`](https://github.com/appium/python-client/commit/8e10ad83ad1fc0948759a3830ce3d90cd0f53b46))

- **deps**: Update selenium requirement from ~=4.3 to ~=4.4
  ([#757](https://github.com/appium/python-client/pull/757),
  [`ff50af0`](https://github.com/appium/python-client/commit/ff50af081c75817f7e4bbfc582fcb0755214eac3))

- **deps**: Update typing-extensions requirement from ~=4.2 to ~=4.3
  ([#745](https://github.com/appium/python-client/pull/745),
  [`8f53696`](https://github.com/appium/python-client/commit/8f53696db85f00dcdaf7d8b969c30bcc24ce7d1d))

- **deps-dev**: Update pre-commit requirement from ~=2.19 to ~=2.20
  ([#746](https://github.com/appium/python-client/pull/746),
  [`217acf1`](https://github.com/appium/python-client/commit/217acf168e4c772d67a745509a9e51e70e643c10))

### Documentation

- Update changelog for 2.6.0
  ([`970f853`](https://github.com/appium/python-client/commit/970f8533e4b75c01fd592912a446344327dc0ac4))


## v2.6.0 (2022-06-28)

### Chores

- Improve autocompletion for methods returning self instance
  ([#739](https://github.com/appium/python-client/pull/739),
  [`ce4de83`](https://github.com/appium/python-client/commit/ce4de83b443b050e295c5c1af0938ce720198bc8))

- **deps**: Bump black from 22.3.0 to 22.6.0
  ([#741](https://github.com/appium/python-client/pull/741),
  [`ac39368`](https://github.com/appium/python-client/commit/ac39368b57bcb91ab72bdf09ed7b19f96a9f6544))

### Documentation

- Update changelog for 2.5.0
  ([`50458bb`](https://github.com/appium/python-client/commit/50458bb3b7ebc74a8a1d417c450b95e43201f0b1))

### Features

- Add Android drivers options ([#740](https://github.com/appium/python-client/pull/740),
  [`470e836`](https://github.com/appium/python-client/commit/470e83674ecce5e5ff947427ed0c443cb7df4ae1))

### Refactoring

- Remove previously deprecated methods and mark reset/close/launch APIs as deprecated
  ([#738](https://github.com/appium/python-client/pull/738),
  [`4c166f4`](https://github.com/appium/python-client/commit/4c166f45516a432ec807195f91fc2f208a3a3c08))


## v2.5.0 (2022-06-25)

### Chores

- Bump version to 2.4.0
  ([`c400357`](https://github.com/appium/python-client/commit/c400357ca0028e7a83124a91331cf69c31be91c4))

- **deps**: Update pylint requirement from ~=2.14.1 to ~=2.14.2
  ([#725](https://github.com/appium/python-client/pull/725),
  [`cc999ce`](https://github.com/appium/python-client/commit/cc999cea4a34510b42af22663c9c8d5037ab9bb2))

- **deps**: Update pylint requirement from ~=2.14.1 to ~=2.14.2
  ([#725](https://github.com/appium/python-client/pull/725),
  [`15b106c`](https://github.com/appium/python-client/commit/15b106c5769fc7b5307f8daecdcfbc7f3cc7dea4))

- **deps**: Update pylint requirement from ~=2.14.2 to ~=2.14.3
  ([#733](https://github.com/appium/python-client/pull/733),
  [`0a0cff2`](https://github.com/appium/python-client/commit/0a0cff2e02ad19a2cb336c3e92fcc7378ed57fe2))

- **deps**: Update selenium requirement from ~=4.2 to ~=4.3
  ([#736](https://github.com/appium/python-client/pull/736),
  [`6eca124`](https://github.com/appium/python-client/commit/6eca12427bcd8be6fd6760193b0321d5bc088a2b))

### Features

- Add Gecko driver options ([#735](https://github.com/appium/python-client/pull/735),
  [`b4e17a3`](https://github.com/appium/python-client/commit/b4e17a3a1efe33f08ac9ef883891b9fad4449a41))

- Add Mac2Driver options ([#730](https://github.com/appium/python-client/pull/730),
  [`312c229`](https://github.com/appium/python-client/commit/312c229fa89b6387236553c6f036085a835d3ed8))

- Add Safari driver options ([#731](https://github.com/appium/python-client/pull/731),
  [`2201e90`](https://github.com/appium/python-client/commit/2201e90eec53cd3df29ed9cfcb5ba94d300fb7a0))

- Add Windows driver options ([#732](https://github.com/appium/python-client/pull/732),
  [`d480eba`](https://github.com/appium/python-client/commit/d480ebaa1fcc52239d2a71d288e73e103f504429))

- Add xcuitest driver options ([#737](https://github.com/appium/python-client/pull/737),
  [`0264d81`](https://github.com/appium/python-client/commit/0264d81d60c30b187da7b2e58cc67f6aad0def5f))

### Refactoring

- Make system_port and system_host options common
  ([#734](https://github.com/appium/python-client/pull/734),
  [`5b958b5`](https://github.com/appium/python-client/commit/5b958b53f1df486314ca82cb35adce9161147aef))


## v2.4.0 (2022-06-17)

### Chores

- Add better error handling for session creation responses
  ([#727](https://github.com/appium/python-client/pull/727),
  [`22dfeca`](https://github.com/appium/python-client/commit/22dfeca560f8f0d5527bfdc0e0200055ee3e30f5))

- Update comments to locator patches ([#724](https://github.com/appium/python-client/pull/724),
  [`0fcea82`](https://github.com/appium/python-client/commit/0fcea82c9bcaf9137bc7b1591c37b092927751a2))

### Documentation

- Update changelog for 2.3.0
  ([`8321b9c`](https://github.com/appium/python-client/commit/8321b9c5122b1f848c34d0dc230e38d522e09fa9))

### Features

- Add common options ([#728](https://github.com/appium/python-client/pull/728),
  [`60ec7ce`](https://github.com/appium/python-client/commit/60ec7ce69a9224eab28af3e89bf9ea1acb920ac4))


## v2.3.0 (2022-06-13)

### Chores

- Disable pylint checks fail CI ([#719](https://github.com/appium/python-client/pull/719),
  [`a394281`](https://github.com/appium/python-client/commit/a3942815a7b60548785db0ea2f8506b25b0693e2))

- **deps**: Update mypy requirement from ~=0.942 to ~=0.950
  ([#712](https://github.com/appium/python-client/pull/712),
  [`336a762`](https://github.com/appium/python-client/commit/336a76257e809f5562e287d68322d9f256d880c7))

- **deps**: Update mypy requirement from ~=0.950 to ~=0.960
  ([#714](https://github.com/appium/python-client/pull/714),
  [`956417a`](https://github.com/appium/python-client/commit/956417a55de28123bcf2404ebbbc95b0d9fcd072))

- **deps**: Update mypy requirement from ~=0.960 to ~=0.961
  ([#718](https://github.com/appium/python-client/pull/718),
  [`0ff83df`](https://github.com/appium/python-client/commit/0ff83df100a4bae2d5547e0ba501b501890f6374))

- **deps**: Update selenium requirement from ~=4.1 to ~=4.2
  ([#715](https://github.com/appium/python-client/pull/715),
  [`697bb64`](https://github.com/appium/python-client/commit/697bb64db15378dfbcd6b4bc3f4931da520259a5))

- **deps**: Update sphinx requirement from <5.0,>=4.0 to >=4.0,<6.0
  ([#716](https://github.com/appium/python-client/pull/716),
  [`1385efc`](https://github.com/appium/python-client/commit/1385efc80d87cb50c600548229ff74d9106c402b))

- **deps**: Update tox requirement from ~=3.24 to ~=3.25
  ([#709](https://github.com/appium/python-client/pull/709),
  [`f5b0526`](https://github.com/appium/python-client/commit/f5b0526f903eee98f443b47d6fec7a4f1d0a4838))

- **deps**: Update typing-extensions requirement from ~=4.1 to ~=4.2
  ([#711](https://github.com/appium/python-client/pull/711),
  [`cb1a4ea`](https://github.com/appium/python-client/commit/cb1a4eaed0628a064deb70ba04fe5a5cd53312a4))

- **deps-dev**: Update pre-commit requirement from ~=2.17 to ~=2.18
  ([#708](https://github.com/appium/python-client/pull/708),
  [`4f8064f`](https://github.com/appium/python-client/commit/4f8064fff2d6d7f197112f2e83be0eacbbec4265))

- **deps-dev**: Update pre-commit requirement from ~=2.18 to ~=2.19
  ([#713](https://github.com/appium/python-client/pull/713),
  [`df33c85`](https://github.com/appium/python-client/commit/df33c85371d933ed0678f759ccf660343c66662a))

### Documentation

- Update README with the new options format
  ([#722](https://github.com/appium/python-client/pull/722),
  [`a2bba19`](https://github.com/appium/python-client/commit/a2bba19360a6205fc6f0679b595ae560181e70c3))

### Features

- Add base options for all supported automation names
  ([#721](https://github.com/appium/python-client/pull/721),
  [`d4c44b4`](https://github.com/appium/python-client/commit/d4c44b4b68c611be88007ee666ee8f59c79ce9f1))

- Add support for w3c options ([#720](https://github.com/appium/python-client/pull/720),
  [`c27138c`](https://github.com/appium/python-client/commit/c27138c0505a6595f9c5f48f3e4d3ccb996301cd))

### Testing

- Use Appium2 to run functional tests ([#723](https://github.com/appium/python-client/pull/723),
  [`b267665`](https://github.com/appium/python-client/commit/b26766583830ae83e20416629c8bdd24b58e5658))


## v2.2.0 (2022-03-30)

### Chores

- Relax selenium version as same as before
  ([`96681e9`](https://github.com/appium/python-client/commit/96681e924b4310bcaa23c839746b4923925a2d96))

- **deps**: Bump black from 22.1.0 to 22.3.0
  ([#705](https://github.com/appium/python-client/pull/705),
  [`79406bc`](https://github.com/appium/python-client/commit/79406bc044f564261e83d6a5ae689b0adcfc7632))

- **deps**: Update mypy requirement from ~=0.930 to ~=0.941
  ([#696](https://github.com/appium/python-client/pull/696),
  [`ce526e6`](https://github.com/appium/python-client/commit/ce526e6f587adcf9c37690dd1a427ec71871de3e))

- **deps**: Update mypy requirement from ~=0.941 to ~=0.942
  ([#703](https://github.com/appium/python-client/pull/703),
  [`56ce5b0`](https://github.com/appium/python-client/commit/56ce5b029a2e878f0fe0c97042f58372327d7a64))

- **deps**: Update pylint requirement from ~=2.12 to ~=2.13
  ([#702](https://github.com/appium/python-client/pull/702),
  [`8826bb3`](https://github.com/appium/python-client/commit/8826bb35ea529a480226361b87b3b345206a6493))

- **deps**: Update pytest requirement from ~=7.0 to ~=7.1
  ([#694](https://github.com/appium/python-client/pull/694),
  [`7dbf323`](https://github.com/appium/python-client/commit/7dbf3237bff5b503049c47d5815250acb8d6180a))

- **deps**: Update typing-extensions requirement from ~=4.0 to ~=4.1
  ([#684](https://github.com/appium/python-client/pull/684),
  [`23553df`](https://github.com/appium/python-client/commit/23553dfc7cb1a87e2fa79a81bb0f36b00bdc5169))

### Documentation

- Update missing changelog
  ([`c972382`](https://github.com/appium/python-client/commit/c97238216e828266819f82538c77a993fdf39cf2))

### Features

- Add non-w3c but still need commands ([#701](https://github.com/appium/python-client/pull/701),
  [`09a0cd0`](https://github.com/appium/python-client/commit/09a0cd0c72cc9e63c26c516f8bd8a4ac7b211808))


## v2.1.4 (2022-02-27)


## v2.1.3 (2022-02-25)

### Chores

- Bump mypy ([#675](https://github.com/appium/python-client/pull/675),
  [`72f942d`](https://github.com/appium/python-client/commit/72f942d2152ee1b0d7539f3bf2705b50d01133f7))

- Restrict selenium client version ([#686](https://github.com/appium/python-client/pull/686),
  [`2c04e4c`](https://github.com/appium/python-client/commit/2c04e4ce59ed04b91088ca55d1d3698653de6ebc))

- **deps**: Bump black from 21.12b0 to 22.1.0
  ([#681](https://github.com/appium/python-client/pull/681),
  [`7a7be33`](https://github.com/appium/python-client/commit/7a7be33827f8a92c3efbd9003c537ae259ad59cd))

- **deps**: Update pytest requirement from ~=6.2 to ~=7.0
  ([#682](https://github.com/appium/python-client/pull/682),
  [`588f83f`](https://github.com/appium/python-client/commit/588f83f28007d58e03c17759a5a5b807f4a08ae8))

- **deps-dev**: Update pre-commit requirement from ~=2.16 to ~=2.17
  ([#678](https://github.com/appium/python-client/pull/678),
  [`71410ba`](https://github.com/appium/python-client/commit/71410bab56522ae3ca36ee7fcb6dee349d6bc65a))

### Refactoring

- Update types descriptions for mixin classes
  ([#677](https://github.com/appium/python-client/pull/677),
  [`895cde1`](https://github.com/appium/python-client/commit/895cde1aa674aaab2f958ae251de0daefd049c02))

### Testing

- Update find element/s methods ([#674](https://github.com/appium/python-client/pull/674),
  [`7dbf4f2`](https://github.com/appium/python-client/commit/7dbf4f2f7ce43f60eded19fa247bb2177b65bafd))

- Update tests to use find_element(by...) ([#674](https://github.com/appium/python-client/pull/674),
  [`7dbf4f2`](https://github.com/appium/python-client/commit/7dbf4f2f7ce43f60eded19fa247bb2177b65bafd))


## v2.1.2 (2021-12-30)

### Bug Fixes

- Default duration in tap ([#673](https://github.com/appium/python-client/pull/673),
  [`24b50d8`](https://github.com/appium/python-client/commit/24b50d8138ea6ae008b0557991c0b5dcd75a15d0))


## v2.1.1 (2021-12-24)

### Chores

- Specify touch ([#670](https://github.com/appium/python-client/pull/670),
  [`6b21a67`](https://github.com/appium/python-client/commit/6b21a6713ff34eb5b8fca71fc24105ff6d2e1c0f))

- **deps**: Bump black from 21.11b1 to 21.12b0
  ([#664](https://github.com/appium/python-client/pull/664),
  [`02d6c8c`](https://github.com/appium/python-client/commit/02d6c8c5d21a1b3b135a5904edfa6acd03f1ac18))

- **deps**: Update astroid requirement from ~=2.8 to ~=2.9
  ([#661](https://github.com/appium/python-client/pull/661),
  [`758b2cd`](https://github.com/appium/python-client/commit/758b2cd37f075a08f492575e7b938206f2828fd6))

- **deps**: Update pylint requirement from ~=2.11 to ~=2.12
  ([#662](https://github.com/appium/python-client/pull/662),
  [`6c7c80c`](https://github.com/appium/python-client/commit/6c7c80c0c7211b9d5a2034a52d576738e53bdccb))

- **deps-dev**: Update pre-commit requirement from ~=2.15 to ~=2.16
  ([#663](https://github.com/appium/python-client/pull/663),
  [`1b94c5f`](https://github.com/appium/python-client/commit/1b94c5fa3568b90dc90d1d4bb5634a573d07aa5a))

### Continuous Integration

- Remove ==2021.5.29 ([#653](https://github.com/appium/python-client/pull/653),
  [`e5cb9ab`](https://github.com/appium/python-client/commit/e5cb9abee0272399289d698fba06a7ddd5fbd039))

### Features

- Use 'touch' pointer action ([#670](https://github.com/appium/python-client/pull/670),
  [`6b21a67`](https://github.com/appium/python-client/commit/6b21a6713ff34eb5b8fca71fc24105ff6d2e1c0f))


## v2.1.0 (2021-11-26)

### Chores

- Add deprecated mark for find_element_by*
  ([#657](https://github.com/appium/python-client/pull/657),
  [`d7cb6b5`](https://github.com/appium/python-client/commit/d7cb6b59598fb594b56d77c47abb02f4f07fa452))

- Relax selenium version control ([#656](https://github.com/appium/python-client/pull/656),
  [`ace98dc`](https://github.com/appium/python-client/commit/ace98dc0dd9be7cd468ddfd775f5f55d24f7fb1d))

- Tweak keyword in metadata
  ([`2a462be`](https://github.com/appium/python-client/commit/2a462becfe31dc4e18559ba246b0856fd3eb2488))

### Features

- Add AppiumBy instead of MobileBy ([#659](https://github.com/appium/python-client/pull/659),
  [`b70422b`](https://github.com/appium/python-client/commit/b70422b67f5254523ed360e1d196df0df04feab4))


## v2.0.0 (2021-11-08)

### Chores

- Add Deprecated for -windows uiautomation
  ([#649](https://github.com/appium/python-client/pull/649),
  [`8ec5441`](https://github.com/appium/python-client/commit/8ec5441d2b5074180eafd8cc7dc511e1d8615496))

- Add deprecated mark in MultiAction class
  ([#648](https://github.com/appium/python-client/pull/648),
  [`1a54fe9`](https://github.com/appium/python-client/commit/1a54fe9010d2305ab9ec2b6f2a6382279832f42d))

- Add deprecation mark in touch actions and multi touch
  ([#648](https://github.com/appium/python-client/pull/648),
  [`1a54fe9`](https://github.com/appium/python-client/commit/1a54fe9010d2305ab9ec2b6f2a6382279832f42d))

- Add logger ([#649](https://github.com/appium/python-client/pull/649),
  [`8ec5441`](https://github.com/appium/python-client/commit/8ec5441d2b5074180eafd8cc7dc511e1d8615496))

- Add Python 3.9 as metadata
  ([`f4d5489`](https://github.com/appium/python-client/commit/f4d5489ae576a3ad126aa99bca7531a89c153d6a))

- Adding deprecation mark in touch actions and multi touch
  ([#648](https://github.com/appium/python-client/pull/648),
  [`1a54fe9`](https://github.com/appium/python-client/commit/1a54fe9010d2305ab9ec2b6f2a6382279832f42d))

- Cleanup no longer needed code in w3c, bump dev Pipfile
  ([#646](https://github.com/appium/python-client/pull/646),
  [`658cadd`](https://github.com/appium/python-client/commit/658cadd065411caf5299450a610fe9fd725cdceb))

- Deprecate -windows uiautomation ([#649](https://github.com/appium/python-client/pull/649),
  [`8ec5441`](https://github.com/appium/python-client/commit/8ec5441d2b5074180eafd8cc7dc511e1d8615496))

- **deps**: Update isort requirement from ~=5.9 to ~=5.10
  ([#650](https://github.com/appium/python-client/pull/650),
  [`a195bf0`](https://github.com/appium/python-client/commit/a195bf0affb813ad1729a90b2096620b27eb5478))

- **deps**: Update pylint requirement from ~=2.10 to ~=2.11
  ([#638](https://github.com/appium/python-client/pull/638),
  [`9baa378`](https://github.com/appium/python-client/commit/9baa3786480c68f00e6bb1a6ea8c5b79fc4c0d62))

- **deps**: Update pytest-cov requirement from ~=2.12 to ~=3.0
  ([#641](https://github.com/appium/python-client/pull/641),
  [`4643402`](https://github.com/appium/python-client/commit/4643402c287dd75ef0ed68dee1e15229116cc00d))

- **deps**: Update sphinx requirement from <4.0,>=3.0 to >=3.0,<5.0
  ([#603](https://github.com/appium/python-client/pull/603),
  [`2df9031`](https://github.com/appium/python-client/commit/2df9031ea83701decd855f0bc8c33c6aaa09a0e5))

- **deps**: Update sphinx-rtd-theme requirement from <1.0 to <2.0
  ([#637](https://github.com/appium/python-client/pull/637),
  [`a2d3df1`](https://github.com/appium/python-client/commit/a2d3df1aa65654727aa8becc104e4c1207c84ab2))

### Continuous Integration

- Add --pre ([#651](https://github.com/appium/python-client/pull/651),
  [`9871231`](https://github.com/appium/python-client/commit/9871231bb89b089a1ac93bf7cbc35439a5783ea5))

- Set pipenv==2021.5.29 to prevent dependencies error
  ([#651](https://github.com/appium/python-client/pull/651),
  [`9871231`](https://github.com/appium/python-client/commit/9871231bb89b089a1ac93bf7cbc35439a5783ea5))

### Documentation

- Update readme
  ([`45b389d`](https://github.com/appium/python-client/commit/45b389d6e183561a57fef9c7c8ea28d15121093d))

- Update readme
  ([`4bc118b`](https://github.com/appium/python-client/commit/4bc118b2158712f972dd43136d32241f05dc94c7))

- Update readme ([#648](https://github.com/appium/python-client/pull/648),
  [`1a54fe9`](https://github.com/appium/python-client/commit/1a54fe9010d2305ab9ec2b6f2a6382279832f42d))

### Features

- Change base selenium client version to selenium 4
  ([#636](https://github.com/appium/python-client/pull/636),
  [`c7d4193`](https://github.com/appium/python-client/commit/c7d4193a26c766da66fa16ecb89fc698a781826c))


## v1.3.0 (2021-09-26)

### Chores

- Add placeholder ([#615](https://github.com/appium/python-client/pull/615),
  [`e48085d`](https://github.com/appium/python-client/commit/e48085d27968a93d9cfb5d86964ac84198b52214))

- **deps**: Update astroid requirement from ~=2.5 to ~=2.7
  ([#629](https://github.com/appium/python-client/pull/629),
  [`76ef1e7`](https://github.com/appium/python-client/commit/76ef1e77b6cb48ac62bee02e5b8003c5fa50a3e2))

- **deps**: Update mypy requirement from ~=0.812 to ~=0.910
  ([#616](https://github.com/appium/python-client/pull/616),
  [`5f603ce`](https://github.com/appium/python-client/commit/5f603cecb9464335f4e1b99e21a880dff12a958a))

- **deps**: Update pylint requirement from ~=2.8 to ~=2.10
  ([#628](https://github.com/appium/python-client/pull/628),
  [`36b4990`](https://github.com/appium/python-client/commit/36b4990bd8c34ce32cf013754058b3eb928d2186))

- **deps**: Update tox requirement from ~=3.23 to ~=3.24
  ([#619](https://github.com/appium/python-client/pull/619),
  [`bc9eb18`](https://github.com/appium/python-client/commit/bc9eb1850f3fb26392e2055ce082c055b86c18dd))

- **deps**: Update types-python-dateutil requirement
  ([#633](https://github.com/appium/python-client/pull/633),
  [`e85d7d4`](https://github.com/appium/python-client/commit/e85d7d402f93f24d21e116040a06d6ee95d2e5a6))

- **deps-dev**: Update pre-commit requirement from ~=2.13 to ~=2.15
  ([#634](https://github.com/appium/python-client/pull/634),
  [`31eda77`](https://github.com/appium/python-client/commit/31eda777d0761689b84a1503f6b7c896f1df361a))

### Features

- Add command with `setattr` ([#615](https://github.com/appium/python-client/pull/615),
  [`e48085d`](https://github.com/appium/python-client/commit/e48085d27968a93d9cfb5d86964ac84198b52214))

- Add satellites in set_location ([#620](https://github.com/appium/python-client/pull/620),
  [`cfb6ee6`](https://github.com/appium/python-client/commit/cfb6ee6487217d0b01c42b2b9d291779ea17dd85))

- Do not raise an error in case method is already defined
  ([#632](https://github.com/appium/python-client/pull/632),
  [`f8d3a38`](https://github.com/appium/python-client/commit/f8d3a38639557081700a273c5dcc641e42112aba))


## v1.2.0 (2021-06-06)

### Chores

- **deps**: Update isort requirement from ~=5.7 to ~=5.8
  ([#596](https://github.com/appium/python-client/pull/596),
  [`91a9d67`](https://github.com/appium/python-client/commit/91a9d6701430599637bb6895f9ffb078ee4bd052))

- **deps**: Update pylint requirement from ~=2.7 to ~=2.8
  ([#600](https://github.com/appium/python-client/pull/600),
  [`18db735`](https://github.com/appium/python-client/commit/18db7355a6f92be5f85fb7ef07b06b78bb9387af))

- **deps**: Update pytest-cov requirement from ~=2.11 to ~=2.12
  ([#606](https://github.com/appium/python-client/pull/606),
  [`ba408b7`](https://github.com/appium/python-client/commit/ba408b74f0d30fc06a51e77f68fc5cfd4ac8f99a))

- **deps-dev**: Update pre-commit requirement from ~=2.11 to ~=2.12
  ([#599](https://github.com/appium/python-client/pull/599),
  [`d0bfdd6`](https://github.com/appium/python-client/commit/d0bfdd63ca10a0950306d0e8e10a720317ce4d91))

- **deps-dev**: Update pre-commit requirement from ~=2.12 to ~=2.13
  ([#607](https://github.com/appium/python-client/pull/607),
  [`37258a3`](https://github.com/appium/python-client/commit/37258a392b630686797e3f7bdcc038bdd6e89d83))

### Features

- Allow to add a command dynamically ([#608](https://github.com/appium/python-client/pull/608),
  [`b4c15e2`](https://github.com/appium/python-client/commit/b4c15e2abe0ce477c2b7fc36cb78e8fd9aae12f0))


## v1.1.0 (2021-03-10)

### Chores

- Add table for screen_record kwarg ([#582](https://github.com/appium/python-client/pull/582),
  [`1a8c736`](https://github.com/appium/python-client/commit/1a8c73675b25aa3b33a591fddb6a56dce82cf647))

- Address selenium-4 branch in readme ([#566](https://github.com/appium/python-client/pull/566),
  [`9c7fbce`](https://github.com/appium/python-client/commit/9c7fbce68d97187a9d1aa07d13c86e0e291e39e4))

- Apply Black code formatter ([#571](https://github.com/appium/python-client/pull/571),
  [`344953a`](https://github.com/appium/python-client/commit/344953a49c7d66c77b2fa9b998a89a26d0e1f0d7))

- Fix functional keyboard tests with appium v1.21.0-beta.0
  ([#574](https://github.com/appium/python-client/pull/574),
  [`70048fc`](https://github.com/appium/python-client/commit/70048fc7c504aea1e57b6bc71c701db7beb60c2c))

- Fix iOS app management functional tests ([#575](https://github.com/appium/python-client/pull/575),
  [`74f599d`](https://github.com/appium/python-client/commit/74f599d847f9624221ce7b27aa2570231dd56de3))

- Update pipfile to respect isort v5 ([#577](https://github.com/appium/python-client/pull/577),
  [`173d3aa`](https://github.com/appium/python-client/commit/173d3aae4289015b0e9a28e5e3bb0e7ccc86061f))

- **deps**: Update astroid requirement from ~=2.4 to ~=2.5
  ([#587](https://github.com/appium/python-client/pull/587),
  [`d5f29f0`](https://github.com/appium/python-client/commit/d5f29f08a2fe9b5a9cca4162726c7cfb4faa42e9))

- **deps**: Update isort requirement from ~=5.0 to ~=5.7
  ([#578](https://github.com/appium/python-client/pull/578),
  [`3706e87`](https://github.com/appium/python-client/commit/3706e87068bd384895272fac6611c8f0c64716c8))

- **deps**: Update mypy requirement from ~=0.800 to ~=0.812
  ([#589](https://github.com/appium/python-client/pull/589),
  [`db035dd`](https://github.com/appium/python-client/commit/db035dd0f4cca60c33293951e1bc0761054b0cdc))

- **deps**: Update pylint requirement from ~=2.6 to ~=2.7
  ([#588](https://github.com/appium/python-client/pull/588),
  [`0ecad2f`](https://github.com/appium/python-client/commit/0ecad2fa1bf7e5e876372eede24f664492fd4fc5))

- **deps**: Update tox requirement from ~=3.21 to ~=3.22
  ([#586](https://github.com/appium/python-client/pull/586),
  [`3c31a65`](https://github.com/appium/python-client/commit/3c31a65cef9a93e065920e4add2d74b12bc0f436))

- **deps**: Update tox requirement from ~=3.22 to ~=3.23
  ([#593](https://github.com/appium/python-client/pull/593),
  [`66208fd`](https://github.com/appium/python-client/commit/66208fdbbc8f0a8b0e90376b404135b57e797fa5))

- **deps-dev**: Update pre-commit requirement from ~=2.10 to ~=2.11
  ([#595](https://github.com/appium/python-client/pull/595),
  [`e49dc78`](https://github.com/appium/python-client/commit/e49dc784d376145f12afe2f61a8ee7348c2ee08e))

### Continuous Integration

- Added py39-dev ([#557](https://github.com/appium/python-client/pull/557),
  [`1ae8c25`](https://github.com/appium/python-client/commit/1ae8c25d3e1da457f4a16710c0b04dc709140277))

- Added py39-dev for travis ([#557](https://github.com/appium/python-client/pull/557),
  [`1ae8c25`](https://github.com/appium/python-client/commit/1ae8c25d3e1da457f4a16710c0b04dc709140277))

- Move azure project to Appium CI, update readme
  ([#564](https://github.com/appium/python-client/pull/564),
  [`3e60e8f`](https://github.com/appium/python-client/commit/3e60e8fff4cfca93541c73c45f9662cdfe6475bc))

- Remove travis ([#581](https://github.com/appium/python-client/pull/581),
  [`1bf0553`](https://github.com/appium/python-client/commit/1bf05530dbccc2478a58bbd45fb8e0ce092bcceb))

- Upgrade xcode and macos ([#556](https://github.com/appium/python-client/pull/556),
  [`9402c6f`](https://github.com/appium/python-client/commit/9402c6ff99de70d42a1031db95bb934942b08a41))

- Upgrade xcode ver and macos ([#556](https://github.com/appium/python-client/pull/556),
  [`9402c6f`](https://github.com/appium/python-client/commit/9402c6ff99de70d42a1031db95bb934942b08a41))

- Use node v12 ([#585](https://github.com/appium/python-client/pull/585),
  [`8eb4c3f`](https://github.com/appium/python-client/commit/8eb4c3f7c2cb95ee81eb9c664de265edf473d9dc))

### Documentation

- Fix wrong code example in README.md ([#555](https://github.com/appium/python-client/pull/555),
  [`17af195`](https://github.com/appium/python-client/commit/17af19565cc1b443b2aecb86291db68a450c420f))

### Features

- Add optional location speed attribute for android devices
  ([#594](https://github.com/appium/python-client/pull/594),
  [`ce78c0d`](https://github.com/appium/python-client/commit/ce78c0de2e15307ae20a8cc3a496f6c794fdeec6))

- Add warning to drop forceMjsonwp for W3C
  ([#567](https://github.com/appium/python-client/pull/567),
  [`e51bcd2`](https://github.com/appium/python-client/commit/e51bcd269cab41b680971026e2974a2bf468a8a2))

- Added descriptions for newly added screenrecord opts
  ([#540](https://github.com/appium/python-client/pull/540),
  [`d8d4aea`](https://github.com/appium/python-client/commit/d8d4aea950e5c20d5299e131f9a9a5075a7d3aa4))

- Added docstring for macOS screenrecord option
  ([#580](https://github.com/appium/python-client/pull/580),
  [`ed5af31`](https://github.com/appium/python-client/commit/ed5af31a38e3bc34af32f601bf9ca0d800bcbc69))


## v1.0.2 (2020-07-15)

### Chores

- Add checking package file count comparison in release script
  ([#547](https://github.com/appium/python-client/pull/547),
  [`e3bd534`](https://github.com/appium/python-client/commit/e3bd5344697757bb8f1fc5722e132e13fa6e8194))

- Add file count in release script ([#547](https://github.com/appium/python-client/pull/547),
  [`e3bd534`](https://github.com/appium/python-client/commit/e3bd5344697757bb8f1fc5722e132e13fa6e8194))

- Add the workaround to avoid service freezes on Windows
  ([#552](https://github.com/appium/python-client/pull/552),
  [`95b01c9`](https://github.com/appium/python-client/commit/95b01c945241559c84804d897a1dddde2feb58d9))


## v1.0.1 (2020-05-18)

### Bug Fixes

- Broken package ([#545](https://github.com/appium/python-client/pull/545),
  [`e4e29f8`](https://github.com/appium/python-client/commit/e4e29f83f9feb4c1a6aa979e3c977af7ff996698))


## v1.0.0 (2020-05-17)

- Initial Release
