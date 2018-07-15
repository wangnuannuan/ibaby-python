Make.py
def get_default_options_parser(add_clean=True, add_options=True,
                               add_app_config=False):
get_default_options_parser(add_app_config=False):
target = 

#targets/
#__init__.py

def get_resolution_order(json_data, target_name, order, level=0):# 遍历 order，l;如果target_name不在l[0]则添加(target_name, level)到 order.
# parents = json_data[target_name].get("inherits", [])找到"inherits"，否则parents=[].遍历parents ，par,get_resolution_order(json_data, par, order, level + 1)
#到parents=[],返回order
def target(name, json_data):
#resolution_order = get_resolution_order(json_data, name, []) 是列表，列表元素元组，有两个元素
# resolution_order_names 取出resolution_order中元组第一个元素组成列表 json_data = 取出key在resolution_order_names的元素
# 返回Target(name=name,json_data,resolution_order=resolution_order,resolution_order_names=resolution_order_names)
def generate_py_target(new_targets, name):# 如果ew_targets的某个键在base_targets=Target.get_json_target_data()抛出错误，total_data = {}，将new_targets，base_target组合到total_data，返回target(name, total_data)

CACHE = dict
CORE_LABELS = {
   "Cortex-M0" : ["M0", "CORTEX_M", "LIKE_CORTEX_M0", "CORTEX"],
   "Cortex-M0+": ["M0P", "CORTEX_M", "LIKE_CORTEX_M0", "CORTEX"],
   "Cortex-M1" : ["M1", "CORTEX_M", "LIKE_CORTEX_M1", "CORTEX"],
   "Cortex-M3" : ["M3", "CORTEX_M", "LIKE_CORTEX_M3", "CORTEX"],
   "Cortex-M4" : ["M4", "CORTEX_M", "RTOS_M4_M7", "LIKE_CORTEX_M4", "CORTEX"],
   "Cortex-M4F" : ["M4", "CORTEX_M", "RTOS_M4_M7", "LIKE_CORTEX_M4", "CORTEX"],
   "Cortex-M7" : ["M7", "CORTEX_M", "RTOS_M4_M7", "LIKE_CORTEX_M7", "CORTEX"],
   "Cortex-M7F" : ["M7", "CORTEX_M", "RTOS_M4_M7", "LIKE_CORTEX_M7", "CORTEX"],
   "Cortex-M7FD" : ["M7", "CORTEX_M", "RTOS_M4_M7", "LIKE_CORTEX_M7", "CORTEX"],
   "Cortex-A9" : ["A9", "CORTEX_A", "LIKE_CORTEX_A9", "CORTEX"],
    "Cortex-M23": ["M23", "CORTEX_M", "LIKE_CORTEX_M23", "CORTEX"],
    "Cortex-M23-NS": ["M23", "CORTEX_M", "LIKE_CORTEX_M23", "CORTEX"],
    "Cortex-M33": ["M33", "CORTEX_M", "LIKE_CORTEX_M33", "CORTEX"],
    "Cortex-M33-NS": ["M33", "CORTEX_M", "LIKE_CORTEX_M33", "CORTEX"]
}
def cache() # 自动缓存一个函数的返回值 装饰器

