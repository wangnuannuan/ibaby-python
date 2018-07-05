

patches_required_folders="library,middleware,os"
patches_required_folder_list=(${patches_required_folders//,/ }) # ，换成/
PREV_DIR=$(pwd) #当前目录的全目录名称
SCRIPT_DIR=$(dirname $0) #取得当前执行的脚本文件的父目录
if which dos2unix >/dev/null 2>&1; then :; else
    echo "You need dos2unix in your path" >&2
    exit 1
fi

cd ${SCRIPT_DIR}
echo "Start to download required source code and apply patches for embARC"
echo ""

exit_ok=0
for patch_folder in ${patches_required_folder_list[@]}
do
	patch_scripts=$(find $patch_folder -maxdepth 2 -name "apply_embARC_patch.sh") # 查找apply_embARC_patch.sh文件
	for script in ${patch_scripts[@]}
	do
		patch_dir=$(dirname ${script}) # 跳转到${script}
		echo "+++++Try to patch ${patch_dir}+++++"
		echo "Run script: chmod +x ${script} && ${script}"
		filetype=$(file ${script} | grep -q CRLF && echo DOS || echo UNIX)
		if [[ ${filetype} == DOS ]] ; then
			echo "Convert ${script} from DOS to UNIX"
			dos2unix ${script}
		fi
		chmod +x ${script} && ${script} #只授予这个文件的所属者执行的权限 
		if [[ $? -eq 0 ]] ; then


echo "-----Patch ${patch_dir} successfully-----"
		else
			echo "-----Patch ${patch_dir} failed-----"
			exit_ok=1
		fi
		echo ""
	done
done
echo ""
if [[ ${exit_ok} -eq 0 ]] ; then
	echo "Apply patches for embARC successfully"
else
	echo "Apply patches for embARC failed"

fi
echo "Patch job ended"
cd ${PREV_DIR}
exit ${exit_ok}



die() {

	echo " *** ERROR: " $* # 以一对双引号给出参数列表

	exit 1 
    #退出shell，并返回给定值1 对于travis ci 在before_install, install or before_script
    #返回非零值则会构建错误并立即停止构建

}
set -x # 执行指令后，会先显示该指令及所下的参数

cd /tmp || die
[ $TRAVIS_OS_NAME != linux ] || {

    sudo apt-get update || die #更新源地址，获取软件包
    sudo apt-get install lib32z1 || die
    sudo apt-get install dos2unix || die
    wget https://github.com/foss-for-synopsys-dwc-arc-processors/toolchain/releases/download/arc-2017.09-release/arc_gnu_2017.09_prebuilt_elf32_le_linux_install.tar.gz || die
    # 从指定的URL下载文件
    tar xzf arc_gnu_2017.09_prebuilt_elf32_le_linux_install.tar.gz || die # 解压
    export PATH=/tmp/arc_gnu_2017.09_prebuilt_elf32_le_linux_install/bin:$PATH || die #添加到环境变量
    arc-elf32-gcc --version || die # 查看arc-elf32-gcc版本号
    sudo apt-get install doxygen || die
    sudo pip install --upgrade pip || die #pip升级

sudo pip install git+https://github.com/sphinx-doc/sphinx || die #安装sphinx
    sudo pip install breathe || die # Breathe是reStructuredText和Sphinx的扩展，能够读取和渲染Doxygen xml输出
    sudo pip install recommonmark || die # 允许在Docutils和Sphinx项目中编写CommonMark,Markdown的强定义，高度兼容的规范
    sudo pip install sphinx_rtd_theme || die 
}


REPO_NAME="github.com/foss-for-synopsys-dwc-arc-processors/embarc_osp.git"
REPO_LINK="https://""${GH_TOKEN}""@""${REPO_NAME}"
die()

{
    echo " *** ERROR: " $*
    exit 1
}
set -x
# Make documentation
echo 'Generating documentation ...'
cd ../doc/documents/example || die
ln -s ../../../example example || die # ln -s 源文件 目标文件 它的功能是为某一个文件在另外一个位置建立一个同不的链接
# Generate xml by doxygen
cd ../..
mkdir -p build/doxygen/xml || die
make doxygen || die # 是GNU的工程化编译工具，用于编译众多相互关联的源代码问价，以实现工程化的管理，提高开发效率
# Generate by sphinx 
make html || die
# tar doc
tar czvf doc.tar.gz build || die

git fetch origin || die
git branch -a || die # 查看远程分支
mkdir gh-pages || die
cd gh-pages || die
git init . || die
git remote add origin ${REPO_LINK} || die #添加远程仓库
git fetch origin -t || die
git checkout -b gh-pages origin/gh-pages || die
cd doc || die
rm -rf embARC_Document.html embARC_Document || rm -rf build
cp ../../doc.tar.gz . || die # 复制文件
tar xzvf doc.tar.gz || die # z代表gzip的压缩包；x代表解压；v代表显示过程信息；f代表后面接的是文件 .
rm -rf doc.tar.gz || die
git add --all || die
# git commit -s -a -m "Update gh-pages branch, Travis build: $TRAVIS_BUILD_NUMBER, commit: ${TRAVIS_COMMIT}"
git commit -s -a -m "Update gh-pages branch, Travis build: $TRAVIS_BUILD_NUMBER" || die
if [ $? -eq 0 ]; then
        git push ${REPO_LINK} gh-pages:gh-pages > /dev/null 2>&1 || die
else
        echo 'No update in gh-pages branch'
fi
exit 0


import json
import os
import sys
example = {"arc_feature_cache":"baremetal/arc_feature/cache",
		"arc_feature_timer_interrupt":"baremetal/arc_feature/timer_interrupt",
		"arc_feature_udma":"baremetal/arc_feature/udma",
		"ble_hm1x":"baremetal/ble_hm1x",
		"blinky":"baremetal/blinky",
		"cxx":"baremetal/cxx",
		"graphic_u8glib":"baremetal/graphic_u8glib",
		"kernel":"freertos/kernel"
		}

folder = ".travis"

if __name__ == '__main__':
	print(example)
	result = {}
	for (k,v) in example.items():
		result[k] = 0
		print("example[%s]=" %k,v)
		pathin = "../example/"+v
		os.chdir(pathin)# 改变当前工作目录到指定的路径
		os.system("make "+sys.argv[1]+" clean") # 执行命令

		if os.system("make "+sys.argv[1]+" -k") != 0:

			result[k] = 1

		pathout = pathin.count('/')*"../"+folder # 统计字符串里某个字符出现的次数

		os.chdir(pathout)

	print(result)



	for (k,v) in result.items():

		if v == 1:

			sys.exit(1)

	

	sys.exit(0)
