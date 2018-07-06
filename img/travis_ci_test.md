### Prerequisites
To start using Travis CI, make sure you have all of the following:
-	GitHub login
-	Admin permissions for a project hosted on GitHub
-	Working code in your project
-	Working build or test script
### To get started with Travis CI 
1.	Using your GitHub account, sign in to GitHub and add the Travis CI app to the repository you want to activate. You’ll need Admin permissions for that repository.
2.	Once you’re signed in to Travis CI, and we’ve synchronized your GitHub repositories, go to your profile page and enable the repository you want to build, Click the settings to set your repository.
3.	Add a `.travis.yml` file to your repository to tell Travis CI what to do.

        language: python
        sudo: required
        dist: trusty
        branches:
          except:
            - gh-pages
        python:
          - "3.6"
        before_install:
          - bash .travis/before_install.sh
          # setup git
          - git config --local user.name "wangnuannuan"
          - git config --local user.email "1961295051@qq.com.com"
        script:
          - bash .travis/script.sh
        matrix:
          include:
            - env: TOOLCHAIN="sphinx" BOARD="none" BD_VER="none" CUR_CORE="none"

    select python as the programming language and the version is 3.6

        language : python    

    use the Sudo Enabled infrastructure, it is a customizable environment running in a virtual machine

        sudo: required
        dist: trusty

    chose the `gh-pages` branch to deploy

        branches:
          except:
            - gh-pages

  A build on Travis CI is made up of two steps:

  1.	`install`: install any dependencies required  2.	`script`: run the build script
  You can run custom commands before the installation step (`before_install`), and before (`before_script`) or after (`after_script`) the script step.
  In a `before_install` step, you can install additional dependencies required by your project such as Ubuntu packages or custom services.
          
          - bash .travis/before_install.sh

  In this step, some additional dependencies including lib32z1, dos2unix , doxygen and some python packages(sphinx, sphinx, recommonmark, sphinx_rtd_theme) are installed. Arc_gnu is added to environmental variable.

        - git config --local user.name "wangnuannuan"
        - git config --local user.email 1961295051@qq.com.com

        Configure git user information.

  If any error occur in this step, an error message will be printed , the exit the shell and return 1.If `before_install`, `install` or `before_script` returns a non-zero exit code, the build is errored and stops immediately.

      script:
        - bash .travis/script.sh

  - add arc gnu to environmental variable.
  - apply patches for embARC
  - add branch gh-pages and deploy to github pages. First , create personal access token in github, then set environment variable named GH_TOKEN with the personal access token.
  - use the gnu to complie the ‘example’ with different board version or CUR_CORE

  If `script` returns a non-zero exit code, the build is failed, but continues to run before being marked as failed.

  When you combine the three main configuration options of Runtime, Environment and Exclusions/Inclusions you have a matrix of all possible combinations:

        matrix:
          include:
            - env: TOOLCHAIN="sphinx" BOARD="none" BD_VER="none" CUR_CORE="none"
              os: linux
            - env: TOOLCHAIN="gnu" BOARD="emsk" BD_VER="11" CUR_CORE="arcem4"
              os: linux
              compiler: gcc

  The `include`  adds particular jobs to the build matrix which have already been populated.

  You can embed status images (also known as badges or icons) that show the status of your build into your README or website.

   - The URLs for status images are shown on your Travis CI Repository page:
      Click the status image in the top right to open a dialog box containing common templates for the status image URL in markdown, html, etc.
   - Select the branch and template in the dialog box
   - Copy the text and paste it into your README or website. You should now be able to view the Build status images for public repositories are publicly available on Travis CI.


4.	Add the .travis.yml file to git, commit and push, to trigger a Travis CI build:
5.	Check the build status page to see if your build passes or fails, according to the return status of the build command by visiting Travis CI .com build status and selecting your repository.