CUMULATIVE_ATTRIBUTES = ['extra_labels', 'macros', 'device_has', 'features']
class Target(namedtuple("Target", "name json_data resolution_order resolution_order_names"))# 继承
	__targets_json_location_default = "xxx/mbed-os/targets/targets.json"
	__targets_json_location = None
	__extra_target_json_files = []
	def get_json_target_data():# 读取targets.json，如果__extra_target_json_files中的json文件中存在不同的key，加进去，返回所有的targets 字典
	def add_extra_targets(source_dir):# source_dir/custom_targets.json若存在，将路径添加到__extra_target_json_files，清除 CACHES
	def set_targets_json_location(location=None):# 将__targets_json_location设置成location(if location)或__targets_json_location_default，__extra_target_json_files = []，清除 CACHES元素
	# Python中所有加载到内存的模块都放在sys.modules。当import一个模块时首先会在这个列表中查找是否已经加载了此模块，
	#如果加载了则只是将模块的名字加入到正在调用import的模块的Local名字空间中。如果没有加载则从sys.path目录中按照模块名称查找模块文件，
	#模块文件可以是py、pyc、pyd，找到后将模块载入内存，并加入到sys.modules中，并将名称导入到当前的Local名字空间。
	def get_module_data():# 返回该模块所有对象
	def __add_paths_to_progen(data):# 将data中"template"键值 对应的值out={"template":XXX/mbed-os/tools/target/export/*对应键值（不是dict,否则递归）} 返回out
	def __getattr_cumulative(self, attrname):# 根据解析顺序查找该类及父类的属性 
	#if attrname in self.json_data[self.resolution[k][0]] def_idx= k,否则抛出错误 
	# starting_value =  self.json_data[self.resolution[k][0]][attrname]
	#遍历m（self.resolution[k][1]-1，self.resolution[k][1]-2，..,0),遍历self.resolution_order，n
	# same_level_targets= n[0] 当你n[1]==m
	#遍历same_level_targets ，a. 如果attrname + "_add" 在self.json_data[a],在starting_value末尾添加self.json_data[a][attrname + "_add"]
	#                          如果attrname + "_remove"在self.json_data[a]，遍历starting_value，b;如果b有“=”且只有一个name_def_map[等号前] = b,如果没有“=”，name_def_map[b]=b
	# 接上 遍历 self.json_data[a][attrname + "_remove"] c,name_def_map不存在键值c,跑错，starting_value移除name_def_map[c]

	# 返回 starting_value
	def __getattr_helper(self, attrname):# 如果attrname是CUMULATIVE_ATTRIBUTES一个，返回__getattr_cumulative(attrname)，
    # else:遍历self.resolution_order，a;返回self.json_data[a[0]][attrname]
    def __getattr__(self, attrname):# self.__dict__[attrname] = self.__getattr_helper(attrname)，返回self.__getattr_helper(attrname)只计算一次，下一次直接返回
    def get_target(target_name):# 返回target(target_name, Target.get_json_target_data())
    def program_cycle_s(self): # return self.__getattr__("program_cycle_s")，self.__dict__["program_cycle_s"]=self.json_data[a[0]]["program_cycle_s"],返回 出错 如果elf.is_disk_virtual返回4，否则返回1.5
    def labels(self):# names = copy(self.resolution_order_names 列表)，移除 键值"Target"；labels = (names + CORE_LABELS[self.core] + self.extra_labels)，
    #如果"UVISOR_SUPPORTED"不在labels中，添加"UVISOR_SUPPORTED"，返回labels
    def init_hooks(self, hook, toolchain):#初始化一个工具链的post-build hooks，仅支持"post binary" hooks(从可执行文件中提取binary image后被执行)
    # class_name, function_name = self.post_binary_hook["function"].split("."),当class_name不在self.get_module_data()或self.get_module_data()[class_name]不是class,抛出错误
    # cls=self.get_module_data()[class_name],如果cls,没有function_name，或cls.function_name不是函数，抛出错误
    # toolchain_restrictions=set(self.post_binary_hook["toolchains"]||[]) toolchain_labels = set(c.__name__ for c in getmro(toolchain.__class__))元组形式返回toolchain.__class__基类，
    # if toolchain_restrictions and not toolchain_labels.intersection(toolchain_restrictions) return
    # hook.hook_add_binary("post", getattr(cls, function_name)) # 最后，钩住所请求的函数

class MTSCode(object):
	def _combine_bins_helper(target_name, binf):# 为特定的目标组合 bin和bootloader

# utils.py
def remove_if_in(lst, thing):#移除lst中的thing
def json_file_to_dict(fname): # 读取一个JSON文件，将字符串的编码方式转换成ascii,同时保持文件中key的顺序 返回一个dict
def run_cmd(command, work_dir=None, chroot=None, redirect=False):# 在前台运行一个命令.if chroot: chroot_cmd=[ '/usr/sbin/chroot', '--userspec=33:33', chroot]
# chroot_cmd= chroot_cmd+ command(其中的chroot字符串去掉)， work_dir = None endif; process = Popen(command, stdout=PIPE,stderr=STDOUT if redirect else PIPE, cwd=work_dir)
# _stdout, _stderr = process.communicate() ,return _stdout, _stderr, process.returncode
def compile_worker(job):# results = [],遍历job['commands']，command; _, _stderr, _rc = run_cmd(command, work_dir=job['work_dir'],chroot=job['chroot']),
# results.append({'code': _rc,'output': _stderr,'command': command}),return {'source': job['source'],'object': job['object'],'commands': job['commands'],'results': results}
def cmd(command, check=True, verbose=False, shell=False, cwd=None):# 执行命令command其中shell参数为False时，命令需要通过列表的方式传入，当shell为True时，可直接传入命令
def get_caller_name(steps=2):
def run_cmd_ext(command):# 
# hoks.py

