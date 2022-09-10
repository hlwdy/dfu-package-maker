# DFU包一键生成器
## 使用方法
Nordic的大部分蓝牙芯片，均可以使用dfu升级包进行烧录。

本python脚本借助Nordic官方的打包工具nrfutil完成DFU package的生成，已适用于Acconeer XM122毫米波雷达。

假设编译生成的input.hex文件位于Debug目录下，运行r.py将一键从hex生成zip包文件，打包完成文件为目录下的DFU_pac.zip。

最后运行push.bat脚本可以完成烧录操作(里面的COM串口可能需要更换)

## 需要准备的文件
首先，你需要生成一个位于本地的private.pem为使用的私钥。其次，你需要有编译好的hex文件。
### 生成Private Key
```
nrfutil keys generate private.pem
```
### 生成Public Key
```
nrfutil keys display --key pk --format code private.pem --out_file dfu_public_key.c
```
可将其添加到Bootloader工程中。

## 关于程序修改
nrfutil打包的命令行参数hw-version和sd-req可结合具体需要进行修改。
```
--hw-version INTEGER            The hardware version.(51/52)
--sd-req TEXT                   The SoftDevice requirements. A comma-
                                  separated list of SoftDevice firmware IDs (1
                                  or more) of which one must be present on the
                                  target device. Each item on the list must be
                                  a two- or four-digit hex number prefixed
                                  with "0x" (e.g. "0x12", "0x1234"). A non-
                                  exhaustive list of well-known values to use
                                  with this option follows:
                                  |s112_nrf52_6.0.0|0xA7|
                                  |s112_nrf52_6.1.0|0xB0|
                                  |s112_nrf52_6.1.1|0xB8|
                                  |s112_nrf52_7.0.0|0xC4|
                                  |s112_nrf52_7.0.1|0xCD|
                                  |s112_nrf52_7.2.0|0x103|
                                  |s112_nrf52_7.3.0|0x126|
                                  |s113_nrf52_7.0.0|0xC3|
                                  |s113_nrf52_7.0.1|0xCC|
                                  |s113_nrf52_7.2.0|0x102|
                                  |s113_nrf52_7.3.0|0x125|
                                  |s122_nrf52_8.0.0|0xEA|
                                  |s122_nrf52_8.1.1|0x112|
                                  |s130_nrf51_1.0.0|0x67|
                                  |s130_nrf51_2.0.0|0x80|
                                  |s130_nrf51_2.0.1|0x87|
                                  |s132_nrf52_2.0.0|0x81|
                                  |s132_nrf52_2.0.1|0x88|
                                  |s132_nrf52_3.0.0|0x8C|
                                  |s132_nrf52_3.1.0|0x91|
                                  |s132_nrf52_4.0.0|0x95|
                                  |s132_nrf52_4.0.2|0x98|
                                  |s132_nrf52_4.0.3|0x99|
                                  |s132_nrf52_4.0.4|0x9E|
                                  |s132_nrf52_4.0.5|0x9F|
                                  |s132_nrf52_5.0.0|0x9D|
                                  |s132_nrf52_5.1.0|0xA5|
                                  |s132_nrf52_6.0.0|0xA8|
                                  |s132_nrf52_6.1.0|0xAF|
                                  |s132_nrf52_6.1.1|0xB7|
                                  |s132_nrf52_7.0.0|0xC2|
                                  |s132_nrf52_7.0.1|0xCB|
                                  |s132_nrf52_7.2.0|0x101|
                                  |s132_nrf52_7.3.0|0x124|
                                  |s140_nrf52_6.0.0|0xA9|
                                  |s140_nrf52_6.1.0|0xAE|
                                  |s140_nrf52_6.1.1|0xB6|
                                  |s140_nrf52_7.0.0|0xC1|
                                  |s140_nrf52_7.0.1|0xCA|
                                  |s140_nrf52_7.2.0|0x100|
                                  |s140_nrf52_7.3.0|0x123|
                                  |s212_nrf52_6.1.1|0xBC|
                                  |s332_nrf52_6.1.1|0xBA|
                                  |s340_nrf52_6.1.1|0xB9|
```