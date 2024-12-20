## The AFR website

The AFR web site is built with Jekyll and is running on GitHub pages.

### Building locally

There are two options to build the website locally:

* Installing and running Jekyll
* Running Jekyll from a Docker container

#### Installing and running Jekyll

Jekyll requires Ruby (>=2.3). If you have Ruby installed (most recent Linuxes
and Macs do have a correct version of Ruby), you can use the following commands
to build the web site:

```shell
# Install dependencies
gem install bundler
bundle install

# Build the web site

bundle exec jekyll build --config _config.yml,_config_local.yml

# Run jekyll with Docker (recommended)
```
docker build -t afr-site .
docker run -p 4000:4000 -v $(pwd):/myapp -it afr-site
```
