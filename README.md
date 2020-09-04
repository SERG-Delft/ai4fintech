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
bundle exec jekyll build

# Run jekyll as web server.
# Automatically rebuilds after a file change
bundle exec jekyll serve
```

#### Running with Docker

You can use Docker to avoid installing Ruby and/or gems. More instructions
[here](https://github.com/envygeeks/jekyll-docker/blob/master/README.md)

```shell
export JEKYLL_VERSION=3.8.4

# Build the web site
docker run --rm -p4000:4000 --volume="$PWD:/srv/jekyll" -it jekyll/builder:$JEKYLL_VERSION jekyll serve
```
