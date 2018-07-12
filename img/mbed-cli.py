

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
      
  
  
  
  
