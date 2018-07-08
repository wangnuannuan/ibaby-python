## Bootloader配置

详细介绍每个Bootloader配置的参数。
有4个配置参数会影响ROM中应用程序的位置：

- target.mbed_app_start
- target.mbed_app_size
- target.bootloader_img
- target.restrict_size
- target.header_format
- target.header_offset
- target.app_offset

所有这些参数在`targets.json`, `mbed_lib.json` 和 `mbed_app.json`有效。您可以为单个目标和通配符目标定义它们*。`mbed_lib.json`中的一个参数可以覆盖`targets.json`的参数，`mbed_app.json`中的一个参数可以覆盖`mbed_lib.json`中的参数。

 `APPLICATION_ADDR` 和 `APPLICATION_SIZE`为C和C++定义，`MBED_APP_START` 和`MBED_APP_SIZE` 为 `linker`定义.

	target.mbed_app_start

这个参数定义了应用的开始地址。您负责将此地址与您正在使用的MCU的闪存布局和向量表大小对齐，当不使用`target.mbed_app_size`,正在构建的应用使用ROM的剩余地址。

这个参数对C和C++可在`APPLICATION_ADDR`可得，对linker在`MBED_APP_START`可得.

	target.mbed_app_size

这个参数定义了应用的大小，可以和`target.mbed_app_start`一起使用，同时定义地址和大小。target.mbed_app_start不存在，则应用程序从ROM的起始位置开始，您负责将应用程序的结束地址与您正在使用的MCU的闪存布局和向量表大小对齐。

这个参数对C和C++可在`APPLICATION_SIZE`可得，对linker在`MBED_APP_SIZE`可得.


此参数与`target.bootloader_img`和`target.restrict_size`相冲突。

	target.bootloader_img

这个参数定义了在built-in postbuild合并过程中使用的`bootloader`镜像。

target.bootloader_img通过获取引导加载程序的大小并向上舍入到下一个闪存擦除块边界，隐式定义当前应用程序代码段的开始。内置的postbuild合并过程自动将当前应用程序与此参数引用的镜像组合在一起。

如上所述，当前应用程序的起始地址对C和C ++在APPLICATION_ADDR可得，链接器通过MBED_APP_START获取。当前应用程序的大小可用作APPLICATION_SIZE和MBED_APP_SIZE。
这个参数还定义BOOTLOADER_ADDR和BOOTLOADER_SIZE作为 `provided bootloader`的起始地址和大小.

这个参数可以和`target.restrict_size`, `target.header_format`, `target.header_offset` 以及 `target.app_offset`一起使用。它会和`target.mbed_app_start` 和 `target.mbed_app_size`冲突。当和`target.restrict_size`一起使用时，定义应用的大小。否则，应用大小是ROM的剩余空间。

	target.restrict_size

此参数将应用程序的大小限制向下舍入到闪存擦除块的最接近的整数倍。当target.bootloader_img存在时，如上计算当前应用程序的代码段的开始; 否则，起始地址是ROM的开头。postbuild合并过程将生成的bootloader二进制填充到其结束地址。

如上所述，当前应用程序的起始地址，C和C ++定义为APPLICATION_ADDR，链接器使用MBED_APP_START，当前应用程序的大小可用作APPLICATION_SIZE和MBED_APP_SIZE。这个参数还定义POST_APPLICATION_ADDR和POST_APPLICATION_SIZE作为起始地址和应用后面的区域大小。

这个参数可以和target.bootloader_img, target.header_format, target.header_offset and target.app_offset.一起使用，但是它与target.mbed_app_start and target.mbed_app_size会产生冲突。与target.bootloader_img一起使用时，该参数定义应用程序的开始。否则，开始是ROM的起始地址。

	target.header_format

target.header_format配置key是一个元组的列表定义了应用程序的报头。每个元组代表单个头部元素的格式： a name (a valid C identifier), a type, a subtype and finally a single argument.例如，const类型定义子类型常量大小，包括32be的子类型，表示这个常量是 32-bit big endian。下面是Mbed OS构建工具支持的类型以及子类型大小。

- const A constant value.
	- 8be A value represented as 8 bits.
	- 16be A value represented as 16 bits big endian.
	- 32be A value represented as 32 bits big endian.
	- 64be A value represented as 64 bits big endian.
	- 8le A value represented as 8 bits.
	- 16le A value represented as 16 bits little endian.
	- 32le A value represented as 32 bits little endian.
	- 64le A value represented as 64 bits little endian.

- timestamp A time stamp value in seconds from epoch in the timezone GMT/UTC. The argument to this type is always null.
	- 64be A time stamp value truncated to 64 bits big endian.
	- 64le A time stamp value truncated to 64 bits little endian.
- digest A digest of an image. All digests are computed in the order they appear. A digest of the header digests the header up to its start address.
	- CRCITT32be A big endian 32-bit checksum of an image with an initial value of 0xffffffff, input reversed, and output reflected.
	- CRCITT32le A little endian 32bit checksum of an image with an initial value of 0xffffffff, input reversed, and output reflected.
	- SHA256 A SHA-2 using a block-size of 256 bits.
	- SHA512 A SHA-2 using a block-size of 512 bits.
- size The size of a list of images, added together.
	- 32be A size represented as 32 bits big endian.
	- 64be A size represented as 64 bits big endain.
	- 32le A size represented as 32 bits little endian.
	- 64le A size represented as 64 bits little endain.

Mbed OS工具在前一个字段结束的地方开始构建应用程序头中的项目。这些工具使用C“packed”结构语义在头文件中构建项目。target.header_format定义了两个宏MBED_HEADER_START，扩展到固件头的起始地址，并且MBED_HEADER_SIZE包含固件头的字节大小。应用程序标头后面的区域开始MBED_HEADER_START + MBED_HEADER_SIZE向上舍入为8个字节的倍数。

可以将target.header_format和target.bootloader_img，target.restrict_size，target.header_offset以及target.app_offset一起使用。它与target.mbed_app_start以及target.mbed_app_size会产生冲突。与target.bootloader_img一起使用时，该参数定义应用程序的开始。否则，开始是ROM的开始。

	target.header_offset

此参数直接在target.header_format中指定定义的标题部分开头的偏移量。此参数在引导加载程序和应用程序标头之间创建空间或断言引导加载程序最多与指定的偏移量一样大。

您可以结合此参数与target.bootloader_img，target.restrict_size，target.header_format和target.app_offset。它与target.mbed_app_start和target.mbed_app_size冲突。

	target.app_offset

此参数指定标题后面的应用程序部分开头的偏移量。此参数在应用程序标头和应用程序之间创建空间。

您可以结合此参数与target.bootloader_img，target.restrict_size，target.header_format和target.header_offset。它与target.mbed_app_start以及target.mbed_app_size冲突。

## Adding and configuring targets

Arm Mbed使用JSON作为其构建目标的描述语言。你可以在targets/targets.json 和项目的根目录的custom_targets.json中找到Mbed目标的JSON描述。在custom_targets.json中添加新目标时，会将它们添加到可用目标列表中。

`Note: The Online Compiler does not support this functionality. You need to use Mbed CLI to take your code offline.`

不允许在custom_targets.json中重定义目标。为了更好地理解目标的定义方式，我们将使用此示例（取自targets.json）：

	    "TEENSY3_1": {
	        "inherits": ["Target"],
	        "core": "Cortex-M4",
	        "extra_labels": ["Freescale", "K20XX", "K20DX256"],
	        "OUTPUT_EXT": "hex",
	        "is_disk_virtual": true,
	        "supported_toolchains": ["GCC_ARM", "ARM"],
	        "post_binary_hook": {
	            "function": "TEENSY3_1Code.binary_hook",
	            "toolchains": ["ARM_STD", "ARM_MICRO", "GCC_ARM"]
	        },
	        "device_name": "MK20DX256xxx7",
	        "detect_code": ["0230"]
	    }