_HOOKS = {}
# Internal mapping of running hooks
_RUNNING_HOOKS = {}
# Available hook types
_HOOK_TYPES = ["binary", "compile", "link", "assemble"]
# Available hook steps
_HOOK_STEPS = ["pre", "replace", "post"]
def hook_tool(function): #一个装饰器 如果_RUNNING_HOOKS中有这个function name返回 function(t_self, *args, **kwargs);如果_HOOKS没有function name，_RUNNING_HOOKS[function.name]=False 返回 function(t_self, *args, **kwargs)；
# t_self的属性"_" + function.__name__ + "_done"设置成 False. _HOOKS[function.__name__]有"replace" ，设置成 res =  _HOOKS[function.__name__](t_self, *args, **kwargs)
# 如果 t_self的"_" + function.__name__ + "_done"属性不是False ，_RUNNING_HOOKS[function.__name__]=False,返回res.
#如果 "pre" in _HOOKS[function.__name__],执行 _HOOKS[function.__name__]["pre"](t_self, *args, **kwargs)，res = function(t_self, *args, **kwargs)
# "post" in _HOOKS[function.__name__],post_res=_HOOKS[function.__name__]["post"](t_self, *args, **kwargs),_RUNNING_HOOKS[function.__name__]=False
#返回post_res or res ; "post" not in _HOOKS[function.__name__],_RUNNING_HOOKS[function.__name__]=False 返回res

class Hook(object): # A compiler class that may be hooked

def __init__(self, target, toolchain):
    _HOOKS.clear()
    self._cmdline_hooks = {}
    self.toolchain = toolchain
    target.init_hooks(self, toolchain)
def _hook_add(hook_type, hook_step, function):# 直接钩各种function；hook_type 不在_HOOK_TYPES或hook_step 不在 in _HOOK_STEPS，返回False.hook_type不在_HOOKS，_HOOKS[hook_type] = {}，_HOOKS[hook_type][hook_step] = function，返回True
def hook_add_compiler(self, hook_step, function): # 添加hook到compiler ,return self._hook_add("compile", hook_step, function)
def hook_add_linker(self, hook_step, function): # 添加hook到linker，return self._hook_add("link", hook_step, function)
def hook_add_assembler(self, hook_step, function):#return self._hook_add("assemble", hook_step, function)
def hook_add_binary(self, hook_step, function):# Add a hook to the elf to binary tool，return self._hook_add("binary", hook_step, function)
def _hook_cmdline(self, hook_type, function):# Add a hook to a command line function，hook_type不在_HOOK_TYPES，返回False,self._cmdline_hooks[hook_type] = function,返回True
def hook_cmdline_compiler(self, function):# Add a hook to the compiler command line,return self._hook_cmdline("compile", function)
def hook_cmdline_linker(self, function):# Add a hook to the linker command line,return self._hook_cmdline("link", function)
def hook_cmdline_assembler(self, function):# Add a hook to the assembler command line,return self._hook_cmdline("assemble", function)
def hook_cmdline_binary(self, function):#Add a hook to the elf to bin tool command line,return self._hook_cmdline("binary", function)
def _get_cmdline(self, hook_type, cmdline):# "Get the command line after running all hooks,如果hook_type在self._cmdline_hooks，返回elf._cmdline_hooks[hook_type](self.toolchain.__class__.__name__, cmdline)
def get_cmdline_compiler(self, cmdline):# Get the compiler command line after running all hooks，return self._get_cmdline("compile", cmdline)
def get_cmdline_linker(self, cmdline):# Get the linker command line after running all hooks，return self._get_cmdline("link", cmdline)
def get_cmdline_assembler(self, cmdline):# return self._get_cmdline("assemble", cmdline)
def get_cmdline_binary(self, cmdline):# return self._get_cmdline("binary", cmdline)

#settings.py

