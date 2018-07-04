前提条件：

- 登陆github， 授权travis访问github上的代码库

- 把需要CI的代码库选上，默认情况下，Travis会在代码push时收到GitHub通知，然后自动获取最新代码，进行CI
- 添加一个`.travis.yml`文件到代码库，该文件会告诉travis ci做哪些事情。
- 把`.travis.yml`t添加到`git`,` commit` ,`push`, 触发travis ci构建。
- 进入构建状态页面，查看构建是否成功。
