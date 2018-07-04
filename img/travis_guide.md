前提条件：

- 登陆github， 授权travis访问github上的代码库

- 把需要CI的代码库选上，默认情况下，Travis会在代码push时收到GitHub通知，然后自动获取最新代码，进行CI
- 添加一个`.travis.yml`文件到代码库，该文件会告诉travis ci做哪些事情。
- 把`.travis.yml`t添加到`git`,` commit` ,`push`, 触发travis ci构建。
- 进入构建状态页面，查看构建是否成功。

### 编程语言
  
  language:ruby/java/node_js/python/php

### 选择基础配置

确定您的构建所运行的基础设施的最佳方法是设置`language`。如果您这样做，您的构建将运行在默认的基础设施上（只有少数例外），这是基于Ubuntu 14.04的容器。您可以通过添加来`sudo: false`到`.travis.yml`显式地选择缺省基础设施.

- 如果您需要一个在虚拟机中运行的更可定制的环境，那么请使用Sudo支持的基础设施

    .travis.yml
    sudo:enable

- 如果您的测试需要在macOS上运行，或者您的项目使用Swift或Objective-C，请使用OSX环境：

    .travis.yml
    os:osx

### travis不仅仅可以运行测试

- 部署到github 主页
  当构建成功之后travis ci可以把静态文件部署到github pages:
  需要提供个人访问令牌（当在命令行或API上使用Git进行Git操作时，可以使用它来代替密码，github进行身份验证：two-factor 验证；在一个使用SAML单点登录（SSO）的组织中访问受保护的内容。与使用SAML SSO的组织一起使用的令牌必须被授权。）并在`.travis.yml`设置部署提供方的详细信息
  
  - 设置 GitHub令牌
    需要使用`public_repo`或`repo`(私有存储库)生成一个个人访问令牌，因为令牌是私有的，在` repository settings `安全的传递给Travis或通过`.travis.yml`加密变量
  - 其他配置
  
    1. `local-dir`:相对于当前目录的的目录，到github页面的的目录为默认目录
    2. `repo`: Repo slug 默认为当前repo
    3. `target-branch:`  推送`local-dir`的内容的分支，默认`gh-pages`
    4. `keep-history:`创建增量提交，而不是force push 默认 false
    5. `fqdn`:可选，为你的网站设置一个自定义域，默认为没有自定义域支持
    6. `project-nam`:用于元数据，默认fqdn 或 repo slug
    7. `email`:可选，提交信息，默认`deploy@travis-ci.org`
    8. `name`:可选，提交者，默认`Deployment Bot`
    9. `committer-from-gh`:可选。默认值false,允许使用令牌的所有者名称和电子邮件提交 覆盖`email`和`name`
    10. `allow-empty-commit`,可选，默认false, Enabled if only keep-history is true.
    11. `github-url`:可选，自托管github 企业的url.默认github.com
    12. `verbose`：可选，对内部步骤进行详细说明，默认为false
    
    https://docs.travis-ci.com/user/getting-started
  

    
    