### 标准属性

本节列出了Mbed构建系统理解的所有属性。除非另有说明，否则所有属性均为可选。

`inherits`

Mbed目标的描述可以从其他目标的一个或多个描述“inhert”.当一个target被其他target所谓的父级targe称为child。子目标自动继承父级目标的属性。子项复制了父项的属性之后，它可能会覆盖，添加或删除这些属性。
避免为目标使用多重继承。如果使用多重继承，请记住，目标描述类似于2.3版之前的Python类继承机制。目标描述继承按以下顺序检查描述：

1. 在当前目标中查找属性。
2. 如果未找到，请在第一个目标的父级中查找属性，然后在父级的父级中查找属性，依此类推。
3. 如果未找到，则相对于当前继承级别，在目标父项的其余部分中查找该属性。

	core

目标的Arm核，可能的值是"Cortex-M0", "Cortex-M0+", "Cortex-M1", "Cortex-M3", "Cortex-M4", "Cortex-M4F", "Cortex-M7", "Cortex-M7F", "Cortex-A9", "Cortex-M23", "Cortex-M23-NS", "Cortex-M33", "Cortex-M33-NS"。


`注意： Mbed OS仅支持带有GCC_ARM工具链的v8-M架构（Cortex-M23和Cortex-M33）设备。`

	public

public针对Mbed构建系统的属性控件允许用户构建。您可以将目标定义为其他目标的父项。定义此类目标时，其描述必须将public属性设置为false。Target如上所示，设置public于false这个原因。

public属性控制着Mbed构建系统允许用户构建的目标（targets),可以定义这些targets作为其他targets的父级。当定义了这样的target，它的描述中必须设置public属性为false.上面targets设置为false就是因为这个原因。

public默认为true。

	macros, macros_add and macros_remove