ROOT= # 当前文件所在目录上一级， /mbed-os
BUILD_DIR = #mbed-os/BUILD Toolchains and Build System Settings
ARM_PATH = "" # ARM Compiler 5
ARMC6_PATH = "" ## ARM Compiler 6
GCC_ARM_PATH = "" ## GCC ARM
GCC_CR_PATH = "" # # GCC CodeRed
IAR_PATH = ""#IAR
GOANNA_PATH = ""# Goanna static analyser. Please overload it in mbed_settings.py
CPPCHECK_CMD = ["cppcheck", "--enable=all"]#cppcheck path (command) and output message format
CPPCHECK_MSG_FORMAT = ["--template=[{severity}] {file}@{line}: {id}:{message}"]
BUILD_OPTIONS = []
MBED_ORG_USER = ""# mbed.org username
PRINT_COMPILER_OUTPUT_AS_LINK = False# Print compiler warnings and errors as link format
COLOR = False # Print warnings/errors in color
CLI_COLOR_MAP = {
    "Warning": "yellow",
    "Error"  : "red"
}
_ENV_PATHS = ['ARM_PATH', 'GCC_ARM_PATH', 'GCC_CR_PATH', 'IAR_PATH','ARMC6_PATH'] #环境变量

# 遍历_ENV_PATHS，_n ,如果环境变量MBED_'+_n存在，当前位置的全部全局变量字典，添加_n,对应值为环境变量MBED_'+_n的值，不存在是，warning
_ENV_VARS = ['PRINT_COMPILER_OUTPUT_AS_LINK', 'COLOR'] # 遍历 _n,如果存在环境变量MBED_+_n，对应值存在，则当前位置的全部全局变量字典，添加_n,对应值为环境变量MBED_'+_n的值
SERVER_PORT = 59432
SERVER_ADDRESS = "10.2.200.94"
LOCALHOST = "10.2.200.94"

MUTs = {
    "1" : {"mcu": "LPC1768",
        "port":"COM41", "disk":'E:\\',
        "peripherals": ["TMP102", "digital_loop", "port_loop", "analog_loop", "SD"]
    },
    "2": {"mcu": "LPC11U24",
        "port":"COM42", "disk":'F:\\',
        "peripherals":  ["TMP102", "digital_loop", "port_loop", "SD"]
    },
    "3" : {"mcu": "KL25Z",
        "port":"COM43", "disk":'G:\\',
        "peripherals":  ["TMP102", "digital_loop", "port_loop", "analog_loop", "SD"]
    },
}

#path.py
BUILD_DIR= # 环境变量"MBED_BUILD_DIR"或mbed-os/BUILD
# Embedded Libraries Sources
LIB_DIR= "xxx/mbed-os/features/unsupported"
TOOLS = "xxx/mbed-os/tools"
TOOLS_DATA = "xxx/mbed-os/tools/data"
TOOLS_BOOTLOADERS = "xxx/mbed-os/tools/bootloaders"
# mbed libraries
MBED_HEADER = "xxx/mbed-os/mbed.h"
MBED_DRIVERS = "xxx/mbed-os/drivers"
MBED_PLATFORM = "xxx/mbed-os/platform"
MBED_HAL = "xxx/mbed-os/hal" 
MBED_CMSIS_PATH = "xxx/mbed-os/cmsis"
MBED_TARGETS_PATH = "xxx/mbed-os/targets" 
MBED_LIBRARIES = "mbed-os/BUILD/mbed"
MBED_LIBRARIES_DRIVERS = "mbed-os/BUILD/mbed/drivers"
MBED_LIBRARIES_PLATFORM = "mbed-os/BUILD/mbed/platform"
MBED_LIBRARIES_HAL = "mbed-os/BUILD/mbed/hal"
MBED_CONFIG_FILE = "xxx/mbed-os/platform/mbed_lib.json"

TEST_DIR = "xxx/mbed-os/features/unsupported/tests"
HOST_TESTS = "xxx/mbed-os/tools/host_tests"

MBED_RPC = "xxx/mbed-os/features/unsupported/rpc"
RPC_LIBRARY = "xxx/mbed-os/BUILD/rpc"

