# 搭建环境
## 开发板
***
## 开发工具
mbedOS支持三种开发工具：

1.在线IDE

2.mbed CLI控制台

3.第三方开发工具，如IAR，MDK

在线IDE编译很方便快捷，但没有调试功能。第三方的IDE都是可视化的，也没啥好介绍的。这里着重会来介绍mbed-cli，它的作用贯穿于整个mbed工作流：代码仓库版本控制、依赖管理、代码发布、从其他地方获取代码、调用编译系统及其他。无论你是用Windows还是Linux的主机，先准备好安装这四个工具：

- [Python](https://www.python.org/downloads/) - mbed CLI 是用Python写的，并且在 version 2.7.11 上做过完整测试，不兼容Python3.x.
- [Git](https://git-scm.com/) - version 1.9.5 or late.
- [Mercurial](https://www.mercurial-scm.org/) - version 2.2.2 or later.
- [GNU ARM](https://launchpad.net/gcc-arm-embedded) - ARM GCC交叉编译工具。

如果运行在Windows上，建议使用Git-Bash。Cygwin在后期编译的时候arm-gcc会有路径错误问题。如果在Linux下，以上这些Git，Mercurial，GNUARM等直接从仓库里下载即可。

通过Pypi安装mbed-cli:

    $ pip install mbed-cli

配置GCC的路径（GNU ARM的安装路径中bin目录）：
    
    $ mbed config --global GCC_ARM_PATH "C:\...\bin"

***
## 调试工具

### pyOCD

pyOCD是mbed官方提供的调试工具，使用Python开发，安装方法如下：
    
    $ pip install --pre -U pyocd

但是pyOCD有个最大的缺陷，monitor的命令非常少（只支持reset, init, halt），对于调试来说手段很有限。所以这里会比较推荐OpenOCD。

### OpenOCD

非常强大的开源OCD，支持的调试接口非常多，不局限于CMSIS-DAP，还支持包括Jlink，OSBDM，ULINK，ST-LINK等等。简单的安装方式是下载GNU ARM Eclipse OCD包：[gnuarmeclipse/openocd](https://github.com/gnu-mcu-eclipse/openocd/releases) 。如果从OpenOCD官网下载，你还需要编译源代码。

### 其它

- 串口工具装一个，方便调试。Putty, minicom，串口调试助手等都可以。
- [mbed serial](https://os.mbed.com/handbook/Windows-serial-configuration)，Windows串口驱动，Linux不需要。

***
## 编译系统及配置
..................
***
# 开始项目

## 导入项目

    $ mbed import <url>

和repo init + sync类似。URL可以是完整的git repo路径（可在[github](https://github.com/)搜索mbed-os-example），如果只给项目名称，会直接导入[ARM mbed](https://github.com/ARMmbed/)里的项目：

    $ mbed import mbed-os-example-client

该命令会处理模块之间的依赖关系，会检查mbed_app.json配置及.lib文件。确保所有依赖的项目源文件都被下载。如果你用git clone将mbed-os-example-client克隆下来，那么依赖库不会被同时下载，需要使用下面的命令：

    $ mbed deploy

## 创建新项目
    $ mbed new <项目名>
默认会生成**项目名**文件夹并下载mbedOS这个依赖库，如果需要其他库，可以用下面的命令:
    
    $ mbed add <git repo url>

mbed会自动下载，保存在子目录下，并且帮你生产.lib文件。不需要这个依赖库时，可以使用remove命令删除.lib及源文件。  
如果已有文件夹，cd至此目录执行：

	$ mbed add .
则会自动下载OS依赖库。

## 编译
编译需要指定target及toolchain：
   
    $ mbed compile -m K64F -t GCC_ARM
> [-m MCU]、[-t toolchain]、[-s SERIAL]、[-b BUILD]等

指定一次即可，后面可以直接使用compile编译，如果需要clean build，加上-c.  
目前支持的工具链有：  
**ARM**, **ARMC6**, _**GCC___ARM**_, **IAR**, **uARM**等，支持的MCU有 **NRF52_DK **, **NRF52840_DK**, **K64F**, **K66F**等。  
## 烧写
以NRF52840为例，直接将生成.hex或者.bin文件拷贝至flash中即可，重启开发板，程序开始运行。
## 调试
参照OpenOcd调试