该macros属性定义了编译代码时可用的宏列表。可以定义这些宏(without /with a value）

例如，`"macros": ["NO_VALUE", "VALUE=10"]`,将添加-DNO_VALUE -DVALUE=10到编译器的命令行。
当目标继承时，可以在子目标声明 macros的值在不使用macros_add 和 macros_remove重新定义macros。一个子目标可能使用 macros_add去添加自己的macros,macros_remove移除macros

extra_labels, extra_labels_add and extra_labels_remove

标签列表定义了构建系统如何查找源，包括目录等。extra_labels使构建系统知道必须扫描此类文件的其他目录。

使用目标继承时,可以使用extra_labels_add and extra_labels_remove声明 extra_labels 的值。和macros_add and macros_remove的机制类似。

features, features_add and features_remove

这一系列特征确保了一个平台上的软件特征。比如extra_labels，features使构建系统知道其必须扫描资源的其他目录。与此不同extra_labels，构建系统识别features列表中的一组固定值。构建系统识别以下功能：

- UVISOR.
- BLE.
- CLIENT.
- IPV4.
- LWIP.
- COMMON_PAL.
- STORAGE.
- NANOSTACK.

下面的特征也会被构建系统识别，都是 Nanostack 配置：

- LOWPAN_BORDER_ROUTER.
- LOWPAN_HOST.
- LOWPAN_ROUTER.
- NANOSTACK_FULL.
- THREAD_BORDER_ROUTER.
- THREAD_END_DEVICE.
- THREAD_ROUTER.
- ETHERNET_HOST.

使用此列表之外的功能时，构建系统会出错。

使用目标继承时，可以使用features_add and features_remove声明feature的值。这是类似macros_add与macros_remove前一节介绍的机制。

	config and overrides

` Arm Mbed configuration system 定制的各种Mbed部件（目标库和应用程序）的编译时配置。每个组件都可以定义许多配置参数。然后可以以各种方式覆盖这些配置参数的值。`

配置列表提供了一种修改子目标或项目中宏的值的方法。每个配置都有一个默认值，以及一个可选的宏名称和帮助文本。默认情况下，宏名称是配置的名称。例如：

	"config": {
	    "clock_src": {
	        "help": "Clock source to use, can be XTAL or RC",
	        "value": "XTAL",
	    },
	    "clock_freq": {
	        "help": "Clock frequency in Mhz",
	        "value": "16",
	        "macro_name": "CLOCK_FREQUENCY_MHZ"
	    }
	}

overrides 允许子目标改变配置的值。例如，如果子目标使用内部RC时钟而不是晶体，则可以添加覆盖：

	"overrides": {
	    "clock_src": "RC"
	}

可以使用文件mbed_app.json中的target_overrides key 一个项目的配置参数。

	"target_overrides": {
	    "*": {
	        "clock_src": "RC"
	    },
	    "NRF51_DK": {
	        "clock_freq": "16"
	    }
	}

	device_has

定义了一个设备有哪些硬件。

Mbed, libraries and application source code基于不同的硬件条件选择驱动。有选择地仅为现有硬件编译驱动程序 或仅运行适用于特定平台的测试。C，C ++和汇编语言提供DEVICE_前缀宏用于访问`device_has`.

	supported_toolchains

upported_toolchains属性是支持目标的工具链列表.可能的值有ARM, uARM, ARMC6, GCC_ARM and IAR.

	default_toolchain

default_toolchain属性命名工具链，该工具链在 Online Compiler编译代码。

	post_binary_hook

某些目标需要特定的操作来生成可编程的二进制镜像。使用post_binary_hook属性和自定义Python代码指定这些操作。post_binary_hook的值必须是带有keys function和可选工具链的JSON对象。在post_binary_hook这个JSON对象中，function key 必须包含一个python函数，可以从`tools/targets/__init__.py`中获取，可选的工具链`toolchain key `必须包含工具链列表需要从post_binary_hook处理。当不为post_binary_hook指定toolchains时，可以假定post_binary_hook适用于所有工具链。对于上面的TEENSY3_1 target，post_binary_hook可以这样定义;

	"post_binary_hook": {
	    "function": "TEENSY3_1Code.binary_hook",
	    "toolchains": ["ARM_STD", "ARM_MICRO", "GCC_ARM"]
	}
当为TEENSY3_1生成初始化二进制镜像，构建系统调用tools/targets/__init__.py.中的binary_hook。构建工具调用TEENSY3_1 post_binary_hook进行构建使用ARM_STD, ARM_MICRO or GCC_ARM工具链

对于TEENSY3_1 ，tools/targets/__init__.py：

	class TEENSY3_1Code:
	    @staticmethod
	    def binary_hook(t_self, resources, elf, binf):
	        from intelhex import IntelHex
	        binh = IntelHex()
	        binh.loadbin(binf, offset = 0)
	
	        with open(binf.replace(".bin", ".hex"), "w") as f:
	            binh.tofile(f, format='hex')

TEENSY3_1 的post_build_hook将输出文件从二进制转换成Intel HEX格式。

	device_name

使用此属性可以传递必要的数据，以便导出到各种第三方工具和IDE以及使用引导加载程序构建应用程序.

我们使用工具ArmPackManager来解析CMSIS包以获取目标信息。index.json存储来自PDSC（Pack Description）的解析信息

device_name将targets.json从Mbed OS中的目标映射到CMSIS Pack中的设备的属性。要支持目标的IAR和uVision导出，必须添加包含此键的"device_name"字段targets.json。http://www.keil.com/pack/Keil.Kinetis_K20_DFP.pdsc是包含TEENSY_31设备（MK20DX256xxx7）的PDSC。ArmPackManager已解析此PDSC，并index.json存储设备信息。设备信息从.pdsc文件的第156行开始：

	<device Dname="MK20DX256xxx7">
	  <processor Dfpu="0" Dmpu="0" Dendian="Little-endian" Dclock="72000000"/>
	  <compile header="Device\Include\MK20D7.h"  define="MK20DX256xxx7"/>
	  <debug      svd="SVD\MK20D7.svd"/>
	  <memory     id="IROM1"                      start="0x00000000"  size="0x40000"    startup="1"   default="1"/>
	  <memory     id="IROM2"                      start="0x10000000"  size="0x8000"     startup="0"   default="0"/>
	  <memory     id="IRAM1"                      start="0x20000000"  size="0x8000"     init   ="0"   default="1"/>
	  <memory     id="IRAM2"                      start="0x1FFF8000"  size="0x8000"     init   ="0"   default="0"/>
	  <algorithm  name="Flash\MK_P256.FLM"        start="0x00000000"  size="0x40000"                  default="1"/>
	  <algorithm  name="Flash\MK_D32_72MHZ.FLM"   start="0x10000000"  size="0x8000"                   default="1"/>
	  <book name="Documents\K20P100M72SF1RM.pdf"         title="MK20DX256xxx7 Reference Manual"/>
	  <book name="Documents\K20P100M72SF1.pdf"           title="MK20DX256xxx7 Data Sheet"/>
	</device>

targets.json中device_name key是MK20DX256xxx7，使用这种特殊的MCU任何目标

	OUTPUT_EXT

OUTPUT_EXT属性控制文件类型，这个类型是由构建系统为某一target发出.将OUTPUT_EXT设置为bin作为二进制类型，hex表示HEX类型，elf表示ELF类型。不鼓励使用ELF，因为构建系统需要出发ELF文件。

	default_lib

default_lib控制GCC_ARM工具链链接哪个库(small or standard).当default_lib设置为std使用标准库，small减小库的大小

	bootloader_supported

控制构建系统是否支持 bootloader 或使用 bootloader 的应用。默认值是false

	release_versions

目标板支持的Mbed OS版本号，可能只包含两个Mbed OS 2, and 5

	supported_form_factors

该supported_form_factors属性是开发板支持的可选形状因子列表。您可以通过将带前缀的宏传递TARGET_FF_给编译器来使用C，C ++和汇编语言。supported_form_factors 是 ARDUINO兼容性的Arduino标头。ST表示兼容ST Morpho headers。


### Style guide

targets.json的 linting脚本在Mbed OS的tools/targets/lint.py
。此脚本是一个实用程序，用于在定义目标和检测目标之间的样式不一致时避免常见错误。此linting脚本根据下面列出的一些规则显示样式错误。

- Rules enforced

有两组规则：影响必须构建目标继承的方式的规则和管理继承层次结构中每个角色可以执行的操作的规则。

- Inheritance rules

目标的继承必须

	MCU -> Board
	MCU -> Module -> Board
	Family -> MCU -> Board
	Family -> MCU -> Module -> Board
	Family -> Subfamily -> MCU -> Board
	Family -> Subfamily -> MCU -> Module -> Board

linting脚本猜测了Boards和Modules停止的位置以及MCU，Families和Subfamilies的开始。MCU, Family or Subfamily 必须在任何层次结构中至少有一个Board or Module 

- Role rules

对于这些目标角色中的每一个，都有一些限制.

- Sample output

 linting 脚本有三个子命令targets, all-targets and orphans.

	targets and all-targets commands

都会显示公共继承层次内的错误。`python tools/targets/lint.py targets EFM32GG_STK3700 EFM32WG_STK3800 LPC11U24_301`会有这样的输出：

	hierarchy: Family (EFM32) -> MCU (EFM32GG990F1024) -> Board (EFM32GG_STK3700)
	target errors:
	  EFM32:
	  - EFM32 is not allowed in extra_labels
	  EFM32GG990F1024:
	  - macros found, and is not allowed
	  - default_lib not found, and is required
	  - device_has not found, and is required
	  EFM32GG_STK3700:
	  - progen found, and is not allowed
	  - device_has found, and is not allowed
	---
	hierarchy: Family (EFM32) -> MCU (EFM32WG990F256) -> Board (EFM32WG_STK3800)
	target errors:
	  EFM32:
	  - EFM32 is not allowed in extra_labels
	  EFM32WG990F256:
	  - macros found, and is not allowed
	  - default_lib not found, and is required
	  - device_has not found, and is required
	  EFM32WG_STK3800:
	  - progen found, and is not allowed
	  - device_has found, and is not allowed
	---
	hierarchy: Family (LPCTarget) -> MCU (LPC11U24_301) -> ???
	hierarchy errors:
	- no boards found in hierarchy
	target errors:
	  LPC11U24_301:
	  - release_versions not found, and is required
	  - default_lib not found, and is required
	  - public not found, and is required

该all-targets命令非常详细，输出与上面的格式匹配，但在此处重现的时间太长。

	orphans command

显示您无法从公共目标到达的所有目标。`python tools/targets/lint.py orphans`

	- CM4_UARM
	- CM4_ARM
	- CM4F_UARM
	- CM4F_ARM
	- LPC1800
	- EFR32MG1P132F256GM48
	- EFR32MG1_BRD4150

### Arm Mbed CLI

Arm提供了Arm Mbed CLI，这是一个打包mbed-cli并基于Python 的命令行工具。

Mbed CLI支持基于Git和Mercurial的版本控制，依赖关系管理，代码发布，对远程托管存储库（GitHub，GitLab和mbed.org）的支持，Arm Mbed OS构建系统的使用，导出功能和其他操作。

### Configuring Mbed CLI


- Mandatory: setting PATH variables

需要添加系统PATH:Git路径

- Mandatory: toolchain selection

您需要告诉Mbed CLI在哪里可以找到要用于编译的工具链。Mbed CLI支持以下工具链：

- ArmArm Compiler 5。使用Arm Compiler 5的5.06版。早于5.06的版本可能与这些工具不兼容。
- GNU Arm Embedded toolchain (GCC) version 6.。使用GCC Arm Embedded版本6; 5.0版或任何旧版本可能与这些工具不兼容。
- IAR EWARM 7.。使用IAR EWARM版本7.70到7.80.x; 其他版本可能与这些工具不兼容。

您必须使用以下方法之一通知Mbed CLI有关编译器的位置：
- Mbed CLI配置命令
- 将编译器的目录添加到PATH。
- 设置环境变量
- 程序根目录中mbed_settings.py，如果该文件尚不存在，工具将自动创建该文件

`注意：您可以配置多个工具链。但是，您一次只能使用一个工具链。使用C ++ 98和GNU C99时，工具链之间的唯一区别就是性能。`

### Through Mbed CLI configuration

Mbed CLI会在项目本地设置和用户范围的“全局”设置中存储编译器位置。使用`mbed config`查看或设置这些配置信息。例如，使用以下命令为用户设置Arm Compiler 5位置：

	$ mbed config -G ARM_PATH "C:\Program Files\ARM"
	[mbed] C:\Program Files\ARM now set as global ARM_PATH

`-G`表示全局设置,允许用户的所有项目使用Arm Compiler 5进行编译。不用`-G`表示使用项目本地设置设置ARM_PATH 。

Mbed CLI支持每个工具链路径的设置。以下是这些设置的列表，以及每个设置中预期路径的说明。

- ARM_PATH Arm编译器安装的基本目录的路径。这应该是包含包含二进制文件armcc和frieinds的目录的目录.例如，如果您的Arm Compiler 5可执行文件armcc位于/home/redacted/ARM_Compiler_5.06u5/bin/armcc,则设置ARM_PATH为/home/redacted/ARM_Compiler_5.06u5.
- IAR_PATH：IAR EWARM编译器安装的基本目录的路径。这应该是包含二进制文件iccarm和friends的目录.例如，如果您的IAR EWARM编译器可执行文件位于C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm/bin/iccarm.exe，则设置IAR_PATH为C:/Program Files/IAR Systems/Embedded Workbench 7.5/arm。
- GCC_ARM_PATH:GCC Arm Embedded Compiler安装的二进制目录的路径。这应该是包含二进制文件arm-none-eabi-gcc和friends的目录。例如，如果您的Gcc Arm嵌入式工具链gcc可执行文件在/usr/bin/arm-none-eabi-gcc，则设置GCC_ARM_PATH为/usr/bin。

### Compiler detection through the PATH

mbed compile命令检查您PATH的可执行文件是否是所涉及的编译器套件的一部分。此检查与shell在命令行上查找可执行文件所执行的操作相同。当mbed compile找到它正在查找的可执行文件时，他会将可执行文件名称为preface（序言，开端）,Mbed CLI不会为找到的任何可执行文件添加前缀GCC_ARM

### Set environment variable

Mbed CLI还可以检测具有特殊命名环境变量的编译器。这些环境变量与其对应的配置变量相同，前缀为MBED_added。例如，在配置Arm Compiler 5时，将MBED_ARM_PATH环境变量设置为Arm Compiler 5安装的基本目录。

### Through mbed_settings.py

Mbed CLI还用mbed_settings.py配置工具链。此文件必须是python模块，并使用与Mbed CLI配置完全相同的配置变量。

`注意：由于mbed_settings.py包含本地设置（可能仅与单台计算机上的单个操作系统相关），因此不应将其检入版本控制。`

### Optional: configuring multiple toolchains

Mbed CLI有一些规则允许在不同项目之间切换时,同时实现同一工具链的不同版本之间无缝切换。前面部分中描述的设置都可以配置同一工具链的不同版本。当多个设置可用于单个工具链时，Mbed CLI会选择最具体的设置。从最具体到最不具体的设置是：

1. mbed_settings.py
2. Mbed CLI本地配置
3. Mbed CLI全局配置
4. 环境变量
5. PATH环境变量

在解析单个mbed compile或mbed test调用的设置时，Mbed CLI会选择当前设置编号最小的。

要使用标准工具链进行通用开发，可以使用任何方法3到5.要覆盖特定项目的工具链版本，可以使用方法1和2.所有这些用于配置工具链的方法可以共存。

### Optional: add Bash tab completion

要安装mbed-cli bash选项卡完成：
1. 导航到该tools/bash_completion目录
2. Copy the mbed script into your /etc/bash_completion.d/ or /usr/local/etc/bash_completion.d directory.
3. Reload your terminal.

### Working with mbed config

Mbed CLI配置语法是：

	mbed config [--global] <var> [value] [--unset]

您可以通过以下方式查看正在使用的Mbed CLI配置：


	$ mbed config --list
	[mbed] Global config:
	ARM_PATH=C:\Program Files\ARM\armcc5.06
	IAR_PATH=C:\Program Files\IAR Workbench 7.0\arm
	
	[mbed] Local config (D:\temp\mbed-os-program):
	No local configuration is set

命令选项：

|option|Explanation|
| :-: | -: |
|--global|定义跨程序的Mbed CLI的默认行为，除非被local settings覆盖|
|None|任何没有--global的配置都是特定于Mbed程序的。它会覆盖全局或默认的Mbed CLI设置。如果未指定值，则Mbed CLI将在当前工作上下文中打印此设置的值。|
|--unset|删除设置|
|--list|列出全局和本地配置|

可用配置：

|option|Explanation|Default value|
| :-: | :-| :-: |
|target|默认target为compile，test和export; 别名mbed target|No default|
|toolchain|默认工具链为compile和test; 可以通过mbed toolchain设置|No default.|
|ARM_PATH, GCC_ARM_PATH, IAR_PATH|定义Arm Compiler，GCC Arm和IAR Workbench工具链的路径|No default.|
|protocol|用于导入或克隆程序和库的默认协议。可能的值是https，http和ssh。ssh如果您已使用GitHub，GitLab，Bitbucket等服务生成并注册了SSH密钥（公钥认证），请使用此选项。|默认值：https|
|depth|用于导入或克隆的克隆深度，仅适用于Git存储库。请注意，虽然此选项可以提高克隆速度，但它也可能会阻止您在引用修订版散列早于克隆深度时正确检出依赖关系树。|No default|
|cache|存储导入或克隆的存储库的小副本的本地路径。Mbed CLI使用它来最小化流量并加速相同存储库的未来导入。使用on或enabled打开系统临时路径中的缓存。使用none以关闭缓存。|Default: none (disabled).|

### Create

Mbed CLI使用当前目录作为工作上下文，与Git，Mercurial和许多其他命令行工具类似。这意味着在调用任何Mbed CLI命令之前，必须先切换到包含您要操作的代码的目录。例如，如果要更新mbed-example-program目录中的Mbed OS源：

	$ cd mbed-example-program
	$ cd mbed-os
	$ mbed update master   # This will update "mbed-os", not "my-program"

各种Mbed CLI功能需要一个程序根，它应该受版本控制 - Mercurial。这使得可以在整个程序及其库的修订版之间切换，控制程序历史记录，将程序与远程存储库同步，与其他人共享等等。版本控制也是Mbed OS源代码的主要和首选交付机制，它允许每个人为Mbed OS做出贡献。

`注意：Mbed CLI将有关库和依赖项的信息存储在使用.lib扩展名的参考文件中（例如lib_name.lib）。虽然这些文件是人类可读的，但不应手动编辑它们 - 让Mbed CLI管理它们。`

### Application workflow

Mbed CLI可以基于Mbed OS 2和Mbed OS 5创建和导入程序。

Mbed CLI的基本工作流程是：

1. 为新应用程序（或库）或导入的应用程序初始化新存储库。在这两种情况下，此操作还会添加Mbed OS代码库。
2. 构建应用程序代码。
3. 测试你的构建。
4. 发布应用

为了支持长期开发，Mbed CLI提供源代码控制，包括库和代码库的选择性更新，对多个工具链的支持以及系统的手动配置

### Creating a program

您可以将新应用程序创建为Mbed OS 5，Mbed OS 2或非版本化（空白）项目

- For Mbed OS 5+

创建新程序时，Mbed CLI会自动导入最新的Mbed OS版本。每个版本都包含所有组件：代码，构建工具和IDE导出器。

	$ mbed new mbed-os-program
	[mbed] Creating new program "mbed-os-program" (git)
	[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at latest revision in the current branch
	[mbed] Updating reference "mbed-os" -> "https://github.com/ARMmbed/mbed-os/#89962277c20729504d1d6c95250fbd36ea5f4a2d"

这将创建一个新文件夹“mbed-os-program”，初始化一个新的存储库并将最新版本的mbed-os依赖项导入到您的程序树中

使用`mbed ls`列出导入到你的程序的所有库：

	$ cd mbed-os-program
	$ mbed ls -a
	mbed-os-program (mbed-os-program)
	`- mbed-os (https://github.com/ARMmbed/mbed-os#89962277c207)

`注意：如果要从工作区中的现有文件夹开始，可以使用mbed new .初始化Mbed程序的文件夹，以及该文件夹中的新Git或Mercurial存储库。`

### Compiling workflow

#### Compiling your application

使用`mbed compile`命令编译代码：

	$ mbed compile -t ARM -m K64F
	Building project mbed-os-program (K64F, GCC_ARM)
	Compile: aesni.c
	Compile: blowfish.c
	Compile: main.cpp
	... [SNIP] ...
	Compile: configuration_store.c
	Link: mbed-os-program
	Elf2Bin: mbed-os-program
	+----------------------------+-------+-------+------+
	| Module                     | .text | .data | .bss |
	+----------------------------+-------+-------+------+
	| Fill                       |   170 |     0 | 2294 |
	| Misc                       | 36282 |  2220 | 2152 |
	| core/hal                   | 15396 |    16 |  568 |
	| core/rtos                  |  6751 |    24 | 2662 |
	| features/FEATURE_IPV4      |    96 |     0 |   48 |
	| frameworks/greentea-client |   912 |    28 |   44 |
	| frameworks/utest           |  3079 |     0 |  732 |
	| Subtotals                  | 62686 |  2288 | 8500 |
	+----------------------------+-------+-------+------+
	Allocated Heap: 65540 bytes
	Allocated Stack: 32768 bytes
	Total Static RAM memory (data + bss): 10788 bytes
	Total RAM memory (data + bss + heap + stack): 109096 bytes
	Total Flash memory (text + data + misc): 66014 bytes
	Image: BUILD/K64F/GCC_ARM/mbed-os-program.bin

- `-m <MCU>`选择一个目标。如果传递参数detect或auto给-m，则Mbed CLI会检测连接的目标
- `-t <TOOLCHAIN>`选择一个工具链（在mbed_settings.py定义的工具链中）,值可以是ARM（Arm Compiler 5），GCC_ARM（GNU Arm Embedded）或IAR（IAR Embedded Workbench for Arm）。
- `--source <SOURCE>`选择源目录。默认为.（当前目录）。您可以指定多个源位置，甚至可以在程序树之外
- `--build <BUILD>`选择构建目录,默认是项目根目录的`BUILD/`

   `注意：mbed compile忽略当前的构建目录; 创建多个构建目录会导致错误。`

- `--profile <PATH_TO_BUILD_PROFILE>`, selects a path to a build profile configuration file. Example: mbed-os/tools/profiles/debug.json.
- `--library` compiles the code as a static .a/.ar library.
- `--no-archive` 禁止由`--library`创建`.a/.ar`文件，而是生成`.o`文件
- `--config` 检查运行时编译配置
- `-S or --supported` 显示支持的目标和工具链的矩阵
- `-f or --flash` flashes/programs  编译成功后连接的目标
- `-c` 从头开始构建，干净的构建或重建。
- `-j <jobs>`控制机器上的编译过程。默认值为0，根据计算机上的核的数量推断出进程数。您可以使用`-j 1`触发源代码的顺序编译。
- `-v or --verbose` 显示详细的诊断输出
- `-vv or --very_verbose` 显示非常详细的诊断输出。

#### Compiling static libraries

您可以通过添加`--library`参数到`mbed compile`来构建代码的静态库.当您想要从同一个Mbed OS代码库构建多个应用程序而无需为每个应用程序重新编译时，静态库非常有用。为了达成这个：

	$ mbed compile -t ARM -m K64F --library --no-archive --source=mbed-os --build=../mbed-os-build
	Building library mbed-os (K64F, ARM)
	[...]
	Completed in: (47.4)s
	
	$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/basic --source=../mbed-os-build --build=../basic-out
	Building project basic (K64F, ARM)
	Compile: main.cpp
	Link: basic
	Elf2Bin: basic
	Image: ../basic-out/basic.bin
	
	$ mbed compile -t ARM -m K64F --source=mbed-os/TESTS/integration/threaded_blinky --source=../mbed-os-build --build=..\/hreaded_blinky-out
	Building project threaded_blinky (K64F, ARM)
	Compile: main.cpp
	Link: threaded_blinky
	Elf2Bin: threaded_blinky
	Image: ../threaded_blinky-out/threaded_blinky.bin

#### Without OS version
You can create plain (empty) programs, without either Mbed OS 5 or Mbed OS 2, by using the --create-only option.

### The compile configuration system

`compile configuration system `提供了配置Mbed程序的灵活机制，它的库和构建目标

#### Inspecting the configuration

`mbed compile --config`可以查看配置
	
	$ mbed compile --config -t GCC_ARM -m K64F

要显示有关配置参数的更详细信息，请使用-v：

	$ mbed compile --config -t GCC_ARM -m K64F -v

通过指定一个或多个前缀来过滤`mbed compile --config`输出.例如，仅显示目标定义的配置

	$ mbed compile --config -t GCC_ARM -m K64F --prefix target

您可以使用--prefix多次。要仅显示应用程序和目标配置，请使用以下两个--prefix选项：

	$ mbed compile --config -t GCC_ARM -m K64F --prefix target --prefix app

### Compile-time customizations

#### Macros

您可以使用-D选项在命令行中指定宏：

	$ mbed compile -t GCC_ARM -m K64F -c -DUVISOR_PRESENT

#### Compile in debug mode

在编译命令行中使用 `--profile mbed-os/tools/profiles/debug.json`

	$ mbed compile -t GCC_ARM -m K64F --profile mbed-os/tools/profiles/debug.json

#### Automate toolchain and target selection

使用mbed target <target>和mbed toolchain <toolchain>，您可以为程序设置默认目标和工具链。每次编译或生成IDE项目文件时都不必指定这些。

您还可以使用mbed target detect，它检测连接的目标板并将其用作每个后续编译和导出的参数。

#### Update programs and libraries

您可以更新本地计算机上的程序和库，以便从远程源（Git或Mercurial）获取更改.与任何Mbed CLI命令一样，mbed update使用当前目录作为工作上下文。在调用之前mbed update，您应该将工作目录更改为要更新的目录。例如，如果您要更新mbed-os，请cd mbed-os在开始更新之前使用。

`同步库引用：在触发更新之前，您可能希望通过运行同步对程序结构所做的任何更改mbed sync，这会更新必要的库引用并删除无效的引用。`

#### Protect against overwriting local changes

如果您的程序或库中有mbed update可能覆盖的更改，则update命令将失败。Mbed CLI不会运行会导致覆盖未提交的本地更改的操作。如果出现错误，请处理您的本地更改（提交或使用以下选项之一），然后重新运行mbed update。

### Updating to an upstream version

####  Updating a program

要将程序更新到另一个上游版本，请转到该程序的根文件夹，然后运行：

	$ mbed update [branch|tag|revision]

这将从远程存储库中获取新修订，将程序更新为指定的分支，标记或修订。如果未指定任何这些，则mbed update更新当前分支的最新版本。mbed update对程序树中的所有依赖项递归执行这一系列操作。

#### Updating a library

您可以将工作目录更改为库文件夹，并使用mbed update将该库及其依赖项更新到与父程序或库中引用的版本不同的版本。这允许您在程序树中试验不同版本的库/依赖项，而无需更改父程序或库。

还有三个附加选项可以修改未发布的本地库的处理方式。

- `mbed update --clean-deps `更新当前程序或库及其依赖项，并丢弃所有本地未发布的存储库。请谨慎使用此选项，因为除非您有备份副本，否则无法还原本地未发布的存储库。
- `mbed update --clean-files ` 更新当前程序或库及其依赖项，丢弃本地未提交的更改并删除任何未跟踪或忽略的文件。请谨慎使用此选项，因为除非您有备份副本，否则无法还原本地未发布的存储库。
- `mbed update --ignore`,更新当前程序或库及其依赖项，并忽略任何本地未发布的库（它们不会被删除或修改，只是被忽略）。

#### Updating examples


更新时有两种主要方案：

- 本地未提交的更改,update.`dirty update`

运行`mbed update [branch|revision|tag_name]`,如果git/mercurial抛出错误，必须提交或存储更改，这将会覆盖掉本地更改。

- 弃本地未提交的更改：`clean update`

运行`mbed update [branch|revision|tag_name] --clean`
指定分支mbed update将仅检出该分支，并且不会自动合并或快进到远程/上游分支。您可以运行mbed update将本地分支与最新的远程分支合并（快进）。在Git上，你可以做到git pull。

#### Combining update options

您可以将Mbed update命令的选项组合用于以下方案：

- `mbed update --clean --clean-deps --clean-files`更新当前程序或库及其依赖项，删除所有本地未发布的库，丢弃本地未提交的更改并删除所有未跟踪或忽略的文件。这将擦除您在源树中所做的每一个更改并恢复库存布局。
- `mbed update --clean --ignore `更新当前程序或库及其依赖项，但忽略任何本地存储库。Mbed CLI可以从公共存储库中更新任何内容。

`请谨慎使用这些，因为无法恢复未提交的更改和未发布的库。`

### Repository caching

为了最大限度地减少流量并减少导入时间,Mbed CLI通过将索引存储在Mbed CLI用户配置文件夹下(folder - typically ~/.mbed/mbed-cache/ on UNIX systems, or %userprofile%/.mbed/mbed-cache/ on Windows systems.)来缓存存储库.与完全检出的存储库相比，索引的大小和文件数量较小，并包含该存储库的整个修订历史记录。这使得Mbed CLI可以快速创建以前下载的存储库索引的副本，并从远程存储库中提取或获取最新的更改，从而大大减少网络流量和下载时间，尤其是对于大型存储库，例如mbed-os。

	mbed cache [on|off|dir <path>|ls|purge|-h|--help]

- `on` - 打开存储库缓存。这使用用户指定的缓存目录或默认目录。见“dir”
- `off` 关闭存储库缓存。请注意，这不会清除缓存的存储库。请参阅`purge`
- `dir`  设置缓存目录,设置为“default”以让Mbed CLI确定缓存目录位置。`~/.mbed/mbed-cache/ on UNIX systems, or %%userprofile%%/.mbed/mbed-cache/ on Windows systems.`
- `ls` 列出缓存的存储库及其大小。
- `purge`  清除缓存的存储库。请注意，这不会关闭缓存。
- `-h`or `--help` 打印缓存命令选项

如果未指定子命令mbed cache，则Mbed CLI将打印当前缓存设置（ENABLED或DISABLED）以及本地缓存目录的路径。

出于安全原因，Mbed CLI将mbed-cache子文件夹用于用户指定的位置。这确保purge即使用户已将root / system文件夹指定为缓存位置（例如，mbed cache dir /或mbed cache dir C:\），也不会删除用户文件。

安全声明：如果在用户主目录/配置文件目录之外使用缓存位置，则其他系统用户可能能够访问存储库缓存，从而访问缓存存储库的数据。

##Collaborate 协作

### Importing an existing program

mbed import将现有程序及其所有依赖项克隆到您的计算机：

	$ mbed import https://github.com/ARMmbed/mbed-os-example-blinky
	[mbed] Importing program "mbed-os-example-blinky" from "https://github.com/ARMmbed/mbed-os-example-blinky" at latest revision in the current branch
	[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #dd36dc4228b5
	$ cd mbed-os-example-blinky

Mbed CLI还支持基于Mbed OS 2的程序，它可以自动检测并且不需要其他选项：

	$ mbed import https://mbed.org/teams/mbed/code/mbed_blinky/
	[mbed] Importing program "mbed_blinky" from "https://mbed.org/teams/mbed/code/mbed_blinky" at latest revision in the current branch
	[mbed] Adding library "mbed" from "http://mbed.org/users/mbed_official/code/mbed/builds" at rev #f9eeca106725
	[mbed] Couldn't find build tools in your program. Downloading the mbed 2.0 SDK tools...
	$ cd mbed-os-example-blinky

您可以使用“import”命令而不指定完整的URL; 如果URL不存在，Mbed CLI会为URL 添加前缀。例如，这个命令：

	$ mbed import mbed-os-example-blinky

### Importing from a Git or GitHub clone

如果您已将Git存储库手动克隆到工作区中，并且要添加所有缺少的库，则可以使用以下deploy命令：

	$ mbed deploy
	[mbed] Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at rev #dd36dc4228b5

不要忘记将当前目录设置为程序的根目录
	
	$ mbed new .

### Adding and removing libraries

在处理代码时，您可能需要向应用程序添加另一个库或删除现有库。向程序添加新库与克隆存储库不同。不要使用hg或克隆库git; 用于mbed add添加库。这可确保同时填充所有库和子库。

从程序中删除库与删除库目录不同。Mbed CLI更新并删除库参考文件。使用mbed remove删除库; 不要删除其目录rm。

#### Adding a library

使用mbed add添加库的最新版本：

	$ mbed add https://developer.mbed.org/users/wim/code/TextLCD/

Use the URL#hash format to add a library from a URL at a specific revision hash:

	mbed add https://developer.mbed.org/users/wim/code/TextLCD/#e5a0dcb43ecc

#### Specifying a destination directory

如果要指定要添加库的目录，可以add为该目录命名一个附加参数。例如，如果您更愿意将以前的库添加到名为“text-lcd”的目录中（而不是TextLCD）：

	$ mbed add https://developer.mbed.org/users/wim/code/TextLCD/ text-lcd

虽然Mbed CLI支持此功能，但我们不鼓励它。添加名称与其源存储库不同的库可能会导致混淆。

#### Removing a library

如果您在任何时候决定不再需要库，则可以使用mbed remove库的路径：

	$ mbed remove text-lcd

### Exporting to desktop IDEs 导出到桌面IDE

如果需要调试代码，可以将源代码树导出到IDE项目文件以使用IDE的调试工具。Mbed CLI支持导出到Keil uVision，IAR Workbench，使用GCC Arm的Makefile，使用GCC Arm的Eclipse和其他IDE。

	$ mbed export -i uvision -m K64F

Mbed CLI 在projectfiles / uvision文件夹中创建一个.uvprojx文件。您可以使用uVision打开项目文件。

### Publishing changes

#### Checking status

在开发程序时，您将编辑它的一部分。您可以通过运行获取程序中所有存储库的状态（递归）mbed status。如果存储库具有未提交的更改，则此命令将显示这些更改。

这是一个例子：
	
	[mbed] Status for "mbed-os-program":
	 M main.cpp
	 M mbed-os.lib
	?? gdb_log.txt
	?? test_spec.json
	
	[mbed] Status for "mbed-os":
	 M tools/toolchains/arm.py
	 M tools/toolchains/gcc.py
	
	[mbed] Status for "mbed-client-classic":
	 M source/m2mtimerpimpl.cpp
	
	[mbed] Status for "mbed-mesh-api":
	 M source/include/static_config.h

然后，您可以通过该存储库的版本控制系统提交或放弃这些更改。

### Pushing upstream

要在上游推送本地树中的更改，请运行mbed publish。mbed publish递归工作，首先推送叶依赖，然后更新依赖并推送它们。

假设您的程序的依赖项列表（通过运行获得mbed ls）如下所示：

	my-mbed-os-example (a5ac4bf2e468)
	|- mbed-os (5fea6e69ec1a)
	`- my-libs (e39199afa2da)
	   |- my-libs/iot-client (571cfef17dd0)
	   `- my-libs/test-framework (cd18b5a50df4)


我们假设您进行了更改iot-client。mbed publish检测叶iot-client依赖项的更改并要求您提交它。然后mbed publish检测my-libs依赖于iot-client，通过更新文件并要求您提交它来更新对其最新版本的my-libs依赖性。这会传播到你的程序，最后传播到你的程序。iot-clientiot-client.libmy-libsmy-mbed-os-example

### Publishing a local program or library 发布本地程序或库

创建新（本地）版本控制托管程序或库时，其修订历史记录仅在本地存在。存储库与远程存储库无关。要发布本地存储库，请按照下列步骤操作：

1. 在远程站点上创建一个新的空存储库。这可以在公共存储库托管服务（GitHub，Bitbucket，mbed.org），您自己的服务或您系统上的其他位置。
2. 在剪贴板中复制新存储库的URL /位置。
3. 在本地存储库目录中打开命令行（例如，将目录更改为mbed-os-example/local-lib）。
4. 关联本地存储库：于Git，运行git remote add origin <url-or-path-to-your-remote-repo>。
5. 运行mbed publish以发布更改。

### The forking workflow

Git启用了一个工作流,publish/push 存储库可能与原始（“origin”）存储库不同,这允许在fork存储库中进行新的修订，同时保持与原始存储库的关联.要使用此工作流程，首先导入Mbed OS程序或Mbed OS本身，然后将push remote与fork关联。例如

	$ git remote set-url --push origin https://github.com/screamerbg/repo-fork

git commit & git push and mbed publish都会push新的修订到你的fork.您可以使用mbed update或git pull从原始存储库中获取.如果您明确想要从fork fetch or pull ，那么您可以使用git pull https://github.com/screamerbg/repo-fork [branch]。

通过上面介绍的工作流程，Mbed CLI维护与原始存储库（您可能希望向其发送pull request）的关联，并使用您推送到fork的 revision hashes记录引用。在您的请求（PR）被接受之前，所有记录的引用都是无效的。一旦PR被接受，你的fork中的所有修订版哈希都将成为原始存储库的一部分，使它们有效。

### Test and debug

使用该mbed test命令编译并运行测试。

- `-m <MCU>`选择编译目标。如果传递了detect或auto参数，则Mbed CLI将尝试检测连接的目标并对其进行编译。
- `-t <TOOLCHAIN>` 选择工具链（mbed_settings.py有定义），其中toolchain可以是ARM（Arm Compiler 5），GCC_ARM（GNU Arm Embedded）或IAR（IAR Embedded Workbench for Arm）。
- `--compile-list` 列出可以运行的所有测试（必须先构建它们）
- `--compile` 只编译测试
- `--run`只运行测试
- `-n <TESTS_BY_NAME>` 限制构建的测试或运行以逗号分隔的列表（例如test1，test2，test3）。
- `--source <SOURCE>` 选择源目录。默认是.（当前目录）。您可以指定多个源位置，甚至可以在程序树之外。
- `--build <BUILD>` 选择构建目录。默认值：程序中 BUILD/
- `--profile <PATH_TO_BUILD_PROFILE>`选择一个目录构建配置。示例：mbed-os/tools/profiles/debug.json。
- `-c or --clean`在编译之前清理构建目录
- `--test-spec <TEST_SPEC>` 设置构建和运行测试时使用的测试规范文件的路径（默认路径是构建目录）。
- `-v or --verbose`用于详细的诊断输出
- `-vv or --very_verbose ` 用于非常详细的诊断输出

调用mbed test：

	$ mbed test -m K64F -t GCC_ARM
	Building library mbed-build (K64F, GCC_ARM)
	Building project GCC_ARM to TESTS-unit-myclass (K64F, GCC_ARM)
	Compile: main.cpp
	Link: TESTS-unit-myclass
	Elf2Bin: TESTS-unit-myclass
	+-----------+-------+-------+------+
	| Module    | .text | .data | .bss |
	+-----------+-------+-------+------+
	| Fill      |   74  |   0   | 2092 |
	| Misc      | 47039 |  204  | 4272 |
	| Subtotals | 47113 |  204  | 6364 |
	+-----------+-------+-------+------+
	Allocated Heap: 65540 bytes
	Allocated Stack: 32768 bytes
	Total Static RAM memory (data + bss): 6568 bytes
	Total RAM memory (data + bss + heap + stack): 104876 bytes
	Total Flash memory (text + data + misc): 48357 bytes
	Image: build\tests\K64F\GCC_ARM\TESTS\mbedmicro-rtos-mbed\mutex\TESTS-unit-myclass.bin
	...[SNIP]...
	mbedgt: test suite report:
	+--------------+---------------+---------------------------------+--------+--------------------+-------------+
	| target       | platform_name | test suite                      | result | elapsed_time (sec) | copy_method |
	+--------------+---------------+---------------------------------+--------+--------------------+-------------+
	| K64F-GCC_ARM | K64F          | TESTS-unit-myclass              | OK     | 21.09              |    shell    |
	+--------------+---------------+---------------------------------+--------+--------------------+-------------+
	mbedgt: test suite results: 1 OK
	mbedgt: test case report:
	+--------------+---------------+------------------------------------------+--------+--------+--------+--------------------+
	| target       | platform_name | test suite         | test case           | passed | failed | result | elapsed_time (sec) |
	+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
	| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass1 | 1      | 0      | OK     | 5.00               |
	| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass2 | 1      | 0      | OK     | 5.00               |
	| K64F-GCC_ARM | K64F          | TESTS-unit-myclass | TESTS-unit-myclass3 | 1      | 0      | OK     | 5.00               |
	+--------------+---------------+--------------------+---------------------+--------+--------+--------+--------------------+
	mbedgt: test case results: 3 OK
	mbedgt: completed in 21.28 sec

您可以在BUILD/tests/<TARGET>/<TOOLCHAIN>程序目录中找到已编译的二进制文件和测试工件。


### Finding available tests

使用以下选项找到可用于构建的测试--compile-list


	
	$ mbed test --compile-list
	Test Case:
	    Name: TESTS-functional-test1
	    Path: .\TESTS\functional\test1
	Test Case:
	    Name: TESTS-functional-test2
	    Path: .\TESTS\functional\test2
	Test Case:
	    Name: TESTS-functional-test3
	    Path: .\TESTS\functional\test3

使用`--run-list`找到可用于运行的测试

	$ mbed test --run-list
	mbedgt: test specification file '.\build\tests\K64F\ARM\test_spec.json' (specified with --test-spec option)
	mbedgt: using '.\build\tests\K64F\ARM\test_spec.json' from current directory!
	mbedgt: available tests for built 'K64F-ARM', location '.\build\tests\K64F\ARM'
	        test 'TESTS-functional-test1'
	        test 'TESTS-functional-test2'
	        test 'TESTS-functional-test3'

### Compiling and running tests

使用`--compile` 指定仅使用构建测试

	$ mbed test -m K64F -t GCC_ARM --compile

使用`--run`指定仅使用运行测试:

	$ mbed test -m K64F -t GCC_ARM --run

如果您未指定任何这些，mbed test将首先编译所有可用的测试，然后运行它们。

#### Limiting the test scope

您可以使用-n选项限制构建和运行的测试的范围。这将以逗号分隔的测试名称列表作为参数：

	$ mbed test -m K64F -t GCC_ARM -n TESTS-functional-test1,TESTS-functional-test2

您可以使用通配符*运行一组共享公共前缀的测试，而无需单独指定每个测试。例如，如果您只想运行三个测试TESTS-functional-test1，TESTS-functional-test2并且TESTS-functional-test3在项目中有其他测试，则可以运行：

	$ mbed test -m NUCLEO_F429ZI -t GCC_ARM -n TESTS-functional*

`注意：某些shell将通配符扩展为*工作目录中存在的文件名。要防止出现这种情况，请参阅shell的文档。`

### Test directory structure

测试代码必须遵循以下目录结构：
	
	mbed-os-program
	 |- main.cpp            # Optional main.cpp with main() if it is an application module.
	 |- pqr.lib             # Required libs
	 |- xyz.lib
	 |- mbed-os
	 |  |- frameworks        # Test dependencies
	 |  |  `_greentea-client # Greentea client required by tests.
	 |  |...
	 |  `- TESTS              # Tests directory. Special name upper case TESTS is excluded during application build process
	 |     |- TestGroup1      # Test Group directory
	 |     |  `- TestCase1    # Test case source directory
	 |     |      `- main.cpp # Test source
	 |     |- TestGroup2
	 |     |   `- TestCase2
	 |     |      `- main.cpp
	 |     `- host_tests      # Python host tests script directory
	 |        |- host_test1.py
	 |        `- host_test2.py
	 `- build                 # Build directory
	     |- <TARGET>          # Target directory
	     | `- <TOOLCHAIN>     # Toolchain directory
	     |   |- TestCase1.bin # Test binary
	     |   `- TestCase2.bin
	     | ....

如上所示，测试存在于TESTS\testgroup\testcase\目录中。请注意，这TESTS是一个特殊的大写目录，在编译时从模块源中排除。

`注意： mbed test在包含目录main之外的函数的应用程序中 不起作用TESTS。`

### Troubleshooting 故障排除

##Ignoring files from mbed build

.mbedignore文件告诉mbed build命令要忽略哪些文件和目录（不处理）。
### Usage 用法

您可以将.mbedignore文件放在mbed build要搜索源文件的任何目录中。最方便的地方是库或应用程序的根目录。但是，这不是必需的。

避免定义跨越库边界的规则; 这些可能导致副作用或构建难以发现的问题。
### Syntax  句法

.mbedignore文件中的每一行都是用于匹配文件的文件模式。构建时将忽略每个匹配的文件或目录。
接受以下通配符：

|Pattern|Meaning|
|:-|:-:|
|*|匹配一切|
|?|匹配任何单个字符。|
|[seq]|匹配seq中的任何字符。|
|[!seq]|匹配不在seq中的任何字符|

该文件使用Python的fnmatch功能进行解析，因此语法遵循基本的shell模式，但有以下例外：

1. 内部每行以.mbedignore文件的路径为前缀
2. 行不能以.或开头/（因为规则1）

未使用globbing功能，因此您无法以递归方式匹配特定文件模式。相反，您需要为每个目录定义规则。

您可以使用相对路径，以便可以在构建树中更深层匹配文件。但是，避免跨越库边界。

### Example

位于source/obsolete/.mbedignore以下内容的文件：

	*.c
	*.h
	second_level/*.c

应用规则1后，内部用于匹配源文件的实际模式为：

	source/obsolete/*.c
	source/obsolete/*.h
	source/obsolete/second_level/*.c

## Build profiles

Arm Mbed OS 5支持三个主要的构建配置：develop, debug and release. 在线编译器使用develop profile。从Arm Mbed CLI构建时，您可以通过添加--profile <profile>标志来选择配置文件。您可以通过提供配置文件的路径来指定用户定义的配置文件。

### Develop profile

- 小而快的代码。
- 完整的错误信息。例如，断言具有文件名和行号。
- 使用调试器时很难遵循代码流程。
- 芯片在空闲时进入睡眠状态：
 - 调试器可能会断开连接。
 - 在某些板上打破Arm Mbed interface上的本地文件系统。

###  Debug profile

- 最大和最慢的配置文件。
- 完整的错误信息。例如，断言具有文件名和行号。
- 使用调试器轻松完成代码。
- 禁用睡眠模式。

### Release profile
- 最小的配置文件仍然很快。
- 最小的错误信息。
- 闲置时芯片进入睡眠状态：
 - 调试器可能会断开连接。
 - 在某些板上打破 Mbed interface上的本地文件系统。 

## Debug builds

设置本地调试工具链后，需要包含程序符号（.elf文件）的固件。由于Arm Mbed在线编译器仅生成省略程序符号的二进制文件，因此需要使用Arm Mbed CLI在本地编译。

`注意：通过删除BUILD文件夹，确保在切换到调试和发布时进行干净的构建。`
###Compile commands

Arm Mbed OS 5.2 and later

	$ mbed compile --profile mbed-os/tools/profiles/debug.json

Arm Mbed OS 5.0 and 5.1

	$ mbed compile -o debug-info
Arm Mbed 2.0
	$ mbed compile --profile .temp/tools/profiles/debug.json

### Exporting with debug symbols

您还可以在导出项目时使用以下命令启用调试符号：

	$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/debug.json

使用以下方式创建发布版本:

	$ mbed export -i uvision -m K64F --profile mbed-os/tools/profiles/default.json

## Toolchain profiles 工具链配置文件

### User perspective 用户观点

工具链或构建系统概要文件是一组保证传递给underyling编译器套件的标志。

这些标志存储在JSON文件中，该文件可能与同一结构的其他JSON文件合并。
###  JSON toolchain profile format

表示工具链配置文件的JSON对象是从工具链（例如GCC_ARM）到其标志（例如 -O3）的字典映射.

结构如下：工具链配置文件支持的每个工具链在根字典中都有一个字典。

该字典包含从标志类型到应该传递给编译器套件的相应部分的标志列表的映射。

必需的标志类型是：

|Key|Description|
|:-:|:-:|
|c|C编译器的标志|
|cxx|C ++编译器的标志|
|common|C和C ++编译器的标志|
|asm|汇编程序的标志|
|ld|链接器的标志|

工具链配置文件的示例：

	{
	    "GCC_ARM": {
	        "common": ["-c", "-Wall", "-Wextra",
	                   "-Wno-unused-parameter", "-Wno-missing-field-initializers",
	                   "-fmessage-length=0", "-fno-exceptions", "-fno-builtin",
	                   "-ffunction-sections", "-fdata-sections", "-funsigned-char",
	                   "-MMD", "-fno-delete-null-pointer-checks",
	                   "-fomit-frame-pointer", "-Os"],
	        "asm": ["-x", "assembler-with-cpp"],
	        "c": ["-std=gnu99"],
	        "cxx": ["-std=gnu++98", "-fno-rtti", "-Wvla"],
	        "ld": ["-Wl,--gc-sections", "-Wl,--wrap,main", "-Wl,--wrap,_malloc_r",
	               "-Wl,--wrap,_free_r", "-Wl,--wrap,_realloc_r",
	               "-Wl,--wrap,_calloc_r", "-Wl,--wrap,exit", "-Wl,--wrap,atexit"]
	    },
	    "ARM": {
	        "common": ["-c", "--gnu", "-Otime", "--split_sections",
	                   "--apcs=interwork", "--brief_diagnostics", "--restrict",
	                   "--multibyte_chars", "-O3"],
	        "asm": [],
	        "c": ["--md", "--no_depend_system_headers", "--c99", "-D__ASSERT_MSG"],
	        "cxx": ["--cpp", "--no_rtti", "--no_vla"],
	        "ld": []
	    },
	    "IAR": {
	        "common": [
	            "--no_wrap_diagnostics", "non-native end of line sequence", "-e",
	            "--diag_suppress=Pa050,Pa084,Pa093,Pa082", "-Oh"],
	        "asm": [],
	        "c": ["--vla"],
	        "cxx": ["--guard_calls", "--no_static_destruction"],
	        "ld": ["--skip_dynamic_initialization", "--threaded_lib"]
	    }
	}

从这个工具链配置文件中，我们可以看出：

- GCC_ARM，ARM以及IAR编译器套件的支持。
- 在ARMC和C ++编译器将使用的优化级别-O3。
- 该IAR连接器将跳过动态初始化。

等等。

### API perspective

工具链接受一个可选参数，build_profile它从标志类型映射到标志列表。提供时，此参数必须包含从标志类型到标志列表的dict映射，以提供给编译器。如果没有此参数，工具链将在每个必需标志类型中使用不包含标志的构建配置文件。必需的标志类型是：

|Key|Description|
|:-:|:-:|
|c|C编译器的标志|
|cxx|C ++编译器的标志|
|common|C和C ++编译器的标志|
|asm|汇编程序的标志|
|ld|链接器的标志|

使用API​​的开发人员必须自己解析用户提供的文件，然后从文件中提取相应的子字典。这些工具提供了一个便利功能，tools.options.extract_profile。解析构建配置文件当从命令行上给出的选项--profile。 此函数将调用args_error当工具链配置文件JSON文件未提供所选工具链的标志时