DSP = "xxx/mbed-os/features/unsupported/dsp"
DSP_CMSIS = "xxx/mbed-os/features/unsupported/dsp/cmsis_dsp"
DSP_ABSTRACTION = "xxx/mbed-os/features/unsupported/dsp/dsp"
DSP_LIBRARIES = "xxx/mbed-os/BUILD/dsp"
# USB Device
USB = "xxx/mbed-os/features/unsupported/USBDevice"
USB_LIBRARIES = "xxx/mbed-os/BUILD/usb"
# Export
EXPORT_DIR = "xxx/mbed-os/BUILD/export"
EXPORT_WORKSPACE = "xxx/mbed-os/BUILD/export/workspace"
EXPORT_TMP = "xxx/mbed-os/BUILD/export/.temp"
# CppUtest library
CPPUTEST_DIR = "xxx/" 
CPPUTEST_SRC = "xxx/cpputest/src/CppUTest" 
CPPUTEST_INC = "xxx/cpputest/include"
# Platform dependant code is here (for armcc compiler)
CPPUTEST_PLATFORM_SRC = "xxx/cpputest/src/Platforms/armcc"
CPPUTEST_PLATFORM_INC= "xxx/cpputest/include/Platforms/armcc"
# Function 'main' used to run all compiled UTs
CPPUTEST_TESTRUNNER_SCR = "xxx/mbed-os/features/unsupported/tests/utest/testrunner"
CPPUTEST_TESTRUNNER_SCR = "xxx/mbed-os/features/unsupported/tests/utest/testrunner"
CPPUTEST_LIBRARY = "xxx/mbed-os/BUILD/cpputest"
tools


mbed_lstools.create##mbed-os/tools/make.py
smbed_settings.py#

def log(msg) # 打印信息
def msg(msg) # 以 mbed msg的格式返回信息
def info(msg,level=1)# level<=0时，按行将字符串以mbed xxx的形式返回
def action(msg)# 按行将信息以mbed xxx的形式打印
def warning(msg) #错误信息输出
def error(msg,code=-1)#按行输出错误，结束返回代码code
def offline_warning(offline, top=True)# 根据两个参数都为True打印 OFFLINE MODE信息
def progress_cursor(title, percent, max_width=80)
def progress()#调用progress_cursor，根据次数依次打印|/-\\
def show_progress()
def hide_progress(max_width=80) #tty设备标准输出，打印max_width
def popen(command, stdin=None, **kwargs)# 产生子进程，执行command
def pquery(command, output_callback=None, stdin=None, **kwargs)#子进程执行command,PIPE进行标准输入输出。Popen.communicate(input=None)
# 和子进程交互：发送数据到stdin，并从stdout和stderr读数据，直到收到EOF。等待子进程结束。可选的input如有有的话，要为字符串类型。
# 此函数返回一个元组： (stdoutdata , stderrdata ) 。
Popen.poll() # 检查子进程是否已结束，设置并返回returncode属性。
def rmtree_readonly(directory): # 删除目录
def sizeof_fmt(num, suffix='B'):
def cd(newdir):# cd到指定路径
def getcwd(): #返回当前工作路径

  
class Git():
  name = "git"  default_branch = 'master'   ignore_file = os.path.join('.git', 'info', 'exclude')
  
  def init(path=None)# git init
  def cleanup(): #删除所有本地分支
  def clone(url, name=None, depth=None, protocol=None):# git clone url name
  def add(dest):# git add dest
  def remove(dest) #git rm -f dest
  def commit(msg=None)# git commit -a -m msg
  def publish(all_refs=None):# all_refs true git push --all  ;
  def fetch() # git fetch --all --tags
  def discard(clean_files=False)# git reset HEAD; git checkout .; if clean_file git clean -fd
  def merge(dest) #git merge dest
  def checkout(rev, clean=False)
  def update(rev=None, clean=False, clean_files=False, is_local=False):#"update git rev: %s,clean: %s,clean_files；%s",rev,clean,clean_files
  def status() # git status -s
  def dirty()# git 'status', '-uno', '--porcelain'
  def untracked()# git 'ls-files', '--others', '--exclude-standard'
  def outgoing():# 获得默认的远程分支；本地分支，不存在继续执行，git 'rev-parse' remote localbranch,出错执行git log
  def isdetached() #  Git.getbranch() == ""返回True
  def getremote() #Finds default remote
  def getremotes(rtype='fetch'):#Finds all associated remotes for the specified remote type
  def seturl(url):# git 'remote', 'set-url', 'origin', url
  def geturl():# getremotes() ,然后返回对应URL
  def getrev():# git 'rev-parse', 'HEAD'
  def getbranch(rev='HEAD'):# git 'rev-parse', '--symbolic-full-name', '--abbrev-ref', rev
  def getrefs():# git 'show-ref', '--dereference';Get all refs
  def getbranches(rev=None, ret_rev=False):# Finds branches (local or remote). Will match rev if specified
  
  
    
class Global:
  path = c:\\users\\jingru\\.mbed
  

