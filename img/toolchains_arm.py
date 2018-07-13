tempfile.mkstemp([suffix=”[, prefix=’tmp'[, dir=None[, text=False]]]])
# mkstemp方法用于创建一个临时文件。该方法仅仅用于创建临时文件，调用tempfile.mkstemp函数后，返回包含两个元素的元组，
# 第一个元素指示操作该临时文件的安全级别，第二个元素指示该临时文件的路径。参数suffix和prefix分别表示临时文件名称的后缀和前缀；
# dir指定了临时文件所在的目录，如果没有指定目录，将根据系统环境变量TMPDIR, TEMP或者TMP的设置来保存临时文件；
# 参数text指定了是否以文本的形式来操作文件，默认为False，表示以二进制的形式来操作文件。
