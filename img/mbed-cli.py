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
  

Class Repo:

  def formurl
  
  def formlib
  
  def frmrepo(path) # 返回{repo.path = abs(path), repo.name = base(path),cache = 用户目录/mbed_cache}
  
  def sync()
  
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
  
  
