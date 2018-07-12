
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

  def formurl() # repo.name repo.path repo.url repo.rec repo.cache
  
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
      
  
  
  
  