Class Cfg :
  path
  file = ".mbed"
  
  def __init__ path = path
  def set(var,val) # 在当前路径下.mbed文件中添加 var = val,如果var已存在，更新值
  def get(var) # 返回 .mbed 文件中var对应的值
  def list() # 以列表的形式返回.mbed 文件中var ！= ROOT 的其他对应的值
  def cache() # 从.mbed 中获取 {'cache':enable,cache_base: CACHE_DIR 路径，cache_dir:cache_base/mbed-cache}

  Class Global# 主用户目录下的.mbed文件，Cfg.path = 用户目录，方法为Cfg的方法
  def mbed_sterm(port, baudrate=9600, echo=True, reset=False, sterm=False): # 
    class MbedTerminal:
      def init:# 根据信息打开一个串口，释放掉input_buffer
      def terminal： #终端程序
      def reset:#serial 设置break
    

Class Repo:

  def formurl() # repo.name repo.path repo.url repo.rec repo.cache is_local/is_build = True
  
     def formlib

      

      def frmrepo(path) # 返回{repo.path = abs(path), repo.name = base(path),cache = 用户目录/mbed_cache}
      def sync()# self.scm==bld self.is_build = True;self.url ;self.rev;self.lib
      def isinsecure(url) # 
      def getscm()# 查找当前路径下是否有.git .hg .bld
  
  Class Program():
  
  path
  name
  is_cwd = False
  is_repo = False
  build_dir = "BUILD"
  
  def  init #
    self.path = abs(path)或当前工作路径
    self.is_cwd = True
    当 .mbed文件存在 is_cwd = False 返回
    self.name = path对应文件
    is_classic = True path/mbed.bld存在时
  def get_cfg(*args, **kwargs)# 返回self.path中.mbed中或用户目录对应的key值
  def set_cfg(*args,**kwargs)# 设置
  def list_cfg()
  def set_root() # 在.mbed中添加 ROOT = .
  def unset_root() #删.mbed文件
  def get_os_dir() # .mbed 中MBED_OS_DIR存在 返回对应值，mbed-os存在，返回对应路径，self.name ="mbed-os"返回self.path
  def get_mbedlib_dir()# 返回delf.path/mbed 的路径
  def get_tools_dir() # 返回含有make.py的文件路径
  def _find_file_paths(paths,file) # 返回paths含有的file路径
  def get_requirements() #  返回mbed-os/mbed-os/tools,self.path,self.path/tools,self.path/.tmp/tools含有requirement.txt的文件路径
  def check_requirments()# 找到requirement.txt，安装未安装的python模块
  def post_action()# slef.path 下不存在mbed_settings.py，将mbed-tools-path下的default_setting.py复制过去，然后check_requirement
  def add_tools(path) # 如果path下没有tools文件夹，clone 下载mbed sdk
  def update_tools(path) #cd 到path下的tools,更新用git repo update
  def get_tools(path) # get_tools_dir 返回路径
  def get_env(path)# .mbed中编译器地址值，复制给环境变量
  def get_target(target)# 返回target target .mbed中TARGET,auto detect检测连接的板子
  def get_toolchain(toolchain) # 返回toolchain 或.mbed中的TOOLCHAIN
  def set_default(target,toolchain)# 设置.mbed中TARGET 和TOOLCHAIN
  def get_macros()#按行读取MACROS.txt，以列表形式返回
  def ignore_build_dir()#self.path/BUILD下'.mbedignore'中写入*\n，不存在时创建
  def detect_target(info = None)
  def get_detected_targets()
  
  mbed_lstools
  
  def craete() # 返回一个类mbed-enabled platform detection for windows,Linux with udev, or Mac OS X
  def mbed_os_support() # 根据系统信息返回 windows7 / LinuxGeneric/Darwin
  def mbed_lstools_os_info()#返回当前使用系统信息 windows7 
  
  lstools_base.py
  
    class MbedLsToolsBase(object):# mbed-lstools的基类定义了mbed-ls工具接口，用于检测主机上的mbed设备
      os_supported = []#此模块支持哪些操作系统＃注意：mbed-lstools_ *模块可以支持多个操作系统
      HOME_DIR = expanduser("~")#将存储全局的目录（OS用户特定的模拟）
      MOCK_FILE_NAME = '.mbedls-mock'
      RETARGET_FILE_NAME = 'mbedls.json'
      DETAILS_TXT_NAME = 'DETAILS.TXT'
      MBED_HTM_NAME = 'mbed.htm'
      
  
  
  
  
